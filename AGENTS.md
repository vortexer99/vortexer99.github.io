# Repository Guidelines

## Project Structure & Module Organization

This repository hosts a personal academic site migrated from Jekyll/Academic Pages to HugoBlox. Current Hugo content lives in `content/`, with major sections such as `content/blog/`, `content/gallery/`, `content/tech/`, and `content/cv/`. Site configuration is under `config/`, HugoBlox metadata is in `hugoblox.yaml`, and custom templates live in `layouts/`. CSS and frontend assets belong in `assets/`; static legacy files that must keep their URLs go in `static/`, `files/`, or `images/`. Directories prefixed with `_` are legacy Jekyll material; avoid editing them unless working on migration or redirects.

## Build, Test, and Development Commands

Install dependencies with:

```bash
pnpm install
```

Run a local preview with:

```bash
pnpm run dev
```

Build the production site and generate the Chinese Pagefind index with:

```bash
pnpm run build
```

Run only search indexing after a Hugo build with:

```bash
pnpm run pagefind
```

Local builds require Hugo Extended matching `hugoblox.yaml` and Node.js/pnpm. GitHub Pages deployment runs through `.github/workflows/deploy.yml`, which calls `.github/workflows/build.yml`.

## Coding Style & Naming Conventions

Use UTF-8 for Markdown and configuration files. Prefer short, descriptive directory slugs for content bundles, for example `content/blog/my-note/index.md`. Keep front matter minimal but valid: dates must be parseable Hugo dates such as `2026-06-22`. Put site-wide visual tweaks in `assets/css/custom.css`; use local Hugo template overrides in `layouts/` only when configuration cannot solve the issue. Keep CSS scoped to clear classes to avoid affecting HugoBlox taxonomies globally.

## Testing Guidelines

There is no separate unit test suite. Treat `pnpm run build` as the main validation step. For search changes, verify `pnpm run pagefind` and keep `--force-language zh` so Chinese content remains searchable. For visual changes, check desktop and mobile pages locally before pushing, especially `blog`, `gallery`, `tech`, and the home page.

## Commit & Pull Request Guidelines

Recent commits use concise, imperative messages such as `Fix blog list hover state` and `Refine homepage updates section`. Follow that style: one focused change per commit, with a clear subject. Pull requests should describe what changed, note any HugoBlox template overrides, link related issues when available, and include screenshots for layout or typography changes. Confirm the GitHub Actions build passes before merging.

## Agent-Specific Instructions

On Windows, read Markdown with explicit UTF-8, for example `Get-Content -Raw -Encoding UTF8 content/blog/_index.md`. Do not edit legacy Jekyll directories unless requested. Avoid global taxonomy overrides unless the change is intended for every taxonomy page.
