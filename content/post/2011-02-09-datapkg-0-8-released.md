---
title: >-
  Datapkg 0.8 Released
slug: datapkg-0-8-released
date: 2011-02-09T17:48:11
themes: [u'Information Economy']
tags: [u'Tech']
projects: [u'Open Knowledge', u'Shuttleworth Fellowship']
posttypes: [u'Updates']
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 857
---

A new release ([v0.8][datapkg-0.8]) of [datapkg][], the tool for distributing, discovering and installing data is out!

  * Release: <http://pypi.python.org/pypi/datapkg>
  * Docs: <http://packages.python.org/datapkg/>

There's a quick getting started section below (also see [the docs][doc]).

[datapkg]: http://okfn.org/projects/datapkg
[datapkg-0.8]: http://ckan.org/milestone/datapkg-0.7
[doc]: http://packages.python.org/datapkg/

### About the release

This release brings substantial improvements to the download functionality of datapkg including support for extending the download system via [plugins][plugins]. The full changelog below has more details and here's an example of the new download system being used to download material selectively from the [COFOG package][cofog] on [CKAN][].

[cofog]: http://ckan.net/package/cofog
[CKAN]: http://ckan.net/

[plugins]: http://packages.python.org/datapkg/extending.html

    # download metadata and all resources from cofog package to current directory
    # Resources to retrieve will be selected interactively
    download ckan://cofog .

    # download all resources
    # Note need to quote *
    download ckan://name path-on-disk "*"

    # download only those resources that have format 'csv' (or 'CSV')
    download ckan://name path-on-disk csv

For more details see the documentation of the download command:

    datapkg help download

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

  * ResourceDownloader objects and plugin point (#964)
  * Refactor PackageDownloader to use ResourceDownloader and support Resource
    filtering
  * Retrieval options for package resourcs (#405). Support selection of
    resources to download (on command line or API) via glob style patterns or
    user interaction.


