---
title: Site Conventions
created: 2026-08-30
---

# Site Conventions

Single source of truth for how this site's content is structured. Repo-only —
excluded from publishing via `contentExclude` in `config.json`. The reader-facing
narrative and rationale live in `info-architecture-for-this-site.md` (published).

`AGENTS.md` is the 30-second version for agents; this file is the full reference.

## Structure

Three buckets. Everything else is a mistake waiting to be collapsed.

```
/            ← everything: notes, essays, concepts, ideas, books, films
/logs        ← daily log only; the date IS the identity (logs/2026-05-10.md)
/projects    ← discrete scoped work with its own lifecycle
```

New content → root. No decision required.

**Exception: large topics.** A topic with many sub-files (e.g. `wto/`) may have
its own folder for overflow storage, but the root entry (`wto.md`) still exists
and is the primary page. Folder = size management, not taxonomy.

Do not create new type-based folders (`blog/`, `notes/`, `ref/`, `post/`,
`works/`, `nonfiction/`, …). Those five names were the same concept; they are dead.

## Filenames

Natural language, Wikipedia-style sentence case. Capitalize the first word and
proper nouns; other words lowercase.

```
Anna Karenina.md          not  anna-karenina.md
Superintelligence.md
Economics.md
Wise society.md
```

- No type suffix — type is a tag.
- No date in filename — goes in `created:` frontmatter. Exception: daily logs.
- No author/year suffix — goes in frontmatter.
- Disambiguation only when genuinely needed: `Anna Karenina (1997 film).md`.
- Existing kebab-case files: leave as-is, not worth migrating.
- URLs: Flowershow slugifies (`/Anna+Karenina`) and rewrites `[[wikilinks]]`
  automatically.

## Frontmatter

Minimum at capture time:

```yaml
---
created: YYYY-MM-DD
---
```

Add `tags` when known. For books/films/articles, `title:` carries the full
display title:

```yaml
# Superintelligence.md
title: "Superintelligence by Nick Bostrom (2014)"
tags: [book]
```

Nothing else is required at capture time. Don't block capture on metadata.

## Type tags

```yaml
tags: [post]        finished, polished — appears on the blog feed
tags: [stub]        fragment or WIP
tags: [bookmark]    link / clipping from elsewhere
tags: [book]        book entry
tags: [film]        film entry
tags: [article]     paper or essay by someone else
tags: [essay]       an original argued piece (mine), long or short
```

Tags compose: `[book, stub]` for a book note in progress, `[essay, draft]` for a
half-written essay.

## Growth stage (essays)

Essays carry a growth stage. The **tag is the canonical state**; the emoji line is
the human-facing skin. Scoped to essays for now — books, films, and bookmarks have
their own lifecycle and don't use this ladder.

| Tag     | Emoji | Body label   | Meaning                                        |
|---------|-------|--------------|-----------------------------------------------|
| `stub`  | 🌱    | **Seed**     | captured, not yet written up                   |
| `draft` | 🌿    | **Draft**    | first pass; argument roughed in, gaps flagged  |
| `post`  | 🌳    | **Evergreen**| finished and polished; on the blog feed        |

Convention: the first line of the body, immediately after the `# H1`, states the
stage:

```markdown
# The Information Design of Footnotes

🌿 **Draft** — first pass, from a long-standing note. Rough but the argument is complete.
```

Keep it to one line: `<emoji> **<label>** — <short status>`. Update the tag and
the line together when a piece moves up the ladder.

## Content conventions

- Markdown with YAML frontmatter.
- Wiki-style links: `[[Anna Karenina]]`.
- YouTube embeds: `![[https://www.youtube.com/watch?v=VIDEO_ID]]`.
- Do not use legacy embed formats: `{{< youtube … >}}`, `[embed]…[/embed]`, raw
  `<iframe>` or `<object>`.

## Publishing

- GitHub-connected: Flowershow rebuilds on push to `main`.
- `config.json` holds site config. Never guess keys — fetch the schema:
  `https://flowershow.app/docs/reference/config-file.md`.
- `contentExclude: string[]` — paths not published and not reachable by URL
  (`/docs` is excluded).
- `contentHide: string[]` — published but hidden from nav and search.
- `redirects` — old URL → new URL, one entry per moved page.

## Not yet written

- **Projects data model** — the frontmatter schema and lifecycle for `/projects`
  entries (status, dates, links, historical-CV entries).

## Related

- `info-architecture-for-this-site.md` — published rationale + key decisions.
- `AGENTS.md` — short agent-facing version.
- `kmojis.md` — published guide to knowledge-work / task emojis (distinct from
  the growth-stage emojis above).
- `docs/plans/` — dated design and migration docs.
