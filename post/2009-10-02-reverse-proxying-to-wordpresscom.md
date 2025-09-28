---
title: >-
  Reverse Proxying to Wordpress.com
slug: reverse-proxying-to-wordpresscom
date: 2009-10-02T10:50:11
themes: []
tags: ['Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 439
---

I wanted to do a reverse proxy to wordpress.com in order to integrate an existing wordpress.com blog into an existing site. This turned out to be a little trickier than I'd thought due to wordpress.com's usage of gzip deflation of their output.

Figured this out thanks to sound advice [here](http://www.apachetutor.org/admin/reverseproxies) and [here](http://wiki.uniformserver.com/index.php/Reverse_Proxy_Server_2:_mod_proxy_html_2):

      ...

      <Proxy *>
            Allow from .mysite.com
      </Proxy>
      ProxyPass / myblog.wordpress.com
      ProxyPassReverse / http://myblog.wordpress.com/
      ProxyHTMLURLMap http://myblog.wordpress.com/ /
      <Location />
        SetOutputFilter proxy-html
        # get rid of Content-Encoding at wordpress end
        # To use this you'll need to do (on debian) a2enmod headers
        RequestHeader unset  Accept-Encoding

        # Alternative method: inflate then deflate again ... (requires more effort at our end)
        # Could NOT get this to work (though suggested by both reference sites!)
        # SetOutputFilter INFLATE;proxy-html;DEFLATE
      </Location>

      ....


