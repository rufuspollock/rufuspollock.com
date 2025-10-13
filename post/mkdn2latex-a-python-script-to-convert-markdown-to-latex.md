---
title: >-
  mkdn2latex: A Python Script to Convert Markdown to LaTex
slug: mkdn2latex-a-python-script-to-convert-markdown-to-latex
date: 2006-11-30T13:28:09
themes: []
tags: ['Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 144
---

**UPDATE (2008-06): a new version is available (v1.2): http://www.rufuspollock.org/2008/06/23/markdown2latex-mkdn2latex-12/**

Over the last year I've written quite a few papers using [markdown](http://www.daringfireball.net/markdown) plus asciimathml. While this is great for web publication (and editing) and gives me lots of styling freedom via css it doesn't produce output that's as nice as that produced by latex especially in paginated form (also latex mathematics support is also currently better than that of obtained from asciimathml or latexmathml).

Unable to find any python code that would do what I want I played around for a couple of hours with the [python-markdown](http://www.freewisdom.org/projects/python-markdown/) script until I got something functional. After a few weeks of use which has allowed me to iron out the bugs and making several improvements I feel the script is now ready for public release. Hope people find it useful.

### Download

Get it from: http://project.knowledgeforge.net/okftext/svn/trunk/python/mkdn2latex.py

(You can also it check it out using subversion from the same url if you want)

For the script to function you will also need to install the [python-markdown](http://www.freewisdom.org/projects/python-markdown/) module v1.5 (make sure you install it under the name markdown.py).

### Usage

The following will print the latex output to the console (standard out):

     $ mkdn2latex.py path-to-markdown-file.mkd

To convert a markdown file straight to a latex output file do:

     $ mkdn2latex.py path-to-markdwon-file.mkd > path-to-output-file.ltx

**NB:** As provided the script expects mathematics in your markdown file to be delimited with '$\$' (this should be dollar dollar -- the slash is there to stop this being rendered as maths in the blog) as opposed to the standard asciimathml delimiters of '`' or '$'.

