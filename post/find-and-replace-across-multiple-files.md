---
title: >-
  Find and Replace Across Multiple Files
slug: find-and-replace-across-multiple-files
date: 2006-09-22T11:21:15
themes: []
tags: ['Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 122
---

Archiving for my own benefit the results of yet another 5 minute look for how to do find and replace across multiple files from the command line:

1. Use sed:

          sed -i 's/foo/foo_bar/g'  *.html

2. use the old perl hack:

          perl -w -pi~ -e 's/foo/bar/' [files]

    Notes: -p: loop, -i edit files in place (backup with extension if supplied), -w enable warnings

3. Install rpl
    * http://freshmeat.net/projects/rpl/
    * port install rpl (mac osx)
    * apt-get install rpl (debian/ubuntu)

Combining either (1) or (2) with *find* is pretty powerful. E.g. to do a find and replace on all html files in all subdirectories:
    
         perl -w -pi -e 's/foo/bar/' `find <path> -name '*.html'`

