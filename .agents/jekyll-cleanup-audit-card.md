# Jekyll Legacy Cleanup Audit Card

Date: 2026-06-23
Repository: `D:\Documents\Utilcode\github\vortexer99.github.io`

## Goal

Audit and eventually clean legacy Jekyll / Academic Pages files after the site migration to HugoBlox, without breaking current Hugo build output or historical URLs.

## Current Assessment

The active site appears to be HugoBlox/Hugo-based:

- Current content lives under `content/`.
- Hugo config lives under `config/`.
- Current templates live under `layouts/`.
- Current CSS/assets live under `assets/`.
- `package.json` scripts call Hugo and Pagefind only:
  - `pnpm run dev` -> `hugo server --disableFastRender`
  - `pnpm run build` -> `hugo --minify && pnpm run pagefind`
  - `pnpm run pagefind` -> `pagefind --site public --force-language zh`

No active build script appears to call Jekyll, Bundler, Ruby, `_config.yml`, or `Gemfile`.

## Important Working Tree Context

At the time this card was written, the worktree already had unrelated uncommitted changes:

- Modified:
  - `config/_default/languages.yaml`
  - `config/_default/params.yaml`
  - `content/_index.md`
- Untracked:
  - `AGENTS.md`
  - `content/_index.zh.md`
  - `data/zh/`
  - `go.sum`
  - `hugo_stats.json`
  - `layouts/_partials/components/`

Do not revert or overwrite those changes while doing cleanup.

## Likely Safe Cleanup Candidates

These are legacy Jekyll / Academic Pages runtime or sample directories/files. They are not expected to be used by HugoBlox, but should still be deleted in a dedicated cleanup commit after a build check:

- `_includes/`
- `_layouts/`
- `_sass/`
- `_data/`
- `_drafts/`
- `_pages/`
- `_portfolio/`
- `_publications/`
- `_publications_copy/`
- `_talks/`
- `_talks_cpoy/`
- `_teaching/`
- `_conferences/`
- `_config.yml`
- `Gemfile`
- `markdown_generator/`
- `talkmap.py`
- `talkmap.ipynb`

Note: `_layouts/` is legacy Jekyll. Do not confuse it with active Hugo `layouts/`.

## Needs Extra Audit Before Deletion

`_posts/` should not be deleted blindly.

Observed counts:

- `content/`: 83 Markdown files
- `_posts/`: 70 Markdown files
- other old Jekyll content collections (`_pages`, `_talks`, `_publications`, `_teaching`, `_portfolio`, `_conferences`): 23 Markdown files

The count suggests many old posts may have been migrated, but title/date/slug coverage must be checked before removing `_posts/`.

Recommended audit:

1. Extract old `_posts/**/*.md` front matter titles, dates, and slugs.
2. Extract current `content/**/*.md` titles, dates, and slugs.
3. Compare by normalized title first, then date and slug.
4. Manually inspect unmatched old posts.
5. Confirm old public URLs either still exist, redirect, or are intentionally dropped.

## Do Not Delete Just Because It Looks Legacy

These paths can preserve current site behavior or old public URLs:

- `content/`
- `config/`
- `layouts/`
- `assets/`
- `static/`
- `files/`
- `images/`

`files/`, `images/`, and `static/` are especially important because old posts may link to assets there.

## Suggested Cleanup Workflow

1. Start from a clean or intentionally understood worktree.
2. Create a focused branch, for example `codex/cleanup-jekyll-legacy`.
3. First delete only the likely safe Jekyll runtime/template/generator files listed above, excluding `_posts/`.
4. Run:

   ```powershell
   pnpm run build
   ```

5. Inspect generated site for major pages:
   - home
   - blog
   - gallery
   - tech
   - cv
6. Commit this first cleanup if build passes.
7. Separately audit `_posts/` migration coverage.
8. Only delete `_posts/` after confirming migrated content and URL handling.

## Useful Commands

List tracked legacy files:

```powershell
git ls-files _conferences _data _drafts _includes _layouts _pages _portfolio _posts _publications _publications_copy _sass _talks _talks_cpoy _teaching Gemfile _config.yml markdown_generator talkmap.py talkmap.ipynb
```

Search current code for legacy references:

```powershell
rg -n "_posts|_pages|_includes|_layouts|_sass|_config\.yml|jekyll|academicpages|academic_pages" -g "!public/**" -g "!node_modules/**" -g "!resources/**" -g "!.git/**"
```

Count Markdown files:

```powershell
Get-ChildItem -Recurse -File -Filter *.md content | Measure-Object
Get-ChildItem -Recurse -File -Filter *.md _posts | Measure-Object
Get-ChildItem -Recurse -File -Filter *.md _pages,_talks,_publications,_teaching,_portfolio,_conferences | Measure-Object
```

## Final Recommendation

Proceed with cleanup, but split it into two commits:

1. Remove Jekyll infrastructure and sample collection files that are not referenced by Hugo.
2. Remove `_posts/` only after a migration coverage audit.

