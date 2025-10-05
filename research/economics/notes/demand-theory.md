---
title: >-
  Demand Theory: A Primer
slug: demand-theory
date: 2007-10-05T15:17:09
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - page_id: 226
---
## Introduction

This primer aims to provide a concise and simple introduction to the theory of demand. As such it does not intend to be comprehensive but to provide enough background for the reader to progress rapidly to empirical work.


## Notation

Bear in mind throughout that an agent need not be an individual but could be a household, or even when dealing with aggregation, the entire population. Also whenever a variable which is normally indexed (such as prices or quantities) is written without an index this indicates the vector of all of those variables.


1. Set of goods indexed usually by $i$

2. $p_{i} =$ Price of good $i$.

3. $q_{i} =$ Quantity of good $i$ (usually the amount demanded or actually consumed).

4. $w =$ total wealth of the agent

5. $y=$ income of the agent (often indexed by i to indicate period)

6. $T$ will indicate time, often the total amount of hours available to an agent.

7. $g_{i}(w, p)$ is the (Marshallian) demand function for good $i$

8. $u(q)$ is the utility function. $u$ on its own will usually stand for a particular level of utility

9. $v(w,p) = max_{q} { u(q) : p \cdot q \leq w }$ is the indirect utility function

10. $h_{i}(u,p)$ is the Hicksian (compensated) demand function for good i. Known as compensated because they show how demand varies with utility held constant.

11. $e(u,p)$ is the expenditure/cost function.

12. The slutsky matrix S defined by $s_{ij} = \partial h_{i}(u,p) / \partial p_{j}$
 
 13. $b_{i} = \frac{p_{i}q_{i}}{w}$ is the budget share for good i

14. $e_{i}$ is the wealth elasticity of demand for good k (at current prices and wealth) defined as: $ e_{i} = \partial \log( g_{i}(w,p)) / \partial \log w $

15. $e_{ij}$ are the cross-price elasticities of demand (if $i = j$ then this is the own-price elasticity). Defined as: $ e_{ij} = \partial \log( g_{i}(w,p)) / \partial \log p_{j} $


## The Basic Properties of Demand Functions

We shall assume a linear budget constraint. That is:

$ w = \sum_{k} p_{k}q_{k} $


### Restrictions on the Demand Function: The Big Four

**Adding Up:** From the budget constraint we have: $ w = \sum_{k} p_{k}g_{k}(w,p) $.

**Homogeneity** The demand function is homogenous of degree 0 in prices and wealth (purely nominal changes should have no effect): $ g_{i}(\lambda w, \lambda p) = g_{i}(w,p) $.

**Slutsky Matrix is Symmetric.**
 
**Negative Semi-Definiteness of the Slutsky Matrix.**

## Remarks

Taking derivatives, adding up implies:

1. Engel Aggregation: $ \sum_{k} p_{k} \frac{\partial g_{k}(w,p)}{\partial w} = 1 $

2. Cournot Aggregation: $ g_{i} + \sum_{k} p_{k} \frac{\partial g_{k}(w,p)}{\partial p_{i}} = 0, \forall i = 1, .... n $

3. **Invertability** (see Deaton and Muellbauer (1980) 48ff). Demand functions that satisfy the four properties above are _integrable_ into a consistent preference ordering. That is we may construct a cost/utility function basis from which such demands can then be derived. Not only is this result important in itself  but it demonstrates that these four properties are the _only_ (necessary) consequences of utility maximization.

## Other Useful Properties

Roy's Identity: This allows us to relate the Marshallian demand functions to the indirect utility function:

1. $ \frac{\partial v / \partial p_{i}} {\partial v / \partial w } = g_{i}(u,p) $

 

 2. Slutsky equation:
 
 $$
    s_{ij} = \frac{\partial h_{i}} {\partial p_{j}} = \frac{\partial g_{i}} {\partial p_{j}}
           + \frac{\partial g_{i}} {\partial w} g_{j}
    $$


## Preference Foundations for Demand Functions

Omitted for time being. This is pretty dull. Refer people to Mas-Collel ea. .... Plan:

1. Axioms
     Cardinal (value matter) and Ordinal (only order matters) preference theory

     The existence of a real-valued utility function
 
     WARP, GARP ... ?


## Deriving Demand Functions from Utility

### Utility Maximization

Given a cardinal utility function $u(q)$ the consumer has the following utility maximization problem (UMP):

$$ \[ max_{q} u(q), \textrm{with } p.q \leq w, q \geq 0 \] $$

Let $ q^{s} $ be values that solve this problem (assuming they exist). Then the demand function is defined by $g(w,p) = q^{s}$


### The Dual: Cost Minimization

There exists a problem dual to the original utility maximization problem, namely the expenditure minimization problem (EMP).

$$ \[ min_{q} w = p . q, \textrm{subject to } u(q) = u \] $$


### Properties of the Cost Function

1. The cost function is homogenous of degree 1 in prices, i.e. $ c(u,\lambda p) = \lambda c(u,p) $

2. The cost function is increasing in $u$, nondecreasing in $p$

3. $c(u,p)$ is concave in prices

4. The cost function is continuous in $p$ and its first and second derivatives with respect to prices exist everywhere (except possibly on a set of meausure 0)

5. (Shepherd's Lemma) Partial derivatives of the cost function with respect to price yield the Hicksian demands: $ \frac{ \partial c(u,p) } { \partial p_{i} } = h{i}(u,p) $

## Summary
[[TODO: insert summary diagram]]


## Aggregation
[[TODO]]

## Footnotes

Though used by almost all textbooks as a starting point this is not necessarily as innocent as it may seem. See Deaton and Muellbauer, Chapter 1, for more discussion of this issue.<a href="#fnr1-469267910" class="footnoteBackLink" title="Jump back to footnote 1 in the text">&#8617;</a>

In order to have equality, i.e. for the constraint to bind, this does also assume the consumer is locally non-satiated. This restriction is known as <em>Walras' Law</em>.<a href="#fnr2-469267910" class="footnoteBackLink" title="Jump back to footnote 1 in the text">&#8617;</a>

