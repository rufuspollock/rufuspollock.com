---
title: CKAN Technical Roadmap Thoughts Dec 2015
date: 2015-12-06
theme: ['Data Systems']
---

Thoughts on the future technical evolution of CKAN including:

* The Hamburger Analogy: data portals have three parts:
  * Presentation layer - visualizations, views, etc
  * Metadata-"bus" / data-bus - a common layer for metadata exchange and data store
  * ETL - metadata and data ingest, processing, etc
* Current core CKAN should become more and more metadata and data bus layer.
* Frontend components including visualization, views, showcase etc (including those currently in CKAN) becomes mini separate services that interface with core via the API
* Data ingest including metadata editors, data importers (datapusher etc) should also become their own microservices that interface wit
* The core (meta)-data bus provides an essential separation between Data Presentation and Preparation
* Could improve CKAN as (meta)-data bus by adopting Data Packages and Table Schema (Tabular Data Packages)

{{< pdf src="../images/2015-12-06-ckan-technical-roadmap-thoughts/ckan-technical-roadmap-thoughts-dec-2015.pdf" >}}

