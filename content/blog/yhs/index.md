---
title: '隐函数求导技巧'
date: 2019-08-16
url: /posts/2019/08/yhs/
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

对于不便用自变量x表达函数及其导数，而方便用y表达的情况较为有用。
$$
  \frac{\mathrm{d}^2 y}{\mathrm{d}x^2}=\frac{\mathrm{d}y}{\mathrm{d}x}\frac{\mathrm{d}}{\mathrm{d}y}\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)
$$

公式： $$\frac{\mathrm{d}^2y}{\mathrm{d}x^2}=\frac{\mathrm{d}y}{\mathrm{d}x}\frac{\mathrm{d}}{\mathrm{d}y}\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)$$ 证： $$\frac{\mathrm{d}y}{\mathrm{d}x}\frac{\mathrm{d}}{\mathrm{d}y}\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)=\frac{\mathrm{d}}{\mathrm{d}x}\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)=\frac{\mathrm{d}^2y}{\mathrm{d}x^2}$$

# 例子

$$y=1+xe^y\qquad \text{求 }\frac{\mathrm{d}^2y}{\mathrm{d}x^2}$$ 两边求导得 $$\frac{\mathrm{d}y}{\mathrm{d}x}=e^y+xe^y\cdot\frac{\mathrm{d}y}{\mathrm{d}x}$$ 于是$$\frac{\mathrm{d}y}{\mathrm{d}x}=\frac{e^y}{1-xe^y}$$ 继续两边对$x$求导会比较麻烦,注意到 $$1-xe^y=2-(1+xe^y)=2-y$$ 有$$\frac{\mathrm{d}y}{\mathrm{d}x}=\frac{e^y}{2-y}$$ 应用公式，得 $$\frac{\mathrm{d}^2y}{\mathrm{d}x^2}=\frac{\mathrm{d}y}{\mathrm{d}x}\frac{\mathrm{d}}{\mathrm{d}y}\left(\frac{e^y}{2-y}\right)=\frac{e^y}{2-y}\cdot\frac{e^y(2-y)+e^y}{(2-y)^2}=\frac{e^{2y}(3-y)}{(2-y)^3}$$

# 小结

此公式对于不便用自变量$x$表达函数及其导数，而方便用$y$表达的情况较为有用。

此公式可进一步推得 $$\frac{\mathrm{d}^2y}{\mathrm{d}x^2}=\frac{1}{2}\frac{\mathrm{d}}{\mathrm{d}y}
\left[
  \left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2
\right]$$ 请读者自行验证。

最后感谢船的人工ocr。
