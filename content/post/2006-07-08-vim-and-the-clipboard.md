---
title: >-
  Vim and the Clipboard
slug: vim-and-the-clipboard
date: 2006-07-08T10:51:22
themes: []
tags: ['Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 105
---

I am a heavy vim user and want to be able to copy and paste from the system clipboard so that, for example, I can edit my posts in vim and then paste them from firefox in here. I should also mention that I prefer to use terminal not gui versions of vim which influences the solutions recommended below.

## Mac OSX ##

Use pbcopy and pbpaste. These are two very useful Mac OSX terminal commands that give access to the system clipboard. To use from vim pipe your selection (using '!') through them, e.g. to copy the whole document to the clipboard:

<code>:%!pbcopy</code>

## Debian/Ubuntu ##

**Method 1:** similar to Mac OSX trick using xclip (sudo apt-get install xclip) and then pipe through that. Specifically:

    :%!xclip -i -selection clipboard

**Method 2:** If you have xterm-clipboard enabled in your version of vim (not the case in the default version of vim installed, you'll need vim-full) you can access the clipboard as a register. Selection register is named '*' and clipboard is named '+'. So to copy to the clipboard get your selection and then do:

<code>"+y</code>

For more information on vim and the xclipboard do:

:help x11-selection

or see <http://vim.sourceforge.net/tips/tip.php?tip_id=71> (2008-01-02: or <http://vim.wikia.com/wiki/In_line_copy_and_paste_to_system_clipboard>).

