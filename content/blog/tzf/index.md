---
title: '调整法证明广义均值不等式'
date: 2019-08-16
url: /posts/2019/08/tzf/
tags:
  - Blogpost
  - Mathematic
  - 1-5 Pages
types:
  - blogpost
topics:
  - mathematics
lengths:
  - 1-5-pages
authors:
  - me
---

如题。

已知：对于$i=1,2\dots n,\;\alpha_i>0,\;x_i>0,\;\sum_{i=1}^{n}\alpha_i=1$

证明： $$f(t)=\begin{cases}
  (\sum_{i=1}^{n}\alpha_ix_i^t)^{\frac{1}{t}}, & t\neq 0\\
  \prod _{i=1}^{n}x_i^{\alpha_i}, & t = 0
   \end{cases}$$ 在$\mathbb{R}$上是$t$的非减函数。

# 说明

对于$\alpha_i=1/n$，$t=2,1,0,-1$时即是常见的均值不等式：均方根不小于算数平均不小于几何平均不小于调和平均。去掉$\alpha_i$的这个限制，实际上是表示加权。

# 简单剖析

先考虑$t\neq 0$的情况。

$$\ln f(t)=\frac{\ln\left(\sum_{i=1}^n\alpha_ix_i^t\right)}{t}$$ 求导得到$$\frac{f'(t)}{f(t)}=\frac{1}{t^2}\cdot\left(t\cdot \frac{\sum_{i=1}^n\alpha_ix_i^t\ln x_i}
    {\sum_{i=1}^n\alpha_ix_i^t}-\ln\left(\sum_{i=1}^n\alpha_ix_i^t\right)\right)$$

由$f(t)>0$知，要$f'(t)\ge 0$，只需要说明$$t\cdot \frac{\sum_{i=1}^n\alpha_ix_i^t\ln x_i}{\sum_{i=1}^n\alpha_ix_i^t}-\ln\left(\sum_{i=1}^n\alpha_ix_i^t\right)\ge 0$$ 即需说明$$t\cdot \sum_{i=1}^{n}\alpha_ix_i^t\ln x_i\ge\left(\sum_{i=1}^{n}\alpha_ix_i^t\right)\cdot \ln\left(\sum_{i=1}^{n}\alpha_ix_i^t\right)$$ 注意到$t\ln x_i=\ln x_i^t$，取$\beta_i=\alpha_ix_i^t$，并记$B=\sum_{i=1}^n\beta_i$。则上不等式化为$$\sum_{i=1}^{n}\beta_i\ln \frac{\beta_i}{\alpha_i}\ge \ln B\cdot\sum_{i=1}^{n}\beta_i$$ 移项，即需要证明$$\sum_{i=1}^{n}\beta_i\ln \frac{\beta_i}{B}\ge \sum_{i=1}^{n}\beta_i\ln \alpha_i$$

# 核心·调整法

在原题中，$x_i,\alpha_i$是给定，独立的，$\beta_i$是由他们构造出来的。但是这里可以把$\beta_i$和$\alpha_i$看成是独立的，而不去关注$x$。注意到不等式两边形式类似，只有对数中的项不同，且$\alpha_i$只出现在右边的对数项中。同时，还满足类似的性质： $$\sum_{i=1}^n\alpha_i=\sum_{i=1}^n \frac{\beta_i}{B}=1$$

那么相当于说对于函数 $$
h(y_1,\dots,y_n)=h(y_i):=\sum_{i=1}^n\beta_i \ln y_i \qquad \sum y_i=1$$ 在$h(\beta_i/B)$时取到最大值。

我们可以感性地认为$\beta_i/B$是一个"平衡"的分配，任何偏离平衡的影响都会导致函数值减小。下面来证明这一点。

考虑求和式中的任意两项，不妨取$S=\beta_1\ln \frac{\beta_1}{B}+\beta_2\frac{\beta_2}{B}$。引入一个对最优分配$\beta_i/B$的在这两项上的微小扰动$\delta$，注意到需要保持不改变分配的和为1， 考虑偏差函数$$g(\delta)=\beta_1\ln \left( \frac{\beta_1}{B}+\delta\right)+\beta_2\ln \left( \frac{\beta_2}{B}-\delta\right)-S$$ 求导得$$g'(\delta)=\frac{B\beta_1}{\beta_1+B\delta}-\frac{B\beta_2}{\beta_2-B\delta}=\frac{-\delta\left(\beta_1+\beta_2\right)}{\left(\frac{\beta_1}{B}+\delta\right)\left(\frac{\beta_2}{B}-\delta \right)}$$ 显然，当$\delta>0$时$g'(\delta)<0$，$\delta<0$时$g'(\delta)>0$ 因此$g(0)$是极大值也是最大值，而$g(0)=0$，因此$g(\delta)<0(\delta\ne 0)$。

于是我们证明了对最优比例的任何扰动，都会使求和变小。也就是说，任何不符合最优比例的求和式，都可以通过一系列取出两项进行调整操作，在接近平衡，向最优比例靠近的同时使值变大。

举个直观的例子：假设最优比例是$\left(\frac{1}{2}，\frac{1}{4}，\frac{1}{8}，\frac{1}{8}\right)$，由比例$(a，b，c，d)$决定的求和值为$T\left[a，b，c，d\right]$，从$T\left[\frac{1}{3}，\frac{1}{3}，\frac{1}{6}，\frac{1}{6}\right]$开始，有不等式串$$T\left[\frac{1}{3}，\frac{1}{3}，\frac{1}{6}，\frac{1}{6}\right]<T\left[\frac{1}{2}，\frac{1}{6}，\frac{1}{6}，\frac{1}{6}\right]<T\left[\frac{1}{2}，\frac{1}{4}，\frac{1}{12}，\frac{1}{6}\right]<T\left[\frac{1}{2}，\frac{1}{4}，\frac{1}{8}，\frac{1}{8}\right]$$

注意其中调整时保持和不变 $$\frac{1}{3}+\frac{1}{3}=\frac{1}{2}+\frac{1}{6}\qquad \frac{1}{6}+\frac{1}{6}=\frac{1}{4}+\frac{1}{12} \qquad \frac{1}{12}+\frac{1}{6}=\frac{1}{8}+\frac{1}{8}$$

于是我们证明了$$\sum_{i=1}^n\beta_i\ln \frac{\beta_i}{B}\ge \sum_{i=1}^{n}\beta_i\ln \alpha_i$$ 简单计算$t\rightarrow0$的极限与单独定义的相等，说明函数的连续性，则原命题得证。

# 其他·下凸证明法

（忘了是哪个同学提供的了）

设$f(x)=x\ln x$，$f(x)$下凸证明略. $$\left(\sum\alpha_ix_i^t\right)\left(\ln\left(\sum\alpha_ix_i^t\right)\right)=f\left(\sum\alpha_ix_i^t\right)$$ $$f\left(\sum\alpha_ix_i^t\right)\le\sum\alpha_if\left(x_i^t\right)$$ $$\sum\alpha_if\left(x_i^t\right)=\sum\alpha_ix_i^t\ln\left(x_i^t\right)$$ 因此 $$\left(\sum\alpha_ix_i^t\right)\left(\ln\left(\sum\alpha_ix_i^t\right)\right)\le \sum\alpha_ix_i^t\ln x_i^t$$

# 后记

关于$\alpha$，$\beta$，$x$的互相影响而产生的争论，因为已经找到了一个比较好的解释并写在上面，就删去了。

感谢zx的人工ocr。
