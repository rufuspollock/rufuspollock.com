# Content Rules

See `info-architecture-for-this-site.md` for the full rationale behind these decisions.

## Structure

```
/                    ← everything: notes, essays, concepts, ideas, books, films
  economics.md
  Anna Karenina.md

/logs                ← daily log only; date IS the identity
  2026-05-10.md

/projects            ← discrete scoped work with its own lifecycle
  /open-knowledge-foundation
```

Three buckets. New content → root, no decision required.

**Exception: large topics.** A topic with many sub-files (e.g. `wto/`) can have its own folder — but root entry (`wto.md`) still exists as the primary page.

## Filenames

Natural language, Wikipedia-style. Title case for proper nouns, lowercase for concepts.

```
Anna Karenina.md          ← not anna-karenina.md
Superintelligence.md
economics.md
wise society.md
```

- No type suffix — type is a tag
- No date in filename — goes in `created:` frontmatter
- No author/year suffix — goes in frontmatter
- Disambiguation only when needed: `Anna Karenina (1997 film).md`
- Daily logs: date only — `logs/2026-05-10.md`

## Frontmatter

Minimum at capture time:

```yaml
---
created: YYYY-MM-DD
---
```

Add tags when known. Nothing else required at capture time.

## Tags

```yaml
tags: [post]        ← finished, polished — appears on blog feed
tags: [stub]        ← fragment or WIP
tags: [bookmark]    ← link/clipping from elsewhere
tags: [book]        ← book entry
tags: [film]        ← film entry
tags: [article]     ← paper or essay by someone else
```

Tags compose: `tags: [book, stub]` for book notes in progress.

## Creating new files

1. Place at **root** — not in any subfolder (exceptions: `logs/`, `projects/`)
2. Filename: natural language, title case for proper nouns
3. Add `created: YYYY-MM-DD` in frontmatter
4. Tags optional, add later

Do not create new type-based folders (blog/, notes/, ref/, post/, works/, nonfiction/, etc.).

## Content conventions

- Markdown with YAML frontmatter
- Wiki-style links: `[[Anna Karenina]]`
- YouTube embeds: `![[https://www.youtube.com/watch?v=VIDEO_ID]]`
- Do not use legacy embed formats: `{{< youtube ... >}}`, `[embed]...[/embed]`, raw `<iframe>`, `<object>`
