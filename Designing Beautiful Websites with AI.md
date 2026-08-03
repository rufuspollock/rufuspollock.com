---
created: 2026-08-04
title: Designing Beautiful Websites with AI
tags: [post]
---

# Designing Beautiful Websites with AI

I want to build websites with real aesthetic identity — not just competent, but beautiful. AI can now produce a decent site fast. But "decent" is the problem: AI-generated design has the same failure mode as AI writing. Competent, polished, and generic. A recognizable house style that isn't *your* style.

I've tried to fight this on two recent projects — [Developmental Spaces](https://developmentalspaces.org/) and the [Second Renaissance ecosystem site](https://ecosystem.secondrenaissance.net/) — by hand-picking a few input images rather than writing a pure text brief. For Developmental Spaces that meant the tower/spiral logo as a visual anchor; for the ecosystem site, some report-design references pulled from an Are.na board (not fully certain which ones made it into the actual prompt). This site (rufuspollock.com) has had an even looser, more ad-hoc process.

Both shipped. Both are fine. Neither has real personality — still reads as AI-average.

The theory of *why* is already written up in my `ux-patterns` project (`howto-moodboards.md`): vague briefs make a model regress to the statistical centre of "good design." A moodboard is supposed to fix this — it's a constraint device, not just inspiration. A few hand-picked images is a thin version of that, and it wasn't enough. What's missing is a real curated set, and — harder — the eye to curate it well, since I don't have strong design taste to begin with.

The idea I keep circling back to (see appendix, and `planning/ideas/inspiration-by-ai.md`) is offloading *search* to AI while keeping *selection* human: AI pulls real candidate sites from curated galleries, I pick between pairs, fast, repeatedly, until a felt direction emerges — closer to preference-learning than to browsing or prompting.

Screenshots of where things stand:

![Developmental Spaces homepage](https://screenshotit.app/https://developmentalspaces.org/)

![Second Renaissance ecosystem homepage](https://screenshotit.app/https://ecosystem.secondrenaissance.net/)

Next: work out whether a pairwise-picker tool actually closes this gap, or whether it's a reps/skill problem no tool shortcuts.

---

## Appendix: SCQ

**Level 1 — general**
- S: Want to build beautiful, aesthetically distinctive websites. AI can now produce output fast.
- C: AI design output is competent but generic — same "middle of the road" failure as AI writing.
- Q: Can AI actually help produce great-quality websites, and how?

**Level 2 — this attempt**
- S: Tried a thin moodboard (a few hand-picked images) on Developmental Spaces and the ecosystem site, rather than a text-only brief.
- C: Still shipped generic-AI-looking results. Full moodboarding process (per `ux-patterns/howto-moodboards.md`) was never really run — too slow/high-friction to do properly, and curation itself needs an eye I'm not confident I have.
- Q: Does a faster AI-source / human-pairwise-select mechanism (see `planning/ideas/inspiration-by-ai.md`) close the gap — or is this a design-reps/skill problem no tool shortcuts?

## Appendix: Related Projects & Ideas

- **[Design Reps with AI](https://ux.rufuspollock.com)** (`planning/projects/2026-design-reps-with-ai.md`) — project to build real design skill through daily small constrained exercises with AI. Prescribes moodboarding before every rep; source of the "moodboard first" rule that kept getting skipped on both live attempts.
- **Inspiration by AI** (`planning/ideas/inspiration-by-ai.md`) — idea for a chat/pairwise tool that sources real reference sites from design-award galleries and lets you converge on a direction via fast A/B picks instead of open browsing. Full text copied into Appendix 2 below.
- **[How to Get Good, Average...](https://ux.rufuspollock.com/howto-moodboards)** — working notes on why vague briefs produce averaged-out AI output, and how moodboards function as constraint devices rather than just inspiration.
- **[ux-patterns archive](https://ux.rufuspollock.com/archive)** and **[report-inspirations](https://ux.rufuspollock.com/report-inspirations)** — existing curated reference collections (50+ sites with screenshots) — raw material for any future moodboard, not yet drawn on for either live attempt.
- **[Developmental Spaces](https://developmentalspaces.org/)** — live site, first design-rep attempt; input was the tower/spiral logo image.
- **[Second Renaissance ecosystem site](https://ecosystem.secondrenaissance.net/)** — live site, second design-rep attempt; input was some Are.na report-design references.

## Appendix 2: "Inspiration by AI" (idea, verbatim)

Interactively describe what you want and work with AI to rapidly find and refine visual examples.

### Key framing note (for us)

Core insight to foreground: **chat is becoming the primary interface for sense-making and creation**.

This product applies that shift to inspiration and early-stage design:

* Instead of searching, scrolling, and bookmarking,
* you *talk* your way into a mood board.

Conversation replaces search queries.
Selection replaces endless browsing.

### Product pitch (working draft)

**User story**

When I start a new digital project—especially a website—the first thing I want is a **mood board**.

I want to quickly gather examples that feel right:

* websites,
* layouts,
* maps,
* icon styles,
* tone and structure.

I don't want to search, filter, and scroll for hours.
I want to **talk my way into a useful reference set**.

**The problem**

Creating mood boards for digital products is slow and fragmented:

* Inspiration is scattered across search engines, Pinterest, bookmarks, articles, screenshots.
* Each project starts from scratch, even though relevant material already exists.
* Visual tools are good at display, but bad at *intent*.
* Notes about *why* something matters are lost or separated from the reference itself.

What's missing is a fast, conversational way to assemble a project-specific set of references.

**The product**

An **AI-first tool for creating mood boards for digital projects**, where chat is the primary interface.

You start by describing what you're working on:

> "I'm creating a website for X."

From there, you **converse your way into a board**:

* Ask for examples.
* React to what you see.
* Refine by choosing options.

The system gathers *real references*—not generated images—and assembles them into a simple board or list.

**How it works (conceptually)**

* **Chat-led discovery** — You describe, react, refine.
* **Visual options + selection** — You're shown concrete examples and choose what resonates.
* **Fast accumulation** — The goal is speed, not polish.
* **Light annotation** — Short notes attach directly to references: "use this layout logic", "tone feels right".

A board can be as simple as a list of links, images, and notes.

**What AI is doing**

AI replaces friction, not judgment:

* It finds and groups relevant examples quickly.
* It offers visual refinements as choices, not commands.
* It lets you move forward without formulating perfect search queries.

No image generation is required.

**What this is (and isn't)**

This is:

* A fast way to create mood boards for digital products.
* A conversational interface to visual inspiration.
* A lightweight, project-specific tool.

This is not:

* A design or layout tool.
* A generative art system.
* A heavy asset-management platform.

**Core value proposition**

Create a useful mood board for a digital project in minutes by **talking your way to real examples** instead of searching, scrolling, and bookmarking.

**Mental model**

ChatGPT for inspiration gathering.
Cursor-style workflows, but for visual references instead of code.

### Refinement: pairwise comparison mechanism (2026-07-18)

**Distilled summary.** Sharpens the "how it works" mechanism above into something concrete:

1. **Brief first.** I give a short brief on the site/project I'm building.
2. **Sourced pool.** AI pulls candidate sites from curated design-award/showcase lists (Awwwards, One Page Love, CSS Design Awards, Siteinspire, etc.) and pre-filters loosely against the brief.
3. **Pairwise choice.** Shown two sites side by side, I pick the one closer to what I want — optionally with a short comment on *why* ("like this palette, not this layout"). Repeat with two new sites each round.
4. **Fast convergence.** A handful of rounds converges on a felt sense of direction — effectively a Tinder-style swipe/A-B refinement toward a mood board or lightweight design system, faster than manual searching/bookmarking.

This is the same "chat your way into a mood board" premise as above, but pairwise comparison (not open-ended chat) is the core interaction — closer to preference-learning than search.

**Motivating application:** the Developmental Spaces website — currently functional but missing the theme/vibe I want, and I lack an easy way to hand AI a design system or mood board reference to get better output. This idea is the missing step before another design pass there.

**Relation to other work:** overlaps with Design Reps with AI's point that moodboarding-before-designing is a skipped step worth habitualizing; this idea is a tool to make that step fast instead of manual. Existing curated references (ux-patterns project, `ux-patterns/report-inspirations/`) are raw material this tool could also draw on, not just award-site scraping.

### Projects

- [x] check for domains: inspirationby.ai is available. (inspirationbyai.com is not)
