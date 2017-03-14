---
title: >-
  'Hello World' with WSGI
slug: a-very-simple-introduction-to-wsgi
date: 2006-08-31T16:24:46
themes: []
tags: [u'Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 120
---

I've been seeing a **lot** of talk about WSGI (Web Server Gateway Interface) and its benefits over the last six months or so and I've been meaning to take a look -- not least because of the potential to use wsgi middleware to make a nice front-controller for [KForge](http://www.kforgeproject.com/).

## First Stop ##

A quick google takes me to: <http://www.wsgi.org/wsgi>. I'm looking to just write the proverbial 'hello world' app at this stage. Most of the references are bit too high level (or complex) for me (though [this one][1] is an exception). So here I'm going to detail my experiences of familiarizing myself with wsgi by writing the classic 'hello world' app (if you looking to do something more sophisticated with wsgi check out a toolkit such as [paste][3] or [pylons][2] the framework built on top of paste).

## Hello World ##

### 1. Install wsgiref ###

wsgiref is the wsgi reference implementation that is now part of python 2.5 standard library. If you are running python version less than 2.5 you will want to do:

      $ sudo easy_install wsgiref

### 2. Get a web server ###

We'll use the wsgiref simple server as detailed in the [docs](http://docs.python.org/dev/lib/module-wsgiref.simpleserver.html) (if you want to use a 'proper' webserver see the section below on making your wsgi app available via fastcgi). Create a python module, simpletest.py say, and insert:

      from wsgiref.simple_server import make_server, demo_app
      
      httpd = make_server('', 8000, demo_app)
      print "Serving HTTP on port 8000..."
      
      # Respond to requests until process is killed
      httpd.serve_forever()
      
      # Alternative: serve one request, then exit
      ##httpd.handle_request()

### 3. Run it ###

Start the server:

      $ python simpletest.py

Then visit <http://localhost:8000/>

Bingo! We've got our first working wsgi app (demo_app should output 'Hello world!' followed by a list of variable values).

### 4. Make our own Hello World app ###

We haven't yet written anything ourselves -- we're just using the demo_app bundled with wsgiref. So change simpletest.py to be:

      def simple_app(environ, start_response):
          """Simplest possible application object""" 
          status = '200 OK'
          response_headers = [('Content-type','text/plain')]
          start_response(status, response_headers)
          return ['My Own Hello World!\n']
      
      from wsgiref.simple_server import make_server, demo_app
      
      httpd = make_server('', 8000, simple_app)
      print "Serving HTTP on port 8000..."
      
      # Respond to requests until process is killed
      httpd.serve_forever()
      
Run this and visit <http://localhost:8000/> and you should see a blank page containing 'My Own Hello World!'.

### 5. Using a Class ###

Finally for completeness here's the same application but done as a class:

      class SimpleApp:
          """Produce the same output, but using a class
          """
          def __init__(self, environ, start_response):
              self.environ = environ
              self.start = start_response

          def __iter__(self):
              status = '200 OK'
              response_headers = [('Content-type','text/plain')]
              self.start(status, response_headers)
              yield 'My Own Hello world!\n'

      from wsgiref.simple_server import make_server, demo_app

      # httpd = make_server('', 8000, simple_app)
      # the same but using a class
      httpd = make_server('', 8000, SimpleApp)
      
      print "Serving HTTP on port 8000..."

      # Respond to requests until process is killed
      httpd.serve_forever()

## Serving an WSGI App via FastCGI ##

This section explains how to serve your WSGI app via FastCGI (other methods using scgi or even cgi take an almost identical approach).

### 1. Install a fastcgi interface to wsgi: ###

Use flup which provides a fastcgi and scgi interface to wsgi:

      $ sudo easy_install flup

### 2. Install a simple standalone fastcgi implementation: ###

1. Download <http://www.saddi.com/software/py-lib/py-lib/fcgi.py>
2. Install this somewhere you can import it as import fcgi

### 3. Attach your wsgi application to this fcgi server ###

Create a python file (server.fcgi) and paste in the following: 

      #!/usr/bin/env python
      from myapplication import app # Assume app is your WSGI application object
      from fcgi import WSGIServer
      WSGIServer(app).run()

Now you can just point your webserver at this file (make sure you've configured it to handle .fcgi files using fastcgi) and your app is available via fastcgi.

## References ##

[1]: http://isapi-wsgi.python-hosting.com/wiki/WSGI-Gateway-or-Glue>
[2]: http://www.pylonshq.com/
[3]: http://www.pythonpaste.org/


