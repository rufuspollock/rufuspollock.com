---
title: >-
  A Pythonic API to Subversion Repositories
slug: a-pythonic-api-to-subversion-repositories
date: 2006-11-15T14:01:35
themes: []
tags: [u'Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 142
---

Whenever I've had a few spare minutes over the last couple of months I've been hacking away on [svnrepo][], a pythonic API to local subversion repositories and it is now robust enough to warrant a 0.1 release. [svnrepo][] is (and was intended to be) very small, just a single module, that wrapped the python subversion bindings for repository access to make them simpler to use and more object-oriented. At present the module requires subversion >= 1.3 but I'm hoping to scale that dependency back in future releases.

### Getting it

The module is Open Source software (MIT-licensed) and you can either:

1. Download it directly from: <http://www.rufuspollock.org/code/svnrepo/svnrepo.py>

2. Or get it the python package index. If you are using setuptools just do:

       $ easy_install svnrepo

### What it looks like

There are unit tests at:

<http://www.rufuspollock.org/code/svnrepo/svnrepo_test.py>

And they are pretty good at demonstrating how to use the API but just for the sake of demonstration. Assume that you have an existing subversion repository at REPOSPATH.

<pre><code>
from svnrepo import *
REPOSPATH = ...
repos = Repository(REPOSPATH)

history = repos.history('/')
for revision in history:
    print history

rev = repos.get_revision() # get the youngest revision
print rev.log # the log message of the revision
print rev.date

# get a node
rootdir = rev.get_node('/')
print rootdir.is_dir()
print rootdir.list_dir()

# create a new revision
newrev = repos.new_revision()
newrev.log = 'My new revision'
newrev.author = 'me'
fs = newrev.file_system
filepath = 'tmp.txt'
newfile = fs.make_file(filepath)

text = 'nothing ever exists entirely alone'
newfile.write(text)
        
propname = 'copyright'
propval = 'nemo'
newfile.set_property(propname, propval)
        
newrev.commit()
</code></pre> 

[svnrepo]: http://www.rufuspollock.org/code/svnrepo/


