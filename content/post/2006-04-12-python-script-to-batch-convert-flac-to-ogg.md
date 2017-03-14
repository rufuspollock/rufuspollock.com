---
title: >-
  Python Script to Batch Convert Flac to Ogg
slug: python-script-to-batch-convert-flac-to-ogg
date: 2006-04-12T10:59:46
themes: []
tags: [u'Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 79
---

<pre style="font-size: 110%">
#!/usr/bin/env python
# Convert a whole directory tree of flac files to oggs
# Just a wrapper on a couple of system commands
# Could be made more 'pythonic' by replacing find with os.walk
# Public Domain: copy, redistribute, reuse freely and without restriction
import os
import shutil
import commands

# base directory for flac files
srcPath = '/var/share/music'
# destination directory for ogg files
destPath = '/var/share/ogg'

cmds = [
        "find . -type d -exec mkdir %s/'{}' \\;" % destPath,
        "find . -name '*.flac' -exec oggenc --quiet --quality 4 '{}' \\;",
        "find . -name '*.ogg' -exec mv '{}' %s/'{}' \\;" % destPath,
        ]

def run_cmd(cmd):
    status, output = commands.getstatusoutput(cmd)
    if status:
        print 'Had error running [%s]: %s' % (cmd, output)

def convert_to_ogg(clean=True):
    if clean:
        shutil.rmtree(destPath)
    if not os.path.exists(destPath):
        os.makedirs(destPath)
    os.chdir(srcPath)
    for cmd in cmds:
        run_cmd(cmd)

if __name__ == '__main__':
    convert_to_ogg()
</pre>

