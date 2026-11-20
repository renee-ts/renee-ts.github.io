---
title: "Lagrangian Duality"
description: "Lagrangian duality, and why a minimization problem is a min max problem, and its dual is a max min problem."
date: 2026-09-12
toc: true
hide-sidebar: true
tags: [optimization]
---

## Introduction
In this blog post, I will discuss a beautiful technique and perspective for solving constrained minimization problems, known as Lagrangian duality. It can be thought of as an extension of the [method of Lagrange Multipliers](https://en.wikipedia.org/wiki/Lagrange_multiplier) and the [Karush-Kuhn-Tucker Conditions](https://en.wikipedia.org/wiki/Karush%E2%80%93Kuhn%E2%80%93Tucker_conditions).

The general set up is that we wish to solve a problem of the following form: 
$$
\begin{align*}
&\text{minimize } J(v)\tag{P}\\
&\text{subject to } \vp_i(v)\le 0, \text{ for } i=1,\ldots, m
\end{align*}
$$
In broad strokes, the idea is as follows. We solve the primal problem (P) by solving another related problem, called the dual problem (D), by introducing the *Lagrangian* of problem (P). Then, we first solve an unconstrained minimization problem with respect to one variable of the Lagrangian, and then an (essentially) unconstrained maximization problem of that, and in certain cases, we recover a solution to (P). All of this is very vague, but the core idea is:

<div class="quote">A minimization problem can be naturally understood as a *min max* problem; there is an associated *max min* problem that is often easier to solve. Saddle points are precisely the min of one variable and the max of another: the *min max* and *max min* coincide. So, we should try to find saddle points of the right function.
</div>

## The Lagrangian and Saddle Points

Let $\Om$ be a normed vector space. Given the data of a function to be minimized $J:\Om\to\RR$, and a set $U = \{x\in\Om : \vp_i(x)\le 0\text{ for }i=1,\ldots, m\}$ defined by $m$ inequality constraints , we define:

<div class="definition">
<span class="definition-label">Definition.</span> The **Lagrangian** $L(v,\mu)$ associated with the functional $J$ and contraints $\vp_i$ is the function $L: \Om \times \RR_{\ge 0}^m \to \RR$ given by $$L(x,\mu) = J(x) + \sum_{i=1}^m \mu_i \vp_i(x)$$
</div>

As alluded to in the introduction, it turns out that saddle points of the Lagrangian, specifically, are quite important for solving (P). To understand why, we first introduce the general notion of saddle point, and then prove a core proposition underlying the theory of Lagrangian duality.

<div class="definition">
<span class="definition-label">Definition.</span> Let $\Om$ and $M$ be open subsets of normed vector spaces, and $L:\Om\times M\to\RR$ a function defined on their product. A point $(u,\lambda)\in\Om\times M$ is a **saddle point** of the function $L$ if $u$ is a *minimum* of the function $L(\cdot, \lambda): \Om\to\RR$ given by $v\mapsto L(v,\lambda)$ for all $v\in \Om$ and $\lambda$ fixed, and $\lambda$ is a *maximum* of the function $L(u,\cdot): M\to\RR$ given by $\lambda \mapsto L(u,\lambda)$ for all $\lambda\in M$ and $u$ fixed. Equivalently, $$ \sup_{\mu\in M}L(u,\mu) = L(u,\lambda) = \inf_{v\in \Om} L(v,\lambda)$$
</div>

<div class="definition">
<span class="definition-label">Remark.</span> Usually, $M$ is considered a set of "multipliers" or "prices", if you will, hence the notation. Usually, $M=\RR_{\ge 0}^m$.
</div>

The following proposition is extremely important, and has great implications for duality theory. It essentially says that at a saddle point, the ordering of $\inf$ and $\sup$ can be interchanged; as alluded to before, Lagrangian duality involves both a $\max\min$ problem (the dual problem) and a $\min\max$ problem (the primal). If these quantities can be claimed equal (as they can at a saddle point of the Lagrangian), then we can solve (P) by solving (D).

<div class="definition">
<span class="definition-label">Proposition.</span> If $(u,\lambda)$ is a saddle point of the Lagrangian $L:\Om\times M\to\RR$, then $$\sup_{\mu\in M}\inf_{v\in \Om} L(v,\mu) = L(u,\lambda) = \inf_{v\in \Om}\sup_{\mu \in M} L(v,\mu)$$
</div>

**Proof**. We'll provide the formal proof first, which is essentially a bunch of symbol-pushing and definition-chasing. First, let $\om\in\Om$ and $\rho\in M$. Then by definition of $\inf$ and $\sup$, we have
$$\inf_{v\in\Om} L(v,\rho) \le L(\om,\rho) \le \sup_{\mu \in M} L(\om, \mu)$$
Since the inequality
$$\inf_{v\in\Om} L(v,\rho) \le \sup_{\mu \in M} L(\om, \mu)\tag{*}$$
holds with no assumptions made on $\rho$, and the right-hand side is independent of $\rho$, this means that 
$$\sup_{\mu\in M}\inf_{v\in\Om} L(v,\mu) \le \sup_{\mu \in M} L(\om, \mu)$$
And similarly, the inequality $(*)$ holds with no assumptions made on $\om$, and the left-hand side is independent of $\om$, so it must be that
$$\sup_{\mu\in M}\inf_{v\in\Om} L(v,\mu) \le \inf_{v\in \Om}\sup_{\mu \in M} L(v, \mu)$$

Now, by the very definition of saddle point, we have
$$L(u,\lambda) = \sup_{\mu\in M} L(u,\mu) \ge \inf_{v\in \Om}\sup_{\mu\in M} L(v,\mu)$$
And
$$L(u,\lambda) = \inf_{v\in \Om} L(v, \lambda) \le \sup_{\mu\in M} \inf_{v\in \Om} L(v, \mu)$$
Or in other words,
$$\inf_{v\in \Om}\sup_{\mu\in M} L(v,\mu) \le \sup_{\mu\in M} \inf_{v\in \Om} L(v, \mu)$$
which completes the proof. $\blacksquare$


### Why the Primal Problem is a Min Max Problem

Let us try to understand a bit why (P) is a $\min\max$ problem. Specifically, the claim is that 
$$\inf_{u\in \Om}\sup_{\mu\in M} L(u,\mu) = \min J(u) \text{, subject to } u\in U$$
As a start, let us write out the left-hand side in full:
$$\inf_{u\in \Om}\sup_{\mu\in M} L(u,\mu) = \inf_{u\in \Om}\sup_{\mu\in M} J(u) + \sum_{i=1}^m \mu_i\vp_i(u)$$
Now, we examine just the $\sup$ term, based on whether $u$ belongs to $\Om$ or not. If $u$ is feasible, then $\vp_i(u)\le 0$, hence since $\mu\in \RR_{\ge0}^m$, the supremum
$$\sup_{\mu\in M} J(u) + \sum_{i=1}^m \mu_i\vp_i(u)$$
is attained when $\mu_i=0$ for all $i$, leaving us precisely with $J(u)$. On the other hand, if $u$ is infeasible, then $\vp_i(u) > 0$ for some $i$. by taking $\mu_i\to\infty$, we have $L(u,\mu)\to\infty$, and we see that in this case, the $\sup$ is never attained. To recap,
$$\sup_{\mu\in\RR_{\ge0}^m} L(u,\mu) = \begin{cases}J(u) &\text{if $u\in U$}\\ \infty &\text{otherwise} \end{cases}$$
It therefore follows that
$$\inf_{u\in U} J(u) = \inf_{u\in \Om}\sup_{\mu\in M} L(u,\mu)$$
and our constrained minimization problem has been recast as an essentially unconstrained $\min\max$ problem; the only constraint is that $\mu\in \RR^m_{\ge0}$. 

Thinking of the $\sum_{i=1}^m \mu_i\vp_i$ term as a "cost" or "penalty", we can think of the primal problem as assigning a penalty of $\infty$ whenever we are outside the feasible domain–the only solutions that can hope to attain even a finite cost, let alone the minimum cost, are those inside $U$.

## The Dual Problem

By the previous result, we are led to the following definition:

<div class="definition">
<span class="definition-label">Proposition.</span> Given the minimization problem (P), the function $G: \RR^m_{\ge0}\to \RR$ given by 
$$G(\mu) = \inf_{v\in\Om} L(v,\mu)$$
is called the **Lagrange dual function**. The problem (D) is defined as

$$
\begin{align*}
&\text{maximize } G(\mu)\tag{D}\\
&\text{subject to } \mu\in\RR_{\ge0}^m
\end{align*}
$$
is called the **Lagrange dual problem**. Here, $\mu$ is called the *dual variable*, and $\mu$ is said to be *dual feasible* if $G(\mu)$ is defined (i.e., not equal to $-\infty$). Finally, if $\lambda\in\RR^m_{\ge0}$ is a maximum of $G$, then we call it a *dual optimal* or an *optimal Lagrange multiplier*.
</div>

<div class="definition">
<span class="definition-label">Remark.</span> It is extremely important to note that $G$ is **concave**, whether or not the $\vp_i$ are convex. This is because $G(\mu) = \inf_{v\in\Om} L(v,\mu)$ is the pointwise infimum of affine functions of $\mu$.
</div>

### Why the Dual Problem is a Max Min Problem
This is more straightforward to see. If $u\in U$ and $\mu\in\RR^m_{\ge0}$, then $\mu\ge 0$ and $\vp_i(u)\le 0$ for all $i$, therefore $$G(\mu) \le L(u,\mu) \le J(u)$$ and so 
$$G(\mu) = \inf_{v\in\Om} L(v,\mu) \le L(u,\mu) = J(u) + \sum_{i=1}^m \mu_i\vp_i(u) \le J(u)$$

Equivalently, for every dual optimal $\lambda^*$ and every primal optimal $u^*$, we have $$G(\lambda^*) \le J(u^*).$$

If we denote the minimum of the Primal Problem (P) by $p^*$ and the maximum of the Dual Problem (D) by $d^*$, then the above inequality implies

## References
<ol>
<li> </li>
</ol>