# Project Phase and Status

Any initiative or project has two distinct tracking dimensions: **phase** and **status**. These are often conflated into a single field, but keeping them separate is genuinely useful.

## The Distinction

**Phase** tracks *where something is in its lifecycle* — the stage of development from idea to retirement. It answers: "What kind of work is this right now?"

**Status** tracks *the current activity level* within that phase. It answers: "Is anyone actively working on this?"

You can always collapse phase and status into a single field if you want simplicity, but having both gives you much more precision.

## Phases

| Phase | Description |
|-------|-------------|
| **Inbox** | Ideation — an idea that has arrived and needs thinking about. Not yet committed to. |
| **Planning** | Being actively planned and prepared — scoping, resourcing, designing. |
| **Shipping** | Being built — active development or execution underway. |
| **Sharing** | Launched but being actively communicated, promoted, or rolled out. |
| **Stable** | Live and running with no active development needed. |
| **Retired** | Archived or discontinued. No longer active. |

## Statuses

| Status | Description |
|--------|-------------|
| **Backlog** | Not being worked on yet — queued for future attention. |
| **In progress** | Actively being worked on now. |
| **Paused** | Was in progress, but currently on hold. |
| **Done** | Completed (within its current phase). |
| **Blocked** | Cannot proceed due to an external dependency or decision needed. |

## Defaults

- Anything entering the system for the first time defaults to **phase: inbox**, **status: backlog**.
- "Done" on status means done *within the current phase* — a project can be done with planning and move into shipping.

## Notes

- Need to dig out earlier material on this from Datopian — likely in an ROC (Requests for Comment) there. This writeup is a first pass to capture the core distinction.
