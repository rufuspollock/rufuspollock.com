---
title: >-
  Theories of Contextual Judgement
slug: theories-of-contextual-judgement
date: 2008-06-23T16:06:39
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - page_id: 321
---

{{< toc >}}

**2008-12: See also the longer and more detailed paper [Theories of Contextual Judgement in Relation to Well-Being and Other Outcomes](/economics/papers/contextual_judgement.pdf)**

## Simple Adaptive Theory

"The affective value of the experiential correlate of a stimulus varies conversely with the sum of the affective values of those experiences preceding this correlate which constitute with it a unitary temporal group".

That is, one compares this stimulus with the total/average value of the set of (previous) experiences associated with it, 'adapting' towards that level (so if it is higher the experience of this stimulus is reduced). In this setup the context is the set of previous stimuli ($$C$$) and the judgement function takes the form ($$\\bar{C}$$ being the average of the previous set of stimuli):

$$ \\[ J(x,C) = f(x,\\bar{C}) \\] $$

If $$f\_{x} > 0$$ (subscripts indicating partial differential) then adaptation means: $$f\_{\\bar{C}} < 0$$.


## Range-Frequency Theory

When assigning 'stimuli' to categories it is done so that (approximately):

Principle 1 (Equal Frequency) there are equal number of stimuli in each category.

Principle 2 (Equal Range): subjects use the rating categories to divide the stimulus range into sub-categories of equal range.

Range-frequency theory combines these together. Formally, the end 'Judgement' (J):

$$ \\[ J = wR + (1-w)F \\] $$

where R and F are the judgements from Range and Frequency principles respectively. Experimental evidence suggests $$w \\approx 0.5$$.

In turn the range judgement can be expressed formally as (where this is the ith stimulus within some context set):

$$ \\[ R\_{i} = \\frac{s\_{i} - s\_{min}} {s\_{max} - s\_{min}} \\] $$

While the frequency judgement formally becomes:

$$ \\[ F\_{i} = \\frac{ r\_{i} - 1 }{ N - 1 } \\] $$

where $$r\_{i}$$ is the rank in the contextual set and there are N stimuli. That is, the frequency value is the difference between its rank and the rank of the lowest stimulus divided by the difference in rank of the highest stimuli and 1.

Thus, average judgement is given by the following formula where $$r = s\_{max} - s\_{min}$$ is the range and $$m=s\_{max}+s\_{min}/2$$ is the midpoint (for an explicit derivation see below).

$$ \\[ \\bar{J} = 0.5 + w \\frac{\\bar{s} - m}{r} \\] $$

This is essentially a measure of skewness (though negatively correlated with conventional measures) varying between 0 and 1. Dropping the 0.5 this becomes  a range between -0.5 and 0.5 and can be expressed as:

Average Judgement = w (Avg. Stimuli - Midpoint of Range) / Range

In reality the actual judgement (J) is not available to others as it is a subjective experience. Rather the judgement is presented to the outside world (e.g. the experimenter) in the form of some explicit category (verbal or otherwise) -- interestingly it seems results differ little between the case where subjects must use an external set of categories or generate their own. To relate categorization (C) to judgement (J) we must assume some functional relation, such as the simple linear one:

$$ \\[ C\_{i} = bJ\_{i} + a \\] $$

### Explicit Derivation of Average Judgement Formula

Average frequency is given by:

$$ \\[ \\frac{1}{N} \\sum\_{i=1}^{N} F\_{i} = \\frac{1}{2 N(N-1)} (N(N+1) - 2N) = 0.5 \\] $$

Average range is given by:

$$ \\[ \\frac{1}{N} \\sum\_{i=1}^{N} R\_{i} = \\frac{\\bar{s} - s\_{min}}{r} \\] $$

Thus average judgement is:

$$ \\[ J = wR + (1-w)F = w (\\frac{\\bar{s} - s\_{min}}{r} + 0.5 (1-w) =  0.5 + w \\frac{ \\bar{s} - m}{r} + w (\\frac{s\_{max} - s\_{min}}{2r} - 0.5) \\] $$

### Further Issues

1. What does one do when categories are non-monotonic




