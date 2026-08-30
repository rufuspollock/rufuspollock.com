---
created: 2021-10-17
title: "What tools combines spreadsheets with text (and images) i.e. csv + markdown + images"
tags: [question]
---

# What tools combines spreadsheets with text (and images) i.e. csv + markdown + images

++tech

We have good tools for tables in the form of spreadsheets and databases. But these are for structured information.

What is a good tool that combines the structured info of a spreadsheet or database with the tool for managing unstructured content like text or images.

I basically want something that looks like: spreadsheet + markdown in git + images in cloudinary.

The problem of markdown with frontmatter is that it is painful to persist changes in frontmatter structure across different entities.

The problem with a spreadsheet (or database) is that text editing experience is poor and storage/versioning is poor compared to e.g. markdown and git.

The problem with both of these is that they are poor for image management and embedding.

I think some of these things are (partially) addressed by new(er) solutions like Notion, Coda etc. The "blocks" revolution does help but in all of these cases the slick product locks all my content into another proprietary backend - a quicksand that I know once i'm stuck in I'll never leave (and more importantly won't be able to innovate on at a fundamental level).

TODO:

* clarify the key dimensions of functionality and assess tools against this e.g.
  * text fields/blocks. Preferably editable in my favourite text editing tool
  * structured info (aka metadata). should be able to modify (e.g. rename fields) across all notes/entities
  * images: image (and video) storage and management
* review existing tooling: e.g. database/spreadsheet, markdown+git+vim, cloudinary or youtubue or ... Plus the more interesting all in one solutions like Notion, Coda or even GDocs.
