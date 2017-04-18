---
title: >-
  Summation Over Matrices
slug: summation-over-matrices
date: 2011-11-18T20:06:46
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - page_id: 1041
---

Start with computationally tractable:

Suppose we have M dimensions with N values for each dimesion. Assume all values used.

So full entries are: $$M^N$$

Suppose we aggregate over 1 dimension we get $$M^{N-1}$$ values and we can do this for N different dimensions yielding:

$$N M^{N-1}$$

Next one we will N choose 2 (columns to aggregate over) times $$M^{N-2}$$

Repeating we see that total number of aggregates is:

$$ Total = \sum_{i=1}^{N} C_{i}^{N} M^{N-i}$$

Now let us assume that N = M, then:

$$
Total = \sum_{i=1...N} C_{i}^{N} N^{N-i}
      = \sum_{i=1...N} \frac{N!}{i!(N-i)!}  N^{N-i}
$$

$$
 Total \leq \sum_{i=1...N} \frac{N^{i}}{i!}  N^{N-i}
      = \sum_{i=1...N} \frac{N^{N}}{i!}
      = N^{N} \sum_{i=1...N} \frac{1}{i!}
$$

And finally:

$$
Total \leq  N^{N} \sum_{i=0...N-1} \frac{1}{2^{i}}
      \leq  2 N^{N} = 2 \textrm{x Number of original entries}
$$

Seems likely that we can do worse than this in real world cases. Would be nice to get an upper bound ....


