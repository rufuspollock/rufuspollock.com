---
title: >-
  Complexity
slug: complexity
date: 2008-03-16T16:46:04
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - page_id: 288
---

{{< toc >}}

# Models

## Bak-Sneppen Model

### Basic version

N 'species' situated around a circle. Species are initially assigned a random 'fitness' in $$[0,1]$$. At each iteration the species with minimal fitness is selected and it *and its 2 neighbours* are replaced by new species with fitnesses randomly (and independently) selected from $$[0,1]$$.

### Formal Version

*This is based on \\cite{gillett\_2007}*

Let $$G$$ be a locally-finite connected graph with vertex set $$V(G)$$ and an associated state space $$\\Omega\_{G} = [0,1]^{N}, N=|G|$$. Then the Bak-Sneppen model on $$G$$ is a discrete time stochastic process $$\\Phi\_{n}$$ with:

1. An inital 'fitness' distribution $$\\pi$$ with $$\\Phi\_{0} = \\pi$$ 
2. An evolution rule: let $$v$$ be the vertex with minimal fitness at time $$n$$ and let $$\\Gamma(v)$$ be $$v$$ plus its neighbours then:
   
    $$
    \\Phi\_{n+1} = \\left \\{
      \\begin{array}{ll}
        U[0,1] & if x \\in \\Gamma(v) \\\\
        \\Phi\_{n}(x) & \\textrm{otherwise}
      \\end{array}
                 \\right. 
    $$

### SOC

From \\cite{gillett\_2007}, p.22:

> The Bak-Sneppen model is considered self-organised critical because the
> typical fitness configuration seen in Figure 2.1 is thought to be critical for
> the model. A critical state is typified by power law distributions. For the
> Bak-Sneppen model a number of things are proposed to have a power law. I
> give here just two related examples. Recall from the picture that apart from
> a small perturbation around the minimal fitness, most fitnesses are situated
> above some threshold. Let us call this threshold p. It is thought that the
> number of updates needed so that all values are above this threshold has a
> power law distribution. Similarly, the number of vertices that need to be
> updated is thought to have a power law distribution. Both the above claims
> need some caveats. Of course the number of fitnesses below p initially is
> important, let us assume that initially there is at most one such vertex.

### Results

Theorem 3.1 of \\cite{gillett\_2007}:

(Informal): Averaging over all starting distributions on a transitive graph $$G$$ the expected length of the first avalanche is infinite (but barely so -- see Thm 3.2).

## Percolation Process

See Ronald Meester's lecture notes at: <http://www.cs.vu.nl/~rmeester/preprints/notes.ps>

Salient results. Let $$d$$ be dimension of the lattice and $$p$$ the probability of an edge being open (so this is edge percolation). Let $$r$$ be probability that the connected component containing the origin is infinite in extent.

  * Thanks to Kolmogorov zero-one result we know that $$r$$ either equal 0 or 1.
  * Crucial thing therefore is determine critical threshold $$p^{0}$$ such that for $$p < p^{0}, r=0$$ and for $$p>p^{0}, r>0$$ (if $$r>0$$ then $$r=1$$). Much of percolation theory is aimed at determining this value.

## Contact Process

Modified from: <http://en.wikipedia.org/wiki/Contact\_process\_(mathematics)>

The contact process is a model of an interacting particle system. It is a continuous time Markov process with state space $${0,1}^{S}$$, where S is a finite or countable graph, usually $$Z^{d}$$ (i.e. the d-dimensional grid). The process is usually interpreted as a model for the spread of an infection: if the state of the process at a given time is $$\\delta$$, then a site x in S is "infected" if $$\\delta(x) = 1$$ and healthy if $$\\delta(x) = 0$$. Infected sites become healthy at a constant rate, while healthy sites become infected at a rate proportional to the number infected neighbors. One can generalize the state space to $$\\{0,\\ldots, \\kappa\\}^S$$, in which it is called the multitype contact process. It represents a model when more than one type of infection is competing for space.

Applications:

  * infections 
  * forest fires

## N-K Model

The N-k model originated as the formalization of a basic evolutionary fitness ideas by Weinberger and Kauffman (~1989). More generally, one is interested in correspondence between characteristics of some object and its 'fitness' -- classic examples being DNA/Amino acids and evolutionary fitness, components of a product and its utility. This presentation is based on the info in \\citet*{weinberger\_1996}.

The characteristics of the object is an $$N$$ length bit string $$b$$ (i.e. $$b\_{i} \\in \\{0,1\\}$$). First assign a (real-valued) fitness contribution $$f\_{i}$$ to the ith ith bit $$b\_{i}$$. Each such assignment is a function *not just* of $$b\_{i}$$ but of its $$0 \\leq k < N$$ other bits called its 'neighbours'. The fitness contribution is a random function of the substring $$s\_{i}$$ consisting of $$b\_{i}$$ and its $$k$$ neighbours. Specifically $$f\_{i}(s\_{i})$$ is random draw from such distribution $$p(x)$$ (e.g. uniform of Gaussians). Note that this distribution though random is usually calculated once-and-for-all at the start to give a deterministic function $$f\_{i}$$ defined over the $$2^{k+1}$$ values that $$s\_{i}$$ can take. Total fitness is then defined as:

$$ \\[ F(b) = \\frac{1}{N} \\sum\_{i}^{N} f\_{i}(s\_{i}) \\] $$

The final part of the model's specification involves defining how $$s\_{i}$$ relates to $$b\_{i}$$. The simplest approach is to choose the actual neighbours (with the sites arranged on a circle). Alternatively one could select randomly. Whatever the case one is generating a directed graph with the bit positions as node and edges to denote neighbours.

### Remarks

1. According to Weinberger simulations suggest that the model is fairly robust to the method for choosing neighbours.

2. Varying $$k$$ allows one to 'tune' the 'ruggedness' of the fitness landscape. To be specific. Take $$k=0$$. Then each site is independent of all others. For each site bit value 0 or bit value 1 is (a.s.) better than the other value; as a result a single specific sequence comprised of the fitter bit value in each position is (a.s.) the single global optimum. Expected walk length to the optimum is $$N/2$$ and from any starting position one improves monotonically towards the optimum. Conversely if $$k=N-1$$ (fully-connected model) one has a completely 'random' landscape. The fitness contribution of each site depends on all other sites and:
  * The fitness of each $$N$$ bit string is independent of its neighbours.
  * Lots of local optima ($$2^{N}/N+1 on average)
  * Walks to optima are short (O(ln(N))) and only a small fraction of local optima are accessible from any initial string (assuming you halt at a local optima).
  * Implication: adaptive walks vary dramatically as the ruggedness of the landscape varies.

3. Complexity (in trad. sense) of finding global optima. (Purpose of \\citet*{weinberger\_1996}). If neighbours are chosen as real neighbours then finding the global optima is a polynomial time problem. If 'neighbours' are chosen randomly the problem is NP complete for $$k \\geq 3$$ (for $$k=2$$ the problem is open).

# Evidence

## \\cite{newman\_1996}

Looks at fossil extinctions. Various SOC models predict that relative frequency, $$p(s)$$, of extinction events of size $$s$$ follows a power-law:

$$ p(s) \\propto s^{-\\tau} $$

Most models predict $$\\tau \\approx 2$$ (though this is also predicted by other, non-SOC, models). Find that:

  * The data is consistent with this prediction.
  * However, no reason for this to imply that terrestial evolution is "a self-organized critical process":
     
    > There is a much simpler explanation for the appearance of a power law in the extinction distribution. We will show given the simplest of assumptions about the causes of the extinction, we can formulate a model of the extinction process which does not rely on coevolution for its results ... and yet predicts a power-law distribution of extinction sizes. Our results appear to be independent of the detailed dynamics of the evolution process, implying that we should expect to see power laws in the extinction record whether evolution is self-organized or not.
    
    Given this, interesting to note this initial quote about power laws:

    > The power-law form is one of the most characteristic features of critical behaviour, and has been taken as evidence of self-organization in a wide variety of systems. [p.1605-1606]

  * The alternative model presented which generates a power law extinction record is: N species with fitness $$x\_{i} \\in [0,1]$$:

     1. At each time-step, a small fraction f of the species selected at random evolve (their fitness set to a new randomly determined value). 
     2. Each period has a stress level $$\\eta \\in [0,1]$$ chosen randomly from some distribution $$G$$ and all species, i, with $$x\_{i} < \\eta$$ go extinct and are replaced by new species whose fitnesses are also chosen uniformly at random in the range $$[0,1]$$.

     The model is robust to using various distributions for $$G$$ and for modifying the form of evolution and replacement.




