---
title: >-
  CKAN v1.2 Released together with Datapkg v0.7
slug: ckan-v1-2-released-together-with-datapkg-v0-7
date: 2010-11-30T21:14:33
themes: [u'Information Economy']
tags: [u'Tech']
projects: [u'Open Knowledge', u'Shuttleworth Fellowship']
posttypes: [u'Own Work', u'Updates']
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 753
---

**This is a cross-post of the [release announcement][ckan-announce] originally put up on the [OKFN Blog][blog.okfn.org].**

----

[ckan-announce]: http://blog.okfn.org/2010/11/30/ckan-v12-released-together-with-datapkg-v07/
[blog.okfn.org]: http://blog.okfn.org/

We're delighted to announce [CKAN v1.2][ckan-v1.2], a new major release of the [CKAN software][ckan]. This is the largest iteration so far with 146 tickets closed and includes some really significant improvements most importantly a new [extension/plugin system][ckan-plugins], SOLR search integration, caching and INSPIRE support (more details below). The [extension work][ckan-plugins] is especially significant as it now means you can extend CKAN without having to delve into *any* core code.

In addition there are now [over 20 CKAN instances][ckan-instances] running around the world and CKAN is being used in official government catalogues in the UK, Norway, Finland and the Netherlands. Furthermore, <http://ckan.net/> -- our main community catalogue -- now has over [1500 data 'packages'][ckan-stats] and has become the official home for the [LOD Cloud][lod-cloud-ckan] (see the [lod group on ckan.net](http://www.ckan.net/group/lodcloud)).

We're also aiming to provide a much more integrated 'datahub' experience with CKAN. Key to this is the provision of a 'storage' component to complement the registry/catalogue component we already have. Integrated storage will support all kinds of important functionality from [automated archival of datasets](http://ckan.org/ticket/402) to [dataset cleaning with google refine](http://ckan.org/ticket/837).

We've already been making progress on this front with the launch of a basic storage service at <http://storage.ckan.net/> (back in September) and the development of the [OFS bucket storage library][ofs]. The functionality is still at an alpha stage and integration with CKAN is still limited so improving this area will be a big aim for the next release (v1.3).

Even in its alpha stage, we are already making use of the storage system, most significantly, in the latest release of [datapkg][datapkg], our tool for distributing, discovering and installing data (and content) â€˜packagesâ€™. In particular, the v0.7 release (more detail below) includes upload support allowing you store (as well as register) your data 'packages'.

[ckan]: http://ckan.org/
[ckan-v1.2]: http://ckan.org/milestone/ckan-v1.2
[ckan-instances]: http://wiki.okfn.org/ckan/instances/
[ckan-plugins]: http://packages.python.org/ckan/plugins.html
[lod-cloud-ckan]: http://blog.okfn.org/2010/09/03/next-version-of-the-linked-open-data-cloud-based-on-ckan/
[ckan-stats]: http://ckan.net/stats/
[ofs]: http://bitbucket.org/okfn/ofs/src

### Highlights of CKAN v1.2 release

  * Package edit form: attach package to groups (#652) & revealable help
  * Form API - Package/Harvester Create/New (#545)
  * Authorization extended: authorization groups (#647) and creation of packages (#648)
  * [Extension / Plug-in interface][ckan-plugins] classes (#741)
  * WordPress twentyten compatible theming (#797)
  * Caching support (ETag) (#693)
  * Harvesting GEMINI2 metadata records from OGC CSW servers (#566)

Minor:

  * New API key header (#466)
  * Group metadata now revisioned (#231)

[All tickets][ckan-v1.2]

## Datapkg Release Notes

A major new release ([v0.7][datapkg-0.7]) of [datapkg][] is out!

  * Release: <http://pypi.python.org/pypi/datapkg>
  * Docs: <http://packages.python.org/datapkg/>

There's a quick getting started section below (also see [the docs][datapkg-doc]).

[datapkg]: http://okfn.org/projects/datapkg
[datapkg-0.7]: http://ckan.org/milestone/datapkg-0.7
[datapkg-doc]: http://packages.python.org/datapkg/

### About the release

This release brings major new functionality to datapkg especially in regard to its integration with [CKAN](http://ckan.net/). datapkg now supports uploading as well as downloading and can now be easily extended via [plugins][datapkg-plugins]. See the full changelog below for more details.

[datapkg-plugins]: http://packages.python.org/datapkg/extending.html

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
    
    # 5. Store some data
    # Edit the gold prices csv making some corrections
    $ cp gold-prices/data mynew.csv
    $ edit mynew.csv
    # Now upload back to storage
    $ datapkg upload mynew.csv ckan://mybucket/ckan-gold-prices/mynew.csv

[Find out more &raquo;][datapkg-doc] -- including how to create, register and distribute your own 'data packages'.

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

### Credits

A big hat-tip to [Mike Chelen](http://friendfeed.com/mikechelen) and Matthew Brett for beta-testing this release and to Will Waites for code contributions.

