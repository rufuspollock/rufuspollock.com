---
title: Information Architecture for this Site
created: 2026-05-10
---

# Information Architecture for this Site

## Core Principle: Flat with Metadata

All content lives at root. Type is frontmatter metadata (tags), not folder location.

Inspired by Wikipedia: every page is equal. Search and backlinks handle discovery. Folders impose a decision cost at creation time that isn't worth paying.

## Structure

```
/                    ← everything: notes, essays, concepts, ideas
  economics.md
  wise-society.md
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

- Concept/essay files: topic slug, no date — `economics.md`, `wise-society.md`
- Daily logs: date only — `2026-05-10.md`
- Date goes in frontmatter (`created:`), not in the filename

Date in filename is only useful when the date is the primary identity (logs). For concepts, it's noise — it ages URLs and implies staleness.

## Fleeting vs Evergreen

Don't decide at creation. Write to root. Things that matter grow through expansion and incoming links. Things that don't — stay stubs. That's fine.

Use `#stub` tag in frontmatter if you want a signal, but don't let it gate creation or determine location.

## Migration

No big-bang migration needed. Gradually move `ref/` files to root as they come up. Kill empty legacy folders as they empty out.
