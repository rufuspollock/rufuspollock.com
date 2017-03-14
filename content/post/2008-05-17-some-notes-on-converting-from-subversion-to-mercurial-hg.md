---
title: >-
  Some Notes on Converting From Subversion to Mercurial (hg)
slug: some-notes-on-converting-from-subversion-to-mercurial-hg
date: 2008-05-17T22:20:13
themes: []
tags: [u'Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 311
---

Distributed versioning systems (VCMs) have now matured to the point that I've been planning to switch from subversion for quite a while -- at least for own personal repositories where there are no coordination issues. Having chosen [mercurial (hg)](http://www.selenic.com/mercurial/) as my DVCM of choice the next step was to actually convert. While there is quite a bit of documentation on this topic available online I didn't always find these had the necessary info. Combined with my experience of several 'snags' along the way I thought it worth documenting my experience in case it proves useful to others.

I'd waited until hg 0.9.5 was available on my distro precisely because I wanted to use the hg convert functionality (alteratives such as tailor looked to have difficulties and though it turned out I could have used hgsvn without problem my original impression of it had been it was oriented for integration of hg and svn rather than straight conversion).

Before I document the steps it is important to get clear one v. important thing about how hg works:

**There is no distinction between a working copy and a repository.**

In particular, each repository is a working copy and vice versa. The actual repo is stored inside the working copy at its root in a .hg directory. When you 'checkout' (svn terminology) you do so simply by 'cloning' an existing repository (or if just want a limited set of changes -- e.g. those since you lasted 'updated' (svn terminology) you can do a 'pull'). In fact you could even just make a plain copy that .hg directory and send it to someone -- though obviously this might not work so well if you are moving between 2 OSs with different filesystems.

Anyway, the main point to take from this is that the result of an hg convert will simply be a new directory with all the files (the working copy) plus a .hg directory in that directory (the repo).

To convert all you do is::

    $ hg convert <svn-repo-or-co> <some-new-directory>

If you get weird errors while trying to convert (e.g. "Unknown Repository type") then turn on debug to get more info:

    hg -v --debug convert SOURCE DEST

(For example, in my case it turned out I hadn't got the python svn bindings installed ...)

The devil however is in the detail:

  1. svn-repo-or-co can be the uri of a subversion repo or the path of a svn checkout. Where a checkout hg convert will just work out the source repo and pull from there 
    1. Note however hg convert will not move across working copy files themselves. The obvious solution to this is to do the convert and then just move the .hg file across into your svn checkout and delete all the .svn directories (or vice-versa)
  2. some-new-directory: this is where the new hg repo/working copy with end up.
  3. After doing hg convert rather surprisingly all of the files in the new hg repository will be listed as '?' (not tracked) when you do a `hg status`. To solve this just do a `hg update`
  4. To speed up conversions it is often worth getting a local copy of the subversion repo (to save pulling lots of stuff over the network connection). To do this either use svnsync or just dump the remote repo and load into a local one (if converting from a working copy you'll then just need to do a `svn switch --relocate`
  5. My repository did not have a branches/tags/trunk layout (instead it has multiples subprojects ...). This led to weird errors involving files and directories at the root of the repository which looked like: 'hg convert abort: path contains illegal component'. I solved this by using the `--filemap` option to `hg convert` and putting explicit renames of the form: `/root-path-1 root-path-1` in that file.
  6. What do you for all the other working copies once you have converted the repo/your working copy? This is now simple:
    1. Clone your hg repo to each of the machines with a working copy. (For this purpose you will probably want to make your original hg repo available over the Internet using either ssh or http protocols (for details see mercurial docs).   
    2. Delete all wc files in this new hg repo
    3. Copy svn working files (just from trunk ...) into this hg repo (alternatively do this the other way round and copy the relevant hg stuff .hg, .hgtags etc into the svn working copy ...)
    4. Remove .svn directories:
        
        `$ find . -name '\.svn' -exec rm -Rf {} \;`
    5. Update inside the new hg repo: `$ hg up`


