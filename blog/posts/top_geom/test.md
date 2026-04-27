---
title: There is Only One Derivative
date: 2026-04-26
toc: true
---

## Introduction
Those who are fortunate enough to have taken a course in multivariable calculus, or vector calculus, are likely familiar with the three "derivative-like" operators: gradient, curl, and divergence. The purpose of this write-up is to observe that these three are actually
all the same thing, the **exterior derivative**, just given a different name. 

For the purposes of this write-up, I will assume the reader has seen some vector calculus, and more importantly, has some familiarity with *differential forms and the exterior
derivative*. If the sentence, "A $1$-form $\om$ on a smooth manifold $M$ is a smooth section of $T^*M$" does not make sense to you, then this blog post may be difficult to follow.

## Vector Calculus Revisited
### Gradient
Henceforth we confine ourselves to $\RR^3$, equipped with the standard basis. If $f:\RR^3\to\RR$ is any *smooth* function (it does not matter how we define smooth, as long as it means at least $C^1$), then its gradient at any point $p$ is 
$$\nabla f(p) = (\partial_1 f(p), \partial_2 f(p),\partial_3f(p))$$
Sometimes we also write $\grad f(p)$. This quantity is often readily interpreted as the direction in which $f$ is increasing fastest, but note that this interpretation has already swept an assumption under the rug!

Namely, $\nabla f(p) \in T_p\RR^3$, which is naturally isomorphic to $\RR^3$, but not literally equal! Hence this interpretation as the direction of steepest ascent fails in the
general case. Regardless, the formula as-written makes sense, and once we pick a suitable Riemannian metric, we can justify the geometric interpretation.

### Curl
Now, let $F: \RR^3\to \RR^3$ be any *smooth* vector field with components $F=(F_1,F_2,F_3)$. Then its curl at any point $p$ is given by

$$\curl F(p) = (\partial_2F_3 - \partial_3F_2, \partial_3F_1 - \partial_1F_3, \partial_1F_2 - \partial_2F_1)$$

Speaking informally, the quantity $\curl F\cdot n$ can be interpreted as the extent to which the vector field $F$ swirls around the vector $n$. Notice that the curl
takes in a vector field, and spits out another vector field. The output $\curl F(p)$ can be very roughly interpreted as the *direction in which $F$ is spinning counterclockwise 
the fastest*.

### Divergence
Again, let $F:\RR^3\to\RR^3$ be a *smooth* vector field with components $F=(F_1,F_2,F_3)$. Its divergence at any given point $p$ is given by 

$$\div F(p) = \partial_1 F_1 + \partial_2 F_2 + \partial_3 F_3$$

Roughly, the divergence of $F$ at $p$ is the extent to which $F$ is "emanating from $p$"–it is negative if $F$ is mostly "going into" $p.$

## Differential Forms

### $k$-forms

### The Wedge Product



## The Exterior Derivative

### Recovering the Gradient

### Recovering the Curl

### Recovering the Divergence

## Stokes' Theorem

## References