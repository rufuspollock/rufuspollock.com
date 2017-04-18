---
title: >-
  Zen of the Command Line
slug: command-line-zen
date: 2010-02-05T21:11:48
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - page_id: 518
---

# Zen of the Command Line

----

<div style="margin: 40px; 0px;">
<h3><a href="http://dev.rufuspollock.org/command-line-zen/">Zen of the command line has a new home: http://dev.rufuspollock.org/command-line-zen</a></h3>
</div>

----

## Find and Replace Across Multiple Files

<http://rufuspollock.org/2006/09/22/find-and-replace-across-multiple-files/>

## Find and Remove Broken Symbolic Links

     find -L ${directory} -type l 
     # remove the broken links
     find -L ${directory} -type l -print0 | xargs -0 rm 

## Bulk rename files

For example to change files with extension mkd to rst:

<pre>
find . -name "*.mkd" | sed "s/\(.*\).mkd/mv \1.mkd \1.rst/g" | sh
<pre>

## s3cmd

a: 2010-06-17
t: s3cmd css

    # does not seem to auto-detect file type w/o prompting
    s3cmd put --guess-mime-type --acl-public *.css s3://your-bucket/your-dir/

## Mercurial

### Stash working copy changes

1\. Use shelve extension

2\. Use Mercurial Queues (MQ)

    # -f needed as we have local changes
    hg qnew -f patch
    hg qpop

    # later
    hg import --no-commit .hg/patches/patch
    hg qdelete patch

3\. Or without MQ:

<pre>
hg diff > patch
hg update -C .
</pre>

then import the patch later ...

