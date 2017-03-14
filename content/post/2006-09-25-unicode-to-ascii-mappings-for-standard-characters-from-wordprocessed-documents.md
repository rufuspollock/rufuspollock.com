---
title: >-
  Unicode to ascii mappings for standard characters from wordprocessed documents
slug: unicode-to-ascii-mappings-for-standard-characters-from-wordprocessed-documents
date: 2006-09-25T17:22:35
themes: []
tags: [u'Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 123
---

Anyone who has converted some old wordprocessed documents to plain ascii text will know that wordprocessors love to insert their only special versions for a few of the standard characters such as ' and " (- also comes up pretty frequently). I personally came across while using [odt2txt](http://www.freewisdom.org/projects/python-markdown/odt2txt.py) plus openoffice to convert some old .rtf and .doc files to plain text. By default odt2txt writes the files as utf-8 which is fine except there is really no reason these shouldn't be full on ascii (plus the standard vim distribution on mac osx doesn't support unicode!). So after some digging around here are the relevant code conversions you will usually need:

    \u2018 (curly right single quote) -> '
    \u2019 (curly left single quote) -> '
    \u201c (curly right double quote) -> "
    \u201d (curly left double quote) -> "

Or in python:

     out = <your-unicode-text>
     out = out.replace( u'\u2018', u"'")
     out = out.replace( u'\u2019', u"'")
     out = out.replace( u'\u201c', u'"')
     out = out.replace( u'\u201d', u'"')
     out.encode('ascii')

