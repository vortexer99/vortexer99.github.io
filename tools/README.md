# Site Manager

Local desktop assistant for managing this HugoBlox site.

Run from the repository root:

```powershell
.\tools\run-site-manager.ps1
```

The first version is a read-only content browser:

- Lists Hugo content files.
- Shows section, tags, authors, date, URL, aliases, file path, and content preview.
- Filters by section, tag, author, and free-text query.
- Opens the source Markdown file or the published page URL.

It uses PySide6, following the same desktop-reader style as `github-radar`.
