# Content Rules

Full reference: `docs/conventions.md` (repo-only).
Published rationale: `info-architecture-for-this-site.md`.

## 30-second version

- **Three buckets:** `/` (everything — notes, essays, books, films), `/logs`
  (daily log, date is the identity), `/projects` (scoped work). New content →
  root, no decision required. Do not create type-based folders (`blog/`, `ref/`,
  `post/`, …).
- **Filenames:** natural language, sentence case — `Anna Karenina.md`, not
  `anna-karenina.md`. No type suffix, no date, no author/year in the name.
- **Frontmatter:** `created: YYYY-MM-DD` is the only thing required at capture.
  Add `tags` when known.
- **Type tags:** `post` (on the feed), `stub` (WIP), `bookmark`, `book`, `film`,
  `article`, `essay`. They compose: `[book, stub]`.
- **Essay growth stage:** tag is canonical, emoji line is the skin.
  `stub`→🌱 **Seed**, `draft`→🌿 **Draft**, `post`→🌳 **Evergreen**. First body
  line after the `# H1`: `<emoji> **<label>** — <short status>`.
- **Links & embeds:** `[[Wiki links]]`; YouTube as
  `![[https://www.youtube.com/watch?v=ID]]`. No `{{< youtube >}}`, `[embed]`, raw
  `<iframe>`.
- **`config.json`:** never guess keys — fetch
  `https://flowershow.app/docs/reference/config-file.md`.
