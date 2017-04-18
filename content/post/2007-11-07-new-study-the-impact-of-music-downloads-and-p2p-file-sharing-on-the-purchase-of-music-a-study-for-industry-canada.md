---
title: >-
  New Study: "The Impact of Music Downloads and P2P File-Sharing on the Purchase of Music: A Study for Industry Canada"
slug: new-study-the-impact-of-music-downloads-and-p2p-file-sharing-on-the-purchase-of-music-a-study-for-industry-canada
date: 2007-11-07T10:37:25
themes: ['Information Economy']
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 239
---

A [new study][study] is out on the relationship of unauthorised downloading and music purchases. The work was carried out by two economists, Birgitte Andersen and Marion Frenz, of Birkbeck College (University of London) for Industry Canada. Entitled [*The Impact of Music Downloads and P2P File-Sharing on the Purchase of Music: A Study for Industry Canada*][study] its description states:

> Industry Canada undertook a music file sharing study during 2006-07 to measure the extent to which music downloads over peer-to-peer file sharing networks, for which the sound recording industry receives no remuneration, affect music purchasing activity in Canada. The data used for this analysis are from a Decima Research survey conducted between April and June, 2006, on behalf of Industry Canada. The report, prepared by University of London researchers, Birgitte Andersen and Marion Frenz, found that music downloads have a positive effect on music purchases among Canadian downloaders but that there is no effect taken over the entire population aged 15 and over.

This is a new contribution to the literature examining the relationship of unauthorised downloading and sales which I first [reviewed][review] two years ago. The results would clearly support those who argue that the positive sampling effect of unauthorised p2p downloading counterbalances (or even outweighs) the substitution effect (for more on these terms see the [review][review]). The effects found are quite substantial, at least when restricted to their P2P downloaders subsample (from the [summary of findings][summary])

> "... our analysis of the Canadian P2P file-sharing subpopulation suggests that there is a strong positive relationship between P2P file-sharing and CD purchasing. That is, among Canadians actually engaged in it, P2P file-sharing increases CD purchasing. We estimate that **the effect of one additional P2P download per month is to increase music purchasing by 0.44 CDs per year**" [emphasis added]

However looking through the paper one needs to be a little cautious in taking these results at face value. In particular, the statement in the abstract that "music downloads have a positive effect on music purchases among Canadian downloaders" is a classic case of interpreting a correlation as a causative relationship (this (mis)interpretation is even more baldly stated in the [summary of findings][summary] -- see previous quote above). Given the cross-sectional nature of their data such an interpretation is particularly dubious (as the authors themselves acknowledge in the [Data and Methodology section][data]: "... regressions based on cross-sectional data cannot prove causality").

Furthermore, there is a major problem here with the regression specification: p2p downloads and music purchases may both be driven by an omitted variable -- for example interest in music. In that case a simple regression of purchases on downloading activity will be upwardsly biased (i.e. the impact of downloads on purchases will be too high) because those interested in music would then both download more *and* purchase more. To address this problem you'd need some form of 'identification' strategy, probably using an instrumental variables approach. (This issue is very similar to that encountered when doing straight regression of sales on downloads -- again the estimated coefficient is going to be upwards biased because both trend (independently) upwards when an album is released.) This problem could be made even worse by focusing solely on downloaders.

Again the authors are aware of this issue but don't feel they can do much about it (from the end of the [Data and Methodology section][data]):

> ... single equation estimations assume that all independent variables are exogenous and all important variables are included in the estimation. If, however, any of the independent variables are influenced by the dependent variable and/or any of the independent variables, or important independent variables are omitted, then the included independent variables tend to be correlated with the error term leading to inconsistent estimates
> 
> Unfortunately, useful instruments are inherently difficult to find and this is why we decided not to use instrumental variable techniques. ...
> ...

While it may be true that there was not much they could do about this issue given the data they had it does mean that one should be cautious in taking the regression results at face value -- in particular the main finding, for the downloaders subsample, of a substantial positive effect of (unauthorised) downloads on CD purchases, which may simply be picking up an omitted variable (for example, interest in music).

[study]: http://strategis.ic.gc.ca/epic/site/ippd-dppi.nsf/en/h_ip01456e.html 
[review]: http://www.rufuspollock.org/economics/p2p_summary.html
[data]: http://strategis.ic.gc.ca/epic/site/ippd-dppi.nsf/en/ip01460e.html
[summary]: http://strategis.ic.gc.ca/epic/site/ippd-dppi.nsf/en/ip01462e.html


