# Asset Management in a Git-Native Publishing Workflow

*Status: working analysis — some threads still open*

---

## Situation

- We publish websites and knowledge bases using a Git-native workflow: Git + Markdown + local editors (Obsidian, VS Code, etc.)
- Assets — images, PDFs, occasionally video — are created and edited alongside content
- In this workflow, co-located assets feel natural: paste an image in Obsidian, it lands in the repo, everything versions together
- For small, low-volume content this works well; most repos stay manageable

## Complication

The workflow breaks down as asset volume grows:

- **Repo size**: 500 images at ~3 MB each = ~1.5 GB. GitHub repos have a recommended limit of ~1–5 GB; at scale this is real. Large repos are slow to clone and painful to work with on local machines.
- **No media library UX**: assets on disc are just files with names — often random or unhelpful. No visual browse, no search, no way to easily find or reuse an image. Editing tools don't solve this.
- **External services break the flow**: moving assets to Cloudinary or S3 means leaving the editor, uploading, copying a URL, pasting it back. This context-switch friction discourages good asset hygiene and slows contributors.
- **Vendor lock-in**: managed asset services (Cloudinary etc.) create financial and ecosystem dependencies; integrations with AI tooling become harder.

> Note: this tension — wanting co-located assets but hitting storage/UX limits — also appears in non-Git tools like WordPress and Framer. This is worth noting because "just move off Git" isn't a clean escape; the problem follows you.

## Question

**What is the right approach to asset management in our Git-native publishing workflow, given that co-location works well at small scale but degrades badly at medium-to-large scale?**

Specifically:

- At what scale does the Git approach break, and what are the actual thresholds to watch?
- If we keep assets in Git for now: what hygiene practices reduce risk?
- If we move assets out: what's the most seamless handoff — one that preserves the paste-and-go editing UX as much as possible?
- Is a dedicated DAM layer the right long-term answer, and what would integration with our workflow look like?

## Recommendation

**For content assets (post images, page photography, project-specific media): keep co-located in Git, compress on ingest.**

Web images don't need to be 3–4 MB. Compressed to ~150–200 KB, 500 images = ~75–100 MB, well within Git's comfortable range. This preserves the paste-and-go editing UX and removes the repo size problem for most projects.

Caveat: compression discards original quality. If originals need to be preserved for reuse at higher resolution or in other formats, they should not live in the Git repo — they belong in a DAM or other storage with the compressed web version committed to Git and the original stored separately. This is a real need but affects a minority of assets; don't let it drive the default workflow.

**For shared/brand assets (logos, recurring promotional imagery, assets reused across multiple Life Itself sites): a lightweight shared store.**

A simple Cloudflare R2 bucket (no egress fees) with a documented folder structure and consistent URL pattern is sufficient for today. This is not a full DAM — it's a shared file store with discipline. A full DAM requires active curation to stay useful; at current team size, that governance overhead isn't worth it. If the volume of genuinely shared assets grows, revisit.

**Summary**:

| Asset type | Approach |
|---|---|
| Content images (posts, pages) | Git co-located, compress to <200 KB on ingest |
| Originals / high-res versions | Store separately in R2 or Drive; don't commit to Git |
| Shared brand / promotional assets | Shared R2 bucket with naming conventions |
| Video | External (R2, Drive, or YouTube embed) — never in Git |

---

## Appendices

### A: When does the Git size problem actually bite?

Rough thresholds:

- GitHub soft-limits repos at ~1 GB (warning) and hard-limits pushes over 100 MB per file
- A reasonably active site with images: 200–300 images × 2–4 MB = 400 MB–1.2 GB. Reachable within a year or two of active publishing.
- Cloning a 2 GB repo on a slow connection or for a new contributor is a real friction point
- Performance in editors and Git operations degrades noticeably above ~500 MB of binary content

Mitigation without leaving Git: compress images aggressively on ingest (aim for <200 KB per image for web use). This can push the ceiling significantly.

**Tooling**: use a pre-commit hook (lefthook + sharp/imagemagick) so compression is automatic and shared across contributors via a committed config file. Pre-commit hooks can be bypassed or skipped if a contributor hasn't set them up, so add a GitHub Actions check as a hard reject gate on PRs — any image over the size threshold blocks the merge. Don't use CI to auto-rewrite commits (fiddly, confusing); use it to enforce. Branch bloat from an oversized file is acceptable; the goal is keeping `main` clean.

### B: Git LFS

Git Large File Storage moves binary files to a separate store while keeping pointers in the repo. Sounds ideal; in practice:

- Requires setup and credential management — adds friction for non-technical contributors
- Breaks some tools (certain editors, CI pipelines, Obsidian workflows)
- Bandwidth/storage on GitHub LFS is metered and not free at scale
- The pointer model is confusing when things go wrong

Verdict: works for engineering teams already comfortable with Git internals. Not a clean solution for a mixed technical/non-technical team.

### C: Other publishing tools hit the same wall

- **Framer**: asset storage limits on lower plans; at scale you end up hotlinking from external storage anyway
- **WordPress**: media library works for small sites but becomes a sprawling mess at scale — hundreds of crops, unorganised uploads, no meaningful taxonomy
- **Substack and similar**: encourage per-post re-upload rather than a shared library — arguably the correct pattern at their scale, since a shared library requires curation to stay useful

The pattern across tools: a shared media library sounds good but requires active management to stay functional. Without that management, it degrades into noise faster than having no library at all.

See Appendix F for a deeper look at whether the integrated media library is the wrong pattern entirely.

### D: The case for a dedicated DAM layer

A Digital Asset Management (DAM) system is a separate service for storing, organising, and serving assets. Key properties:

- Visual browse and search (what local file systems lack)
- Stable, CDN-backed URLs (assets don't move)
- Access control and team sharing
- Image transformation on delivery (resize, format conversion)

If we're going to move assets out of Git anyway, a proper DAM is better than raw S3 or Cloudinary because it provides the media library UX that contributors actually need.

**Open question**: does the DAM need to be organisation-wide (shared across all Life Itself sites) or per-project? Organisation-wide is more powerful but requires governance — who manages it, how assets are named and tagged, what happens to old assets.

### E: What a seamless non-co-located workflow might look like

The friction in external asset storage is the context switch: leave editor → go to upload UI → copy URL → return to editor → paste. 

A tolerable version of this might look like:

- Shared S3-compatible bucket (e.g. Cloudflare R2 — no egress costs) with a simple upload UI or CLI
- Editor plugin or drag-drop tool that uploads and returns a Markdown image link directly
- Consistent URL structure so links are predictable and portable

This doesn't fully replicate the paste-in-place UX of co-located assets, but it removes the worst of the context switching.

---

### F: Is the integrated media library an anti-pattern?

The instinct to want a media library in your publishing platform is understandable — you're uploading images, you want to find them again. But in practice, integrated media libraries tend to fail:

- **WordPress media library**: becomes cluttered quickly. Users scroll through hundreds of unrelated crops and uploads, can't find what they want, and often end up going to the live website, re-downloading the image, and re-uploading it. The library exists but provides no real value.
- **Ghost and Substack**: have largely abandoned the shared library model. You upload an image for a post; it lives with that post. No shared pool to manage or curate.

This is probably the correct pattern. The reason:

- Asset curation — deciding which images are good, tagging them, keeping them organised — is a distinct activity from publishing. It happens in a different context (Figma, a photo library, a DAM) and requires different tooling.
- Reuse across posts is rarer than it seems. When it does happen, download-and-re-upload is a perfectly acceptable workflow — it keeps assets tied to the content they appear in rather than depending on a shared pointer.
- The alternative (a shared library inside the CMS) creates implicit dependencies: delete or rename an asset, and pages that used it silently break.

**Implication for our workflow**: we don't necessarily need a media library integrated into our publishing platform. We need assets to be reliably stored with their content (not dependent on external links that can rot), and we need a low-friction way to get images in. A separate DAM is worth considering only if there's genuine value in shared, reusable, curated assets — not just as a convenience store for uploads.

*Open threads: org-wide DAM governance; tooling for image compression on ingest; whether Obsidian plugins exist that handle R2/S3 upload natively.*

---

## FAQ

**Q: What if I compress an image for the web and later need the original high-res version?**

Not a real problem. The original still exists wherever it came from — your phone, a camera card, Google Photos, a photographer's delivery folder. You didn't destroy it by compressing a copy for publishing. The workflow is: paste-to-publish gets a compressed copy, the original stays at its source. The only way this becomes a problem is if you compress-and-delete the source — so don't. Keep originals where they naturally live; the web copy in Git is just a web copy. For the vast majority of content images, you will never need the original again anyway.
