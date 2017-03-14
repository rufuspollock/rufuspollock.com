---
title: >-
  The Size of the Public Domain
slug: the-size-of-the-public-domain
date: 2009-06-12T13:53:47
themes: [u'Information Economy']
tags: []
projects: [u'Academia', u'EUPD']
posttypes: [u'Own Work']
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 422
---

This post continues the work begun in this [earlier post on "Estimating Information Production and the Size of the Public Domain"][infoprod]. **Update: 2009-07-17** there is now a [follow-up post](/2009/06/12/the-size-of-the-public-domain-ii).

[infoprod]:http://www.rufuspollock.org/2009/06/09/estimating-information-production-and-the-size-of-the-public-domain/

Having already obtained estimates of the number of items (publications) produced each year based on library catalogue data our next step is to convert this into an estimate of the "size" of the public domain. (NB: as already discussed, "size" could mean several different things. Here, at least to start with, we're going to take the simplest and crudest approach and equate size with number of publications/items.)

The natural, and most obvious, approach here is to go through our 1 million+ items and [compute their public domain status (as discussed in this earlier post)][compute]. Unfortunately, as detailed there, this is problematic because we often have insufficient information in library catalogues with which to compute PD status with certainty -- in particular, author death dates are frequently absent. Thus, it will be necessary to fall back on some approximate method.

[compute]:http://www.rufuspollock.org/2009/03/12/computing-copyright-or-public-domain-status-of-cultural-works/

For example, we can use base PD status on simple publication dates: if a book was published, say, 140 years ago it is very likely it is in the public domain -- for it to be in copyright its author must have lived more than 70 years after the book came out (remember copyright lasts for life plus 70 years in the EU)! Conversely, any publication less than 70 years old is almost certainly *not* in the public domain. For periods in between we can assume some proportion of publications are PD starting close to zero for more recent items and rising towards one for older ones. A calculation along those lines is provided in the following table:

<table class="data" border="1"><thead><tr><th>Start</th><th>End</th><th>Items</th><th>% PD</th><th>Number PD</th></tr></thead>
<tbody>
<tr><td>1400</td><td>1870</td><td>389291</td><td>100</td><td>389291</td></tr>
<tr><td>1870</td><td>1880</td><td>50564</td><td>95</td><td>48035</td></tr>
<tr><td>1880</td><td>1890</td><td>66857</td><td>90</td><td>60171</td></tr>
<tr><td>1890</td><td>1900</td><td>66883</td><td>80</td><td>53506</td></tr>
<tr><td>1900</td><td>1910</td><td>70360</td><td>50</td><td>35180</td></tr>
<tr><td>1910</td><td>1920</td><td>60489</td><td>30</td><td>18146</td></tr>
<tr><td>1920</td><td>1930</td><td>78670</td><td>10</td><td>7867</td></tr>
<tr><td>1930</td><td>1940</td><td>90576</td><td>5</td><td>4528</td></tr>
<tr><td>Total</td><td></td><td>873690</td><td>0.71</td><td>616724</td></tr>
</tbody>
</table>
<p class="caption">Number of UK Public Domain Publications (Based on Cambridge University Library Catalogue Data)</caption>

So, based on the assumptions regarding PD proportions given in the table, there are somewhat over 600 thousand PD books according to the holdings of Cambridge University Library (of which just over half, approx 390k are from before 1870). The British Library dataset is approx 4x as big as Cambridge University Library and the numbers scale up roughly proportionately giving a total of over **2.4 million** items.

Of course this is a fairly crude approach based purely on publication date and it be improved in a variety of ways, most notably by using the authorial birth date information which is usually present in catalogue data (we can also use death date information where present). This will be the subject of the next post. (**2009-07-17** the post is up [here](/2009/06/12/the-size-of-the-public-domain-ii)).


