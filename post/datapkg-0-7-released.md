---
title: >-
  Datapkg 0.7 Released
slug: datapkg-0-7-released
date: 2010-11-29T18:25:49
themes: ['Information Economy']
tags: ['Tech']
projects: ['Open Knowledge', 'Shuttleworth Fellowship']
posttypes: ['Updates']
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 746
---

A major new release ([v0.7][datapkg-0.7]) of [datapkg][] is out!

  * Release: <http://pypi.python.org/pypi/datapkg>
  * Docs: <http://packages.python.org/datapkg/>

There's a quick getting started section below (also see [the docs][doc]).

[datapkg]: http://okfn.org/projects/datapkg
[datapkg-0.7]: http://ckan.org/milestone/datapkg-0.7
[doc]: http://packages.python.org/datapkg/

### About the release

This release brings major new functionality to datapkg especially in regard to its integration with [CKAN](http://ckan.net/). datapkg now supports uploading as well as downloading and can now be easily extended via [plugins][plugins]. See the full changelog below for more details.

[plugins]: http://packages.python.org/datapkg/extending.html

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

[Find out more &raquo;][doc] -- including how to create, register and distribute your own 'data packages'.

### Changelog

  * MAJOR: Support for uploading datapkgs (upload.py)
  * MAJOR: Much improved and extended documenation
  * MAJOR: New sqlite-based DB index giving support for a simple, central,
    'local' index (ticket:360)
  * MAJOR: Make datapkg easily extendable

    * Support for adding new Index types with plugins
    * Support for adding new Commands with command plugins
    * Support for adding new Distributions with distribution plugins

  * Improved package download support (also now pluggable)
  * Reimplement url download using only python std lib (removing urlgrabber
    requirment and simplifying installation)
  * Improved spec: support for db type index + better documentation
  * Better configuration management (especially internally)
  * Reduce dependencies by removing usage of PasteScript and PasteDeploy
  * Various minor bugfixes and code improvements


