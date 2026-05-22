---
title: Info Architecture Migration Plan
created: 2026-05-10
status: draft
---

# Info Architecture Migration Plan

Implements the structure defined in `/info-architecture-for-this-site.md`.

## Jobs to Be Done (JTBD)

Two audiences: **self** (personal knowledge base + retrieval) and **general public** (readers finding essays via search or sharing). Both matter; they pull in different directions.

### J1: Fast capture — zero friction, zero decisions

> "I have an idea / link / fragment / full essay. I want it saved immediately with no overhead."

- Modes: desktop editor, Claude agent, copy-paste from web
- Rule must be simple enough for Claude to follow without asking
- No decision about type, folder, or status at capture time
- Add metadata later, not now

### J2: Public reading — polished essays surfaced for strangers

> "Someone lands on the site. What should they see?"

- Blog/essays feed = finished, intentional work only
- Distinction from notes: **polish and completeness**, not topic or length
- Notes are public too but not prominently surfaced — a reader who finds one should be fine, but they're not the shop window

### J3: Personal retrieval — find my own stuff fast

> "I wrote something about X six months ago. Where is it?"

- Search is primary
- Backlinks and `related:` frontmatter are secondary
- Recent changes feed serves this too (what was I working on?)

### J4: Recent changes — what's new or updated

> "What have I added or changed lately?"

- Serves both self (navigation, memory) and public (signal of activity)
- Driven by git commit date or `updated:` frontmatter field — TBD

These jobs drive the tag/metadata decisions below.

## Goal

Collapse false taxonomy folders into root. Result: flat structure with `/logs` and `/projects` as the only permanent special-purpose folders.

## Metadata / Tagging Design

Folder location no longer signals type. Tags do instead — additive, composable, no forced exclusivity (same reason Wikipedia uses categories not folders).

Key frontmatter fields:

| Field | Purpose |
|-------|---------|
| `created:` | Date first written |
| `updated:` | Drives "recent changes" feed |
| `tags:` | List — see tag vocabulary below |

### Tag vocabulary

| Tag | Meaning |
|-----|---------|
| `post` | Finished, polished — appears on blog feed |
| `stub` | Fragment or WIP — don't surface prominently |
| `bookmark` | Link/clipping from elsewhere |

Tags compose freely: a file can be `[post, stub]` while being revised, or `[bookmark, post]` if a clipping grew into an essay.

- Blog page = filter `tags contains post`
- Recent changes = sort by `updated:` or git commit date
- No tag required at capture — add later

**Capture rule (for humans and AI agents):**
> Create file at root. Filename = topic slug (no date). Add `created:` in frontmatter. Done. Tags can be added later.

## Audit Findings

### Folder inventory

| Folder | Files | Notes |
|--------|-------|-------|
| `post/` | 666 | WordPress-era blog posts. 589 have `wordpress:` frontmatter. 620 have `slug:`. These are the bulk of public URL history. |
| `ref/` | 34 | Dated notes (no WordPress history). Safe to move to root. |
| `nonfiction/` | 9 | WordPress provenance (`slug:`, `wordpress:`). Need redirects before move. |
| `works/` | 5 | Book reviews/notes. No index file. No WordPress frontmatter apparent. Low risk. |
| `clippings/` | 6 | Article titles as filenames. No WordPress history. Move to root with `type: bookmark`. |
| `research/` | 10 | Nested deep: `research/economics/papers/`, `research/economics/notes/`, `research/economics/teaching/`. Treat as topic folder, keep as-is. |
| `misc/` | 4 | `alternative-management.md`, `investing-reading-list.md`, `note-taking-software.md`, `index.md`. Move to root. |
| `writings/` | 1 | Just `index.md` — nav link target, currently a stub page. Keep as nav stub or redesign. |
| `speaking/` | 2 | `archive.md`, `index.md`. Not in nav. Low priority. |
| `blog/` | 2 | `index.md` + `all.md` — these are Flowershow page templates, not content. `index.md` uses `<List dir="/post" pageSize={30} />`. |
| `book/` | 1 | `index.md` only. Nav link target. Keep. |
| `content/` | 0 | Empty. Delete. |
| `papers/` | 0 md | Contains PDFs and other assets — holdovers from past. URLs may matter. Leave as-is, assess separately. |

### How the blog feed currently works

`blog/index.md` contains `<List dir="/post" pageSize={30} />` — Flowershow MDX component that reads from `/post/`. Moving posts to root requires changing this to filter by `type: post` frontmatter instead. This is the key technical change.

### Nav hardcoded paths (config.json)

`/about`, `/now`, `/tao`, `/writings`, `/projects`, `/book`, `/blog`, `/newsletter`, `/contact`

`/writings` and `/blog` are nav links. Both need to keep working after migration (either via redirect or kept as index stubs).

### Redirect situation

- `post/` URLs are the biggest risk: 620 files with slugs, many with WordPress history. These live at `/post/slug` currently. Target after migration: `/slug`.
- Redirects: mix of Flowershow config + Cloudflare. Scale is the constraint, not mechanism.
- Existing redirect log exists — check before adding new ones.

## Folders to Kill

| Folder | Action | Risk |
|--------|--------|------|
| `ref/` | Move to root | Low — no public URL history |
| `nonfiction/` | Move to root + redirects from `/nonfiction/slug` | Medium — WordPress provenance |
| `works/` | Move to root | Low |
| `clippings/` | Move to root, add `type: bookmark` | Low |
| `misc/` | Move to root (minus index.md) | Low |
| `speaking/` | Assess; likely move archive.md to root | Low |
| `content/` | Delete (empty) | None |
| `papers/` | Delete (empty) | None |
| `post/` | **Big lift** — keep folder but change blog mechanism to filter by `type: post`; OR mass-move + bulk redirects | High |

## Folders to Keep

| Folder | Reason |
|--------|--------|
| `logs/` | Correct structure, date = identity |
| `projects/` | Correct structure |
| `tao/` | Leave for now |
| `wto/` | Large topic, size management |
| `research/` | Deep topic nesting, keep as-is |
| `about/` | Functional site section |
| `book/` | Nav target |
| `blog/` | Keep as nav stub; update List component to use `type: post` filter instead of `dir="/post"` |
| `writings/` | Nav target — redesign or redirect |

## Redirects

- Flowershow + Cloudflare (mix fine)
- Check existing redirect log before adding
- Add redirects before or simultaneously with file moves — never after
- `post/` is the big one: 620 potential redirects `/post/slug` → `/slug`

## Steps

### Filename convention for moved files

Natural language, Wikipedia-style. When moving a file:
- Rename to natural title if currently kebab: `superintelligence-bostrom-2014.md` → `Superintelligence.md`
- No type suffix: `Anna Karenina.md` not `Anna Karenina Book.md`
- No date/author suffix: goes in frontmatter
- Existing kebab files at root: leave as-is (not worth migrating)

### 1. Quick wins (low risk, do now)

- [ ] Delete empty folder: `content/`
- [ ] Move `ref/` files to root
- [ ] Move `clippings/` to root, add `tags: [bookmark]` to frontmatter
- [ ] Move `works/` to root (rename to natural titles)
- [ ] Move `misc/` content files to root (drop index.md)

### 2. Metadata + blog mechanism redesign

- [x] Replace `<List dir="/post">` in `blog/index.md` with "under construction, use search" notice
- [ ] ~~Update List component to filter by `tags: [post]`~~ — blocked: Flowershow has no clean tag-filter listing yet. Revisit when available via [obsidian-bases](https://flowershow.app/docs/reference/obsidian-bases.md)
- [ ] Decide how "recent changes" feed works (git date vs `updated:` field)
- [ ] Write capture rule for AGENTS.md

### 3. Medium-risk moves

- [ ] Move `nonfiction/` to root — add redirects from `/nonfiction/slug` → `/slug`
- [ ] Move `speaking/archive.md` to root

### 4. Big lift — `post/` folder

Options:
- **A. Keep `/post/` folder** — just change blog mechanism to `type: post` filter. Zero URL breakage. Clean separation of legacy from new.
- **B. Move to root** — mass move + 620 bulk redirects. Cleaner long-term but high effort.

Recommendation: **Option A first**. Change the mechanism, leave files in place. Migrate individual posts to root over time as they're touched.

### 5. Cleanup

- [ ] Update `info-architecture-for-this-site.md` if decisions changed
- [ ] Verify site builds

## Out of Scope (for now)

- `tao/` — leave as-is
- `research/` — deep topic structure, leave
- `wp-content/` — separate cleanup task

## Risk Summary

| Action | Risk |
|--------|------|
| Delete empty folders | None |
| Move ref/, clippings/, works/, misc/ | Low |
| Move nonfiction/ | Medium (redirects needed) |
| Redesign blog mechanism | Medium (test build after) |
| Move post/ to root | High (bulk redirects, defer) |
