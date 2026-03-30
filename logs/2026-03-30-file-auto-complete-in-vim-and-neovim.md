# File Auto-complete in Vim and Neovim

I wanted file auto-completion in Markdown notes, especially for wiki-links like `[[another-note]]`, paths, headings, and ambiguous filenames such as multiple `README.md` files in one vault.

The first thing I learned is that installing an LSP server is not the same thing as getting a good completion experience. I started with `marksman`, and while it can attach to Neovim and provide Markdown intelligence, installing the binary alone was not enough. Neovim still needed an actual completion UI.

I eventually switched to `markdown-oxide`, which is a better fit for note-taking workflows. The setup that made the most sense was:

- `markdown-oxide` as the Markdown LSP
- `nvim-cmp` as the completion UI
- `cmp-nvim-lsp` as the bridge between `nvim-cmp` and the LSP

The important Neovim detail was keeping the configuration narrow. I only enabled `nvim-cmp` for Markdown buffers, and I used the documented `markdown_oxide` keyword pattern so completion can match spaces, `/`, and `#` inside wiki-links and heading references.

That matters because the built-in Neovim completion popup is fairly limited for this kind of Markdown navigation. Once I moved to `nvim-cmp`, the setup was much closer to what I actually wanted: note-oriented completion, not a general coding environment.

Tips for others:

- Decide what you want first: a coding LSP setup or a note-linking setup. They are not the same.
- Do not assume `brew install ...` is the full job. You still need Neovim-side completion configured.
- If your goal is Markdown links and wiki-links, `markdown-oxide` plus `nvim-cmp` is a better fit than a bare LSP plus Neovim's default completion.
- If you have lots of duplicate filenames, a richer completion UI helps much more than the default popup.
- Check `:LspInfo` to confirm the server is actually attached in the Markdown buffer you are editing.

The shortest version of the setup is: install `markdown-oxide`, install `nvim-cmp` and `cmp-nvim-lsp`, wire them together only for Markdown, and treat this as a note-writing workflow rather than a code-completion workflow.
