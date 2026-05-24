---
title: Rufu-7la Final Rufus Migration Plan
created: 2026-05-24
status: approved
source: /Users/rgrp/src/lifeitself/community
target: /Users/rgrp/src/me/rufuspollock.com
---

# Rufu-7la Final Rufus Migration Plan

## Summary

Migrate the remaining `rufuspollock.com` items from `~/src/lifeitself/community` into the personal site using the updated information architecture: flat root files, natural filenames, and type/status via tags.

Do not migrate into `post/`, `works/`, `ref/`, or other type folders.

Before moving files, update the manifest so it reflects the corrected rules:

- Remove stale `excalidraw/wisdom-gap-2020-05-08.excalidraw.md` because `community` deleted it as obsolete in commit `97667c6`.
- Update counts from `88` to `87`.
- Reduce `Blog postable maybe` from `47` to `46`.
- Replace kebab-case target paths with natural target names.

## Key Migration Rules

- Place migrated markdown at repo root except true discrete project folders; for this batch, default all content to root.
- Preserve natural source filenames when already good, e.g. `Annick de Witt.md`.
- Convert kebab/date/author-style filenames to natural names based on the work or page title.
- For book/work/article notes, use the bare work title as filename.
- Add `title:` frontmatter for fuller display/SEO titles, e.g. `title: "Superintelligence by Nick Bostrom (2014)"`.
- Add `created:` from source frontmatter first, then source `date`, then manifest created guess.
- Preserve useful existing frontmatter such as `authors`, `aliases`, `posted`, and source-specific metadata unless it conflicts with the information architecture.
- Do not add author/year/type suffixes to filenames.

Examples:

- `books/clear-2018-atomic-habits.md` -> `Atomic Habits.md`
- `books/yunkaporta-2019-sand-talk-how.md` -> `Sand Talk.md`
- `books/skidelsky-skidelsky-2013-how-much-enough.md` -> `How Much is Enough.md`

## Tags And Blog Postability

Use the updated information architecture tag vocabulary:

- `tags: [book]` for book notes.
- `tags: [article]` for notes on papers, essays, or articles by others.
- `tags: [bookmark]` for link/clipping notes such as the BBC bookmark.
- `tags: [stub]` for thin placeholders or skeletal notes.
- `tags: [post]` only when the migrated page is finished and should appear in the blog feed.

The manifest `Blog` column remains an editorial planning signal:

- `yes` means candidate for `tags: [post]`, but still requires duplicate and quality check.
- `maybe` means migrate as a note/work entry without `post`; keep the manifest/editorial signal for later.
- `no` means no `post` tag.

Default for this migration: do not automatically add `tags: [post]` to every `Blog: yes` item. Add `post` only for items that are clearly finished and not already represented by an existing personal-site post.

Existing duplicate example: `books/wilber-2017-trump-and-a-post-truth-world.md` already overlaps with `post/wilber-trump-post-truth-world.md`, so migrate or merge cautiously rather than creating a second surfaced post.

## Assets And Links

Use the existing personal-site asset pattern:

- Copy pasted images, PDFs, and note assets to `images/assets/`.
- Copy Excalidraw markdown and companion SVG files to `Excalidraw/`.
- Rewrite local embeds and links after copying:
  - `../assets/notes/foo.png` -> `images/assets/foo.png`
  - `excalidraw/foo.excalidraw.svg` -> `Excalidraw/foo.excalidraw.svg`
- Migrate only assets referenced by migrated files.
- Remove source assets from `community` only when they are tracked and no longer referenced by remaining community files.
- Do not restore or migrate the obsolete Wisdom Gap Excalidraw unless a later explicit decision reverses this plan.

## Implementation Sequence

1. Update and commit the manifest:
   - remove stale Wisdom Gap row
   - update summary counts
   - update target names to natural filenames
   - clarify tag/blog-postability rules in review notes
2. Generate a dry-run migration map:
   - source path
   - target filename
   - tags to add
   - assets to copy
   - source-local links to rewrite
   - collision status
3. Migrate markdown and assets into `rufuspollock.com`:
   - preserve source content
   - normalize frontmatter minimally
   - add required `created:`
   - add information architecture tags where clear
   - rewrite local asset and wiki links
4. Remove migrated source markdown and orphaned migrated assets from `community`.
5. Commit in small, reviewable commits:
   - docs manifest update in `rufuspollock.com`
   - content import in `rufuspollock.com`
   - source removals in `community`

## Test Plan

- Verify every non-stale manifest row exists in the target repo after migration.
- Verify every migrated source markdown file is removed from `community`.
- Verify every local asset reference in migrated files resolves to an existing file.
- Verify no referenced source asset is removed from `community` while still used by remaining community files.
- Run `rg` checks for stale source paths such as `../assets/notes`, `../../assets/notes`, and `excalidraw/`.
- Run the site build if the repo has a working build command; otherwise run static link/path checks and report that no build was available.
- Check `git status --short` in both repos before final report.

## Assumptions

- `info-architecture-for-this-site.md` and `AGENTS.md` override the older folder-based guidance in `README.md` for this migration.
- Existing user edits to `info-architecture-for-this-site.md` are intentional and should not be modified unless explicitly requested.
- The final migration should prepare content for the flat information architecture, not preserve legacy `works/`, `ref/`, or `post/` placement.
