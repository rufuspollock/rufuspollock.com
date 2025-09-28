---
title: >-
  csv2ascii: display csv as ascii tables
slug: csv2ascii-display-csv-as-ascii-tables
date: 2006-10-13T08:22:38
themes: []
tags: ['Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 132
---

Having looked around for a while without success for something that would spit out csv files as ascii tables I decided to hack something together. The result is a small python script [csv2ascii.py][]. It is currently fairly crude, for example it just truncates cell text which is too long, but I hope I'll have some more time to improve it soon.

[csv2ascii.py]:http://www.rufuspollock.org/code/bin/csv2ascii.py

### Example

Suppose you had the following in a file called example.csv:

<pre>
"YEAR","PH","RPH","RPH_1","LN_RPH","LN_RPH_1","HH","LN_HH"
1971,7.8523,43.9168,42.9594,3.7822,3.7602,16185,9.691843   
1972,10.5047,55.1134,43.9168370988587,4.0093,3.7822,16397,9.704855
</pre>

Running:

     $ ./csv2ascii.py example.csv

Would result in:

<pre>
+------+------+------+------+------+------+------+------+
| YEAR |  PH  | RPH  |RPH_1 |LN_RPH|LN_RPH|  HH  |LN_HH |
+------+------+------+------+------+------+------+------+
| 1971 |7.8523|43.916|42.959|3.7822|3.7602|16185 |9.6918|
+------+------+------+------+------+------+------+------+
| 1972 |10.504|55.113|43.916|4.0093|3.7822|16397 |9.7048|
+------+------+------+------+------+------+------+------+
</pre>

