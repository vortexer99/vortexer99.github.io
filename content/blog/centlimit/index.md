---
title: '随机序列的收敛性和中心极限定理'
date: 2018-11-05
url: /posts/2018/11/centlimit
tags:
  - Blogpost
  - Mathematic
  - 6-10 Pages
types:
  - blogpost
topics:
  - mathematics
lengths:
  - 6-10-pages
authors:
  - me
---

2018.11.5，2018.11.7 庄逸在李启寨概统课及课下整理扩充。

随机序列的收敛性和中心极限定理

（2018.11.5，2018.11.7庄逸在李启寨概统课及课下整理扩充）

随机序列的收敛性

·几乎必然收敛、依概率收敛和依分布收敛

> $$X_{1},X_{2},\ldots 几乎必然收敛于X \Leftrightarrow \lim_{n \rightarrow \infty}{P\left( X_{n} = X \right)} = 1，记为X_{n}\overset{a.s.}{\rightarrow}X$$
>
> $$X_{1},X_{2},\ldots 依概率收敛于X \Leftrightarrow \forall\varepsilon > 0,\lim_{n \rightarrow \infty}{P\left( \left| X_{n} - X \right| > \varepsilon \right)} = 0，记为X_{n}\overset{P}{\rightarrow}X$$
>
> $$X_{1},X_{2},\ldots 依分布收敛于X \Leftrightarrow 对分布函数F(X)的任何连续点x均成立$$
>
> $$\lim_{n \rightarrow \infty\ }{P\left( X_{n} \leq x \right) = P(X \leq x)}，记为X_{n}\overset{d}{\rightarrow}X$$
>
> $$X_{n} = X + \frac{1}{n}依概率收敛于X但不几乎必然收敛于X$$
>
> （条件不足，在假定四阶矩存在的情况下则几乎必然收敛）
>
> 几乎必然收敛和依概率收敛的差别在于**相差的概率为零**和**分布完全相同**不一样
>
> 考虑连续区间上的分布挖去一个点（甚至有限个点）。
>
> 更精细的考察推荐广泛查阅资料和例子（如维基等）。勿全信此处（因为我自己也还弄不太清楚）
>
> 推荐[一篇博客](http://www.algorithmdog.com/%E5%87%A0%E4%B9%8E%E5%BF%85%E7%84%B6%E6%94%B6%E6%95%9B%E5%92%8C%E4%BE%9D%E6%A6%82%E7%8E%87%E6%94%B6%E6%95%9B)

·三种收敛的强弱和性质

> $$X_{n}\overset{a.s.}{\rightarrow}X \Rightarrow X_{n}\overset{P}{\rightarrow}X \Rightarrow X_{n}\overset{d}{\rightarrow}X$$
>
> 几乎必然收敛最强，依概率收敛齐次，依分布收敛最弱
>
> $$X_{n}\overset{d}{\rightarrow}X,Y_{n}\overset{P}{\rightarrow}0\ 则X_{n} + Y_{n}\overset{d}{\rightarrow}X$$
>
> $$X_{n}\overset{d}{\rightarrow}X,Y_{n}\overset{P}{\rightarrow}C\ 则X_{n}Y_{n}\overset{d}{\rightarrow}CX$$

·平均收敛

> $$X_{1},X_{2},\ldots\ r次平均收敛于X \Leftrightarrow \lim_{n \rightarrow \infty}{E\left| X_{n} - X \right|^{r}} = 0$$
>
> $$r = 2也称均方收敛$$

·马尔科夫不等式

> $$若X只取非负值的随机变量，则对\forall\varepsilon > 0,P(X \geq \varepsilon) \leq \frac{EX}{\varepsilon}$$
>
> $$证明：EX - \varepsilon P(X \geq \varepsilon) = \int_{0}^{\infty}{xf(x)dx} - \int_{\varepsilon}^{\infty}{\varepsilon f(x)dx} = \int_{\varepsilon}^{\infty}{(x - \varepsilon)f(x)dx} + \int_{0}^{\varepsilon}{xf(x)dx}$$
>
> $$两项均不小于零，因此\ EX - \varepsilon P(X \geq \varepsilon) \geq 0$$

·切比雪夫不等式

> $$设随机变量X的方差存在，则\forall\varepsilon > 0,P\left( |X - EX| \geq \varepsilon \right) \leq \frac{DX}{\varepsilon^{2}}$$
>
> $$证明：利用马尔科夫不等式，$$
>
> $$P\left( |X - EX| \geq \varepsilon \right) = P\left( (X - EX)^{2} \geq \varepsilon^{2} \right) \leq \frac{E(X - EX)^{2}}{\varepsilon^{2}} = \frac{DX}{\varepsilon^{2}}$$

·切比雪夫弱大数律

> $$设X_{1},X_{2},\ldots 是相互独立的随机变量序列，EX_{i} = \mu_{i}$$
>
> $$E\left( X_{i} - \mu_{i} \right)^{2} = \sigma_{i}^{2}(i \geq 1)且\left\{ \sigma_{i}^{2},i \geq 1 \right\} 有界，S_{n} = \sum_{i = 1}^{n}X_{i}(n \geq 1)$$
>
> $$则当n \rightarrow \infty 时，\frac{S_{n} - ES_{n}}{n}\overset{P}{\rightarrow}0$$
>
> 用切比雪夫不等式证明
>
> $$D\left( \frac{S_{n}}{n} \right) = \frac{1}{n^{2}}\sum_{i = 1}^{n}\sigma_{i}^{2} \in \left\lbrack \frac{\sigma_{m}^{2}}{n},\frac{\sigma_{M}^{2}}{n} \right\rbrack$$
>
> $$P\left( \left| \frac{S_{n} - ES_{n}}{n} \right| \geq \varepsilon \right) = P\left( \left| \frac{S_{n}}{n} - E\left( \frac{S_{n}}{n} \right) \right| \geq \varepsilon \right) \leq \frac{D\left( \frac{S_{n}}{n} \right)}{\varepsilon^{2}} \leq \frac{\sigma_{M}^{2}}{n\varepsilon^{2}} \rightarrow 0,当n \rightarrow \infty$$

关于定理的意义

> 条件：方差均有限
>
> $$\frac{S_{n} - ES_{n}}{n} = \frac{S_{n}}{n} - E\left( \frac{S_{n}}{n} \right) ≔ \overline{X} - E\overline{X} = \frac{\sum_{k = 1}^{n}\left( X_{k} - EX_{k} \right)}{n} = \sum_{k = 1}^{n}\left( \frac{X_{k}}{n} - E\left( \frac{X_{k}}{n} \right) \right)$$
>
> $$注意此处\frac{S_{n}}{n},\overline{X},\frac{X_{k}}{n}等均为随机变量，E\overline{X} \neq \frac{1}{n}\sum_{i = 1}^{n}X_{i}，而应该是一个数。$$
>
> $$\frac{S_{n} - ES_{n}}{n}\overset{P}{\rightarrow}0 \Leftrightarrow \overline{X} - E\overline{X}\overset{P}{\rightarrow}0 \Leftrightarrow \forall\varepsilon > 0,\lim_{n \rightarrow \infty}{P\left( \left| \overline{X} - E\overline{X} \right| > \varepsilon \right)} = 0$$
>
> 大数定律是（随机变量序列的算术平均值）向（随机变量各数学期望的算术平均值）收敛的定律。

推论

> $$设X_{n}是一列独立同分布(i.i.d)的随机变量序列，具有公共的数学期望\mu 和方差\sigma^{2},$$
>
> $$S_{n} = \sum_{i = 1}^{n}X_{i}(n \geq 1)，则\frac{S_{n}}{n}\overset{P}{\rightarrow}\mu\ (n \rightarrow \infty)$$
>
> $$证明：\frac{S_{n} - ES_{n}}{n} = \frac{S_{n}}{n} - \frac{1}{n}ES_{n} = \frac{S_{n}}{n} - \frac{1}{n} \cdot n\mu = \frac{S_{n}}{n} - \mu$$
>
> $$\frac{S_{n}}{n} - \mu\overset{P}{\rightarrow}0 \Rightarrow \frac{S_{n}}{n}\overset{P}{\rightarrow}\mu$$

贝努力大数律

> $$设单次试验中事件A发生的概率为p，$$
>
> $$在n( \geq 2)次独立试验中A发生了X_{n}次，则\frac{X_{n}}{n}\overset{P}{\rightarrow}p\ \ \ (n \rightarrow \infty)$$

Cantelli强大数律

> $$设X_{1},X_{2},\ldots 是相互独立的随机变量序列，EX_{i} = \mu_{i}$$
>
> $$E\left( X_{i} - \mu_{i} \right)^{4}均有限，S_{n} = \sum_{i = 1}^{n}X_{i}(n \geq 1)$$
>
> $$则当n \rightarrow \infty 时，\frac{S_{n} - ES_{n}}{n}\overset{a.s.}{\rightarrow}0$$
>
> 老师注：一般而言$E(X^{4})$存在的话低阶的也都存在，也就是说$E(X^{4})$存在的话四阶中心矩就存在。

推论

> $$设X_{n}是一列独立同分布(i.i.d)的随机变量序列$$
>
> $$\mu = EX_{i}和{EX}_{i}^{4}存在，S_{n} = \sum_{i = 1}^{n}X_{i}(n \geq 1)，则$$
>
> $$\frac{S_{n}}{n}\overset{a.s.}{\rightarrow}\mu\ (n \rightarrow \infty)$$

Borel强大数律

> $$设单次试验中事件A发生的概率为p，在n( \geq 2)次独立试验中$$
>
> $$A发生了X_{n}次，则\frac{X_{n}}{n}\overset{a.s.}{\rightarrow}p\ \ \ (n \rightarrow \infty)$$

中心极限定理

棣莫弗-拉普拉斯中心极限定理

$$设X_{1},X_{2},\ldots,X_{n}相互独立并且具有相同的分布，$$

$$P\left( X_{1} = 1 \right) = 1 - P(X = 0) = p,0 < p < 1，则有$$

$$\frac{X_{1} + X_{2} + \ldots + X_{n} - np}{\sqrt{np(1 - p)}}\overset{d}{\rightarrow}N(0,1)$$

二项分布经过标准化（减去均值，除以标准差）后分布可用标准正态分布估计。

$$即\lim_{n \rightarrow \infty}{P\left( \frac{X_{1} + X_{2} + \ldots + X_{n} - np}{\sqrt{np(1 - p)}} \leq x \right)} = \Phi(x),\forall x\mathbb{\in R}$$

棣莫弗-拉普拉斯中心极限定理是历史上最早的中心极限定理，它告诉我们可以用正态分布来近似二项分布。

林德伯格-莱维中心极限定理

$$设X_{1},X_{2},\ldots,X_{n}为i.i.d的随机变量序列，具有公共的数学期望\mu 和方差\sigma^{2}$$

$$\frac{1}{\sqrt{n\sigma^{2}}}\left( X_{1} + X_{2} + \ldots + X_{n} - n\mu \right)\overset{d}{\rightarrow}N(0,1)$$

$$即\forall x\mathbb{\in R,}有\lim_{n \rightarrow \infty}{F_{n}(x)} = \Phi(x)$$

$$其中F_{n}(x)为\frac{1}{\sqrt{n\sigma^{2}}}\left( X_{1} + X_{2} + \ldots + X_{n} - n\mu \right)的概率分布函数$$

$$\Phi(x)为标准正态分布N(0,1)的概率分布函数$$

波动是有规律的。

二项分布的估计方法

$$设X_{1},X_{2},\ldots,X_{n}\ i.i.d服从0 - 1分布，成功的概率为p$$

$$则X = X_{1} + X_{2}\ldots + X_{n}\sim B(n,p)，由中心极限定理$$

$$\frac{X_{1} + X_{2} + \ldots + X_{n} - np}{\sqrt{np(1 - p)}}\overset{d}{\rightarrow}N(0,1)$$

$$对任意两个正整数t_{1} < t_{2}$$

$$P\left( t_{1} \leq X \leq t_{2} \right) = P\left( \frac{t_{1} - np}{\sqrt{np(1 - p)}} \leq \frac{X - np}{\sqrt{np(1 - p)}} \leq \frac{t_{2} - np}{\sqrt{np(1 - p)}} \right)$$

$$\approx \Phi\left( \frac{t_{2} - np}{\sqrt{np(1 - p)}} \right) - \Phi\left( \frac{t_{1} - np}{\sqrt{np(1 - p)}} \right)\ \ \ \ \ \ \ \ \ \ \ \because\frac{X - np}{\sqrt{np(1 - p)}}\sim N(0,1)$$

为了提高估计的精度，修正上式为

$$\Phi\left( \frac{t_{2} - 0.5 - np}{\sqrt{np(1 - p)}} \right) - \Phi\left( \frac{t_{1} - 0.5 - np}{\sqrt{np(1 - p)}} \right)$$

例：设一个考生参加100道题的英语标准化考试，每道题均为4个备选答案的选择题，且只有一个答案是正确的。每道题他都随机选择一个答案，假设评分标准为：选对得1分，选错和不选得0分。问该考生最终得分大于等于25的概率。

$$P\left( X_{1} + \ldots + X_{100} \geq 25 \right) = P\left( \frac{\frac{1}{100}\sum_{i = 1}^{100}{X_{i} - 0.25}}{\sqrt{0.25(1 - 0.25)\text{/}100}} \geq 0 \right) = 1 - \Phi(0) = \frac{1}{2}$$

注：此时如果用-0.5的修正会造成较大误差，问题在于标准正态分布0附近变化剧烈。

注：其实应该算$P\left( 25 \leq + \ldots + X_{100} \leq 100 \right)$，但是100算比较大了，其概率上面直接当成1。精确计算可得到其概率为0.（约200个9）503......

注：用二项分布计算得到

$$\sum_{i = 25}^{100}C_{100}^{i}\left( \frac{1}{4} \right)^{i}\left( \frac{3}{4} \right)^{100 - i} \approx 0.53832886791858856826$$
