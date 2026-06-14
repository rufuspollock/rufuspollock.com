---
created: 2026-06-14
tags: [pattern, howto]
---

# Managing Large Binary Assets in Project Repos

## The Problem

You're tracking a MacBook repair issue. You have a 90MB screen-flicker video, PDFs of Apple support correspondence, some screenshots. You want them linked from your project notes. But your notes live in a git repo — dumping 90MB videos into git is a bad idea (bloated history, slow clones, pain forever).

Different from a website build where assets need to be web-visible — here you just need assets findable locally and backed up.

## Pattern: Local `assets/` Folder + Google Drive Sync

```
~/planning/
  projects/
    macbook-repair.md       ← tracked in git
  assets/                   ← gitignored, synced via Google Drive
    macbook-repair/
      screen-flicker.mp4
      apple-support-thread.pdf
      genius-bar-receipt.pdf
```

Link from your notes:

```markdown
## Evidence
- [Screen flicker video](../assets/macbook-repair/screen-flicker.mp4)
- [Apple support thread](../assets/macbook-repair/apple-support-thread.pdf)
```

`.gitignore` entry:

```
assets/
```

## Setup: Google Drive Desktop Folder Sync

Google Drive Desktop can sync any local folder to Drive — you don't have to put files inside `~/Google Drive/`.

1. Open Google Drive Desktop → Preferences → **My Computer** tab
2. Add your `~/planning/assets/` folder
3. Done — files upload automatically on drop

Use **Stream** mode (not Mirror) if you don't want everything downloaded locally — files appear as stubs, download on demand when opened.

## Why This Works

- **Drop convenience** — drag file into `assets/macbook-repair/`, it's backed up and linkable. No upload dance.
- **Local editor links work** — relative paths, Obsidian links, all fine
- **Git stays clean** — no binary blobs, no LFS overhead
- **Backed up** — Google Drive handles it, survives laptop death
- **On-demand local storage** — Stream mode means 90MB video only downloads when you open it

## Related

- [[asset management in git-native publishing workflows]] — website/publishing context where assets need to be web-visible
