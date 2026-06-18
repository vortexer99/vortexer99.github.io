---
title: '分部积分算erf原函数的定积分'
date: 2018-01-15
url: /posts/2018/01/partint/
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

已知f(x)=(∫1 to x)e^t^2 dt，求(∫0 to 1)f(x)dx

$$已知f(x) = \int_{1}^{x}{e^{t^{2}}dt}$$

$$求\int_{0}^{1}{f(x)dx}$$

$解$：

首先大家要知道$e^{t^{2}}$是一个典型的

没有初等原函数的函数。

所以直接积分是做不出来的。

待求式可写为

$$\int_{0}^{1}{\left( \int_{1}^{x}{e^{t^{2}}dt} \right)dx}$$

利用分部积分，上式

$$= \left\lbrack x\int_{1}^{x}{e^{t^{2}}dt} \right\rbrack_{0}^{1} - \int_{0}^{1}{xe^{x^{2}}dx}$$

第一项代入1，由定积分性质可得为0

代入0，由最前面的$x$可得也为0

因此第一项虽然无法求出确切函数，

但是刚好能被消掉。

而此时第二项比最开始多了一个$x$，

就可以计算原函数。

$$\int_{0}^{1}{xe^{x^{2}}dx} = \frac{1}{2}\int_{0}^{1}{e^{x^{2}}d(x^{2})} = \frac{1}{2}{\lbrack e^{x^{2}}\rbrack}_{0}^{1} = \frac{e - 1}{2}$$

$$因此答案为\frac{1 - e}{2}$$

$$求\int_{}^{}{\left( \ln{\ln x} + \frac{1}{\ln x} \right)dx}$$

这里直接对整个函数分部积分似乎是做不出来的。

$$将它分为\int_{}^{}{\ln{\ln x}dx} + \int_{}^{}\frac{1}{\ln x}dx$$

对前面一项分部积分，神奇的事情就出现了。

$$\int_{}^{}{\ln{\ln x}dx} + \int_{}^{}\frac{1}{\ln x}dx$$

$$= x\ln{\ln x} - \int_{}^{}{x\frac{1}{\ln x}\frac{1}{x}}dx + \int_{}^{}\frac{1}{\ln x}dx$$

$$= x\ln{\ln x}( + C)$$

*\
*

【此段节选自《吉米多维奇数学分析习题集题解》，费定晖等】

吉米多维奇1824，1825题

$$求\int_{}^{}\frac{xe^{\arctan x}}{\left( 1 + x^{2} \right)^{\frac{3}{2}}}\ dx,\ \ \int_{}^{}\frac{e^{\arctan x}}{\left( 1 + x^{2} \right)^{\frac{3}{2}}}\ dx$$

解：

$$记I_{1} = \int_{}^{}\frac{xe^{\arctan x}}{\left( 1 + x^{2} \right)^{\frac{3}{2}}}\ dx\ ,\ \ I_{2} = \int_{}^{}\frac{e^{\arctan x}}{\left( 1 + x^{2} \right)^{\frac{3}{2}}}\ dx$$

$$I_{1} = - \int_{}^{}e^{\arctan x}\ d\left( \left( 1 + x^{2} \right)^{- \frac{1}{2}} \right)$$

$$= - e^{\arctan x}\left( 1 + x^{2} \right)^{- \frac{1}{2}} + \int_{}^{}\left( 1 + x^{2} \right)^{- \frac{1}{2}}e^{\arctan x}\frac{1}{1 + x^{2}}\ dx$$

$$= - \frac{e^{\arctan x}}{\left( 1 + x^{2} \right)^{\frac{1}{2}}} + I_{2}\ \ \ \ ①$$

$$I_{1} = \int_{}^{}\frac{xe^{\arctan x}}{\left( 1 + x^{2} \right)^{\frac{1}{2}}}\ d\left( \arctan x \right) = \int_{}^{}\frac{x}{\left( 1 + x^{2} \right)^{\frac{1}{2}}}\ d\left( e^{\arctan x} \right)$$

$$= \frac{xe^{\arctan x}}{\left( 1 + x^{2} \right)^{\frac{1}{2}}} - \int_{}^{}\frac{\left( 1 + x^{2} \right)^{\frac{1}{2}} - x\left( 1 + x^{2} \right)^{- \frac{1}{2}}}{1 + x^{2}}e^{\arctan x}dx$$

$$= \frac{xe^{\arctan x}}{\left( 1 + x^{2} \right)^{\frac{1}{2}}} - \int_{}^{}\frac{e^{\arctan x}dx}{\left( 1 + x^{2} \right)^{\frac{3}{2}}}$$

$$= \frac{xe^{\arctan x}}{\left( 1 + x^{2} \right)^{\frac{1}{2}}} - I_{2}\ \ \ \ \ ②$$

$$于是\frac{① + ②}{2} = I_{1} = \frac{(x - 1)e^{\arctan x}}{2\left( 1 + x^{2} \right)^{\frac{1}{2}}} + C$$

$$\frac{② - ①}{2} = 0 = \frac{(x + 1)e^{\arctan x}}{\left( 1 + x^{2} \right)^{\frac{1}{2}}} - 2I_{2}$$

$$I_{2} = \frac{(x + 1)e^{\arctan x}}{2\left( 1 + x^{2} \right)^{\frac{1}{2}}} + C$$

遇到不好做的积分题时，特别是带变上限积分时，

多考虑分部积分，往往会有奇效。
