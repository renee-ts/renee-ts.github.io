---
title: "Triangle With Minimum Perimeter"
date: 2026-06-25
toc: true
hide-sidebar: true
tags: [puzzles]
---

## Introduction
The following problem is Problem B-2 from the [1998 Putnam Competition](https://kskedlaya.org/putnam-archive/1998.pdf):

<div class="definition">
<span class="definition-label">Problem.</span> Let $0 < a < b$ and consider the point $p=(a,b)$. Determine the minimum perimeter of a triangle with one vertex at $p$, one on the $x$-axis, and one on the line $y=x$. You may assume that a triangle of minimum perimeter exists.
</div>

This problem is actually quite tractable, as long as we make a few simple observations about symmetry. As a warm-up, we'll first consider an easier, related problem.

## Warmup

<div class="definition">
<span class="definition-label">Problem.</span> Let $(a,b)$ and $(c,d)$ be two points such that $0 < a,b,c,d$. Determine the length of the shortest path from $(a,b)$ to $(c,d)$ that touches the horizontal axis.†<span class="sidenote"><span class="sidenote-marker">†</span> I saw this problem in <emph> The Art and Craft of Problem Solving</emph> by Paul Zeitz, though it's quite well-known and I'm not sure of the original source.
</div>
<div class="definition">
<span class="definition-label">Solution.</span> 

Label the points $p:=(a,b)$ and $q:=(c,d)$, and let $-q:=(c,-d)$, the reflection of $q$ across the $x$-axis. The crucial observation is as follows:

<div class="quote">The path of minimum length from $(a,b)$ to $(c,d)$ that touches the $x$-axis  has the same length as the path of minimum length from $(a,b)$ to $(c,-d)$.
</div>

In short, this is because reflection is an isometry: the distance from $r$ to $q$ is the same as the distance from $r$ to $-q$, as can be seen in the following diagram:

(ADD DIAGRAM)

Thus, if $r'$ is any point on the $x$-axis, then the path from $p$ to $r$ to $q$ has length $d(p,r') + d(r', q) = d(p,r') + d(r', -q) \ge d(p, -q)$, with equality if and only if $r'$ lies on the straight line from $p$ to $-q$.

It follows by the Pythagorean theorem that the minimum length is: $$\sqrt{(c-a)^2 + (b+d)^2}$$
</div>

## Problem Solution

Let us now return to the given problem. How can we generalize ideas from the warmup problem to the original? We can start by rephrasing the Putnam question in a way that resembles the warm-up more closely: we are tasked to find the minimum length of path from $p$ to $p$, such that the path touches both the $x$-axis and the line $y=x$.

Now, denote $q := (a, -b)$ and $r := (b,a)$, the reflections of $p$ across the $x$-axis and across the line $y=x$, respectively. Let $s$ be any point on the line $y=x$ and $t$ any point on the $x$-axis. Then $rs = sp$ since reflections are isometries, and $tq = pt$ by similar reasoning. 

(ADD DIAGRAM)

Each choice of points $s,t$ corresponds to a triangle $\triangle pst$, whose perimeter is $$sp + pt + ts = rs+ts + tq \ge d(r, q) = \sqrt{2a^2+2b^2},$$ 
where the inequality follows from the triangle inequality. In other words, a lower bound for the perimeter of any qualifying triangle is $\sqrt{2a^2+2b^2}$. To attain the minimum, we therefore must choose $s, t$ such that they lie on the line from $r$ to $q$, therefore attaining the minimum of $\sqrt{2a^2+2b^2}$.

## References
<ol>
<li> [Problem Source](https://kskedlaya.org/putnam-archive/1998.pdf) </li>
<li> The Art and Craft of Problem Solving, by Paul Zeitz.</li>
</ol>