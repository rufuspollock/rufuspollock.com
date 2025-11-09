---
created: 2025-11-09
completed:
status: 🆕
priority:
kind: pattern
resolution:
status_notes:
  - 2025-11-09 added stub entry here.
start: "2005"
end:
---


A pattern I’ve been exploring for over a decade: store content in a raw, simple form — ideally plain text or Markdown — inside a Git repository. From there, generate publications through lightweight rendering tools. The idea is to treat text like code: versioned, inspectable, forkable, and transparent.

The principle is simplicity — the Unix philosophy for publishing. Everything is a pipe: small, open tools working together. This allows anyone to reproduce, remix, and republish without proprietary systems or complex CMS layers.

I’d already used this approach in _Open Shakespeare_, and later saw parallel experiments like _Gitenberg_.

The pattern remains powerful: open, composable, and enduring.

---

A method for storing and publishing textual material (e.g. reports, datasets, literature) using Git as the backend:

* Keep source material as plain text (Markdown or similar).
* Store and version it in Git repositories.
* Use lightweight rendering tools to generate websites or documents.
* Follow the Unix philosophy: small, composable tools; text as the universal interface.
* Publish as static sites rather than dynamic CMS-driven systems.

This pattern enables openness, durability, reproducibility, and simplicity — a decentralized infrastructure for public knowledge.