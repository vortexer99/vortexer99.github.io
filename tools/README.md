# Site Manager

Local desktop assistant for managing this HugoBlox site.

Run from the repository root:

```powershell
.\tools\run-site-manager.ps1
```

Current features:

- Lists Hugo content files.
- Shows section, legacy tags, normalized taxonomies, authors, date, URL, aliases, file path, and content preview.
- Filters by section, legacy tag, type, topic, project, length, author, and free-text query.
- Edits ordinary Markdown posts in place, including title, date, URL, authors, tags, types, topics, project tags, lengths, aliases, page type, and body text.
- Normalizes `types`, `topics`, `project_tags`, and `lengths` from the imported legacy `tags`.
- Protects complex landing pages by making them read-only in the editor. Use `Open File` for manual edits to pages with nested front matter such as `sections`.
- Opens the source Markdown file or the published page URL.

It uses PySide6, following the same desktop-reader style as `github-radar`.
