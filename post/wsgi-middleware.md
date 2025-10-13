---
title: >-
  WSGI Middleware
slug: wsgi-middleware
date: 2006-09-28T19:15:29
themes: []
tags: ['Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 127
---

# WSGI Middleware #

In a [previous tutorial][tut-01] we just wrote a basic 'Hello World'
application in WSGI. At the end of you might, rightly, have been wondering
what's the point of WSGI -- after all you could have written that 'Hello World'
app using plain CGI (or anything else for that matter). In this tutorial we are
going to start answering that question by taking a look at WSGI middleware and
write a simple piece of middleware ourselves.

[tut-01]: http://www.thefactz.org/ideas/archives/120

## A Simple Example ##

Here a simple piece of middleware that adds authentication based on the remote
address of the client (this tutorial and its code is available in raw form at
http://www.rufuspollock.org/code/wsgi/):

<pre><code>
from wsgiref.simple_server import make_server, demo_app

class AuthenticationMiddleware:
    """A modified version of an original example at:
    http://isapi-wsgi.python-hosting.com/wiki/WSGI-Gateway-or-Glue
    """

    def __init__(self, app, allowed_addresses):
        """
        @param app: the WSGI app we will that comes after us
        @param allowed_addresses: list of remote addresses from which to allow
                                  access
        """
        self.app = app
        self.allowed_addresses = allowed_addresses

    def __call__(self, environ, start_response):
        """The standard WSGI interface"""
        addr = environ.get('REMOTE_ADDR','UNKNOWN') 

        if addr in self.allowed_addresses: # pass through to the next app
            return self.app(environ, start_response)
        else: # put up a response denied
            start_response(
                '403 Forbidden', [('Content-type', 'text/html')])
            return ['You are forbidden to view this resource']

addresses = [ '127.0.0.1' ]
simple_app_with_auth = AuthenticationMiddleware(demo_app, addresses)

if __name__ == '__main__': 

    httpd = make_server('', 8000, simple_app_with_auth)
    print "Serving HTTP on port 8000..."

    # Respond to requests until process is killed
    httpd.serve_forever()
</code></pre>

## The Basic Idea ##

As explained in [pep-333] the basic idea of middleware is of something that
'plays both sides':

> Note that a single object may play the role of a server with respect to some
> application(s), while also acting as an application with respect to some
> server(s). Such "middleware" components can perform such functions as:
> 
>   * Routing a request to different application objects based on the target
>   URL, after rewriting the environ accordingly.  * Allowing multiple
>   applications or frameworks to run side-by-side in the same process * Load
>   balancing and remote processing, by forwarding requests and responses over
>   a network * Perform content postprocessing, such as applying XSL
>   stylesheets

A diagram helps:
 

                 WSGI SERVER
    
                   V   A
                   V   A
                   |   |
                   |   |
          +---------------------+
          |        |   |        |
          |   +-------------+   |
          |   |    V   A    |   |
          |   |   +-----+   |   |
          |   |   | APP |   |   |
          |   |   +-----+   |   |
          |   | MIDDLEWARE1 |   |
          |   +-------------+   |
          |     MIDDLEWARE2     |
          +---------------------+

       The WSGI Application + Middleware 'Onion'

Basically middleware wraps an underlying wsgi application and then presents itself as the new wsgi application to external callers. In python code the above would like:

    core_app = SomeWsgiApplication()
    # remember the middleware is itself a wsgi application
    wrapped_once = Middleware1(core_app)
    # wrap the new wsgi application!
    wrapped_twice = Middleware2(wrapped_once)

    # alternatively we could do it all in one
    wrapped = Middleware2(Middleware1(core_app))

## Remarks ##

Middleware is useful because it dramatically increases the possibilities for using
standard web application plumbing -- any piece of middleware can now be plugged
together very easily with either other middleware or an application.

Middleware is usually one of three types:

  * pre-processors
  * post-processors
  * those that do both (rare)

Examples of pre-processors are:
  
  * Authenticators (including session management)
  * Dispatchers including proxies and controllers

Examples of post-processors:

  * Applying an [XSL style sheet][xslt-middleware]
  * Tidying html or providing [safe xhtml][]

[xslt-middleware]: http://www.decafbad.com/2005/07/xmlwiki/lib/xmlwiki/xslfilter.py 
[safe xhtml]: http://www-128.ibm.com/developerworks/library/wa-wsgi/ 

In general, pre-processors are a little simpler because they
don't have to deal with the 'chunking' aspect of WSGI (a WSGI application
return an iterable rather than just a single buffer so as to allow 'chunking'
of output -- this will be useful, for example, when streaming large files, see
the'Buffering and Streaming' section in [PEP 333][pep-333] for more information).

[pep-333]: http://www.python.org/dev/peps/pep-0333/


