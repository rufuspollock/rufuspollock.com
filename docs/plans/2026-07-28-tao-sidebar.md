# TAO Sidebar Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Restrict Flowershow's generated sidebar to the TAO section without changing the TAO index page.

**Architecture:** Use Flowershow's documented route-aware sidebar configuration in the site's root `config.json`. The `/tao` prefix controls both where the sidebar appears and which content tree it displays.

**Tech Stack:** Flowershow, JSON, Markdown

---

### Task 1: Configure the TAO sidebar

**Files:**
- Modify: `config.json`

**Step 1: Add the minimal configuration**

Add `showSidebar: true` and a `sidebar` object containing `orderBy: "title"` and `paths: ["/tao"]`.

**Step 2: Validate JSON syntax and exact values**

Run a Node.js assertion that parses `config.json` and checks the three configured values.

Expected: command exits successfully with `TAO sidebar config valid`.

**Step 3: Verify scope**

Run `git diff --check` and confirm `git diff -- tao/index.md` is empty.

Expected: no whitespace errors and no TAO index changes.
