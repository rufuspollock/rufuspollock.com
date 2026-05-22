---
title: Information Architecture for this Site
created: 2026-05-10
---

# Information Architecture for this Site

## Core Principle: Flat with Metadata

All content lives at root. Type is frontmatter tags, not folder location.

Inspired by Wikipedia: every page is equal. Search and backlinks handle discovery. Folders impose a decision cost at creation time that isn't worth paying.

## Structure

```
/                    ← everything: notes, essays, concepts, ideas
  economics.md
  Anna Karenina.md
  info-architecture-for-this-site.md   ← this file

/logs                ← daily log only; date IS the identity
  2025-10-20.md
  2026-05-10.md

/projects            ← discrete scoped work with its own lifecycle
  /open-knowledge-foundation
```

Three buckets. Simple enough to hold in your head. New content → root, no decision required.

**Exception: large topics.** A topic with many sub-files (e.g. `wto/`) can have its own folder — but the folder is not a collection type, it's just overflow storage for one topic. The root entry (`wto.md`) still exists and is the primary page. Folder = size management, not taxonomy.

## What Dies

Folders that imposed false taxonomy, now collapsed into root:

- `ref/` — these were just dated notes; they belong at root
- `blog/`, `post/`, `writings/`, `nonfiction/`, `works/` — same concept, five names

## Filenames

**Natural language, Wikipedia-style.** Title case for proper nouns and titles, lowercase for concepts.

```
Anna Karenina.md          ← not anna-karenina-book.md
Superintelligence.md      ← not superintelligence-bostrom-2014.md
economics.md              ← concept, lowercase fine
wise society.md           ← or "Wise Society.md"
```

- No type suffix in filename — type is a tag, not the name
- No date in filename — date goes in `created:` frontmatter
- No author/year suffix — goes in frontmatter
- Disambiguation only when genuinely needed: `Anna Karenina.md` (novel) vs `Anna Karenina (1997 film).md`
- Obsidian backlinks stay clean: `[[Anna Karenina]]` not `[[anna-karenina|Anna Karenina]]`
- URLs: publishing layer (Flowershow) slugifies to `/anna-karenina` automatically

Daily logs: date only — `2026-05-10.md`

Existing kebab-case files (`economics.md`, `wise-society.md`): leave as-is, not worth migrating.

## Tags

```yaml
tags: [post]        ← finished, polished — appears on blog feed
tags: [stub]        ← fragment or WIP
tags: [bookmark]    ← link/clipping from elsewhere
```

Tags compose: `tags: [post, stub]` while revising. Add later — don't block capture on it.

## Fleeting vs Evergreen

Don't decide at creation. Write to root. Things that matter grow through expansion and incoming links. Things that don't — stay stubs. That's fine.

## Migration

No big-bang migration needed. Gradually move legacy folder files to root as they come up. Kill empty folders as they empty out. See `docs/plans/2026-05-10-info-architecture-migration.md`.

---

## Appendix: Key Decisions

### A1. Flat structure vs folder taxonomy

**Decision:** Flat root with tags.

| Option | Pro | Con |
|--------|-----|-----|
| Folder per type (blog/, notes/, etc.) | Familiar, browsable | Decision cost at creation; same content fits multiple folders; rigid |
| Flat + tags | Zero capture friction; composable; Wikipedia-proven | Requires tag discipline over time |

Tags win because decision fatigue at creation time is the real enemy. Folder location can't be added "later" without moving files; tags can.

### A2. Filename style: kebab-case vs natural language

**Decision:** Natural language, Wikipedia-style.

| Option | Pro | Con |
|--------|-----|-----|
| `anna-karenina.md` | Shell-friendly, URL-safe | Obsidian links need aliases; unnatural to read/type |
| `Anna Karenina.md` | Clean Obsidian links `[[Anna Karenina]]`; matches human mental model; Wikipedia-proven at scale | Spaces need escaping in shell |

Natural language wins. URL encoding of spaces is invisible in modern browsers; Flowershow slugifies to `/anna-karenina` at the URL layer anyway. Shell friction is real but minor compared to daily Obsidian use.

### A3. Type suffix in filename vs tags

**Decision:** No suffix. Type is a tag.

`Anna Karenina Book.md` vs `Anna Karenina.md` + `tags: [book-review]`

Suffix forces a decision upfront and creates naming drift (`Book` vs `Book Review` vs `Notes`). Tag added later, composes with others, easily changed.

### A4. Date in filename vs frontmatter

**Decision:** Date in frontmatter (`created:`), not filename — except logs where date IS the identity.

Date in filename implies the content is anchored in time and signals staleness to readers. Concepts don't have a birthday worth advertising. Git history is the authoritative record anyway.
