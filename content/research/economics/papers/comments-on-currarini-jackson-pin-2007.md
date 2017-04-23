---
title: >-
  Comments on "An Economic Model of Friendship: Homophily, Minorities and Segregation" by Currarini, Jackson and Pin (2007)
slug: comments-on-currarini-jackson-pin-2007
date: 2008-01-14T13:28:36
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - page_id: 262
---

{{< toc >}}

  * **2008-06: There is now a [pdf version of these comments available](/economics/papers/comments_on_currarini_pin_jackson_2007.pdf)**. This may be a better way to read this as some people have reported difficulties with viewing the maths in the page (requires mathml support -- via firefox + mathml fonts or IE).

This is brief note to comment on *An Economic Model of Friendship: Homophily, Minorities and Segregation* by Currarini, Jackson and Pin (2007) (hereafter CJP).

The authors go through a fair amount of work using a matching process to generate results with the basic empirical patterns they lay out in the introduction (see below for summary). The purpose of this comment is to derive the same results in what I believe is a simpler, and more intuitive, manner.


### Definitions

These definitions are taken directly from the original paper.

  * Total population: $N$ consisting two types $i,j$: $N = N\_{i} + N\_{j}$
  * Relative fraction of type k in population: $w\_{k} = N\_{k} / N$ (k = i,j)
  * $s\_{k}, d\_{k}$ is number of frienships a type $k$ agent has with own type and other type respectively.
  * Define homophily index: $H\_{k} = s\_{k} / (s\_{k} + d\_{k}$
  * Define **Inbreeding Homophily Index**: $IH\_{k} = H\_{k} - w\_{k} / (1-w\_{k})$
  * Friendships display *base line* homophily if: $H\_{k} = w\_{k}$
  * Friendships displays *relative homophily* if $N\_{i} > N\_{j}$ implies $s\_{i} > s\_{j}$ and $d\_{i} < d\_{j}$ and then $H\_{i} > H\_{j}$.
  * Friendships display *inbreeding homophily* if: $H\_{k} > w\_{k} \Leftrightarrow IH\_{k} > 0$

### Empirical Regularities

CJP mention four major empirical regularities to explain (referred to as E1-E4 below):

  1. There is relative homophily.
  2. Larger groups make more friends: $s\_{k} + d\_{k}$ is increasing in $N\_{k}$ (Fig 3)
  3. There is Inbreeding Homophily for most groups: $IH\_{k} > 0$
  4. Inbreeding homophily is hump-shaped (inverse u-shaped) as a function of population share, formally: $IH\_{k}$ is increasing then decreasing as a function of $w\_{k}$ (or even more formally ...). (Fig 4).

### Deriving Results

In this section I proceed to derive most of these empirical regularities but using what I believe is a simpler and more intuitive framework than that used in CJP.

Assume that probabibility $p\_{s}, p\_{d}$ be probability you make friends with your own type and other type respectively (common across groups -- if you want we can generalise to have it not common but it adds little).

ASIDE: If you want microfoundations for this assume that there is a constant cost $c$ of making friends and that the value of a friendship with ith person in own group/other group respectively is a random variable $X\_{s}^{i}, X\_{d}^{i}$. Whenever you meet someone you both know this value and you make friends if $X\_{y}^{i} > c$ ($y \in {s,d}$). NB: (a) this could be other way round: constant value and random costs or even both ... (b) we can easily generalise to diminishing returns (implemented here as increasing costs ...).

Then:

(Expected) number of friends of own type $ = s\_{i} = N\_{i} p\_{s} = N w\_{i} p\_{s}$

and

(Expected) number of friends of other type: $d\_{i} = N\_{j} p\_{d} = N w\_{j} p\_{d}$.

This immediately gives that $N\_{i} > N\_{j}$ implies $s\_{i} > s\_{j}, d\_{i} < d\_{j}$ (E1).

Let total number of (expected) friends be $M\_{i} = s\_{i} + d\_{i}$. Then, noting that $w\_{j} = 1-w\_{i}$

$$ M\_{i} = si + di = N w\_{i} p\_{s} + N w\_{j} p\_{d} = N (wi (p\_{s}-p\_{d}) + p\_{d}) $$

This is increasing in $w\_{i}$ and we have E2.

Turning to the Homophily index we have using $w\_{j} = 1 - w\_{i}$:

$$ \[ H\_{i} = \frac{s\_{i}}{s\_{i} + d\_{i}} = \frac{N\_{i} p\_{s}}{(N\_{i} p\_{s} + N\_{j}p\_{d}} = \frac{w\_{i} p\_{s}}{w\_{i} p\_{s} + w\_{j} p\_{d}} = \frac{w\_{i} p\_{s}}{w\_{i}(p\_{s} - p\_{d}) + p\_{d}} \] $$

This is clearly increasing in $w\_{i}$ which is equivalent, for fixed total population $N$, to increasing in $N\_{i}$. Hence we have demonstrated the last requirement for relative homophily and have deduced all of E2.

Finally let's turn to inbreeding homophily:

$$IH\_{i} = \frac{H\_{i} - w\_{i}}{1-w\_{i}} = \frac{H\_{i} - w\_{i}}{w\_{j}}$$

Substituting for $H\_{i}$ and rearranging gives:

$$IH\_{i} = \frac{w\_{i}(p\_{s}w\_{j}) - w\_{i}w\_{j}p\_{d}}{w\_{j}(w\_{i}(p\_{s}-p\_{d}) + p\_{d})} = \frac{w\_{i}(p\_{s}-p\_{d})}{w\_{i} (p\_{s}-p\_{d}) + p\_{d}} $$

Thus if $p\_{s} > p\_{d}$ (i.e. there is any preference for own group friends) then $IH\_{i} > 0$ and we have empirical regularity 3 -- inbreeding homophily.

In terms of the shape of $IH\_{i}$ as a function of proportional group size, $w\_{i}$, we do not get an exact fit with the empirical data. Here $IH\_{i}$ grows initially but then flattens out but does *not* actually go down -- the empirical pattern is that $IH\_{i}$ is 'hump-shaped', i.e. initially increasing and then eventually decreasing. This is again similar to the results in the paper which derive the initially increasing effect but not the downward sloping effect.

### Further Remarks

One obvious away to obtain this downward sloping impact would be to modify the model to introduce diminishing returns -- modelled here most easily as increase in the (opportunity) cost of making friends. Further numerical experimentation (see inline python file below) as well as analytical calculations indicate that introducing simple diminishing returns to frienship does *not* make the $IH\_{i}$ curve downward sloping -- though it does make the model and the other results more realistic.

Here simple diminishing returns mean diminishing returns to friendship which are commmon across types (i.e. diminishing returns operate at the level of the total number of friends with no distinction by type). The obvious next step would be to allow different diminishing returns functions for friend types individually -- this is equivalent (in some sense) to having a taste for variety in friendship. While not yet fully investigated the results so far suggest that this would be able to generate some degree of downward slope in the $IH$ curve.

### Code

I've also written a short python script that allows one to investigate the basic homophily model using a different functional forms for the cost and value functions. If you are interested in getting hold of this please just contact me.
