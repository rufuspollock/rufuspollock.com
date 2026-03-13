# rufuspollock.com

Rufus Pollock's personal website including blog and digital garden / knowledgebase.

Website: http://rufuspollock.com/

Built with FlowerShow (markdown-based static site generator). Config in `config.json` (theme: "lessflowery").

## Repo Structure

### Content directories (where to write things)

- `post/` — Blog posts. The main archive (~500 posts). Filenames are slug-style, e.g. `my-post-title.md`. Frontmatter: `title`, `date`, etc.
- `blog/` — Blog listing pages only (`index.md`, `all.md`). Do NOT put posts here.
- `ref/` — Digital garden / reference notes. Dated format: `YYYY-MM-DD topic description.md`. Short captures: quotes, observations, references, evergreen notes.
- `works/` — Notes on books, films, TV, media. Named after the work. Longer, structured reflections.
- `logs/` — Dated journal/log entries (`YYYY-MM-DD.md`). What you did or thought about on a given day.
- `nonfiction/` — Longer nonfiction essays/articles.
- `research/` — Research topic folders.
- `projects/` — Project description pages.
- `drafts/` — Work in progress (gitignored).

### Top-level markdown files

Various standalone pages: `about/`, `now.md`, `contact.md`, `index.md`, `writings.md`, `garden.md`, etc. These are site pages, not blog posts.

### Assets & infrastructure

- `static/` — Static assets served as-is.
- `images/`, `media/` — Image and media files.
- `templates/` — Site templates (FlowerShow/theme).
- `config.json` — Site configuration (nav, theme, analytics).

## Conventions

- Content is markdown with YAML frontmatter (`title`, `date`, `description`, etc.).
- New blog posts go in `post/` with a descriptive slug filename.
- New reference/capture notes go in `ref/` with dated filename format.
- New book/film notes go in `works/`.
- Wiki-style links use `[[double brackets]]`.
