---
title: >-
  PyWordpress - Python Library for Wordpress
slug: pywordpress-python-library-for-wordpress
date: 2011-01-05T10:42:15
themes: []
tags: ['Tech']
projects: []
posttypes: ['Own Work']
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 814
---

Announcing [pywordpress][], a python interface to Wordpress using the Wordpress XML-RPC API.

 * Download: <http://pypi.python.org/pypi/pywordpress/>
 * Source code: <https://bitbucket.org/rgrp/pywordpress/>

[pywordpress]: https://bitbucket.org/rgrp/pywordpress

Usage
=====

Command line
------------

Check out the commands::

    wordpress.py -h 

You will need to create a config with the details (url, login) of the wordpress
instance you want to work with::

    cp config.ini.tmpl config.ini
    # now edit away ...
    vim config.ini


Python library
--------------

Read the code documentation::

    >>> from pywordpress import Wordpress
    >>> help(Wordpress)


