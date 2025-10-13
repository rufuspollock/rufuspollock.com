---
title: >-
  Flexible Dates in Python (including BC)
slug: flexible-dates-in-python
date: 2009-06-18T19:37:09
themes: ['Information Economy']
tags: ['Books', 'Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 537
---

I've had [occasion](http://www.rufuspollock.org/2009/03/12/computing-copyright-or-public-domain-status-of-cultural-works/) [recently](http://www.rufuspollock.org/2009/06/12/the-size-of-the-public-domain/) to frequently work with "dates" that come in a lot of shapes and sizes including:

  * Dates in distant past and future including BC/BCE dates
  * Dates in a wild variety of formats: Jan 1890, January 1890, 1st Dec 1890, Spring 1890 etc
  * Dates of varying precision: e.g. 1890, 1890-01 (i.e. Jan 1890), 1890-01-02
  * Imprecise dates: c1890, 1890?, fl 1890 etc

Unfortunately existing support for these in python is fairly weak. I therefore authored a python FlexiDate module (now part of [datautil][] <strike>part of a new [swiss (army knife) package](http://pypi.python.org/pypi/swiss/)</strike>) which is focused on supporting:

[datautil]: http://pypi.python.org/pypi/datautil

  1. Dates outside of Python (or DB) supported period (esp. dates < 0 AD)
  2. Imprecise dates (c.1860, 18??, fl. 1534, etc)
  3. Normalization of these dates to machine processable versions especially:
    * ISO 8601
    * Dates sortable in the database (in correct date order)

## Background

Things we would like:

  1. Dates outside of Python (or DB) supported period (esp. dates < 0 AD)
  2. Imprecise dates (c.1860, 18??, fl. 1534, etc)
  3. Normalization of dates to machine processable versions
  4. Sortable in the database (in correct date order)
  5. Human readability as dates will be re-edited/viewed by people

Not all of these requirements are satisfiable at once in a simple way.

Be clear about what we want:

  1. Storage (and preservation) of "user" dates (both normal and non-normal)
  2. Normalization of dates (e.g. to ~ ISO 8601)
  3. Integration with database (sortability and serializability)

Solution for 1: Represent dates as strings.

Solution for 2: Have a parser (via an intermediate FlexiDate object).

Solution for 3: convert to a float.

Remark: no string based date format will sort dates correctly based on std
string ordering (PF: let x,y be +ve dates and X,Y their string representations
then if X &lt; Y => -X &lt; -Y (wrong!))

Thus we need to add some other field if we wish dates to be correctly sorted
(or not worry about sorting of -ve dates ...)

1. For any given date attribute have 2 actual fields:

  * user version -- the version edited by users
  * normalized/parsed version -- a version that is usable by machines

2. Store both versions in a single field but with some form of serialization.

3. Convert dates to long ints (unlimited in precision) and put this in a
separate field and use that for sorting.


### Comments

Initially thought that we should parse before saving into a FlexiDate format
but: a) why bother b) when parsing always hard not to be lossy (in particular
when converting to iso8601 using e.g. dateutil very difficult to not add info
e.g. parsing 1860 can easily give us 1860-01-01 ...).


### References and Existing Libraries

  * Excellent dateutil (which we use)
  * http://wiki.python.org/moin/WorkingWithTime
  * ISO 8601: http://www.iso.org/iso/date_and_time_format
     * http://code.google.com/p/pyiso8601/source/browse/trunk/iso8601/iso8601.py
  * http://www.feedparser.org/docs/date-parsing.html
  * http://seehuhn.de/pages/pdate


