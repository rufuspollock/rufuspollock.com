---
title: >-
  Adding Mathematics to Markdown
slug: adding-mathematics-to-markdown
date: 2007-01-08T11:53:30
themes: []
tags: [u'Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 148
---

Following my release of the [markdown to latex script](http://www.thefactz.org/ideas/archives/144) I've had a few enquiries from people asking about integrating mathematics with markdown generally (e.g. for web output as well as for output to latex). I'd already been using mathematics in markdown and then processing to html before I wrote the mkdn2latex script and in a world where one didn't need to produce nice pdfs for conferences and journals it would be my preferred format. Anyway here's a summary of the ways in which you can add mathematics support to basic markdown:

### Mathematics in Markdown Howto

There are two possible options for pure web output with mathematics using markdown:

1. Add asciimathml/latexmathml support into the html files in which the markdown output will be inserted (these are javascript files to convert latex like mathematics to mathml on the fly see [1][] and [2][] -- note that i recommend latexmathml as it is closer to latex).

2. Convert to latex and then convert to html use latex2html or similar

For pure html work I've used approach (1) up until now. This requires no change to your markdown processor only that you link to the right asciimathml/latexmathml javascript in the resulting html document (you can see an example in [this simple wrapper around the basic markdown script][3])

In both cases you will want to insert math sections into your source markdown file. My convention is that any maths whether in paragraph or out should be enclosed in double dollars as in: \$\$ .... \$\$  (note that the \\ should not be there but because latexmathml script is being used on this blog we need to escape one of the $ so that the text actually displays -- as opposed to being render as mathematics). This is slightly different from the standard asciimathml/latexmathml conventions which just use a single $). I've made the necessary modifications (very minor) to asciimathml and latexmathml and you can find them at:

http://knowledgeforge.net/okftext/svn/trunk/js/

(look in the src subdirectories)

To summarize:

1. Create your markdown documents as normal.

2. To add mathematics just add it as for latex but using $\$ as delimiters. (If you plan to use javascript approach read up on those scripts to see what parts of latex they support). For example this would be fine (again ignore the backslashes):

         A simple markdown file, $$x$$, with some mathematics:
         
         \$\$ x^{2} + y^{2} = z^{2} \$\$
         
         A new paragraph after a block of mathematics ...

3. Then:

   1. EITHER convert to markdown as usual but then insert link to modified latexmathml.js in your html documents (or if using original latexmathml just convert $$ to $ everywhere)
   2. OR convert markdown to latex using my script and then use latex2html

[1]:http://www1.chapman.edu/~jipsen/asciimath.html
[2]:http://www.maths.nottingham.ac.uk/personal/drw/lm.html
[3]:http://project.knowledgeforge.net/okftext/svn/trunk/python/okftext/mkdn.py
 


