---
title: >-
  Problems with selfupdate when updating a very old macports
slug: problems-with-selfupdate-when-updating-a-very-old-macports
date: 2007-02-13T13:06:19
themes: []
tags: [u'Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 159
---

Just like [this guy](http://lists.macosforge.org/pipermail/macports-users/2006-December/000997.html) when trying to do $ port selfupdate I'd get errors like:

    Selfupdate failed: couldn't open
    ".../var/db/dports/sources/rsync.rsync.opendarwin.org_dpupdate1/base/dp_version":
    no such file or directory

The problem is that my macports version is very old and after an rsync dp\_version is now in base/config rather than just base. Furthermore because the rsync happens before you check dp_config putting in a symlink or just copying the file over won't work as it gets deleted again before it is checked. The solution I found was to edit /Library/Tcl/darwinports1.0/darwinports.tcl and find this bit of code:

    # get new darwinports version and write the old version back
    set fd [open [file join $dp_base_path dp_version] r]
    gets $fd dp_version_new
    close $fd
    ui_msg "New DarwinPorts base version $dp_version_new"

Then change the first line after the comment so that it reads (i.e. insert 'config'):

    # get new darwinports version and write the old version back
    set fd [open [file join $dp_base_path config dp_version] r]
    gets $fd dp_version_new
    close $fd
    ui_msg "New DarwinPorts base version $dp_version_new"

And hey presto! selfupdate now works.

