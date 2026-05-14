---
title: "Information Geometry Chapter 01: Connections"
date: 2026-05-15
toc: true
hide-sidebar: true
tags: [information-geometry, differential-geometry]
---

## Introduction

Welcome to the first chapter in [my series on information geometry](/blog/tag/information-geometry/index.html)! This is the second of two posts in the information geometry series intended to provide (some of) the requisite background in differential geometry.

This second post aims to cover geodesics and connections, and follows quite closely chapter four of John M. Lee's book, *Introduction to Riemannian Manifolds*. In the previous chapter, the crucial concept that we built up to was the notion of a Riemannian metric: a way of smoothly assigning a symmetric positive-definite bilinear form to each point $p\in M$. This bilinear form allows us to measure lengths of vectors and other emergent quantities, so long as they lie in the same tangent space $T_pM$ for some $p\in M$. The remaining question is: "How can we compare tangent vectors that live in different tangent spaces?" And this will be the focus of the current chapter. 

To answer this question, we will build up to the *covariant derivative* and define *connections*, which turn out to be precisely the additional structure on $M$ needed to compare tangent vectors across different tangent spaces. We begin by motivating the preceding constructions from the perspective of geodesics, first in Euclidean space. Throughout, $(M,g)$ or $M$ will always denote a Riemannian manifold.

## Geodesics
A geodesic in $\RR^k$ is just a straight line. One characterization is that given two points, a straight line is the path between them of minimal length. It is tempting to extend this definition to a general Riemannian manifold $(M,g)$, but it turns out that it is a bit unwieldy to use in practice.

The alternative, more useful perspective, is that a straight line in $\RR^k$ is one that does not "curve" any more than it needs to, in order to stay in $\RR^k$. Of course, since $\RR^k$ is itself completely flat, that means that any curve that does not curve any more than it needs to is also itself "completely flat". 

### Curves in Euclidean Space
Let $I\subseteq \RR$ and $\gamma:I\to\RR^k,\ \gamma(t) = (\gamma^1(t),\ldots, \gamma^k(t))$ be a curve in $\RR^k$.

<div class="definition">
<span class="definition-label">Definition.</span> The *velocity* of $\gamma$ is defined to be 
$$\gamma'(t) := \dot\gamma^1(t)\frac{\partial}{\partial x^1}\big|_{\gamma(t)} + \ldots + \dot\gamma^k(t)\frac{\partial}{\partial x^k}\big|_{\gamma(t)} \in T_{\gamma(t)}\RR^k,$$
where $\dot\gamma^i$ denotes the time-derivative of each component $\gamma^i:\RR\to\RR$. This expression can also be written more simply in $\RR^k,$ using that $T_p\RR^k = \RR^k$ for all $p\in \RR^k$, as 
$$\gamma'(t) = \left(\frac{d}{dt}\gamma^1(t),\ldots, \frac{d}{dt}\gamma^k(t)\right)$$
</div>
The equivalence of the above expressions comes from the choice of maximal atlas $(\RR^k, \RR^k, \id)$ for $\RR^k$, giving the basis $\left(\frac{\partial}{\partial x^i}\right)_{1\le i \le k}$ of $T_p\RR^k$ for all $p$.

The acceleration of a curve can be defined in a similar way:

<div class="definition">
<span class="definition-label">Definition.</span> The *acceleration* of $\gamma$ is defined to be 
$$\gamma''(t) := \ddot\gamma^1(t)\frac{\partial}{\partial x^1}\big|_{\gamma(t)} + \ldots + \ddot\gamma^k(t)\frac{\partial}{\partial x^k}\big|_{\gamma(t)} \in T_{\gamma(t)}\RR^k,$$
where $\ddot\gamma^i$ denotes the second time-derivative of each component $\gamma^i:\RR\to\RR$. This expression can similarly be written more simply in $\RR^k$:
$$\gamma''(t) = \left(\frac{d^2}{dt^2}\gamma^1(t),\ldots, \frac{d^2}{dt^2}\gamma^k(t)\right)$$
</div>

### Differentiating Vector Fields

We can similarly take directional derivatives of vector fields on $\RR^k$. Let $\mfx(\RR^k)$ denote the space of vector fields on $\RR^k$, and let $Y\in\mfx(\RR^k)$ with components $Y=(Y^1,\ldots, Y^k)$, and let $v\in T_p\RR^k$. Since each $Y^i$ is a smooth function $\RR^k\to \RR$, it is easy to define the directional derivative of $Y^i$ in the direction $v$:
$$D_v(Y^i) := v^1 \frac{\partial Y^i(p)}{\partial x^1} + \ldots + v^k\frac{\partial Y^i(p)}{\partial x^k} = \lim_{t\to 0} \frac{Y^i(p+tv) - Y^i(p)}{t}$$
With the last equality holding in $\RR^k$ for the same reasons as the simplifications above hold. So, we can differentiate a vector field component by component:

<div class="definition">
<span class="definition-label">Definition.</span> Let $Y\in\mfx(\RR^k)$ and $v\in T_p\RR^k$. Then the *directional derivative of $Y$ in the direction $v$* is defined by the formula
$$\bar\nabla_v Y := D_v(Y^1) \frac{\partial}{\partial x^1}\big|_p + \ldots + D_v(Y^k) \frac{\partial}{\partial x^k}\big|_p \in T_p\RR^k$$
</div>

Importantly, we are now able to define the derivative of a vector field $Y$ with respect to *another vector field* $X$ in Euclidean space:

<div class="definition">
<span class="definition-label">Definition.</span> Let $X,Y\in\mfx(\RR^k)$ be vector fields. Then the *derivative of $Y$ with respect to $X$* is a vector field defined at each point $p$ by the formula
$$\bar\nabla_X Y := D_{X(p)}(Y^1) \frac{\partial}{\partial x^1}\big|_p + \ldots + D_{X(p)}(Y^k) \frac{\partial}{\partial x^k}\big|_p \in \mfx(\RR^k)$$
</div>

## Acceleration on Manifolds

### Water on a Sphere

Let us now explore what it means for a curve to "only curves as much as it needs to". A prototypical picture to keep in mind is the following: consider a stream of water flowing over a surface in $\RR^3$. Provided the surface is not flat, the water does not naturally flow in a straight line: it conforms to the curvature of the surface. For instance, if the water is flowing over a sphere (with sufficient gravity to keep the water pinned to the sphere) from north to south pole, then it will flow along what one might call, in geography, a longitudinal arc.

Assuming the water flows at constant speed, then the component of its acceleration in the direction of its velocity is zero. And since it only curves as much as it needs to, the component of its acceleration orthogonal to its velocity (within the tangent plane) is also zero. This suggests that the water's acceleration is normal to the surface of the sphere (indeed, from a physics perspective, its acceleration is downwards into the center of the sphere!).

This suggests we need a useful working definition of the acceleration of a curve. That way, we could define a geodesic on $M$ as a curve whose acceleration at any point $p$ is a normal vector to $T_pM$. However, there are two issues: first, this definition is not *intrinsic* to the surface: it assumes that the surface is sitting inside some large Euclidean space $\RR^N$. Secondly, we had initially defined acceleration in Euclidean space as the time-derivative of velocity. But this relied heavily on the fact that $T_p\RR^k = T_{p'}\RR^k = \RR^k$ for all $p,p'\in\RR^k$. In the more general case, we have
$$\gamma'(p) \in T_{\gamma(p)}M \text{ and } \gamma'(p+tv) \in T_{\gamma(p+tv)}M$$ and these tangent spaces need not be equal! Hence the proposed expression
$$\gamma''(t) = \lim_{t\to 0}\frac{\gamma'(p) - \gamma'(p+tv)}{t}$$ does not make sense; it does not pass a simple [type check](https://en.wikipedia.org/wiki/Type_system#Type_checking).

Thus, we need a way of "connecting" nearby tangent spaces.

## Connections
Motivated by our previous discussion, it is important for our definition of a connection to satisfy similar properties as $\bar\nabla$. We begin by examining the more general case, where we have a smooth vector bundle $\pi:E\to M$ over a manifold $M$. Let $\Gamma(E)$ denote the space of smooth sections of $E$. 

<div class="definition">
<span class="definition-label">Definition.</span> A *connection* in $E$ is a map
$$\nabla: \mfx(M) \times \Gamma(E) \to \Gamma(E),$$ written $(X,Y)\mapsto \nabla_X Y$, satisfying the following properties:
<ol>
1. $\nabla_X Y$ is linear over $C^\infty(M)$ in $X$: for $f_1,f_2\in C^\infty(M)$ and $X_1,X_2\in \mfx(M)$, $$\nabla_{f_1X_1 + f_2X_2}Y = f_1\nabla_{X_1}Y + f_2\nabla_{X_2}Y$$
2. $\nabla_XY$ is linear over $\RR$ in $Y$: for $a_1,a_2\in\RR$ and $Y_1,Y_2\in\Gamma(E)$, $$\nabla_X(a_1Y_1+a_2Y_2) = a_1\nabla_XY_1 + a_2\nabla_XY_2$$
3. $\nabla$ satisfies a *product* rule: for $f\in\C^\infty(M)$, $$\nabla_X(fY) = f\nabla_XY + (Xf)Y$$
</ol>
Moreover, $\nabla_XY$ is called the *covariant derivative of $Y$ in the direction $X$*.
</div>

<div class="definition">
<span class="definition-label">Remark.</span> What we have defined above is also called a **Koszul Connection**, but we will refer to such operators as *connections*. Other types of connections arise naturally in information geometry, and will be explained as needed.
</div>

A key property of connections is that, although we defined them in terms of global sections, a connection is a local operator: namely,

<div class="definition">
<span class="definition-label">Proposition.</span> Suppose $\nabla$ is a connection in a smooth vector bundle $\pi:E\to M$. For every $x\in \mfx(M)$, $Y\in\Gamma(E)$, and $p\in M$, if $X=\tilde X$ and $Y=\tilde Y$ on a neighborhood of $p$, then $\nabla_{\tilde X} \tilde Y|_p = \nabla_X Y|_p$.
</div>
Henceforth, we restrict our focus to tangent bundles over smooth manifolds.

## References
<ol>
<li> *Introduction to Riemannian Manifolds*, by John M. Lee</li>
<li> *Differential Geometry of Curves and Surfaces*, by Kristopher Tapp</li>
<li> Notes on Differential Topology by <a href="https://www.utsc.utoronto.ca/people/kupers/">Alexander Kupers </a>, which do not seem to be uploaded. </li>
</ol>