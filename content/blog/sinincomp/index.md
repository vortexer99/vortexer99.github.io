---
title: '三角函数在复数域中的值域'
date: 2018-01-07
url: /posts/2018/01/sinincomp/
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

已知 𝑧 ∈ 𝐂且 \|𝑧\| ≤ 1, 求\|sin 𝑧\|的最大值。

$$已知\ z \in \mathbf{C}且\ |z| \leq 1,求\left| \sin z \right|的最大值。$$

$$设\ z = x + yi，x,y \in \mathbf{R}\ ，x^{2} + y^{2} \leq 1$$

$$\sin z = \sin(x + yi) = \sin x\cos{yi} + \cos x\sin{yi}$$

(和角公式在复数域中也成立，证明略，

可利用复数域中三角函数的定义)

$$利用\sin x = - i\sinh{ix},\cos x = \cosh{ix}$$

$$\sin z = \sin x{\cos h}y + \cos x{\sin h}y\ i$$

$$\left| \sin z \right|^{2} = \sin^{2}x\cosh^{2}y + \cos^{2}x\sinh^{2}y$$

$$= \sin^{2}x\left( 1 + \sinh^{2}y \right) + \cos^{2}x\sinh^{2}y$$

$$= \sin^{2}x + \sinh^{2}y$$

显然，只需考虑$x \geq 0,y \geq 0$的情况即可。

并注意到$\sin^{2}x,\sinh^{2}x在\lbrack 0,1\rbrack 上递增$，

$$因此最大值一定在x^{2} + y^{2} = 1上取到。$$

$$于是y = \sqrt{1 - x^{2}}$$

$$令\left| \sin z \right|^{2} = \sin^{2}x + \sinh^{2}\sqrt{1 - x^{2}} = f(x)$$

$$下求f(x)在\lbrack 0,1\rbrack 上最大值。$$

$$首先求导观察：$$

$$f^{'}(x) = \sin{2x} - \frac{x}{\sqrt{1 - x^{2}}}\sinh{2\sqrt{1 - x^{2}}}$$

$$= \sin{2x} - \frac{x}{2\sqrt{1 - x^{2}}}\left( e^{2\sqrt{1 - x^{2}}} - e^{- 2\sqrt{1 - x^{2}}} \right)$$

$$又有\sin,又有e，还有根号，事情仿佛陷入了僵局。$$

接下去该怎么办呢？

$$我们可以对e^{x}作泰勒展开。$$

![](media/media/image1.jpeg){width="2.7918558617672793in" height="2.545923009623797in"}

$$e^{x} = 1 + x + \frac{1}{2}x^{2} + \frac{1}{6}x^{3} + \ldots$$

$$e^{- x} = 1 - x + \frac{1}{2}x^{2} - \frac{1}{6}x^{3} + \ldots$$

$$e^{x} - e^{- x} = 2\left( x + \frac{1}{6}x^{3} + \ldots \right)$$

$$当x > 0时有e^{x} - e^{- x} > 2x$$

$$故\sin{2x} - \frac{x}{2\sqrt{1 - x^{2}}}\left( e^{2\sqrt{1 - x^{2}}} - e^{- 2\sqrt{1 - x^{2}}} \right)$$

$$< \sin{2x} - \frac{x}{2\sqrt{1 - x^{2}}} \cdot 2\left( 2\sqrt{1 - x^{2}} \right)$$

$$= \sin{2x} - 2x$$

$$< 0$$

$$因此f^{'}(x) < 0,x \in \lbrack 0,1\rbrack$$

$$f(x)有最大值f(0) = \sinh^{2}1$$

$$\therefore\left| \sin z \right|在给定条件下最大值为\sinh 1$$
