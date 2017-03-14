---
title: >-
  Web-Based Annotation
slug: web-based-annotation
date: 2006-12-19T17:38:10
themes: [u'Data Systems']
tags: [u'Tech']
projects: [u'Open Knowledge']
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 153
---

We intend to add annotation/commentarysupport to the [open shakespeare](http://www.openshakespeare.org) [web demo](http://demo.openshakespeare.org/) either in this release or next. As a first step I've been looking to see what (open-source) web-based annotation systems are already out there. Below is a list of what I've been able to find so far (if you know of more *please* post a comment). After examining several of these in some detail the one we're going to try our properly is marginalia (if you're interested our current efforts to do this including writing a python wsgi annotation service backend can be found [here in the subversion repository](http://project.knowledgeforge.net/shakespeare/svn/annotater/trunk/)).

1. stet: javascript annotation system used for gpl v3 comments system
    * <http://en.wikipedia.org/wiki/Stet_(software)>
    * Bit of a hack at present and did not seem designed for external reuse (when I last looked the README was fairly emphatic that this was very alpha with little documentation)

2. commentary: javascript based wsgi middleware developed by ian bicking
    * <http://pythonpaste.org/commentary/>
    * Rather hacked together (apparently he coded it in a week). Had problems getting it working locally and no documentation to help in adaptation. Seems to be unmaintained (demo site is currently down) which is perhaps not surprising given how many other projects Ian has on the go.
    * One nice feature is that you don't seem to have to mess with the underlying web pages you want to add comments to (this only works if you are sitting on top of another wsgi application)

3. marginalia: javascript library and spec for adding web annotation to pages
    * <http://www.geof.net/code/annotation/>
    * javascript code seems well factored and understandable and docs are good

4. annotea: W3C project based on RDF
    * <http://www.w3.org/2001/Annotea/>
    * Been around a long time and now seems to be inactive
    * Server and client support rather lacking. No simple interface based on, e.g., javascript -- you have to write a special client yourself -- which is a *major* drawback
    * That said the protocol is [well-documented][annotea-protocol] and so writing a client (or a server) shouldn't be that hard (other than having to mess around with rdf in javascript ...) 
    * The [Schema](http://www.w3.org/2000/10/annotation-ns#) seems reasonable
    * xpointer based which [according to the marginalia site][1] is a problem

[1]: http://www.geof.net/code/annotation/technical
[annotea-protocol]: http://www.w3.org/2001/Annotea/User/Protocol.html

