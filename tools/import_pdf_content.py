from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import os
from dataclasses import dataclass
from pathlib import Path


PDF_LINK_RE = re.compile(r"(?P<full>\[(?P<label>[^\]]+)\]\((?P<href>/files/[^)]+?\.pdf)\))", re.I)
FRONT_MATTER_RE = re.compile(r"\A(---\r?\n.*?\r?\n---\r?\n)(?P<body>.*)\Z", re.S)
INPUT_RE = re.compile(r"\\(?:input|include)\{([^}]+)\}")
IMPORTED_FROM_RE = re.compile(r"<!-- Imported from (.*?) -->")
INCLUDEGRAPHICS_RE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")
HTML_IMG_RE = re.compile(r"<img(?P<before>[^>]*?)src=\"(?P<src>[^\"]+)\"(?P<after>[^>]*)>", re.I)
MD_IMAGE_RE = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<src>[^)]+)\)(?P<attrs>\{[^}]+\})?")
IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".pdf")
SOURCE_ROOT_ENV = "PDF_IMPORT_SOURCE_ROOT"


@dataclass
class LinkRecord:
    content_path: Path
    title: str
    href: str
    label: str
    site_pdf: Path
    site_size: int | None


@dataclass
class SourceMatch:
    source_pdf: Path | None
    source_file: Path | None
    reason: str
    score: int


def norm(value: str) -> str:
    return re.sub(r"[^0-9a-z]+", "", value.lower())


def decode_text(path: Path) -> str:
    data = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "gb18030", "big5"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def split_front_matter(text: str) -> tuple[str, str]:
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return "", text
    return match.group(1), match.group("body")


def front_matter_title(text: str) -> str:
    front, _ = split_front_matter(text)
    match = re.search(r"^title:\s*['\"]?(.*?)['\"]?\s*$", front, re.M)
    return match.group(1) if match else ""


def find_pdf_links(repo: Path, content_globs: list[str]) -> list[LinkRecord]:
    records: list[LinkRecord] = []
    paths: list[Path] = []
    for pattern in content_globs:
        paths.extend(repo.glob(pattern))

    for path in sorted(set(paths)):
        text = path.read_text(encoding="utf-8")
        title = front_matter_title(text)
        for match in PDF_LINK_RE.finditer(text):
            href = match.group("href")
            site_pdf = repo / href.lstrip("/").replace("/", "\\")
            records.append(
                LinkRecord(
                    content_path=path,
                    title=title,
                    href=href,
                    label=match.group("label"),
                    site_pdf=site_pdf,
                    site_size=site_pdf.stat().st_size if site_pdf.exists() else None,
                )
            )
    return records


def source_candidates_for_pdf(source_pdf: Path | None) -> list[Path]:
    if source_pdf is None:
        return []

    dirs = [source_pdf.parent]
    if source_pdf.parent.parent != source_pdf.parent:
        dirs.append(source_pdf.parent.parent)

    candidates: list[tuple[int, Path]] = []
    for directory in dirs:
        if not directory.exists():
            continue
        for ext in ("*.tex", "*.docx", "*.md"):
            for path in directory.glob(ext):
                name = path.name.lower()
                if path.name.startswith("~$"):
                    continue
                if any(bad in name for bad in ("config", "_region_", ".bak", ".tex~")):
                    continue
                size = path.stat().st_size
                same_stem = norm(path.stem) == norm(source_pdf.stem)
                suffix = path.suffix.lower()
                has_document = False
                if suffix == ".tex" and size <= 2_000_000:
                    try:
                        has_document = "\\begin{document}" in decode_text(path)
                    except OSError:
                        has_document = False
                score = size
                if same_stem and (suffix != ".tex" or has_document or size > 500):
                    score += 10_000_000
                if suffix == ".tex":
                    score += 1_000
                if suffix == ".tex" and not has_document:
                    score -= 9_000_000
                candidates.append((score, path))

    return [path for _, path in sorted(candidates, reverse=True)]


def choose_source_file(source_pdf: Path | None) -> Path | None:
    candidates = source_candidates_for_pdf(source_pdf)
    return candidates[0] if candidates else None


def build_source_index(source_root: Path) -> tuple[list[Path], list[Path]]:
    source_pdfs = [path for path in source_root.rglob("*.pdf") if path.is_file()]
    source_files = [
        path
        for ext in ("*.tex", "*.docx", "*.md")
        for path in source_root.rglob(ext)
        if path.is_file()
        and not path.name.startswith("~$")
        and "\\auto\\" not in str(path)
        and "/auto/" not in str(path)
        and ".tex~" not in path.name.lower()
    ]
    return source_pdfs, source_files


def load_manual_source_map(source_root: Path, map_path: Path | None) -> dict[str, Path]:
    if map_path is None or not map_path.exists():
        return {}

    raw = json.loads(map_path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError(f"source map must be a JSON object: {map_path}")

    manual_sources: dict[str, Path] = {}
    for href, source in raw.items():
        if not isinstance(href, str) or not isinstance(source, str):
            raise ValueError(f"source map keys and values must be strings: {map_path}")
        source_path = Path(source)
        if not source_path.is_absolute():
            source_path = source_root / source
        manual_sources[href] = source_path
    return manual_sources


def match_record(
    record: LinkRecord,
    source_pdfs: list[Path],
    source_files: list[Path],
    manual_sources: dict[str, Path],
) -> SourceMatch:
    manual_source = manual_sources.get(record.href)
    if manual_source:
        if manual_source.exists():
            return SourceMatch(None, manual_source, "manual source mapping", 110)

    href_stem = Path(record.href).stem
    href_norm = norm(href_stem)

    exact_pdf_name = [p for p in source_pdfs if norm(p.stem) == href_norm]
    if exact_pdf_name:
        source_pdf = sorted(exact_pdf_name, key=lambda p: p.stat().st_size, reverse=True)[0]
        source_file = choose_source_file(source_pdf)
        if source_file:
            return SourceMatch(source_pdf, source_file, "exact PDF basename", 100)

    if record.site_size is not None:
        same_size = [p for p in source_pdfs if p.stat().st_size == record.site_size]
        if same_size:
            source_pdf = sorted(same_size, key=lambda p: len(str(p)))[0]
            source_file = choose_source_file(source_pdf)
            if source_file:
                return SourceMatch(source_pdf, source_file, "identical PDF file size", 95)

    page_hint = norm(record.content_path.parent.name + " " + record.title + " " + href_stem)
    best: tuple[int, Path] | None = None
    for source_file in source_files:
        haystack = norm(str(source_file.relative_to(source_file.parents[len(source_file.parents) - len(source_file.parents)])) if False else str(source_file))
        score = 0
        if href_norm and href_norm in haystack:
            score += 60
        digits = "".join(re.findall(r"\d+", href_stem))
        if digits and digits[:6] in haystack:
            score += 30
        for token in re.findall(r"[a-z0-9]{3,}", page_hint):
            if token in haystack:
                score += min(len(token), 8)
        if best is None or score > best[0]:
            best = (score, source_file)

    if best and best[0] >= 45:
        return SourceMatch(None, best[1], "fuzzy source path", best[0])
    return SourceMatch(None, None, "no source found", 0)


def expand_tex(path: Path, seen: set[Path] | None = None) -> str:
    seen = seen or set()
    path = path.resolve()
    if path in seen:
        return ""
    seen.add(path)
    text = decode_text(path)

    def repl(match: re.Match[str]) -> str:
        raw = match.group(1)
        candidate = path.parent / raw
        if candidate.suffix == "":
            candidate = candidate.with_suffix(".tex")
        if candidate.exists() and candidate.suffix.lower() == ".tex":
            return "\n" + expand_tex(candidate, seen) + "\n"
        return match.group(0)

    return INPUT_RE.sub(repl, text)


def sanitize_tex(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\\url\|([^|]+)\|", r"\\url{\1}", text)
    list_env = r"(?:itemize|enumerate|description)"
    text = re.sub(rf"\\textit\{{\s*(\\begin\{{{list_env}\}})", r"\1", text)
    text = re.sub(rf"(\\end\{{{list_env}\}})\s*\}}", r"\1", text)
    return text


def document_body(text: str) -> str | None:
    match = re.search(r"\\begin\{document\}(.*?)\\end\{document\}", text, flags=re.S)
    if not match:
        return None
    return match.group(1)


def run_pandoc(source: Path, out_path: Path, media_dir: Path, temp_dir: Path) -> tuple[bool, str]:
    suffix = source.suffix.lower()
    temp_source = source
    args: list[str]

    if suffix == ".tex":
        temp_dir.mkdir(parents=True, exist_ok=True)
        text = sanitize_tex(expand_tex(source))
        digest = hashlib.sha1(str(source).encode("utf-8")).hexdigest()[:10]
        temp_source = temp_dir / f"{source.stem}-{digest}.tex"
        temp_source.write_text(text, encoding="utf-8")
        args = pandoc_tex_args(temp_source, source.parent, out_path)
    elif suffix == ".docx":
        args = [
            "pandoc",
            str(source),
            "--from",
            "docx",
            "--to",
            "markdown+tex_math_dollars+pipe_tables",
            "--wrap=none",
            "--extract-media",
            str(media_dir),
            "-o",
            str(out_path),
        ]
    elif suffix == ".md":
        shutil.copyfile(source, out_path)
        return True, ""
    else:
        return False, f"unsupported source type: {suffix}"

    result = subprocess.run(args, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    message = result.stdout + result.stderr
    if result.returncode == 0 and suffix == ".tex":
        try:
            too_short = len(out_path.read_text(encoding="utf-8").strip()) < 80
        except OSError:
            too_short = True
        if too_short:
            body = document_body(text)
            if body:
                body_source = temp_dir / f"{source.stem}-{hashlib.sha1((str(source) + '-body').encode('utf-8')).hexdigest()[:10]}-body.tex"
                body_source.write_text(body, encoding="utf-8")
                retry = subprocess.run(
                    pandoc_tex_args(body_source, source.parent, out_path),
                    text=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                if retry.returncode == 0:
                    return True, message + retry.stdout + retry.stderr
                return False, message + retry.stdout + retry.stderr
    return result.returncode == 0, message


def pandoc_tex_args(source: Path, resource_path: Path, out_path: Path) -> list[str]:
    return [
        "pandoc",
        str(source),
        "--from",
        "latex+raw_tex",
        "--to",
        "markdown+tex_math_dollars+raw_tex+pipe_tables",
        "--wrap=none",
        "--resource-path",
        str(resource_path),
        "-o",
        str(out_path),
    ]


def cleanup_markdown(text: str, page_title: str) -> str:
    text = text.replace("\r\n", "\n")
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"\n{3,}", "\n\n", text)
    lines = text.strip().splitlines()
    if lines:
        first = lines[0].strip()
        clean_title = page_title.strip().strip("'\"")
        if first.startswith("# ") and norm(first[2:]) == norm(clean_title):
            lines = lines[1:]
    text = "\n".join(lines).strip()
    text = text.replace("\\tightlist", "")
    text = clean_unrenderable_latex(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def clean_unrenderable_latex(text: str) -> str:
    text = re.sub(r"`\\eqref\{([^}]+)\}`\{=latex\}", r"(\1)", text)
    text = re.sub(r"`\\ref\{([^}]+)\}`\{=latex\}", r"\1", text)
    text = re.sub(r"`\\printbibliography(?:\{[^}]*\})?`\{=latex\}", "\n\n## 参考文献\n\n", text)
    text = re.sub(r"`\\(?:label|vfill)\{[^}]*\}`\{=latex\}", "", text)
    text = re.sub(r"`\\vfill`\{=latex\}", "", text)
    text = re.sub(r"\\label\{[^}]+\}", "", text)
    return text


def cleanup_pdf_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\f", "\n\n---\n\n")
    lines = [line.rstrip() for line in text.splitlines()]
    cleaned: list[str] = []
    blank = 0
    for line in lines:
        if line.strip():
            blank = 0
            cleaned.append(line)
        else:
            blank += 1
            if blank <= 1:
                cleaned.append("")
    text = "\n".join(cleaned)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def run_pdftotext(pdf_path: Path, out_path: Path) -> tuple[bool, str]:
    result = subprocess.run(
        ["pdftotext", "-layout", "-enc", "UTF-8", str(pdf_path), str(out_path)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.returncode == 0, result.stdout + result.stderr


def rel_url(path: Path, base: Path) -> str:
    return path.relative_to(base).as_posix()


def source_dirs_from_markdown(text: str) -> list[Path]:
    dirs: list[Path] = []
    for match in IMPORTED_FROM_RE.finditer(text):
        source = Path(match.group(1).strip())
        directory = source.parent if source.suffix else source
        if directory.exists() and directory not in dirs:
            dirs.append(directory)
    return dirs


def resolve_asset(raw_src: str, source_dirs: list[Path], page_dir: Path, media_dir: Path) -> str:
    raw_src = raw_src.strip().strip("'\"")
    if raw_src.startswith(("http://", "https://", "/")):
        return raw_src

    normalized = raw_src.replace("\\", "/")
    drive_path = re.search(r"[A-Za-z]:[/\\].*", raw_src)
    if drive_path:
        drive_candidate = Path(drive_path.group(0))
        if drive_candidate.exists():
            return copy_or_relativize_asset(drive_candidate, page_dir, media_dir)

    possible_absolute = Path(raw_src)
    if possible_absolute.is_absolute() and possible_absolute.exists():
        return copy_or_relativize_asset(possible_absolute, page_dir, media_dir)

    for source_dir in source_dirs:
        candidates = []
        direct = source_dir / normalized
        candidates.append(direct)
        if direct.suffix == "":
            candidates.extend(direct.with_suffix(ext) for ext in IMAGE_EXTENSIONS)
        candidates.extend(source_dir.rglob(Path(normalized).name))
        if Path(normalized).suffix == "":
            for ext in IMAGE_EXTENSIONS:
                candidates.extend(source_dir.rglob(Path(normalized).name + ext))

        for candidate in candidates:
            if candidate.exists() and candidate.is_file():
                return copy_or_relativize_asset(candidate, page_dir, media_dir)

    return raw_src


def copy_or_relativize_asset(asset: Path, page_dir: Path, media_dir: Path) -> str:
    asset = asset.resolve()
    page_dir = page_dir.resolve()
    try:
        return rel_url(asset, page_dir)
    except ValueError:
        pass

    media_dir.mkdir(parents=True, exist_ok=True)
    target = media_dir / asset.name
    if asset.suffix.lower() == ".pdf":
        target = media_dir / f"{asset.stem}.png"
        if not target.exists():
            output_prefix = media_dir / asset.stem
            subprocess.run(
                ["pdftoppm", "-singlefile", "-png", str(asset), str(output_prefix)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            if not target.exists():
                target = media_dir / asset.name
                shutil.copyfile(asset, target)
    elif not target.exists() or asset.stat().st_size != target.stat().st_size:
        shutil.copyfile(asset, target)
    return rel_url(target, page_dir)


def fix_markdown_assets(markdown: str, source_dirs: list[Path], page_dir: Path) -> str:
    if not source_dirs and "media/" not in markdown and "\\includegraphics" not in markdown:
        return markdown
    media_dir = page_dir / "media"

    def repl_include(match: re.Match[str]) -> str:
        src = resolve_asset(match.group(1), source_dirs, page_dir, media_dir)
        return f'<img src="{src}" />'

    def repl_html(match: re.Match[str]) -> str:
        src = resolve_asset(match.group("src"), source_dirs, page_dir, media_dir)
        return f'<img{match.group("before")}src="{src}"{match.group("after")}>'

    def repl_md(match: re.Match[str]) -> str:
        src = resolve_asset(match.group("src"), source_dirs, page_dir, media_dir)
        attrs = match.group("attrs") or ""
        return f"![{match.group('alt')}]({src}){attrs}"

    markdown = INCLUDEGRAPHICS_RE.sub(repl_include, markdown)
    markdown = HTML_IMG_RE.sub(repl_html, markdown)
    markdown = MD_IMAGE_RE.sub(repl_md, markdown)
    return markdown


def remove_link_from_body(body: str, href: str) -> str:
    pattern = re.compile(rf"^\s*\[[^\]]+\]\({re.escape(href)}\)\s*(?:  )?\s*$\n?", re.I | re.M)
    return pattern.sub("", body)


def import_record(
    repo: Path,
    record: LinkRecord,
    match: SourceMatch,
    temp_dir: Path,
    dry_run: bool,
    pdf_text_fallback: bool,
) -> dict[str, str | int | None]:
    status = {
        "content": str(record.content_path.relative_to(repo)),
        "href": record.href,
        "title": record.title,
        "source_pdf": str(match.source_pdf) if match.source_pdf else None,
        "source_file": str(match.source_file) if match.source_file else None,
        "reason": match.reason,
        "score": match.score,
        "status": "pending",
        "message": "",
    }
    if match.source_file is None:
        if pdf_text_fallback and record.site_pdf.exists():
            if dry_run:
                status["status"] = "dry-run-pdf-text"
                status["message"] = "PDF text fallback available"
                return status
            content_text = record.content_path.read_text(encoding="utf-8")
            front, body = split_front_matter(content_text)
            converted_path = temp_dir / f"{record.content_path.parent.name}-{hashlib.sha1(record.href.encode()).hexdigest()[:8]}-pdf.txt"
            ok, message = run_pdftotext(record.site_pdf, converted_path)
            if not ok:
                status["status"] = "failed"
                status["message"] = message.strip()
                return status
            converted = cleanup_pdf_text(converted_path.read_text(encoding="utf-8", errors="replace"))
            if len(converted.strip()) < 80:
                status["status"] = "failed"
                status["message"] = "extracted PDF text is suspiciously short"
                return status
            new_body = remove_link_from_body(body, record.href).rstrip()
            if new_body:
                new_body += "\n\n"
            new_body += f"<!-- Imported from PDF text extraction: {record.site_pdf} -->\n\n"
            new_body += converted
            record.content_path.write_text(front + new_body.rstrip() + "\n", encoding="utf-8")
            status["status"] = "extracted-pdf"
            status["message"] = f"{len(converted)} markdown chars"
            return status
        status["status"] = "skipped"
        status["message"] = "no source file"
        return status

    if dry_run:
        status["status"] = "dry-run"
        return status

    content_text = record.content_path.read_text(encoding="utf-8")
    front, body = split_front_matter(content_text)
    import_key = f"Imported from {match.source_file}"
    if import_key in body and record.href not in body:
        status["status"] = "skipped"
        status["message"] = "already imported"
        return status

    media_dir = record.content_path.parent / "media"
    converted_path = temp_dir / f"{record.content_path.parent.name}-{hashlib.sha1(record.href.encode()).hexdigest()[:8]}.md"
    ok, message = run_pandoc(match.source_file, converted_path, media_dir, temp_dir)
    if not ok:
        status["status"] = "failed"
        status["message"] = message.strip()
        return status

    converted = cleanup_markdown(converted_path.read_text(encoding="utf-8"), record.title)
    converted = fix_markdown_assets(converted, [match.source_file.parent], record.content_path.parent)
    if len(converted.strip()) < 80:
        status["status"] = "failed"
        status["message"] = "converted markdown is suspiciously short"
        return status

    new_body = remove_link_from_body(body, record.href).rstrip()
    if new_body:
        new_body += "\n\n"
    new_body += f"<!-- {import_key} -->\n\n"
    new_body += converted
    record.content_path.write_text(front + new_body.rstrip() + "\n", encoding="utf-8")
    status["status"] = "imported"
    status["message"] = f"{len(converted)} markdown chars"
    return status


def fix_existing_assets(repo: Path, content_globs: list[str]) -> list[dict[str, str]]:
    paths: list[Path] = []
    for pattern in content_globs:
        paths.extend(repo.glob(pattern))
    results: list[dict[str, str]] = []
    for path in sorted(set(paths)):
        text = path.read_text(encoding="utf-8")
        source_dirs = source_dirs_from_markdown(text)
        if not source_dirs:
            continue
        fixed = fix_markdown_assets(text, source_dirs, path.parent)
        if fixed != text:
            path.write_text(fixed, encoding="utf-8")
            results.append({"content": str(path.relative_to(repo)), "status": "fixed-assets"})
    return results


def strip_import_comments_and_local_alt_text(repo: Path, content_globs: list[str]) -> list[dict[str, str]]:
    paths: list[Path] = []
    for pattern in content_globs:
        paths.extend(repo.glob(pattern))
    results: list[dict[str, str]] = []
    for path in sorted(set(paths)):
        text = path.read_text(encoding="utf-8")
        fixed = text
        touched = False
        next_fixed = re.sub(r"\n?<!-- Imported from .*? -->\n?", "\n", fixed)
        if next_fixed != fixed:
            touched = True
            fixed = next_fixed
        next_fixed = re.sub(r"\n?<!-- Imported from PDF text extraction: .*? -->\n?", "\n", fixed)
        if next_fixed != fixed:
            touched = True
            fixed = next_fixed

        def clean_alt(match: re.Match[str]) -> str:
            nonlocal touched
            alt = match.group("alt")
            if re.search(r"[A-Za-z]:\\", alt):
                alt = ""
                touched = True
            return f"![{alt}]({match.group('src')}){match.group('attrs') or ''}"

        fixed = MD_IMAGE_RE.sub(clean_alt, fixed)
        if touched:
            fixed = re.sub(r"\n{3,}", "\n\n", fixed)
        if fixed != text:
            path.write_text(fixed, encoding="utf-8")
            results.append({"content": str(path.relative_to(repo)), "status": "stripped-local-paths"})
    return results


def trim_trailing_whitespace(repo: Path, content_globs: list[str]) -> list[dict[str, str]]:
    paths: list[Path] = []
    for pattern in content_globs:
        paths.extend(repo.glob(pattern))
    results: list[dict[str, str]] = []
    for path in sorted(set(paths)):
        text = path.read_text(encoding="utf-8")
        fixed = "\n".join(line.rstrip() for line in text.splitlines())
        if text.endswith("\n"):
            fixed += "\n"
        if fixed != text:
            path.write_text(fixed, encoding="utf-8")
            results.append({"content": str(path.relative_to(repo)), "status": "trimmed"})
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Import PDF source content into Hugo Markdown page bundles.")
    parser.add_argument(
        "--source-root",
        default=os.environ.get(SOURCE_ROOT_ENV),
        help=f"Root directory containing source files. Can also be set with {SOURCE_ROOT_ENV}.",
    )
    parser.add_argument(
        "--source-map",
        type=Path,
        default=None,
        help="Optional private JSON map of PDF hrefs to source paths. Relative paths resolve under --source-root.",
    )
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--fix-assets", action="store_true")
    parser.add_argument("--strip-local-paths", action="store_true")
    parser.add_argument("--trim-trailing-whitespace", action="store_true")
    parser.add_argument("--pdf-text-fallback", action="store_true")
    parser.add_argument("--report", default=".codex_tmp_pdf_import/report.json")
    parser.add_argument(
        "--glob",
        action="append",
        default=["content/blog/**/index.md", "content/tech/**/index.md"],
        help="Content glob to scan. May be passed multiple times.",
    )
    args = parser.parse_args()

    repo = Path.cwd()
    temp_dir = repo / ".codex_tmp_pdf_import"
    temp_dir.mkdir(parents=True, exist_ok=True)

    if args.fix_assets:
        results = fix_existing_assets(repo, args.glob)
        report_path = repo / args.report
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({"counts": {"fixed-assets": len(results)}, "report": str(report_path)}, ensure_ascii=False, indent=2))
        return 0

    if args.strip_local_paths:
        results = strip_import_comments_and_local_alt_text(repo, args.glob)
        report_path = repo / args.report
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({"counts": {"stripped-local-paths": len(results)}, "report": str(report_path)}, ensure_ascii=False, indent=2))
        return 0

    if args.trim_trailing_whitespace:
        results = trim_trailing_whitespace(repo, args.glob)
        report_path = repo / args.report
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({"counts": {"trimmed": len(results)}, "report": str(report_path)}, ensure_ascii=False, indent=2))
        return 0

    if not args.source_root:
        print(
            f"error: --source-root is required for import mode, or set {SOURCE_ROOT_ENV}",
            file=sys.stderr,
        )
        return 2

    source_root = Path(args.source_root)
    if not source_root.exists():
        print(f"error: source root does not exist: {source_root}", file=sys.stderr)
        return 2

    records = find_pdf_links(repo, args.glob)
    source_pdfs, source_files = build_source_index(source_root)
    manual_sources = load_manual_source_map(source_root, args.source_map)
    matches = [
        (record, match_record(record, source_pdfs, source_files, manual_sources))
        for record in records
    ]

    results = [
        import_record(
            repo,
            record,
            match,
            temp_dir,
            dry_run=not args.apply,
            pdf_text_fallback=args.pdf_text_fallback,
        )
        for record, match in matches
    ]
    report_path = repo / args.report
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")

    counts: dict[str, int] = {}
    for result in results:
        counts[str(result["status"])] = counts.get(str(result["status"]), 0) + 1
    print(json.dumps({"counts": counts, "report": str(report_path)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
