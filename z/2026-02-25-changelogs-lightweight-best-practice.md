---
title: "Changelogs: Write Them or Generate Them?"
date: 2026-02-25
---

# Changelogs: Write Them or Generate Them?

I work across several projects — small tools, larger applications, org-wide software — and keeping a changelog is one of those things I know I should do and keep not doing consistently.

Software projects need changelogs so users know what's changed — traditionally a `CHANGELOG.md` in the repo, now increasingly a dedicated page on the project website. The hard part isn't the format, it's the discipline. Changelog entries require a conscious moment of "now I will write this up" — easy to forget, easy to defer, and annoying as overhead when you're in flow. You could generate them automatically from Git commits, but raw commit logs are rarely user-facing prose. You could write them by hand, but then you don't.

What's the lightest-weight approach that actually gets done? Is there a way to generate good changelog entries from Git history, or is the real answer to write them explicitly — perhaps with AI assistance — at the moment of shipping, making the overhead low enough that you'll actually do it?

## The Options

### 1. Write by hand (with AI assistance)

You decide a change is worth noting and write a sentence or two — or ask an AI to draft it for you given a quick description. The quality is high and it's genuinely lightweight with AI help. The problem is purely discipline: you have to remember to do it, and it's the first thing to slip when you're busy.

### 2. Generate automatically from Git commits

Tools like [git-cliff](https://git-cliff.org/) can produce a structured changelog from your commit history automatically, especially if you follow [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `chore:` prefixes). In a clean repo with good commit hygiene this works well. In the real world — messy merges, WIP commits, inconsistent messages — the output needs heavy editing and can be worse than writing from scratch.

### 3. AI-assisted generation with light human curation (recommended)

The sweet spot: run a script or prompt that pulls recent commits, feeds them to an LLM, and gets back a clean draft changelog entry. You review and edit in a minute or two rather than writing from scratch. This tolerates messy commits because the LLM can filter noise and rewrite for a user audience. It also doesn't require perfect commit discipline upfront.

We use conventional commits on most projects, but messy merge commits and inconsistent coverage mean pure automation rarely produces something you'd want to publish without a pass. The hybrid approach gives you the automation benefit while keeping quality control.

## Storing Your Changelog

The simplest and most conventional approach: a single `CHANGELOG.md` in the root of your repo, following the [Keep a Changelog](https://keepachangelog.com) format. Each release gets a `##` section with the version and date, and changes grouped under `### Added`, `### Changed`, `### Fixed` etc.

```markdown
## [Unreleased]

## [1.2.0] - 2026-02-25
### Added
- Export to CSV on the reports page

### Fixed
- Login redirect loop on Safari
```

This is readable in the repo, easy to parse for a website changelog page, and the LLM skill below just prepends a new section each time you run it.

## The Recipe

The goal is a single command — or a one-shot prompt to an AI assistant — that:

1. Gets all commits since the last changelog entry (or last tag)
2. Filters noise (merge commits, chores, trivial fixes)
3. Groups meaningful changes into Added / Changed / Fixed
4. Drafts a new `## [version] - date` section
5. Prepends it to `CHANGELOG.md` for your review

See the appendix below for a concrete skill/prompt you can give to Claude, ChatGPT, or any LLM to do this in any project.

---

## Appendix: LLM Skill — Generate Changelog Entry

> Copy this prompt and give it to an AI assistant (Claude, ChatGPT, etc.) in your project directory. It will generate a draft changelog entry ready for review.

---

You are helping generate a changelog entry for this project.

**Step 1: Get recent commits**

Run the following to get commits since the last changelog entry or tag. If there is a `CHANGELOG.md`, find the most recent `## [` heading and use that date or tag as the boundary. Otherwise use the last 30 commits.

```bash
# Since last tag:
git log $(git describe --tags --abbrev=0)..HEAD --oneline --no-merges

# Or last 30 commits if no tags:
git log --oneline --no-merges -30
```

**Step 2: Filter and group**

From the commit list:
- Ignore commits that are: merge commits, dependency bumps, formatting/linting, typo fixes, CI config changes, or anything prefixed `chore:` or `refactor:` unless significant
- Group remaining commits into:
  - **Added** — new features or capabilities
  - **Changed** — modifications to existing behaviour
  - **Fixed** — bug fixes
  - **Removed** — anything removed

**Step 3: Draft the entry**

Write a new changelog section in this format:

```markdown
## [Unreleased] - YYYY-MM-DD
### Added
- <user-facing description, not commit message verbatim>

### Fixed
- <user-facing description>
```

Write each item as a short sentence from the user's perspective. Avoid developer jargon where possible. If the version number is known, use it instead of `Unreleased`.

**Step 4: Prepend to CHANGELOG.md**

If a `CHANGELOG.md` exists, show the new section and ask the user to confirm before prepending it. If no `CHANGELOG.md` exists, create one with a standard header followed by the new entry.

**Output:** Show the draft entry for review before writing anything to disk.

---

*Tools like [git-cliff](https://git-cliff.org/) and [Changeish](https://dev.to/itlackey/changeish-automate-your-changelog-with-ai-45kj) can automate parts of this pipeline if you want to go further.*
