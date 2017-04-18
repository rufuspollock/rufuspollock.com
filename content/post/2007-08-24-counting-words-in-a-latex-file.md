---
title: >-
  Counting Words in a Latex File
slug: counting-words-in-a-latex-file
date: 2007-08-24T13:04:13
themes: []
tags: ['Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 211
---

Much of this was inspired by [this blog post](http://ubuntu.wordpress.com/2007/02/07/true-word-count-in-latex/). Having tested on my own set of files I would suggest that these methods could be ranked in order of accuracy as:

  1. TexCount.pl
  2. untex + wc
  2. wc
  3. pdf file

### wc

    $ wc -w file.tex

This is very simple but is pretty inaccurate since wc has no awareness of tex commands or mathematics (which results in overcounting) and does not expand things like bibliographies (which results in undercounting). Overall the result is likely to be a substantial overcount.

### Look at the resulting pdf file.

    $ pdftotext file.pdf - | egrep -E '\w\w\w+' | iconv -f ISO-8859-15 -t UTF-8 | wc

More sophisticated but in my experience results in grossly overestimated wordcounts due to inability to deal with mathematics and issues with pdftotext (lots of words get broken up that shouldn't be).

### TexCount.pl

Get it from: <http://folk.uio.no/einarro/Comp/texwordcount.html>

This seemed to be pretty good.

### untex + wc

   $ untex file.tex | wc

Again likely to overcount for mathematics and fairly limited removal of tex commands (though may undercount due to omission of citation/biblio type stuff).

