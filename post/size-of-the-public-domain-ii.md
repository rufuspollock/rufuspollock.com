---
title: >-
  Size of the Public Domain II
slug: size-of-the-public-domain-ii
date: 2009-07-16T11:24:14
themes: ['Information Economy']
tags: []
projects: ['Academia', 'EUPD']
posttypes: ['Own Work']
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 434
---

This follows up my [previous post][prev-post]. Here we are going to calculation public domain numbers based directly on authorial birth/death date information rather than on guesstimated weightings. We're going to focus on the Cambridge University Library (CUL) data we used previously.

[prev-post]:http://www.rufuspollock.org/2009/06/12/the-size-of-the-public-domain/

<table class="data">
<thead><tr><th>Pub. Date</th><th>Total</th><th>No Author</th><th>Any Date</th><th>Death Date</th></tr></thead>
<tbody>
<tr><td>1870-1880</td><td>50564</td><td>6634 (13%)</td><td>23016 (45%)</td><td>21876 (43%)</td></tr>
<tr><td>1880-1890</td><td>66857</td><td>8225 (12%)</td><td>31135 (46%)</td><td>28570 (42%)</td></tr>
<tr><td>1890-1900</td><td>66883</td><td>8733 (13%)</td><td>32169 (48%)</td><td>28971 (43%)</td></tr>
<tr><td>1900-1910</td><td>70360</td><td>8594 (12%)</td><td>35401 (50%)</td><td>29922 (42%)</td></tr>
<tr><td>1910-1920</td><td>60489</td><td>7722 (12%)</td><td>31336 (51%)</td><td>24608 (40%)</td></tr>
<tr><td>1920-1930</td><td>78670</td><td>9023 (11%)</td><td>44219 (56%)</td><td>32658 (41%)</td></tr>
<tr><td>1930-1940</td><td>90576</td><td>11004 (12%)</td><td>46849 (51%)</td><td>29372 (32%)</td></tr>
<tr><td>1940-1950</td><td>72692</td><td>7638 (10%)</td><td>36495 (50%)</td><td>22155 (30%)</td></tr>
</tbody>
</table>

<p class="caption">Table 1: PD Relevant Information Availability</p>


Table 1 presents a summary of how much relevant information is available for items (books) of particular vintages in the CUL catalogue -- we only show data from 1870 to 1950 on the presumption that (almost) all pre-1870 publications are PD (their authors would have had to live for *more* than 70 years post-publication for this not to be the case) and almost all publications post 1950 are in copyright today (their authors would have to have died *before* 1940 for this not to be the case).

As the table shows, at best only just over 40% of items have a recorded authorial death date and extending to include birth dates only raises this proportion to, at best, the mid mid-to-low fifties. Taking account of items which lack any associated author, raises these figures somewhat further to around 60%, though we should note that the reason for the lack of an associated author is not clear -- is it because they are genuinely anonymous or simply because the information has not been recorded? Thus, even for the earliest items listed a large proportion of items (50% or more) lack the necessary information for direct computation of public domain status.

At the same time, we can take some heart, and some interesting facts, from this table. First, a reasonable proportion, amounting to many thousands of items, did have associated death dates. Second, at least for older items, the majority of those with any date had a death date (95% for 1870-1880 and still at over 70% for 1920-1930). Third, and this is a more general observation, proportions were surprisingly constant over time. For example, the proportion of 'anonymous' items lies in a narrow band between 10% and 13% for the entire periods. Similarly the proportion of items with any date information ranged only from 45% to 56%. At the same time, and reassuringly, though the proportion with death dates is relatively constant for the oldest periods, in the more recent ones it falls substantially; as one would expect given that some of the authors from those more recent eras are still alive.



<table class="data"><thead><tr><th>Pub. Date</th><th>Total</th><th>PD</th><th>Not PD</th><th>?</th><th>Prop 1</th><th>Prop 2</th></tr></thead>
<tbody>
<tr><td>1870-1880</td><td>50565</td><td>22157 (43%)</td><td>68 (0%)</td><td>28340 (56%)</td><td>99%</td><td>96%</td></tr>
<tr><td>1880-1890</td><td>66858</td><td>28325 (42%)</td><td>649 (0%)</td><td>37884 (56%)</td><td>97%</td><td>90%</td></tr>
<tr><td>1890-1900</td><td>66884</td><td>26723 (39%)</td><td>2418 (3%)</td><td>37743 (56%)</td><td>91%</td><td>83%</td></tr>
<tr><td>1900-1910</td><td>70362</td><td>24032 (34%)</td><td>5838 (8%)</td><td>40492 (57%)</td><td>80%</td><td>67%</td></tr>
<tr><td>1910-1920</td><td>60491</td><td>16200 (26%)</td><td>8306 (13%)</td><td>35985 (59%)</td><td>66%</td><td>51%</td></tr>
<tr><td>1920-1930</td><td>78671</td><td>16127 (20%)</td><td>16351 (20%)</td><td>46193 (58%)</td><td>49%</td><td>36%</td></tr>
<tr><td>1930-1940</td><td>90583</td><td>8973 (9%)</td><td>20835 (23%)</td><td>60775 (67%)</td><td>30%</td><td>19%</td></tr>
<tr><td>1940-1950</td><td>72696</td><td>5000 (6%)</td><td>19316 (26%)</td><td>48380 (66%)</td><td>20%</td><td>13%</td></tr>
</tbody>
</table>

<p class="caption">Table 2: PD Status by Decade.  '?' indicates items where PD status could not be computed. Prop(ortion) 1 equals total PD divided by total for which status could be computed (sum of total PD and Not PD). Prop(ortion) 2 equals total PD divided by number of items for which any author date was known ('Any Date' in previous table).</p>

Table 2 reports the results of direct computation of PD status based on the information available. Note that, in doing these computations, we have augmented the basic life plus 70 rule with the additional assumptions that a) all items published in 1870 or before are PD b) no author is older than 100 (so if a birth date is more 170 years ago the item is PD) c) every author lives at least until 30 (so that any work published by an author born less than a 100 years ago is automatically *not* PD).

As is to be expected, for the majority of the periods, the availability of PD status (either PD or Not PD) closely tracks the availability of death date information -- the total for which PD status can be determined (the sum of PD and Not PD) almost exactly equals the total for which death date information is available. It is only in the last period 1940-1950 that the birth date appears to make any contribution. More interesting, is how the number PD and Not PD vary over time, especially relative to each other (and as a proportion of the records for which any date is available).

These two proportions/ratios are recorded in the last two columns which record, respectively: 1) the PD total relative to the number of items for which any status could be computed (i.e. the sum of PD and Not PD) 2) the PD total relative to the total number of items for which any date information is available. These ratios change dramatically over the periods shown: starting in the 1870-1880 period in the high 90%s by the 1940s they are down to 20% or below.

<table class="data" id="pd-proportions"><thead><tr><th>Pub. Date</th><th>% PD</th></tr></thead>
<tbody>
<tr><td>0000-1870</td><td>100</td></tr>
<tr><td>1870-1880</td><td>95</td></tr>
<tr><td>1880-1890</td><td>90</td></tr>
<tr><td>1890-1900</td><td>85</td></tr>
<tr><td>1900-1910</td><td>65</td></tr>
<tr><td>1910-1920</td><td>40</td></tr>
<tr><td>1920-1930</td><td>25</td></tr>
<tr><td>1930-1940</td><td>10</td></tr>
<tr><td>1940-1950</td><td>6</td></tr>
<tr><td>1950-Now</td><td>0</td></tr>
</tbody>
</table>
<p class="caption">Table 3: Suggested PD Proportions</p>

The key question for us is how to extrapolate these PD proportions to the full set of records -- i.e. from the set of records for which there is the necessary birth/death date information to that where there is not. The simplest, and most obvious, approach is to assume that the proportions are identical and therefore that the PD proportions calculated on the partial dataset apply to the whole. However, there are some obvious deficiencies in this approach.

In particular, our ability to compute a PD status is largely linked to the existence of a death date and it is likely that the presence of this information is itself correlated with authorial age -- after all a death date can only exist once that person has died! This correlation, and the bias it gives rise to, is probably small in the early periods -- the authors of any pre 1930 work are almost certainly no longer alive today. However, for the later periods, the bias may be more substantial -- it is in these last two periods (1930-1940 and 1940-1950) that there is a significant reduction in the number of records with a death date and (relatedly) a significant increase in the number of records for whom the PD status is unknown.

Thus, in converting the partial PD proportions to full PD proportions it seems sensible to revise down somewhat the partial figures with the revision being greater in later periods. Moreover, we have a lower bound for any downwards revision provided by the total PD as a proportion of all records -- which even in the 1940-1950 period stood at 6%. In light of these considerations Table 3 gives fairly conservative figures for PD proportions that when estimating PD size based on publication dates. Interestingly, even with out conservative assumptions, these proportions are rather higher than those used in our [previous analysis][prev-post].







