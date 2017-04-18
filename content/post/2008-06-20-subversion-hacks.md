---
title: >-
  Subversion Hacks
slug: subversion-hacks
date: 2008-06-20T13:45:55
themes: []
tags: ['Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 455
---

Automatically Adding or Removing Files
==============================

Especially useful when, for example, versioning /etc/:

<pre>
Files to remove:

svn stat -q | grep '^!'
svn stat -q | grep '^!' | sed -e 's/^!\s*//' | xargs | svn rm

Files to add:

svn stat | grep '^?'
svn stat -q | grep '^?' | sed -e 's/^?\s*//' | xargs | svn rm

find . -name '*dpkg-old*' -exec rm -i {} \;
</pre>

