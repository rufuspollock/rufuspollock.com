---
title: >-
  Datapkg v0.7 Beta Released
slug: datapkg-v0-7-beta-released
date: 2010-10-14T12:21:30
themes: ['Information Economy']
tags: ['Tech']
projects: ['Open Knowledge', 'Shuttleworth Fellowship']
posttypes: ['Own Work', 'Updates']
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 679
---

I've just put out a beta of a major new version of [datapkg](http://okfn.org/projects/datapkg) (see changelog below):

  * Release: <http://pypi.python.org/pypi/datapkg>
  * Docs: <http://packages.python.org/datapkg/>

There's a quick getting started section below (also see docs).

[doc]: http://packages.python.org/datapkg/

### About the release

This is a substantial release with a lot of new features. As this is a
client app which will run on a variety of platforms its been released
as a beta first so there's a chance to catch any of the cross-platform
compatibility bugs that inevitably show up. (My favourite from last time was a variation between python 2.5
and 2.6 in the way urlparse functioned for non-standard schemes ...)

I'd therefore really welcome any feedback especially regarding bugs
and from people using platforms I don't usually -- such as windows!

### Get started fast

    # 1. Install: (requires python and easy_install)
    $ easy_install datapkg
    # Or, if you don't like easy_install
    $ pip install datapkg or even the raw source!

    # 2. [optional] Take a look at the manual
    $ datapkg man

    # 3. Search for something
    $ datapkg search ckan:// gold
    gold-prices -- Gold Prices in London 1950-2008 (Monthly)

    # 4. Get some data
    # This will result in a csv file at /tmp/gold-prices/data
    $ datapkg download ckan://gold-prices /tmp

[Find out more &raquo;][doc] -- including how to create, register and distribute your own 'data packages.

### Changelog

 * (MAJOR) Support for uploading datapkgs (upload.py)
 * (MAJOR) Much improved and extended documenation
 * (MAJOR) Make datapkg easily extendable
   * Support for adding new Index types with plugins
   * Support for adding new Commands with command plugins
   * Support for adding new Distributions with distribution plugins
 * Improved package download support (also now pluggable)
 * New sqlite-based DB index (ticket:360)
 * Improved spec: support for db type index + better documentation
 * Better configuration management (especially internally)
 * Reduce dependencies by removing dependency on PasteScript and PasteDeploy
 * Various minor bugfixes and code improvements


