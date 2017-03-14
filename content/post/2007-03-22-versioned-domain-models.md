---
title: >-
  Versioned Domain Models
slug: versioned-domain-models
date: 2007-03-22T16:16:10
themes: []
tags: [u'Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 170
---

I've been thinking about how to have a versioned domain model similar to the way we have versioned filesystems (e.g. subversion) for over two years. Over the last few months whatever bits of free time I've had have gone into developing a prototype built on top of sqlobject and I've now got a rough and ready (but fully functional) library: 

<http://project.knowledgeforge.net/ckan/svn/vdm/branches/sqlobj/>

A demo of how it is used is best shown by the tests:

<http://project.knowledgeforge.net/ckan/svn/vdm/branches/sqlobj/vdm/dm_test.py>

Why be tied to SQLObject: obviously being so directly tied to sqlobject is not such a great thing but I intentionally chose to build on it because so many people will already be writing their domain models using SQLObject.

