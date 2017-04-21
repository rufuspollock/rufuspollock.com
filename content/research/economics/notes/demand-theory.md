---
title: >-
  Demand Theory: A Primer
slug: demand-theory
date: 2007-10-05T15:17:09
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - page_id: 226
---

{{< toc >}}

<h2>Introduction</h2>
<p>This primer aims to provide a concise and simple introduction to the theory of demand. As such it does not intend to be comprehensive but to provide enough background for the reader to progress rapidly to empirical work.
</p>

<h2>Notation</h2>
<p>  Bear in mind throughout that an agent need not be an individual but could be a household, or even when dealing with aggregation, the entire population. Also whenever a variable which is normally indexed (such as prices or quantities) is written without an index this indicates the vector of all of those variables.
</p>
<ol>
 <li>
     Set of goods indexed usually by $$i$$
 </li>

 <li>
     $$p_{i} =$$ Price of good $$i$$.
 </li>

 <li>
     $$q_{i} =$$ Quantity of good $$i$$ (usually the amount demanded or actually consumed).
 </li>

 <li>
     $$w =$$ total wealth of the agent
 </li>

 <li>
     $$y$$ income of the agent (often indexed by i to indicate period)
 </li>

 <li>
     $$T$$ will indicate time, often the total amount of hours available to an agent.
 </li>

 <li>
     $$g_{i}(w, p)$$ is the (Marshallian) demand function for good $$i$$
 </li>

 <li>
     $$u(q)$$ is the utility function. $$u$$ on its own will usually stand for a particular level of utility
 </li>

 <li>
     $$v(w,p) = max_{q} { u(q) : p \cdot q \leq w }$$ is the indirect utility function
 </li>

 <li>
     $$h_{i}(u,p)$$ is the Hicksian (compensated) demand function for good i. Known as compensated because they show how demand varies with utility held constant.
 </li>

 <li>
     $$e(u,p)$$ is the expenditure/cost function.
 </li>

 <li>
     The slutsky matrix S defined by $$s_{ij} = \partial h_{i}(u,p) / \partial p_{j}$$
 </li>

 <li>
     $$b_{i} = \frac{p_{i}q_{i}}{w}$$ is the budget share for good i
 </li>

 <li>
     $$e_{i}$$ is the wealth elasticity of demand for good k (at current prices and wealth) defined as: $$ e_{i} = \partial \log( g_{i}(w,p)) / \partial \log w $$
 </li>

 <li>
     $$e_{ij}$$ are the cross-price elasticities of demand (if $$i = j$$ then this is the own-price elasticity). Defined as: $$ e_{ij} = \partial \log( g_{i}(w,p)) / \partial \log p_{j} \] $$
 </li>
</ol>

<h2>The Basic Properties of Demand Functions</h2>
<p>We shall assume a linear budget constraint.<sup id="fnr1-469267910"><a href="#fn1-469267910">1</a></sup> That is:<sup id="fnr2-469267910"><a href="#fn2-469267910">2</a></sup>
</p>
<p>$$ \[ w = \sum_{k} p_{k}q_{k} \] $$
</p>

<h3>Restrictions on the Demand Function: The Big Four</h3>
<ol>
 <li>
     <strong>Adding Up:</strong> From the budget constraint we have: $$ w = \sum_{k} p_{k}g_{k}(w,p) $$.
 </li>

 <li>
     <strong>Homogeneity</strong> The demand function is homogenous of degree 0 in prices and wealth (purely nominal changes should have no effect): $$ g_{i}(\lambda w, \lambda p) = g_{i}(w,p) $$.
 </li>

 <li>
     <strong>Slutsky Matrix is Symmetric.</strong>
 </li>

 <li>
     <strong>Negative Semi-Definiteness of the Slutsky Matrix.</strong>
  <br />
 </li>
</ol>

<h4>Remarks</h4>
<p>Taking derivatives, adding up implies:
</p>
<ol>
 <li>
     Engel Aggregation: $$ \sum_{k} p_{k} \frac{\partial g_{k}(w,p)}{\partial w} = 1 $$
 </li>

 <li>
     Cournot Aggregation: $$ g_{i} + \sum_{k} p_{k} \frac{\partial g_{k}(w,p)}{\partial p_{i}} = 0, \forall i = 1, .... n $$
 </li>

 <li>
     <strong>Invertability</strong> (see Deaton and Muellbauer (1980) 48ff). Demand functions that satisfy the four properties above are <em>integrable</em> into a consistent preference ordering. That is we may construct a cost/utility function basis from which such demands can then be derived. Not only is this result important in itself  but it demonstrates that these four properties are the <em>only</em> (necessary) consequences of utility maximization.
 </li>
</ol>

<h3>Other Useful Properties</h3>
<ol>
 <li><p>Roy's Identity: This allows us to relate the Marshallian demand functions to the indirect utility function:
</p>
<p> $$ \[ \frac{\partial v / \partial p_{i}} {\partial v / \partial w } = g_{i}(u,p) \] $$
</p>

 </li>

 <li><p>Slutsky equation:
</p>
<p> $$ \[
    s_{ij} = \frac{\partial h_{i}} {\partial p_{j}} = \frac{\partial g_{i}} {\partial p_{j}}
           + \frac{\partial g_{i}} {\partial w} g_{j}
    \] $$
</p>

 </li>
</ol>

<h2>Preference Foundations for Demand Functions</h2>
<p>Omitted for time being. This is pretty dull. Refer people to Mas-Collel ea. .... Plan:
</p>
<ol>
 <li>
     Axioms
 </li>

 <li>
     Cardinal (value matter) and Ordinal (only order matters) preference theory
 </li>

 <li>
     The existence of a real-valued utility function
 </li>

 <li>
     WARP, GARP ... ?
 </li>
</ol>

<h2>Deriving Demand Functions from Utility</h2>

<h3>Utility Maximization</h3>
<p>Given a cardinal utility function $$u(q)$$ the consumer has the following utility maximization problem (UMP):
</p>
<p>$$ \[ max_{q} u(q), \textrm{with } p.q \leq w, q \geq 0 \] $$
</p>
<p>Let $$ q^{s} $$ be values that solve this problem (assuming they exist). Then the demand function is defined by $$g(w,p) = q^{s}$$
     <br />
</p>

<h3>The Dual: Cost Minimization</h3>
<p>There exists a problem dual to the original utility maximization problem, namely the expenditure minimization problem (EMP).
</p>
<p>$$ \[ min_{q} w = p . q, \textrm{subject to } u(q) = u \] $$
</p>

<h4>Properties of the Cost Function</h4>
<ol>
 <li>
     The cost function is homogenous of degree 1 in prices, i.e. $$ c(u,\lambda p) = \lambda c(u,p) $$
 </li>

 <li>
     The cost function is increasing in $$u$$, nondecreasing in $$p$$
 </li>

 <li>
     $$c(u,p)$$ is concave in prices
 </li>

 <li>
     The cost function is continuous in $$p$$ and its first and second derivatives with respect to prices exist everywhere (except possibly on a set of meausure 0)
 </li>

 <li>
     (Shepherd's Lemma) Partial derivatives of the cost function with respect to price yield the Hicksian demands: $$ \frac{\partial c(u,p)} {\partial p_{i} } = h_{i}(u,p) $$
 </li>
</ol>

<h3>Summary</h3>
<p>[[TODO: insert summary diagram]]
</p>

<h2>Aggregation</h2>
<p>[[TODO]]
</p>

<h2>Footnotes</h2>

<div class="footnote"><ol>
 <li id="fn1-469267910">
     Though used by almost all textbooks as a starting point this is not necessarily as innocent as it may seem. See Deaton and Muellbauer, Chapter 1, for more discussion of this issue.<a href="#fnr1-469267910" class="footnoteBackLink" title="Jump back to footnote 1 in the text">&#8617;</a>
 </li>

 <li id="fn2-469267910">
     In order to have equality, i.e. for the constraint to bind, this does also assume the consumer is locally non-satiated. This restriction is known as <em>Walras' Law</em>.<a href="#fnr2-469267910" class="footnoteBackLink" title="Jump back to footnote 1 in the text">&#8617;</a>
 </li>
</ol>
</div>


