# Tao Migration Design

**Date:** 2026-04-07

## Goal

Retire the separate `../tao` Flowershow site by moving its content into this repo under `/tao`, while reusing the Tao artwork as the main site navbar icon and favicon.

## Decisions

- Create a new top-level `tao/` section in this repo.
- Convert `../tao/README.md` into `tao/index.md`.
- Preserve the existing Tao pages inside `tao/` as standalone markdown files.
- Do not keep `tao/z/` as a separate subtree here.
- Move `../tao/z/Whimsical way reduce meetings.md` into the main `ref/` collection for now.
- Copy the Tao images into this repo and reference them from the main `config.json`.
- Update the main navbar `Tao` link from the external hostname to `/tao`.

## Rationale

This keeps the migration low-risk and keeps the redirect story simple: the old Tao host can redirect into `/tao/*` on the main site. Keeping Tao as its own section avoids forcing editorial decisions about where each page belongs in the broader site taxonomy.

## Paths

- Content: `tao/`
- Imported images: `images/tao/`
- Migrated note from `z/`: `ref/`
- Site config: `config.json`

## Notes

- `logs/2026-04-03.md` was already untracked before this migration and is unrelated.
