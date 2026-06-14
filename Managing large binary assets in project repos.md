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

## Limitations of Google Drive Desktop

The setup above works but has real constraints worth understanding:

- **"My Computer" backup and Stream mode are separate things.** Stream mode applies to Drive-native files, not to local folders you're backing up via the My Computer tab.
- **No local garbage collection.** Backing up a local folder uploads everything but does not evict files from your local machine. Your local folder stays full — no automatic space reclamation.
- **No control over destination subfolder.** Backed-up folders land under `Computers > [machine name]` in Drive. You can't freely choose where in your Drive hierarchy they go.

So if what you want is "stream a local folder with on-demand local eviction to save disk space" — Google Drive Desktop doesn't do that.

## Alternative: rclone + Cloudflare R2

rclone gives more control and is worth considering if you want the full behaviour:

**What you actually want:**
> Local `assets/` → cloud bucket, with a local cache that evicts old files to save space, and cloud keeps everything even after local delete.

**rclone + R2 gets close:**

- `rclone sync local/assets r2:my-bucket/assets` — controlled folder-to-folder mapping, run on demand or via cron
- `rclone mount r2:my-bucket/assets ~/assets` — mounts R2 as a local filesystem (FUSE). Acts like a network drive: writes upload to cloud, reads fetch from cloud. Bidirectional. Local cache size is configurable (`--vfs-cache-max-size`) so disk usage stays bounded.
- R2 versioning or lifecycle rules handle the "keep even after local delete" archive concern
- R2 egress is free (unlike S3), so streaming reads cost nothing

**Limitation of rclone mount:** not as polished as Google Drive — can be flaky, latency on first open, requires running a background process.

**Honest summary:** no tool does all of this smoothly on Mac today. Google Drive is polished but won't manage local disk space for you. rclone + R2 gives full control but requires more setup and tolerance for rough edges. If "just works" matters most, use Drive with Mirror mode and accept the local disk usage. If you want on-demand streaming with space management, rclone + R2 is the right direction.

## Related

- [[asset management in git-native publishing workflows]] — website/publishing context where assets need to be web-visible
