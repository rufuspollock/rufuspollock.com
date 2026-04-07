# Tao Migration Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Move the sibling Tao site into this repo under `/tao`, update navigation to point there, and reuse the Tao image as the main site logo and favicon.

**Architecture:** Keep Tao as a self-contained content section at the repo top level so URLs stay simple and redirects from the retired host remain mechanical. Import the Tao image assets into this repo and update the shared site config to use local image paths for both the navbar icon and favicon.

**Tech Stack:** Flowershow markdown content, `config.json`, static image assets

---

### Task 1: Create the Tao section

**Files:**
- Create: `tao/index.md`
- Create: `tao/Hypotheses.md`
- Create: `tao/Issues.md`
- Create: `tao/Job Stories.md`
- Create: `tao/Meetings.md`
- Create: `tao/Standups.md`

**Step 1: Create `tao/index.md` from the old Tao README**

Preserve the copy with only path updates needed for local assets.

**Step 2: Copy the remaining Tao markdown pages into `tao/`**

Keep filenames stable so the section remains close to the source vault.

**Step 3: Adjust asset paths inside imported Tao pages**

Point image references at local repo-served paths instead of the sibling repo.

### Task 2: Import shared Tao assets and wire config

**Files:**
- Modify: `config.json`
- Create: `images/tao/climbing-mountain-liuzhou-man.jpg`
- Create: `images/tao/climbing-mountain-liuzhou.jpg`

**Step 1: Copy the two Tao images into `images/tao/`**

Keep the original filenames to reduce churn.

**Step 2: Update `config.json`**

- Change the `Tao` nav link to `/tao`
- Add a top-level `favicon` entry pointing at `/images/tao/climbing-mountain-liuzhou-man.jpg`
- Add `nav.logo` pointing at the same image

### Task 3: Rehome the stray Tao note into `ref/`

**Files:**
- Create: `ref/Whimsical way reduce meetings.md`

**Step 1: Copy the `../tao/z/Whimsical way reduce meetings.md` note into `ref/`**

Keep the content intact and continue linking to `[[Meetings]]` for now.

### Task 4: Verify the migration

**Files:**
- Review: `config.json`
- Review: `tao/`
- Review: `ref/Whimsical way reduce meetings.md`

**Step 1: Run `git diff --stat`**

Confirm the migration touched only the intended config, content, plan docs, and image paths.

**Step 2: Run `git diff -- config.json tao ref docs/plans`**

Check that nav, favicon, and imported markdown content all match the approved design.
