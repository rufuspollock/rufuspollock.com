---
title: >-
  Open-Source Annotation Toolkit for Inline, Online Web Annotation
slug: open-source-annotation-toolkit-for-inline-online-web-annotation
date: 2010-11-11T10:55:03
themes: []
tags: ['Tech']
projects: ['Open Knowledge', 'Shuttleworth Fellowship']
posttypes: ['Own Work', 'Updates']
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 701
---

I've been working on web-annotation -- inline, online annotation of web texts -- for [several years](/2006/12/19/web-based-annotation/).

My original motivation was to support annotation of texts in http://openshakespeare.org/ so we can collaboratively build up critical notes but since then I've seen this need again and again -- in drafting new open data licenses, with scholars working on medieval canon law, when taking my own notes on academic papers.

<img src="http://rufuspollock.org/wp-content/uploads/2010/11/openshakespeare-annotate-zoom-20101108.png" alt="http://openshakespeare.org annotation" title="openshakespeare-annotate-zoom-20101108" class="displayed" style="width: auto;" />
<p class="caption"><a href="http://openshakespeare.org/work/annotate/hamlet">
Open Shakespeare's Hamlet in annotate mode</a></p>

What's surprised me is that there appears to be no good opensource tool out there to do this. There are several commercial offerings (including annotation in google docs), and there have been opensource attempts such as annotea, Stet (for GPLv3), marginalia, and co-ment but none of these really seemed to work -- my [original implementation in 2006/2007](http://openshakespeare.org/2007/04/10/annotation-is-working) of annotation for http://openshakespeare.org/ used http://geof.net/'s (excellent) marginalia library but I ultimately ran into performance and integration problems).

Thus, a year and a half ago, in collaboration with [Nick Stenning](http://whiteink.com/), we started developing an [annotator project][annotator] to create a new, simple javascript (+backend) library for web-annotation. Our main goals were and are:

  * **Annotation of *arbitrary* text ranges**
  * **Annotate** any web (html) document
  * **Easy to use** -- 2 lines of javascript to insert this in your web page/app etc
  * **Well-factored and library-structured** -- easy to integrate and easy to extend

Nick's (who's a *great* javascript (and css) developer), has been responsible for writing all of the frontend (i.e. the annotation stuff you actually see!) while I've developed the backend annotation store.

In the way of spare-time projects, development has been rather slower than we would have liked but we now have a **functioning alpha which has now been running successfully on http://openshakespeare.org/ for the last 6 months**.

Furthermore, the system is completely app-agnostic and is incredibly easy to use -- adding annotation to your web page only requires one line of jquery javascript (assuming a backend is set up):

>     $('#your-element-id').annotator()

**Interested?** Below are links to project information including the source code and docs and mailing list. We're especially eager to get feedback from those looking to integrate into other apps or who would like to help develop the library features.

[annotator]: http://okfn.org/projects/annotator/

### Project Info

  * [Official project home page][annotator]
  * [Mailing list](http://lists.okfn.org/mailman/listinfo/okfn-help)
  * Email us directly at *annotator [at] okfn [dot] org*.

### Source code

  * Javascript library: http://github.com/nickstenning/annotator [docs](https://github.com/nickstenning/annotator/blob/master/README.markdown)
  * Backend: http://github.com/nickstenning/annotator-store-py [docs](https://github.com/nickstenning/annotator-store-py/blob/master/README.rst)
    * SQL + Python backend
    * Alpha couchdb backend
  
### Features

  * Open JSON-REST annotation protocol - simple JSON and REST-based
  * Javascript (jquery-based) library for inserting inline annotations in a given document supporting this protocol
  * One or more backends implementing this protocol (emphasis on backends that are easy to deploy using standard tools e.g. using sql database or couchdb)
  * Really simple: just do (jquery-esqe) $('myelement').annotator() to get up and running
  * Fast even on large documents
  * Support of multiple users
  * Pluggable backends


