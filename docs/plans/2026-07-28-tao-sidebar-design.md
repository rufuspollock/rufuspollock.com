# TAO sidebar design

## Goal

Show Flowershow's generated sidebar on the TAO index and all TAO subpages, while keeping unrelated site content out of that sidebar.

## Design

Keep `tao/index.md` unchanged. Configure the existing root `config.json` with `showSidebar: true` and a single sidebar path prefix, `/tao`. Flowershow will then display the sidebar only on routes under `/tao` and populate it only from that section's content tree.

Sort entries by page title so the navigation is readable and independent of filename casing. Do not add a `List` component or enable MDX because the requested navigation belongs in the sidebar, not in the page body.

## Verification

- Parse `config.json` as JSON.
- Assert that `showSidebar` is `true`, `sidebar.paths` is exactly `["/tao"]`, and `sidebar.orderBy` is `"title"`.
- Confirm that `tao/index.md` has no working-tree changes.

