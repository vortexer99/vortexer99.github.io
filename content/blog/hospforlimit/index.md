---
title: '利用洛必达求数列极限'
date: 2018-01-05
url: /posts/2018/01/hospforlimit/
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

设 0 < 𝑥1 < 1, 𝑥𝑛+1 = sin 𝑥𝑛，证明： lim 𝑛→∞ √𝑛 𝑥𝑛 =√3

$$设\ 0 < x_{1} < 1,\ x_{n + 1} = \sin x_{n}$$

$$证明：\lim_{n \rightarrow \infty}{\sqrt{n}{\ x}_{n}} = \sqrt{3}$$

$$证：要求\lim_{n \rightarrow \infty}{\sqrt{n}{\ x}_{n}}，等价于求\lim_{n \rightarrow \infty}{n\ x_{n}^{2}}，$$

$$等价于求\lim_{n \rightarrow \infty}\frac{n}{\frac{1}{x_{n}^{2}}}$$

$$对于数列x_{n}，唯一的稳定点只有0 = \sin 0$$

$$不难得到\lim_{n \rightarrow \infty}{\ x}_{n} = 0$$

$$因此\lim_{n \rightarrow \infty}\frac{1}{x_{n}^{2}} = \infty$$

$$同时显然有\lim_{n \rightarrow \infty}\ n = \infty$$

应用离散形式的洛必达法则

$$\lim_{n \rightarrow \infty}\frac{n}{\frac{1}{x_{n}^{2}}} = \lim_{n \rightarrow \infty}\frac{(n + 1) - n}{\frac{1}{x_{n + 1}^{2}} - \frac{1}{x_{n}^{2}}} = \lim_{n \rightarrow \infty}\frac{1}{\frac{1}{x_{n + 1}^{2}} - \frac{1}{x_{n}^{2}}}$$

$$= \lim_{n \rightarrow \infty}\frac{x_{n + 1}^{2}x_{n}^{2}}{x_{n}^{2} - x_{n + 1}^{2}} = \lim_{n \rightarrow \infty}\frac{\sin^{2}x_{n}x_{n}^{2}}{x_{n}^{2} - \sin^{2}x_{n}}$$

$$= \lim_{t \rightarrow 0}\frac{\sin^{2}t\ t^{2}}{t^{2} - \sin^{2}t}$$

此时可按照连续函数处理。

$$\lim_{t \rightarrow 0}\frac{\sin^{2}t\ t^{2}}{t^{2} - \sin^{2}t} = \lim_{t \rightarrow 0}\frac{2t\sin^{2}t + 2\sin t\cos t\ t^{2}}{2t - 2\sin t\cos t}$$

$$= \lim_{t \rightarrow 0}\frac{2\sin^{2}t + 4t\sin t\cos t + 4t\sin t\cos t + 2t^{2}\cos{2t}}{2 - 2\cos{2t}}$$

$$= \lim_{t \rightarrow 0}\frac{\sin^{2}t + 2t\sin{2t} + t^{2}\cos{2t}}{1 - \cos{2t}}$$

$$= \lim_{t \rightarrow 0}\frac{2\sin t\cos t + 2\sin{2t} + 4t\cos{2t} + 2t\cos{2t} - 2t^{2}\sin{2t}}{2\sin{2t}}$$

$$= \lim_{t \rightarrow 0}\frac{3\sin{2t} + 6t\cos{2t} - 2t^{2}\sin{2t}}{2\sin{2t}}$$

$$= \lim_{t \rightarrow 0}\frac{6\cos{2t} + 6\cos{2t} - 12t\sin{2t} - 4t\sin{2t} - 4t^{2}\cos{2t}}{4\cos{2t}}$$

$$= 3$$

怎么要导这么多次=\_=真是活久见。果断换用泰勒。

$$\sin^{2}t = \left( t - \frac{1}{6}t^{3} + o\left( t^{3} \right) \right)^{2} = t^{2} - \frac{1}{3}t^{4} + o\left( t^{4} \right)$$

$$\lim_{t \rightarrow 0}\frac{\sin^{2}t\ t^{2}}{t^{2} - \sin^{2}t} = \lim_{t \rightarrow 0}\frac{{(t}^{2} - \frac{1}{3}t^{4} + o\left( t^{4} \right))\ t^{2}}{t^{2} - \left( t^{2} - \frac{1}{3}t^{4} + o\left( t^{4} \right) \right)}$$

$$= \lim_{t \rightarrow 0}\frac{\left( 1 - \frac{1}{3}t^{2} \right)t^{4} + o\left( t^{6} \right)}{\frac{1}{3}t^{4} + o\left( t^{4} \right))} = \lim_{t \rightarrow 0}\frac{\left( 1 - \frac{1}{3}t^{2} \right) + o\left( t^{2} \right)}{\frac{1}{3} + o(1))}$$

$$= 3$$

开根号就得到

$$\lim_{n \rightarrow \infty}{\sqrt{n}{\ x}_{n}} = \sqrt{3}$$

此题的核心方法是利用洛必达，设法消除n对极限的影响。

从而只需要研究数列中相邻项即可，而这是有递推公式可以用的。
