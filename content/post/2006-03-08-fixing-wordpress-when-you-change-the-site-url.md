---
title: >-
  Fixing Wordpress When You Change the Site URL
slug: fixing-wordpress-when-you-change-the-site-url
date: 2006-03-08T22:49:17
themes: []
tags: ['Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 70
---

Very annoyingly if you update the WP site url (or move your blog without updating site url) your install will be b0rked and you will have to go mess around with the db. What you need to do (tested on WP 2.0) is:

<pre>
update wp_options set option_value = '[wordpress -address]' where option_name = 'siteurl';
</pre>
<pre>
update wp_options set option_value = '[site -address]' where option_name = 'home';
</pre>

