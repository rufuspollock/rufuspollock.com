# Apply the Reading System to rufuspollock.com

Bead: `rp-5og`. Status: planned, not started. Written 2026-10-27 as a handoff.

## Goal

Make reading on rufuspollock.com as good as the In Tech We Trust mockups: Magazine-style type, red accent, small "Chapter N" labels, quiet small footnotes, sidenotes on long essays. Done as general Flowershow styling that improves most pages, not a one-off page.

## Source material (read these first)

- Reading System v0.1 (the source of truth): `~/src/rufuspollock/ux-patterns/reading-system/` — `reading.css`, `reading.js`, `README.md`. Live demo: https://claude.ai/artifact/L9JyqBYN941wu8ofFJGYAo (try `#magazine`).
- Mockup v2 and Rufus's verdicts: `~/src/rufuspollock/ux-patterns/essay-pages/mockups/in-tech-we-trust/README.md`.
- Research board behind it: https://claude.ai/artifact/PVtWUxMDeaWh8bi15bBeW9
- Flowershow docs (fetch `.md`, never guess): custom styles `https://flowershow.app/docs/reference/custom-styles.md`, class hooks `https://flowershow.app/docs/reference/theme-class-reference.md`, page scripts `https://flowershow.app/docs/reference/page-scripts.md`, head code `https://flowershow.app/docs/reference/custom-head.md`, config `https://flowershow.app/docs/reference/config-file.md`.

## Decision: which theme

**Magazine, adapted for a personal site.** Rufus rated Magazine and Academic as having the most personality and better type weighting; Personal felt heavy. Magazine also carries the parts he singled out: the red chapter label above an elegant title, and the drop caps.

- Type: Cormorant Garamond for headings, Newsreader for body text, Instrument Sans for small labels and UI.
- Accent: red (`#c8281e`), swappable with one variable.
- House rules: never indented paragraphs (space between them); footnotes and their numerals small and light; one vertical spacing scale.
- Ordinary pages stay calm: headings left-aligned, no drop caps. Long essays get the full treatment (below).

## How it applies: three tiers

Flowershow page DOM (from the class reference): `main.page-main > .page-header (.page-header-title, .page-header-description, .page-header-metadata-container) + .page-body > .rendered-mdx`. Posts (`layout: post`, dated folders) use `article.post-page` with `.post-header`, `.post-dek`, `.post-byline`. ToC rail: `.page-toc-container > .toc > .toc-item`. Callouts: `[data-callout]`.

### Tier 1: every page (CSS only, `custom.css`)

Restyle Flowershow's own markup, no wrapper needed:

- Map theme variables: `--font-heading`, `--font-body`, `--color-l-accent`, `--color-l-foreground`/background (and the `--color-d-*` dark pair, see Dark mode).
- Under `.rendered-mdx`: Reading System prose rules for `p` (spacing scale, `text-wrap: pretty`, hyphens, old-style numerals), `h2` to `h5` (Magazine treatments: h3 display semibold, h4 small red uppercase label with a short rule, h5 display italic), `blockquote` as epigraph, `hr` as ⁂, links (thin accent underline), `strong` weight.
- Footnotes as remark-gfm emits them (`sup a[data-footnote-ref]`, `section[data-footnotes]`): small, light, two columns at the end.
- Page header: `.page-header-title` in Cormorant 600; `.page-header-description` / `.post-dek` as Magazine subtitle (italic Newsreader); byline and date in Instrument Sans.
- ToC rail (`.toc`): restyle to match `rs-toc` (Instrument Sans, muted, accent for active).
- Measure: body text about 33em; check `--post-max-width` and the center column width.
- Fonts: Google Fonts `<link>` via the `head` field in `config.json` (premium, Rufus has it) or `@import` at the top of `custom.css`.

Must not break: list/index pages, `/logs`, `/changelog`, tag pages, callouts, code blocks, tables, images, the `/tao` sidebar.

### Tier 2: essays (opt-in per page, page script)

For long pieces (tag `essay`, or many footnotes), add to frontmatter:

```yaml
scripts: /js/reading.js
```

The script (adapted from `reading-system/reading.js`) adds `rs-essay` to the page, and with it:

- footnotes become sidenotes: in the right margin on wide screens, tap-to-open on phones;
- `h2`s get the red "Chapter N" label (only when the essay is chaptered; otherwise plain) and Magazine centred chapter titles;
- drop cap on the first paragraph of each chapter;
- optional chapter bar with reading progress.

Layout: sidenotes need the right margin, which Flowershow's ToC rail uses. On essay pages, hide the ToC rail (`showToc: false` per page if supported, else CSS under `.rs-essay`) and use the space for notes; keep contents in the chapter bar's drawer. Widen the center column on essay pages so text plus margin fit (text about 33em plus 230px margin).

Page-script rules (from the Flowershow docs): wrap in a function, start with `if (!document.currentScript?.isConnected) return;`, be safe to run many times, remove listeners and the `rs-essay` class on `flowershow:page-leave`, and make the page read well before the script runs (footnotes stay at the end without it).

### Tier 3: flagship papers (optional, later)

For a paper with a cover, summary, citation and series (like the Second Renaissance papers), a standalone `.html` page using the full Reading System template (`reading-system/demo/template.html`). Not part of this bead.

## Dark mode

The Reading System is light-only; the site may offer a dark mode switch (check `theme` settings in `config.json` and the live site). Either define dark values for the tokens (ink on near-black, red lightened to about `#ff6b5e`, rules and tints from `--color-foreground-*`) under `:root[data-theme="dark"]`, or turn the switch off. Recommendation: define dark values; keep it small.

## Steps

1. **Baseline.** Screenshot (desktop and phone, light and dark) five pages: an essay with notes (`everything-is-so-difficult-marcello-fellinis-la-dolce-vita.md`, 24 notes), a long paper (`open-source-software-and-government.md`, 21 notes), an ordinary note (`Zak Stein.md`), a bookmark (`Carl Sagan's 1995 warning on America's future resurfaces.md`), and an index (`/blog` or `/writings`). Check the real DOM of footnotes and headings on the live site.
2. **Tier 1 CSS.** Write `custom.css` from `reading.css`: keep the prose, footnote and spacing rules, re-scope `.rs-text` to `.rendered-mdx`, map tokens to Flowershow variables. Header comment: source path and Reading System version. Fonts via `head`.
3. **Check Tier 1** on the five pages plus callouts, tables, code, `/tao`, `/logs`, tag pages. Fix regressions.
4. **Tier 2 script.** Adapt `reading.js` into `js/reading.js` (Flowershow root selector `.rendered-mdx`, page-script lifecycle, add/remove `rs-essay`). Add essay-mode CSS under `.rs-essay` in `custom.css`. Turn it on for the two pilot essays.
5. **Dark mode** values, then re-check the five pages in dark.
6. **Rufus review** of the pilots (light, dark, phone). Apply feedback.
7. **Roll out** Tier 2 to the other long essays (list in step 1 notes: pages with more than 5 footnotes). Add a short note to `docs/conventions.md`: "long essays: add `scripts: /js/reading.js`".
8. **Upstream.** Port any fixes back to `ux-patterns/reading-system/` so it stays the source of truth.

## Done when

- `custom.css` and `js/reading.js` are live on rufuspollock.com; ordinary pages read with the new type and spacing and nothing regresses on index, log, tag and TAO pages.
- The two pilot essays show sidenotes, chapter labels and drop caps on desktop, and tap-to-open notes on phone; light and dark both work.
- Rufus has reviewed the pilots; changes are committed and pushed; the bead is closed with links to before/after screenshots.

## Open questions for Rufus

1. Apply Tier 1 to every page now, or start with essays only? **Recommend: every page**, since the prose layer is low-risk and the type is the main win.
2. Dark mode: design dark values or turn the switch off? **Recommend: design them** (small job).
3. Chapter labels on unchaptered essays: none, or "Part N" from `h2`s? **Recommend: none**; only label essays whose `h2`s are real chapters.
