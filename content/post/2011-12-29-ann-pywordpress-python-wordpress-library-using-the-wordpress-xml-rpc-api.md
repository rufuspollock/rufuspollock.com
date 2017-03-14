---
title: >-
  ANN: PyWordpress - Python Wordpress Library using the Wordpress XML-RPC API
slug: ann-pywordpress-python-wordpress-library-using-the-wordpress-xml-rpc-api
date: 2011-12-29T11:24:55
themes: []
tags: [u'Tech']
projects: [u'Open Knowledge']
posttypes: [u'Own Work']
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1081
---

Announcing [PyWordpress][], a Python library for Wordpress that provides a pythonic interface to Wordpress using the Wordpress XML-RPC API:

* Code on github: <https://github.com/rgrp/pywordpress>
* Python Package Index: <http://pypi.python.org/pypi/pywordpress/>

Along with a wrapper for the main functions it also provides various helper methods, for example to create many pages at once. This is somewhat of a belated announce as the first version of this was written almost a year ago!

[PyWordpress]: https://github.com/rgrp/pywordpress

### Usage

#### Command line

Check out the commands::

    wordpress.py -h 

Commands::

    create_many_pages: Create many pages at once (and only create pages which do not already exist).
    delete_all_pages: Delete all pages (i.e. delete_page for each page in instance).
    delete_page: http://codex.wordpress.org/XML-RPC_wp#wp.deletePage
    edit_page: http://codex.wordpress.org/XML-RPC_wp#wp.editPage
    get_authors: http://codex.wordpress.org/XML-RPC_wp#wp.getAuthors
    get_categories: http://codex.wordpress.org/XML-RPC_wp#wp.getCategories
    get_page: http://codex.wordpress.org/XML-RPC_wp#wp.getPage
    get_page_list: http://codex.wordpress.org/XML-RPC_wp#wp.getPageList
    get_pages: http://codex.wordpress.org/XML-RPC_wp#wp.getPages
    get_tags: http://codex.wordpress.org/XML-RPC_wp#wp.getTags
    init_from_config: Class method to initialize a `Wordpress` instance from an ini file.
    new_page: http://codex.wordpress.org/XML-RPC_wp#wp.newPage

You will need to create a config with the details (url, login) of the wordpress
instance you want to work with::

    cp config.ini.tmpl config.ini
    # now edit away ...
    vim config.ini

#### Python library

Read the code documentation::

    >>> from pywordpress import Wordpress
    >>> help(Wordpress)

### License

MIT-licensed: http://www.opensource.org/licenses/mit-license.php


