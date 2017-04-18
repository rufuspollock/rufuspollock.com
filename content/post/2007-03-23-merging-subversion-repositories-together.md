---
title: >-
  Merging Subversion Repositories Together
slug: merging-subversion-repositories-together
date: 2007-03-23T21:05:31
themes: []
tags: ['Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 171
---

Have repository {start-repo} and want to merge into {old-repo} at {some-dir-name}

    # if you just wanted trunk replace with this
    # svndump {start-repo} | svndumpfilter include trunk 
    svnadmin dump {start-repo} > my-dump
    # copy file to main server and change to web-user
    svnadmin load --parent-dir {some-dir-name} {old-repo} < my-dump

