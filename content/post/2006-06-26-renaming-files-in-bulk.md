---
title: >-
  Renaming Files in Bulk
slug: renaming-files-in-bulk
date: 2006-06-26T18:28:15
themes: []
tags: ['Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 103
---

Just some random ideas on how to do this culled from elsewhere

Rename *.foo to *.bar:

<pre>
ls -d *.foo | sed -e 's/.*/mv & &/' | sh
</pre>

