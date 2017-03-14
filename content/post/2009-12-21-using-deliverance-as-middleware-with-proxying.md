---
title: >-
  Using Deliverance as Middleware (with Proxying)
slug: using-deliverance-as-middleware-with-proxying
date: 2009-12-21T15:00:51
themes: []
tags: [u'Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 467
---

[Deliverance][] is a great library that lets you easily re-theme external websites on the fly. Designed as WSGI middleware, it can be easily combined with some proxying to integrate a bunch of websites together 

You can use deliverance plus proxying out-of-the-box using the deliverance-proxy command. However, I was interested in using Deliverance as middleware **from code**. This turned out to be none too trivial to do -- all the examples on the internet seemed to focus on using deliverance-proxy or using it in an ini file.

After much wrestling, most notably with odd issues with gzipped (deflated) content I got it working and you can find a demo implementation (see [demo.py](http://rufuspollock.org/code/deliverance/demo.py) and [README.txt](http://rufuspollock.org/code/deliverance/README.txt)) here:

<http://rufuspollock.org/code/deliverance/>

I should also mention the following sources which were all of help in my quest: 

  * <http://codespeak.net/svn/z3/deliverance/sandbox/ianb/ploneconf2008/index.txt>
  * <http://www.gawel.org/weblog/en/2008/12/skinning-with-pyquery-and-deliverance>
  * <http://macadames.wordpress.com/2009/05/23/some-deliverance-tips/>
  * <http://www.coactivate.org/projects/deliverance/lists/deliverance-discussion/archive/2009/05/1241444934295/forum_view>
  * <http://www.sixfeetup.com/blog/2009/4/27/deploying-plone-and-zine-together-with-deliverance-using-repoze>

[Deliverance]: http://pypi.python.org/pypi/Deliverance/


