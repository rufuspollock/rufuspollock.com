---
created: 2026-01-27
---

# AI-guided daily planning — the progressive-narrowing experiment

A standing problem: I want to know what to work on *next* without burning twenty minutes digging through projects, notes and vague half-tasks first. The mess isn't a storage problem. It's a *narrowing* problem — getting from a large field of possible work to one concrete thing I can start now.

In late January 2026 I ran a little experiment: treat daily planning as a fast, **interactive** session with an AI that does the narrowing for me. One question at a time, decisions made on incomplete information, a hard stop the moment I have something to start. No optimising. No "perfect" plan.

This post preserves the two prompts and the protocol I used, so the experiment is archived in one place.

## The shape: progressive narrowing

The core loop is the same whether I run it solo on paper or with an AI:

1. **Frame** — how many minutes do I have, what's my energy (Low/Med/High).
2. **Project inventory** — name 3–6 active projects (things that take ≥1 week). Names only, no justification.
3. **Order by leverage** — highest → lowest, where leverage = "progress here makes other things easier or clearer." First-pass intuition, no optimising.
4. **Scope gate** — of the top two, which could produce a *finished artifact* today? If neither → meta-work (planning, clarification).
5. **Generate** — 4–6 candidate micro-tasks (10–30 min, verb-first, immediately startable, no "think about", no external dependencies).
6. **Commit** — pick 3–4. Cut test: "if I only did one of these today, which would still make the day count?" — star it.
7. **Start** — output the list, ⭐ first, then stop and start the starred task. Do not re-plan.

Key constraint: planning time is *proportional* to work time. If I only have 30 minutes of work, 5 minutes of planning is plenty.

Fallback when foggy: "When this work is *done enough*, what questions would I be able to answer confidently?" List 5–10, derive tasks from them, return to step 6.

## The single-prompt AI version

The verbatim prompt I'd hand an assistant:

> You are a **focused planning guide**, not a brainstormer or coach. Help me select **what to work on next**, quickly and decisively, by progressive narrowing via questions. Decisions are made on incomplete information.
>
> **Done when** I have 3–4 concrete micro-tasks (10–30 min each) and one is marked the immediate next action — then stop asking and tell me to start.
>
> **Protocol:** ask **one question at a time**; don't explain theory; push gently toward commitment. (1) Frame: time + energy. (2) List 3–6 active projects, names only. (3) Order by leverage. (4) Of the top two, which yields a finished artifact today? Force a choice; neither → meta-work. (5) Surface the next points of solo progress, then write 4–6 verb-first micro-tasks. (6) Cut to 3–4; "if I only did one, which makes the day count?" → ⭐. (7) Output the checklist, ⭐ first, then: "Planning is complete. Start the starred task now for 10 minutes. Do not re-plan. Return only if blocked." End the session.

A later variant integrated a `projects/` directory directly — scan the markdown files, present open tasks from the chosen project, and let me pick from existing tasks instead of generating from scratch. That's the seam where this stopped being a prompt and started wanting to be a tool.

## A real session (excerpt)

What it actually felt like, lightly trimmed:

> **Me:** I've got 30 minutes. Projects: Life Itself research website, the LI website, Reports That Matter, my project backlog, the LI strategic plan, and this meta-task of deciding what to work on.
>
> **AI:** Order them highest → lowest leverage.
>
> **Me:** Strategic plan and the meta-task first, then the backlog.
>
> **AI:** Which of the top two yields a finished artifact in 30 minutes?
>
> **Me:** Neither fully — but I can move *structure*. Honestly the useful thing is to define what "done" even means for the strategy.
>
> **AI:** Then one meta-micro-task now: write 8–10 questions such that, if answered, you'd say the strategy is done enough to move forward. No prose, no solutions — just the questions.

That reframe — from "do the strategy" to "define done for the strategy" — was the whole value of the session. The narrowing surfaced it in about four minutes.

## What I learned

- **Narrowing beats organising.** A better-organised list is just better-organised overwhelm. The win is the cut, not the catalogue.
- **The stop condition is the feature.** Ending the moment there's a startable task — before it feels "complete" — is what keeps planning from eating the work.
- **The mess wants to be addressable.** Once the AI is reading my actual `projects/` files rather than asking me to recite them, the prompt is straining to become a proper skill with the portfolio as its substrate.

That last point is where this went next — toward a planning *skill* that reads the whole project graph and my calendar and runs the session over real context. But the seed is here: get from the mess to one concrete next action, fast, and then go.
