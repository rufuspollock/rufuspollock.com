---
title: >-
  hg-git and pushing to git from mercurial
slug: hg-git-and-pushing-to-git-from-mercurial
date: 2011-02-12T13:06:59
themes: []
tags: [u'Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 868
---

Documenting my experience pushing mercurial repos to git (and github specifically).

### Install hg-git

Follow <https://bitbucket.org/durin42/hg-git/src/tip/README.md>

Install dulwich >= 0.6. On ubuntu:

    sudo apt-get install python-dulwich

Get the latest version of hg-git:

    hg clone https://bitbucket.org/durin42/hg-git

Add it to your extensions

    [extensions]
    git = path/to/hg-git/hggit

### Push an existing mercurial repo

Assuming you've got a git repo somewhere, e.g. for me (rgrp) on github:

     cd my-current-mercurial-repo
     hg push git+ssh://git@github.com/rgrp/myrepo

**Really important note:** do ***not*** change git before the @ sign to your username as you would in mercurial but leave it as 'git' (this cost me around 20m of googling with errors like

    Permission denied (publickey).
    abort: the remote end hung up unexpectedly

You may also want to check your ssh setup with github really is working (see <http://help.github.com/troubleshooting-ssh/>).

