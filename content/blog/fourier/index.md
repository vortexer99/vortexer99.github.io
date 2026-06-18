---
title: '借期末考题论傅里叶变换的顺序对解pde复杂性的影响'
date: 2019-01-18
url: /posts/2019/01/fourier/
tags:
  - Blogpost
  - Mathematic
  - Mathematical method of Physics
  - 1-5 Pages
types:
  - blogpost
topics:
  - mathematics
  - mathematical-methods-in-physics
lengths:
  - 1-5-pages
authors:
  - me
---

期末考试用傅里叶变换解题 ut-4uxx-u=0，结果解了半天没解出来，下来一看变一下傅里叶变换应用的顺序竟然快这么多？

# 期末考题

数学物理方法期末考试有一道题目如下。 $$\begin{align}
    &u_t-4u_{xx}-u=0\\
    &u(x,0)=\phi(x)=
      \left\{
      \begin{aligned}
        0,&~x\leq 0\\
        1,&~x>0
      \end{aligned}
      \right.
  \end{align}$$ 题目要求用傅里叶变换解。在考试解题中发现变换顺序不同导致复杂性有很大的区别。

# 换元法解

在用傅里叶变换解之前，首先先用简单的换元法解，作为参考。

和扩散方程相比，这一方程仅仅多了一项$u$的函数，可以通过类似积分因子的方法将其消去。 令$v(x,t)=u(x,t)\exp{-t}$，验证 $$v_t-4v_{xx}=u_t\exp{-t}-u\exp{-t}-4u_{xx}\exp{-t}=(u_t-4u_{xx}-u)\exp{-t}=0$$ 初始条件 $$v(x,0)=u(x,0)=\phi(x)$$

于是$v$满足最简单的齐次扩散方程初值问题，用poisson公式求解。其中$k=4$ $$v=\frac{1}{\sqrt{\pi}}\intr \exp{-z^2}\phi(x-\sqrt{4kt}z)\mathrm{d}z
  =\frac{1}{\sqrt{\pi}}\int_{-\infty}^{x/\sqrt{4kt}}\exp{-z^2}\mathrm{d}z$$ 结合误差函数，得到 $$v=\frac{1}{2}+\frac{1}{2} \mathrm{erf}
  \left(
    \frac{x}{\sqrt{4kt}}
  \right)$$ 代回得 $$u=\frac{1}{2}\exp{t}+\frac{1}{2}\exp{t} \mathrm{erf}
  \left(
    \frac{x}{4\sqrt{t}}
  \right)$$

# 傅里叶变换解1

然后我们来看Fourier变换的方法。设经过对$x$的傅里叶变换，函数$u(x,t)$变为$\hat{u}(\xi,t)$。

于是，经过傅里叶变换，方程变为

$$\hat{u}_t-4(\mathrm{i}\xi)^2\hat{u}-\hat{u}=0 ~\Rightarrow~ \hat{u}_t=(1-4\xi^2)\hat{u}$$ 按关于$t$的常微分方程类似做法，结合$\hat{u}(\xi,0)=\hat{\phi}(\xi)$，得到 $$\hat{u}=\hat{\phi}(\xi)\exp{(1-4\xi^2)t}$$

对其进行逆变换，得到 $$u=\mathit{F}^{-1}(\hat{\phi}(\xi)\exp{(1-4\xi^2)t})=\exp{t}\phi(x)*\mathit{F}^{-1}(\exp{-4\xi^2t})$$

计算变换 $$\mathit{F}^{-1}(\exp{-4\xi^2t})=\frac{1}{2\pi}\intr \exp{-4\xi^2t+\mathrm{i}\xi x}\mathrm{d}\xi
  =\frac{1}{4\pi\sqrt{t}}\intr \exp{-\xi^2+\frac{\mathrm{i}x}{2\sqrt{t}}\xi}\mathrm{d}\xi
  =\frac{1}{4\sqrt{\pi t}}\exp{-\frac{x^2}{16t}}$$

然后计算卷积 $$\phi(x)*\mathit{F}^{-1}(\exp{-4\xi^2t})=\frac{1}{4\sqrt{\pi t}}\intr\exp{-\frac{(x-y)^2}{16t}}\phi(y)\mathrm{d}y$$ 作变换$z=(x-y)/4\sqrt{t}$，上式变为 $$\frac{1}{\sqrt{\pi}}\intr e^{-z^2}\phi(x-4\sqrt{t}z)\mathrm{d}z=\frac{1}{\sqrt{\pi}}\int_{-\infty}^{x/4\sqrt{t}}\exp{-z^2}\mathrm{d}z
  =\frac{1}{2}+\frac{1}{2}\mathrm{erf}
  \left(
\frac{x}{4\sqrt{t}}
\right)$$ 最终得到 $$u=\frac{1}{2}\exp{t}+\frac{1}{2}\exp{t} \mathrm{erf}
  \left(
    \frac{x}{4\sqrt{t}}
  \right)$$

这是较为简单的傅里叶变换解题途径。

# 傅里叶变换解2

但是如果先定出变换后的系数函数，再逆变换回来，事情就变得非常棘手。

从解出 $$\hat{u}=\hat{\phi}(\xi)\exp{(1-4\xi^2)t}$$ 开始，先计算 $$\hat{\phi}(\xi)=\intr \phi(x)\exp{-\mathrm{i}x\xi}\mathrm{d}x
  =\int_0^{+\infty}\exp{-\mathrm{i}x\xi}\mathrm{d}x
  =\frac{1}{-\mathrm{i}\xi}\exp{-\mathrm{i}x\xi}|^{\infty}_0=\frac{1}{\mathrm{i}\xi}$$ 在做这个积分的时候其实心里是犯嘀咕的，因为无穷代进去它并没有一个固定的值，虚指数如此积分也有待商榷。 不过，可以来验证一下。这个$\phi(x)$其实是Heavyside函数，在广义函数意义下它的导数为$\delta$函数。 而$\delta$函数的傅里叶变换是确凿无疑的。结合$\delta$函数的性质，有 $$\mathit{F}(\delta)=\intr \delta(x)\exp{-\mathrm{i}x\xi}\mathrm{d}x=1$$

然后我们考虑傅里叶变化的导数性质。 $$\mathit{F}(\delta)=\mathit{F}(\phi')=\mathrm{i}\xi \mathit{F}(\phi)=1$$ 于是 $$\mathit{F}(\phi)=\frac{1}{\mathrm{i}\xi}$$ 验证确实如此。所以认为这变换是正确的。

接着，得到变换解为$\hat{u}=\frac{1}{\mathrm{i}\xi}\exp{(1-4\xi^2)t}$，要将其逆变换回去。提出$\exp{t}$，计算式为 $$u=\frac{\exp{t}}{2\pi}\intr \frac{1}{\mathrm{i}\xi}\exp{-4\xi^2t}\exp{\mathrm{i}x\xi}\mathrm{d}\xi$$ 这个式子看着实在头疼，光是$1/\xi$项就很难处理。不过经过考试时孜孜不倦地研究，还是给做了出来。

首先将$\exp{\mathrm{i}x\xi}$展开成正余弦形式$\cos{x\xi}+\mathrm{i}\sin{x\xi}$，并利用函数的奇偶性进行化简。

$1/\mathrm{i}\xi$为奇函数，$\exp{-4\xi^2t}$为偶函数，因此对于偶函数$\cos$项，整个函数为奇函数，在$\mathbb{R}$上积分为零。 于是最后只剩下 $$\label{lab}
  u=\frac{\exp{t}}{\pi}\int_0^{+\infty}\frac{1}{\xi}\exp{-4\xi^2t}\sin{x\xi}\mathrm{d}\xi$$

为了消除恼人的$\xi^{-1}$项，可以对$x$求偏导，使得$\sin{x\xi}$项抛一个$\xi$出来消去分数。 $$u_x=\frac{\exp{t}}{\pi}\int_0^{+\infty}\exp{-4\xi^2t}\cos{x\xi}\mathrm{d}\xi$$ 为了简便计算这个积分，再次引入$\mathrm{i}\sin{x\xi}$项，将其化为指数函数。最后积分完后取其实部即可。 $$u_x=\frac{\exp{t}}{\pi} \mathrm{Re}
  \left(
    \int_0^{+\infty}\exp{-4\xi^2t+\mathrm{i}\xi x}\mathrm{d}\xi
  \right)$$ 对$\xi$缩放使得内部积分变为 $$\frac{1}{2\sqrt{t}}\int_0^{+\infty}\exp{-\xi^2+\mathrm{i}\frac{x}{2\sqrt{t}}\xi}\mathrm{d}\xi
  = \frac{1}{2\sqrt{t}}\int_0^{+\infty}\exp{-(\xi-\frac{\mathrm{i}x}{4\sqrt{t}})^2-\frac{x^2}{16t}}\mathrm{d}\xi
  = \frac{1}{2\sqrt{t}}\exp{-\frac{x^2}{16t}}\int_{-\mathrm{i}x/4\sqrt{t}}^{+\infty}\exp{-\xi^2}\mathrm{d}\xi$$ 最后一个积分可分为两项 $$\int_{-\mathrm{i}x/4\sqrt{t}}^{+\infty}\exp{-\xi^2}\mathrm{d}\xi=\frac{\sqrt{\pi}}{2}+\int_{-\mathrm{i}x/4\sqrt{t}}^{0}\exp{-\xi^2}\mathrm{d}\xi
  =\frac{\sqrt{\pi}}{2}+\int_0^{\mathrm{i}x/4\sqrt{t}}\exp{-\xi^2}\mathrm{d}\xi$$ 设$z=\xi/\mathrm{i}$，则可验证最后一项为虚数。 $$\int_0^{\mathrm{i}x/4\sqrt{t}}\exp{-\xi^2}\mathrm{d}\xi
  =\int_0^{x/4\sqrt{t}}\exp{-(\mathrm{i}z)^2}\mathrm{i}\mathrm{d}z
  =\mathrm{i}\int_0^{x/4\sqrt{t}}\exp{-z^2}\mathrm{d}z$$ 于是在取实部时，这一项就会消失。最后得到 $$u_x=\frac{\exp{t}}{\pi}\frac{1}{2\sqrt{t}}\exp{-x^2/16t}\frac{\sqrt{\pi}}{2}=\frac{\exp{t}}{4\sqrt{\pi t}}\exp{-x^2/16t}$$ 对$x$积分，注意到$1/4\sqrt{t}$可以用来代换。 $$u=\frac{\exp{t}}{2} \mathrm{erf}
  \left(
    \frac{x}{4\sqrt{t}}
  \right)+f(t)$$

设误差函数为$v$，利用原方程和误差函数的性质 $$u_t-4u_{xx}-u=0 \qquad v_t-4v_{xx}=0$$ 得到 $$f(t)=f'(t)~\Rightarrow~f(t)=C\exp{t}$$

然后要通过初始条件确定$C$。注意到扩散方程的$t>0$， 将初始条件的$t=0$改为$t\rightarrow 0^+$，则可知当$x>0$时，$x/4\sqrt{t}$趋向于正无穷，$v\rightarrow 1$。 当$x<0$时，变量趋于负无穷，$v\rightarrow -1$。于是 $$u(x,0)=
  \left\{
    \begin{aligned}
      & -1/2+C,&x<0\\
      & 1/2+C,&x>0\\
    \end{aligned}
  \right. ~=\phi(x)$$ 显然$C=1/2$，于是 $$u=\frac{1}{2}\exp{t} \mathrm{erf}
  \left(
    \frac{x}{4\sqrt{t}}
  \right)+\frac{1}{2}\exp{t}$$

可见，相比前一种傅里叶变换做法，这里先将变换函数$\hat{u}$完全确定后再反变换回来非常棘手， 而且还在一些地方需要做玄学的考量。

## 匪夷所思的事情

以下均是针对第二种傅里叶变换而言。

按照最后求解常数$C$的结果，原题的初始条件应修改为 $$u(x,0)=\phi(x)=
      \left\{
      \begin{aligned}
        0,&~x< 0\\
        \frac{1}{2},&~x=0\\
        1,&~x>0
      \end{aligned}
      \right.$$ 因为当$x=0$时应当有$v=0$。

另外，在求导消去$\xi^{-1}$时，即对`\autoref{lab}`{=latex}而言， 可以用积分式代替求导，即令 $$\frac{\sin{x\xi}}{\xi}=\int_{-\infty}^x\cos{\tau\xi}\mathrm{d}\tau$$ 然后通过交换积分次序进行类似的下一步操作。这样在最后可以通过积分直接得出$\exp{t}/2$项而不用大费周章地去待定系数。 但是，匪夷所思的事情是这里的积分下限居然是$-\infty$而不是零，否则最后$\exp{t}/2$这一项就会**消失**。
