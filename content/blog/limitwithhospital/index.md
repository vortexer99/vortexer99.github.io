---
title: '利用洛必达证明极限'
date: 2019-08-16
url: /posts/2019/08/hospital/
tags:
  - Blogpost
  - Mathematic
  - Mathematical Analysis
  - 1-5 Pages
types:
  - blogpost
topics:
  - mathematics
  - mathematical-analysis
lengths:
  - 1-5-pages
authors:
  - me
---

一道题，已知 f 在 (a, +∞) 上可导，且 limx→+∞ f(x) + f ′(x) = b（有限或为无穷），求证limx→+∞ f(x) = b

已知$f$在$(a,+\infty)$上可导，且$\lim_{x\rightarrow +\infty} f(x)+f'(x)=b$（有限或为无穷），求证$\lim_{x\rightarrow +\infty} f(x)=b$

# 证明

如果有 $$\label{eq:2}
\lim_{x\rightarrow +\infty}\exp{x}f(x) = \infty$$ 那么利用洛必达巧妙证明 $$\begin{aligned}
  \label{eq:1}
  \lim_{x\rightarrow +\infty}f(x)=\lim_{x\rightarrow +\infty}\frac{\exp{x}f(x)}{\exp{x}}=\lim_{x\rightarrow +\infty}\frac{\exp{x}(f(x))+f'(x))}{\exp{x}}=\lim_{x\rightarrow +\infty}f(x)+f'(x)
\end{aligned}$$

而如果 $$\label{eq:2}
\lim_{x\rightarrow +\infty}\exp{x}f(x) < \infty$$ 那么可知$\lim_{x\rightarrow +\infty}f(x)=0$，进而$\lim_{x\rightarrow +\infty}f'(x)=0$，等式仍然成立。
