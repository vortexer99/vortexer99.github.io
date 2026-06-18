---
title: '指数三角函数幂级数求和化简'
date: 2019-03-12
url: /posts/2019/03/sum/
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

今天刷电动力学的时候，作者用分离变量法解出了一个位势方程，并声称解“明显”由指数三角函数幂级数求和化简为arctan形式，为什么呢？

今天刷电动力学的时候，作者用分离变量法解出了一个位势方程，并 声称解"明显"可以化简成以下形式。 $$V(x,y)=\frac{4V_0}{\pi}\sum_{i=1,3,...}^{\infty}\frac{1}{n}\exp{-n\pi x/a}\sin{\brack{\frac{n\pi y}{a}}}
  =\frac{2V_0}{\pi}\arctan{\brack{\frac{\sin{\pi y/a}}{\sinh{\pi x/a}}}}$$

然而作为一名辣鸡读者，看着一点都不显然。于是推了一下。

先试了对后面的$\arctan$进行展开，结果出来$\sin$和$\sinh$的幂次，没法处理，卒。

但是仍然可以从$\arctan$的展开式入手，众所周知（其实我也是百度查的） $$\arctan{x}=x-\frac{x^3}{3}+\frac{x^5}{5}-\frac{x^7}{7}+\dots$$

和左端进行对比，发现已经有了$1/n$。然后试着凑幂次。指数部分可以拎出一个$n$来作幂次， 但是三角函数不行。然而想到可以利用复变函数把三角函数化成指数，并且形式类似也可拎出一个$n$来。 这样，幂指数也解决了。

此时还差一个符号。在展开式中各项是正负交替的，原式则是全正。有没有什么办法把展开式中的负号 全变正呢？代$-x$试试，发现没用，因为都是奇次。注意到符号的周期其实是指数增长的4倍，不难想到 可以代$ix$凑。这次刚好------ $$\arctan{ix}=i\brack{x+\frac{x^3}{3}+\frac{x^5}{5}+\frac{x^7}{7}+\dots}$$

最后只需要将多出来的$i$除掉即可。于是可以开始按照展开式把它收回去。注意，一开始最好直接用 共轭消除法将$\sin$化为指数，而不要加一项$\cos$最后取虚部或实部。否则就会万分艰难，卡在$\mathrm{Re}(\arctan(sth))$上。 （论我为啥推了一个下午还没推出来） $$\begin{aligned}
  V(x,y)&=\frac{4V_0}{\pi}\sum_{i=1,3,...}^{\infty}\frac{1}{n}\exp{-n\pi x/a}\sin{\brack{\frac{n\pi y}{a}}}\\
        &=\frac{4V_0}{\pi}\frac{1}{2i}\brack{
          \sum_{i=1,3,...}^{\infty}\frac{1}{n}\exp{-n\pi x/a}\exp{n\pi iy/a}-\sum_{i=1,3,...}^{\infty}\frac{1}{n}\exp{-n\pi x/a}\exp{-n\pi iy/a}
          }\\
        &=-\frac{2iV_0}{\pi}\brack{
          \sum_{i=1,3,...}^{\infty}\frac{1}{n}\brack{\exp{\frac{\pi}{a}(iy-x)}}^n-\sum_{i=1,3,...}^{\infty}\frac{1}{n}\brack{\exp{\frac{\pi}{a}(-iy-x)}}^n}\\
  &=-\frac{2V_0}{\pi}\brack{\arctan{\brack{i\exp{\frac{\pi}{a}(iy-x)}}}-\arctan{\brack{i\exp{\frac{\pi}{a}(-iy-x)}}}}
\end{aligned}$$

此时可利用公式合并。这个其实就是和角公式的应用，可以手动推一下。 $$\begin{aligned}
  \arctan a - \arctan b&=\arctan (\tan (\arctan a - \arctan b))\\
                         &=\arctan \brack{\frac{a-b}{1+ab}}
\end{aligned}$$ 于是得到 $$\begin{aligned}
  V(x,y)&=-\frac{2V_0}{\pi}\arctan\brack{
          i\frac{\exp{\frac{\pi}{a}(iy-x)}-\exp{\frac{\pi}{a}(-iy-x)}}{1-\exp{\frac{\pi}{a}(iy-x)}\exp{\frac{\pi}{a}(-iy-x)}}}\\
  &=\frac{2V_0}{\pi}\arctan\brack{
    \frac{\exp{-\pi x/a}}{i}\frac{\exp{\frac{\pi}{a}iy}-\exp{-\frac{\pi}{a}iy}}{1-\exp{\frac{\pi}{a}(-2x)}}}\\
        &=\frac{2V_0}{\pi}\arctan\brack{\frac{1}{i}\frac{\exp{\frac{\pi}{a}iy}-\exp{-\frac{\pi}{a}iy}}{\exp{\frac{\pi}{a}x}-\exp{-\frac{\pi}{a}x}}}\\
  &=\frac{2V_0}{\pi}\arctan{\brack{\frac{\sin{\pi y/a}}{\sinh{\pi x/a}}}}
\end{aligned}$$

现在看看还是挺显然的嘿嘿嘿。不过我们能学到什么呢？

一是用分离变量法解出题目，得到级数解后，可以尝试着将其化简，利用其中的系数、指数特征，和已有的函数展开式进行对比，以获得可能的线索。 二是现有的展开式和得到的级数解有一些细微差别时，可以代诸如$-x$，$ix$来尝试消除差异。三是将三角函数化为指数函数时，最好使用共轭消去法， 避免引入$\mathrm{Re},\mathrm{Im}$函数造成推导困难。

感谢某孙学长2333
