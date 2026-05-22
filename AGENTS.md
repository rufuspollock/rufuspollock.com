Read README.md for repo structure and conventions.

## Content capture rule

When creating a new file:
1. Place it at **root** — not in any subfolder (exceptions: `logs/`, `projects/`)
2. Filename: natural language, title case for proper nouns — `Anna Karenina.md`, `wise society.md`. No date, no type suffix, no author/year.
3. Add `created: YYYY-MM-DD` in frontmatter. Nothing else required at capture time.
4. Tags optional, add later: `tags: [post]` for finished essays, `tags: [bookmark]` for links/clippings, `tags: [stub]` for fragments.

Exceptions:
- Daily log → `logs/YYYY-MM-DD.md`
- Discrete project work → `projects/<project-name>/`
- Large topic with many sub-files → its own folder (e.g. `wto/`), but root entry still exists

Do not create new type-based folders (blog/, notes/, ref/, etc.).

## Content conventions
- For new YouTube embeds, use `![[https://www.youtube.com/watch?v=VIDEO_ID]]`.
- Do not use legacy YouTube formats such as `{{< youtube ... >}}`, `[embed]...[/embed]`, raw `<iframe>`, or `<object>` in newly created posts unless explicitly asked.
