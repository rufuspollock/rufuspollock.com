---
title: >-
  Accessing open access repositories using the python oaipmh package
slug: accessing-open-access-repositories-using-the-python-oaipmh-package
date: 2006-10-06T08:22:43
themes: []
tags: [u'Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 131
---

The Open Access Initiative Protocol for Metadata Harvesting (OAIPMH) is growing rapidly as the standard web protocol for making metadata, primarily bibliographic information, available online for programmatic access and I've long meant to write something that would allow be to pull information down from remote repositories into my local bibliographic database automatically (it would save an awful lot of typing).

I've mentioned the [oaipmh package provided by infrae.com](http://www.infrae.com/download/oaipmh) [before](http://www.thefactz.org/ideas/archives/14) however the documentation they provide has got rather out of date and though I've made a few attempts I've never quite been able to get it to work. However after a bit more effort recently with the newer v2.0+ of the package I've managed to get something basic working which you can find at <http://www.rufuspollock.org/code/oaipmh/demo.py>.

I should note that my main interest, at least at present, is in the client-side, not the server-side of oaipmh so the code is oriented in that direction -- as I mentioned above my aim is to automatically pull down article metadata into my local bibliographic system from sites such as [repec](http://repec.org/) ([repec oai url](http://oai.repec.openlib.org/)).

