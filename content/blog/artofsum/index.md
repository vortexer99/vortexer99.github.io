---
title: '∑の艺术'
date: 2018-05-22
url: /posts/2018/05/artofsum/
tags:
  - Blogpost
  - Mathematic
  - Combinatorics
  - 31-100 Pages
types:
  - blogpost
topics:
  - mathematics
  - combinatorics
lengths:
  - 31-100-pages
authors:
  - me
---

关于求和记号Σ的基本定义，性质的（比较严格的）展开讨论。

是在我自己写的东西里面非常喜欢的一篇，把基础定义写明白了，各种定理就会自己往上发展出来。这一篇后来想用更严格的方式重新写一遍，但是可惜后来没有动笔。在那一套体系下，Σ被定义为一个集合M，一个从集合M到群G的函数和群G上的某一种运算的三元组到一个数的映射。

# 目录 {#目录 .TOC-Heading}

[1.1 默认约定 [3](#_Toc507114563)](#_Toc507114563)

[1.2 换元定理 [5](#_Toc507114564)](#_Toc507114564)

[1.3 合并定理 [9](#_Toc507114565)](#_Toc507114565)

[1.4 嵌套交换定理 [11](#_Toc507114566)](#_Toc507114566)

[1.5 合并、换元II [17](#_Toc507114567)](#_Toc507114567)

[1.6 线性合并定理 [21](#_Toc507114568)](#_Toc507114568)

[1.7 函数穿透定理 [23](#_Toc507114569)](#_Toc507114569)

[2.1 多重求和形式 [28](#_Toc507114570)](#_Toc507114570)

[2.2 条件求和形式 [30](#_Toc507114571)](#_Toc507114571)

[2.3 任意步长求和形式 [36](#_Toc507114572)](#_Toc507114572)

[2.4 不等求和形式 [41](#_Toc507114573)](#_Toc507114573)

[2.5 任选求和形式 [48](#_Toc507114574)](#_Toc507114574)

[2.6 置换轮换对称求和形式 [54](#_Toc507114575)](#_Toc507114575)

[3 多项式 [57](#_Toc507114576)](#_Toc507114576)

[4.1 阿贝尔分部求和定理 [60](#_Toc507114577)](#_Toc507114577)

[4.2 定义计算积分 [62](#_Toc507114578)](#_Toc507114578)

[5.1 一排原子转动惯量 [67](#_Toc507114579)](#_Toc507114579)

[5.2 平行轴、垂直轴定理 [71](#_Toc507114580)](#_Toc507114580)

[5.3 正余弦等差求和 [74](#_Toc507114581)](#_Toc507114581)

[5.4 1234567×7654321 [76](#_Toc507114582)](#_Toc507114582)

[5.5 正整数方幂和 [79](#_Toc507114583)](#_Toc507114583)

[附录一 阶乘与斯特林数 [88](#_Toc507114584)](#_Toc507114584)

[]{#_Toc507114563 .anchor}1.1 默认约定

一些符号说明：

在本专题（∑の艺术）中，

所有表示优先级运算顺序的括号

均用小括号表示；

函数自变量用中括号限定；

$≔$表示左边的记号由右边定义；

$= :$同理；

如不加特殊说明，所有出现的$n \in N^{*}$;

对$b - a \in \mathbf{N}$，定义$\mathbf{Z}\lbrack a,b\rbrack$为$\{ a,a + 1,...,b\}$,

特别地，当$a = b$时规定$\mathbf{Z}\lbrack a,b\rbrack ≔ \{ a\}$;

n维向量 $\mathbf{k} ≔ \left( k_{1},k_{2},\ldots,k_{n} \right)$

当对$\forall t \in \mathbf{Z}\lbrack 1,n\rbrack$，有$b_{t} - a_{t} \in \mathbf{N}$时，

定义$\mathbf{Z}\left\lbrack \mathbf{a},\mathbf{b} \right\rbrack = \left\{ \mathbf{k} \middle| k_{t} \in \mathbf{Z}\left\lbrack a_{t},b_{t} \right\rbrack,t \in \mathbf{Z}\lbrack 1,n\rbrack \right\}$

标准形式的求和运算如下定义：

**[定义1.1.1]{.underline}** 标准求和形式

$$\sum_{k = a}^{b}{f\lbrack k\rbrack} ≔ f\lbrack a\rbrack + f\lbrack a + 1\rbrack + \ldots + f\lbrack b\rbrack$$

其中$b - a \in \mathbf{N},\ a,b$不能由$k_{1}$定义;

$f\lbrack x\rbrack$任意选取但必须使每一项有意义.

类似地，如下定义标准型求积运算：

**[定义1.1.2]{.underline}** 标准求积形式

$$\prod_{k = a}^{b}{f\lbrack k\rbrack ≔ f\lbrack a\rbrack f\lbrack a + 1\rbrack\ldots f\lbrack b\rbrack}$$

其中 $b - a \in \mathbf{N},\ a,b$不能由$k_{1}$定义;

$f\lbrack x\rbrack$任意选取但必须使每一项有意义.

解释说明：

1.  $b - a \in \mathbf{N}$表示$b > a$且相差某个整数,

注意$a,b$可以同时不为正整数.

2.  在满足条件的情况下，$a,b$可任意选取，

但不可与$k_{1}$相关，因为在求和之前不存在$k_{1}$,

而$a,b$必须给定。

3.  $a,b$虽然不能和$k_{1}$相关，

但是可以是外部参数的函数.

因此，$a,b$仍然是可变的。

[]{#_Toc507114564 .anchor}1.2 换元定理

我们想通过换元对被求和式做一些简化，

找个函数$g$令$g\left\lbrack k_{1} \right\rbrack = k_{2}$ ($k_{2}$是还未使用过的变量)

但是$g$的选取并不是任意的，一个简单的例子是

$$\sum_{k_{1} = 1}^{4}\sqrt{k_{1}} \neq \sum_{k_{1} = 1}^{2}\sqrt{{k_{1}}^{2}} = \sum_{k_{1} = 1}^{2}k_{1}$$

究其原因是求和时候少了几项。

因此条件一是$k_{1}每自增1，k_{2}也相应增加1或减少1.$

同时$g$的选取当然得使求和有意义，

对于同增的情况，我们有以下定理：

**[定理1.2.1]{.underline}** 基础换元定理

设函数$g$满足以下条件：

1°$\forall x,y \in \mathbf{Z}\lbrack a,b\rbrack,g\lbrack x\rbrack - g\lbrack y\rbrack = x - y$

2°$对t \in \mathbf{Z}\lbrack a,b\rbrack,g^{- 1}\lbrack t\rbrack \in \left\{ x \middle| f\lbrack x\rbrack 有意义 \right\}$

则有$g\lbrack x\rbrack = x + m,m \in R,x \in \mathbf{Z}\lbrack a,b\rbrack$,且

$$\sum_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack} = \sum_{k_{2} = g\lbrack a\rbrack}^{g\lbrack b\rbrack}{f\left\lbrack g^{- 1}\left\lbrack k_{2} \right\rbrack \right\rbrack} = \sum_{k_{2} = a + m}^{b + m}{f\left\lbrack k_{2} - m \right\rbrack}$$

证明：

$$\forall x \in \mathbf{Z}\lbrack a,b\rbrack,g\lbrack x\rbrack - g\lbrack a\rbrack = x - a.$$

$$取m = g\lbrack a\rbrack - a,则g\lbrack x\rbrack = x + m$$

$$\therefore 右边 = f\lbrack a + m - m\rbrack + f\lbrack a + m + 1 - m\rbrack + \ldots + f\lbrack b + m - m\rbrack$$

$$= f\lbrack a\rbrack + f\lbrack a + 1\rbrack + \ldots + f\lbrack b\rbrack = 左边$$

**[推论1.2.2]{.underline}** 改名定理

取$g\lbrack x\rbrack = x$,得到

$$\sum_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack} = \sum_{k_{2} = a}^{b}{f\left\lbrack k_{2} \right\rbrack}$$

这表明可以直接用另一字母代替全部的$k_{1}$

其实这是不证自明的，因为

$k_{1}$是在求和运算中才有意义的局部变量

$k_{1}$是在求和运算中才有意义的局部变量

$k_{1}$是在求和运算中才有意义的局部变量

\*牢记这一点，后面很多地方会很好理解。

既然在求和之前局部变量是没有定义的，

那么定义的时候取什么字母都是没有本质区别的，

只要求和式中统一用这个变量字母就行。

推论1.2.3

联合利用1.2.1,1.2.2，得到

$$\sum_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack} = \sum_{k_{1} = a + t}^{b + t}{f\left\lbrack k_{1} - t \right\rbrack} ≔ \sum_{k_{1} = a + t}^{b + t}{h\left\lbrack k_{1} \right\rbrack}$$

这个操作相当于"$k_{1}用k_{1} - t代掉$"，

而且被当做基本操作在各类解答中广泛使用,

初学者感到一下转不过弯来往往是在这里。

例1.2.4

$$现在你面前有\sum_{k_{1} = 26}^{57}\frac{\left( k_{1} + 3 \right)\left( k_{1} - 8 \right)}{\left( k_{1} - 14 \right)\left( k_{1} + 2 \right)}$$

而你出于某种需要想把$\left( k_{1} - 8 \right)$变成$k_{1}$,

请试着找到一种最对你口味的思维方式。

这里给出两种确定求和上下界的方式：

1°用$k_{1} + 8$代，$k_{1} + 8 = 26$,下面变成$k_{1} = 18$

上面$k_{1} + 8 = 57$,于是写个$49$上去。

2°因为换元前后第一项实际上相同，

将$26$代入$k_{1} - 8$,得到$18$，于是下面变成$18$;

同理$57$代入$k_{1} - 8 = 49$

这样就有一种备用方法来验证。

最后写一下答案：

$$\sum_{k_{1} = 26}^{57}\frac{(k_{1} + 3)(k_{1} - 8)}{(k_{1} - 14)(k_{1} + 2)} = \sum_{k_{1} = 18}^{49}\frac{(k_{1} + 11)k_{1}}{(k_{1} - 6)(k_{1} + 10)}$$

对于减一的情况，类似有

$$\forall x \in \{ a,a + 1,\ldots,b\},g\lbrack x\rbrack - g\lbrack y\rbrack = y - x$$

$$用常数a代入y,有g\lbrack x\rbrack - g\lbrack a\rbrack = a - x$$

$$设m = a + g\lbrack a\rbrack,则g\lbrack x\rbrack = - x + m，于是有$$

**[定理1.2.5]{.underline}** 逆序求和定理

$$设函数g\lbrack x\rbrack = - x + m满足：$$

$$对t \in \mathbf{Z}\lbrack a,b\rbrack,g^{- 1}\lbrack t\rbrack \in \{ x|f\lbrack x\rbrack 有意义\}$$

$$\sum_{k_{1} = a}^{b}{f\lbrack k_{1}\rbrack} = \sum_{k_{2} = g\lbrack b\rbrack}^{g\lbrack a\rbrack}{f\lbrack g^{- 1}\lbrack k_{2}\rbrack\rbrack} = \sum_{k_{2} = m - b}^{m - a}{f\lbrack m - k_{2}\rbrack}$$

证明略。注意因为此时$g\lbrack a\rbrack > g\lbrack b\rbrack$上下界交换$。$

[]{#_Toc507114565 .anchor}1.3 合并定理

**[定理1.3.1]{.underline}** 前后合并定理

$$\sum_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack} + \sum_{k_{1} = b + 1}^{c}{f\lbrack k_{1}\rbrack} = \sum_{k_{1} = a}^{c}{f\left\lbrack k_{1} \right\rbrack}$$

证明：利用加法结合律即可。

**[推论1.3.2]{.underline}** 裂一项定理

实际操作时，往往使用以下几个式子：

$$\sum_{k_{1} = a}^{b}{f\lbrack k_{1}\rbrack} = \sum_{k_{1} = a}^{b - 1}{f\left\lbrack k_{1} + 1 \right\rbrack + f\lbrack a\rbrack\ \ \ \ \ (b > a)}$$

$$\sum_{k_{1} = a}^{b}{f\lbrack k_{1}\rbrack} = \sum_{k_{1} = a + 1}^{b}{f\left\lbrack k_{1} - 1 \right\rbrack + f\lbrack b\rbrack\ \ \ \ \ (b > a)}$$

$$\sum_{k_{1} = a}^{b}{f\lbrack k_{1}\rbrack} = \sum_{k_{1} = a}^{b + 1}{f\left\lbrack k_{1} - 1 \right\rbrack - f\lbrack a - 1\rbrack\ }$$

$$\sum_{k_{1} = a}^{b}{f\lbrack k_{1}\rbrack} = \sum_{k_{1} = a - 1}^{b}{f\left\lbrack k_{1} + 1 \right\rbrack - f\lbrack b + 1\rbrack\ }$$

证明：只需要补出中间的一步

$$\sum_{k_{1} = a}^{b}{f\lbrack k_{1}\rbrack} = \sum_{k_{1} = a + 1}^{b}{f\left\lbrack k_{1} \right\rbrack + f\lbrack a\rbrack}$$

利用换元定理，得到

$$\sum_{k_{1} = a + 1}^{b}{f\left\lbrack k_{1} \right\rbrack + f\lbrack a\rbrack} = \sum_{k_{1} = a}^{b - 1}{f\left\lbrack k_{1} + 1 \right\rbrack + f\lbrack a\rbrack}$$

其他几个式子类似。

**[定理1.3.3]{.underline}** 相间合并定理

$$\sum_{k_{1} = a}^{b}{f\left\lbrack 2k_{1} \right\rbrack} + \sum_{k_{1} = a}^{b}{f\left\lbrack 2k_{1} + 1 \right\rbrack} = \sum_{k_{1} = 2a}^{2b + 1}{f\left\lbrack k_{1} \right\rbrack}$$

证明：全写出来，不证自明:)

**[推论1.3.4]{.underline}** 多项相间合并定理

$$\sum_{k_{2} = 0}^{n - 1}{\left( \sum_{k_{1} = a}^{b}{f\left\lbrack nk_{1} + k_{2} \right\rbrack} \right) = \sum_{k_{1} = na}^{nb + n - 1}{f\lbrack k_{1}\rbrack}}$$

之后将给出1.3.4的详细证明。

注意到1.3.4中出现了$n$倍的$k_{1}$,由此可以

进一步拓展换元定理。但是，为了推得它，我们还需要构建另一基本定理------嵌套交换定理。

[]{#_Toc507114566 .anchor}1.4 嵌套交换定理

**[引理1.4.1]{.underline}** 系数穿透定理

$$对\forall\lambda \in \mathbf{R}，\lambda\sum_{k_{1} = a}^{b}{f\lbrack k_{1}\rbrack} = \sum_{k_{1} = a}^{b}{\lambda f\lbrack k_{1}\rbrack}$$

证明：归纳乘法对加法的分配律即可。

**[定理1.4.2]{.underline}** 乘法嵌套交换定理I

$$\left( \sum_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack} \right)\left( \sum_{k_{2} = c}^{d}{g\left\lbrack k_{2} \right\rbrack} \right)$$

$$= \sum_{k_{2} = c}^{d}\left( \left( \sum_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack} \right)g\left\lbrack k_{2} \right\rbrack \right) = \sum_{k_{1} = a}^{b}\left( \left( \sum_{k_{2} = c}^{d}{g\left\lbrack k_{2} \right\rbrack} \right)f\left\lbrack k_{1} \right\rbrack \right)$$

$$= \sum_{k_{2} = c}^{d}\left( \sum_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack}g\left\lbrack k_{2} \right\rbrack \right) = \sum_{k_{1} = a}^{b}\left( \sum_{k_{2} = c}^{d}{g\left\lbrack k_{2} \right\rbrack}f\left\lbrack k_{1} \right\rbrack \right)$$

$$证明：利用1\text{.4.1}，将\sum_{k_{1} = a}^{b}{f\lbrack k_{1}\rbrack 视为\lambda},得到$$

$$(\sum_{k_{1} = a}^{b}{f\lbrack k_{1}\rbrack})(\sum_{k_{2} = c}^{d}{g\lbrack k_{2}\rbrack}) = \sum_{k_{2} = c}^{d}\left( \left( \sum_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack} \right)g\left\lbrack k_{2} \right\rbrack \right)$$

$$将每一项的g\lbrack k_{2}\rbrack 视为\lambda ，得到$$

$$(\sum_{k_{1} = a}^{b}{f\lbrack k_{1}\rbrack})g\lbrack k_{2}\rbrack = \sum_{k_{1} = a}^{b}{g\lbrack k_{2}\rbrack f\lbrack k_{1}\rbrack}$$

$$因而\sum_{k_{2} = c}^{d}\left( \left( \sum_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack} \right)g\left\lbrack k_{2} \right\rbrack \right) = \sum_{k_{2} = c}^{d}\left( \sum_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack}g\left\lbrack k_{2} \right\rbrack \right)$$

$$同理，可得到另外两个等式。$$

$$有两点需要牢记:$$

$$1{^\circ}\ \ \ \ \sum_{k_{1} = a}^{b}{f\lbrack k_{1}\rbrack 是个常数}！常数！常数！$$

$$2{^\circ}\ \ \ \ 嵌套形式\sum_{k_{1} = a}^{b}\left( \left( \sum_{k_{2} = c}^{d}{g\left\lbrack k_{2} \right\rbrack} \right)f\left\lbrack k_{1} \right\rbrack \right)$$

$$对于第一层求和，k_{1}是变量，\sum_{k_{2} = c}^{d}{g\lbrack k_{2}\rbrack 是个常数}$$

$$对于第二层求和，k_{2}是变量，{和k}_{1}相关的量都是常数$$

**[定义1.4.3]{.underline}** 乘法嵌套Σ形式

$$\sum_{k_{1} = a}^{b}{\sum_{k_{2} = c}^{d}{f\left\lbrack k_{1} \right\rbrack g\left\lbrack k_{2} \right\rbrack}}: = \sum_{k_{1} = a}^{b}\left( \sum_{k_{2} = c}^{d}{f\left\lbrack k_{1} \right\rbrack g\left\lbrack k_{2} \right\rbrack} \right)$$

$$特别地，当a = c,b = d时，有$$

$$\sum_{k_{1},k_{2} = a}^{b}{f\lbrack k_{1}\rbrack g\lbrack k_{2}\rbrack}: = \sum_{k_{1} = a}^{b}{\sum_{k_{2} = a}^{b}{f\left\lbrack k_{1} \right\rbrack}g\left\lbrack k_{2} \right\rbrack}$$

**[定理1.4.4]{.underline}** 乘法嵌套交换定理II

现在我们可以写得更人性化一些。

$$\sum_{k_{1} = a}^{b}{f\lbrack k_{1}\rbrack} \times \sum_{k_{2} = c}^{d}{g\lbrack k_{2}\rbrack}$$

$$= \sum_{k_{1} = a}^{b}\left( f\left\lbrack k_{1} \right\rbrack\sum_{k_{2} = c}^{d}{g\left\lbrack k_{2} \right\rbrack} \right) = \sum_{k_{2} = c}^{d}\left( g\left\lbrack k_{2} \right\rbrack\sum_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack} \right)$$

$$= \sum_{k_{1} = a}^{b}{\sum_{k_{2} = c}^{d}{f\lbrack k_{1}\rbrack g\lbrack k_{2}\rbrack}} = \sum_{k_{2} = c}^{d}{\sum_{k_{1} = a}^{b}{f\lbrack k_{1}\rbrack g\lbrack k_{2}\rbrack}}$$

$$对于\sum_{k_{1} = a}^{b}{\sum_{k_{2} = c}^{d}{f\lbrack k_{1}\rbrack g\lbrack k_{2}\rbrack}}，{若c或d与k}_{1}相关，$$

$$不妨设c由函数h\lbrack k_{1}\rbrack 决定，则交换定理不成立。$$

$$\sum_{k_{1} = a}^{b}{\sum_{k_{2} = h\lbrack k_{1}\rbrack}^{d}{f\lbrack k_{1}\rbrack g\lbrack k_{2}\rbrack}} \neq \sum_{k_{2} = h\lbrack k_{1}\rbrack}^{d}{\sum_{k_{1} = a}^{b}{f\lbrack k_{1}\rbrack g\lbrack k_{2}\rbrack}}$$

事实上，右式的存在就是个错误，因为在确定$k_{2}$的求和范围时$k_{1}$还不存在。

现在仍然存活的式子是：

$$\sum_{k_{1} = a}^{b}{\sum_{k_{2} = h\lbrack k_{1}\rbrack}^{d}{f\lbrack k_{1}\rbrack g\lbrack k_{2}\rbrack}} = \sum_{k_{1} = a}^{b}\left( f\left\lbrack k_{1} \right\rbrack\sum_{k_{2} = h\left\lbrack k_{1} \right\rbrack}^{d}{g\left\lbrack k_{2} \right\rbrack} \right)$$

但是如果满足一定条件，仍可以进行嵌套交换操作。

**[定理1.4.5]{.underline}** 三角嵌套交换定理

对于二层求和，以两个求和变量建立坐标系，如果被求和计算的点形成一个等腰直角三角形，那么由横向遍历和纵向遍历两种方式效果相同可得三角嵌套交换定理。

$$左上三角：\sum_{k_{1} = a}^{b}{\sum_{k_{2} = k_{1}}^{b}{f\lbrack k_{1},k_{2}\rbrack}} = \sum_{k_{2} = a}^{b}{\sum_{k_{1} = a}^{k_{2}}{f\lbrack k_{1},k_{2}\rbrack}}$$

$$左下三角：\sum_{k_{1} = a}^{b}{\sum_{k_{2} = a}^{a + b - k_{1}}{f\lbrack k_{1},k_{2}\rbrack}} = \sum_{k_{2} = a}^{b}{\sum_{k_{1} = a}^{a + b - k_{2}}{f\lbrack k_{1},k_{2}\rbrack}}$$

$$右上三角：\sum_{k_{1} = a}^{b}{\sum_{k_{2} = a + b - k_{1}}^{b}{f\lbrack k_{1},k_{2}\rbrack}} = \sum_{k_{2} = a}^{b}{\sum_{k_{1} = a + b - k_{2}}^{b}{f\lbrack k_{1},k_{2}\rbrack}}$$

$$右下三角：\sum_{k_{1} = a}^{b}{\sum_{k_{2} = a}^{k_{1}}{f\left\lbrack k_{1},k_{2} \right\rbrack}} = \sum_{k_{2} = a}^{b}{\sum_{k_{1} = k_{2}}^{b}{f\left\lbrack k_{1},k_{2} \right\rbrack}}$$

由简单换元可知，求和变量有一定偏移亦可进行相似操作，如

$$\sum_{k_{1} = a}^{b}{\sum_{k_{2} = a + m}^{k_{1} + m}{f\left\lbrack k_{1},k_{2} \right\rbrack}} = \sum_{k_{1} = a}^{b}{\sum_{k_{2} = a}^{k_{1}}{f\left\lbrack k_{1},k_{2} + m \right\rbrack}}$$

$$= \sum_{k_{2} = a}^{b}{\sum_{k_{1} = k_{2}}^{b}{f\left\lbrack k_{1},k_{2} + m \right\rbrack}} = \sum_{k_{2} = a + m}^{b + m}{\sum_{k_{1} = k_{2} - m}^{b}{f\left\lbrack k_{1},k_{2} \right\rbrack}}$$

若求和点形成一个直角$+ 45{^\circ}$梯形，则可以将其切分为两部分，对两部分单独应用相应的嵌套交换定理。如：

$$\sum_{k_{1} = a}^{b}{\sum_{k_{2} = a - m}^{k_{1}}{f\left\lbrack k_{1},k_{2} \right\rbrack}}\ \ \ \ \ \ \ (m \in \mathbf{N}^{\mathbf{+}})$$

$$= \sum_{k_{1} = a}^{b}\left( \sum_{k_{2} = a}^{k_{1}}{f\left\lbrack k_{1},k_{2} \right\rbrack} + \sum_{k_{2} = a - m}^{a - 1}{f\left\lbrack k_{1},k_{2} \right\rbrack} \right)$$

$$= \sum_{k_{2} = a}^{b}{\sum_{k_{1} = k_{2}}^{b}{f\lbrack k_{1},k_{2}\rbrack}} + \sum_{k_{2} = a - m}^{a - 1}{\sum_{k_{1} = a}^{b}{f\left\lbrack k_{1},k_{2} \right\rbrack}}$$

注意，在应用这些嵌套交换时关键不是死套公式，而是或在纸上或在脑中能描出求和点形成的区域，再通过不同的遍历方式确定交换后的求和范围。

在之后的章节就会看到，嵌套交换定理的应用十分广泛。

值得注意的是，对于求和式，我们主要考虑两方面：求和变量的变化范围及被求和的函数。

由本节内容可知，在多层求和中，内层求和的

$$``系数"（如\sum_{k_{1} = a}^{b}\left( f\left\lbrack k_{1} \right\rbrack\sum_{k_{2} = h\left\lbrack k_{1} \right\rbrack}^{d}{g\left\lbrack k_{2} \right\rbrack} \right)中的f\lbrack k_{1}\rbrack\ ）$$

一定与内层求和变量无关，因而总是能放入内层求和中。

如此，多层求和式刚写出来时可能比较混乱，但是这样处理后总能对应两个方面清楚地分为两部分：

$$\sum_{k_{1} = a_{1}}^{b_{1}}{\sum_{k_{2} = a_{2}}^{b_{2}}{\ldots\sum_{k_{n} = a_{n}}^{b_{n}}\ }}与f\left\lbrack k_{1},k_{2},\ldots,k_{n} \right\rbrack$$

有助于我们将其分开考虑，分别进行一些操作（如交换求和号，函数计算）。这正是嵌套交换定理最大的魅力所在。

[]{#_Toc507114567 .anchor}1.5 合并、换元II

**[例1.5.1]{.underline}** 2的幂次分组求和

在1.3中我们得到了多项相间合并公式，

现在我们考虑作进一步拓展。

按照2的幂次来分组求和，即类似于

$$(a_{1}) + (a_{2} + a_{3}) + (a_{4} + a_{5} + a_{6} + a_{7})的形式。$$

（注意这里的$a$只表示数组）

$$显然有\sum_{k_{1} = 0}^{n - 1}{\sum_{k_{2} = 2^{k_{1}}}^{2^{k_{1} + 1} - 1}{f\lbrack k_{2}\rbrack}} = \sum_{k_{1} = 1}^{2^{n} - 1}{f\lbrack k_{1}\rbrack}$$

接下来考虑更一般的形式，

即每组按$g\lbrack n\rbrack$到$g\lbrack n + 1\rbrack - 1$分。

对照上面的例子，有如下定理。

**[定理1.5.2]{.underline}** 合并定理

$$\sum_{k_{1} = a}^{b}{\sum_{k_{2} = g\lbrack k_{1}\rbrack}^{g\lbrack k_{1} + 1\rbrack - 1}{f\lbrack k_{2}\rbrack}} = \sum_{k_{1} = g\lbrack a\rbrack}^{g\lbrack b + 1\rbrack - 1}{f\lbrack k_{1}\rbrack}$$

$$其中g\lbrack x\rbrack 需要满足的条件是：$$

$${对k}_{1} \in \mathbf{Z}\lbrack a,b\rbrack,g\lbrack k_{1} + 1\rbrack - g\lbrack k_{1}\rbrack \in N^{*}$$

证明：将外层求和按定义展开，

反复使用1.3.1 前后合并定理即可。

$$应用这个定理，代入a = 0,b = n - 1,g\lbrack x\rbrack = 2^{x}$$

即可得到例1.5.1.

$$而代入g\lbrack x\rbrack = nx,得到\sum_{k_{1} = a}^{b}{\sum_{k_{2} = {nk}_{1}}^{{nk}_{1} + n - 1}{f\lbrack k_{2}\rbrack}}$$

利用换元定理，得到

$$\sum_{k_{1} = a}^{b}{\sum_{k_{2} = {nk}_{1}}^{{nk}_{1} + n - 1}{f\lbrack k_{2}\rbrack}} = \sum_{k_{1} = a}^{b}{\sum_{k_{2} = 0}^{n - 1}{f\lbrack k_{2} + {nk}_{1}\rbrack}}$$

利用嵌套交换定理，得到

$$\sum_{k_{1} = a}^{b}{\sum_{k_{2} = 0}^{n - 1}{f\lbrack k_{2} + {nk}_{1}\rbrack}} = \sum_{k_{2} = 0}^{n - 1}{\sum_{k_{1} = a}^{b}{f\lbrack{nk}_{1} + k_{2}\rbrack}}$$

应用1.5.2,最终得到

$$\sum_{k_{2} = 0}^{n - 1}{\sum_{k_{1} = a}^{b}{f\lbrack{nk}_{1} + k_{2}\rbrack}} = \sum_{k_{1} = na}^{nb + n - 1}{f\lbrack k_{1}\rbrack}$$

这也就是1.3.5所得到的公式

另外，2.3给出了另一种证法

接下去我们考虑进一步的换元方式。

**[定义1.5.3]{.underline}** 换元核

$$在求和式\sum_{k_{1} = a}^{b}{\sum_{k_{2} = g\lbrack k_{1}\rbrack}^{g\lbrack k_{1} + 1\rbrack - 1}{f\lbrack k_{2}\rbrack}}中，$$

$$定义由f,g{决定的换元核K}_{f,g}$$

$$K_{f,g}\lbrack k_{1}\rbrack: = \sum_{k_{2} = g\lbrack k_{1}\rbrack}^{g\lbrack k_{1} + 1\rbrack - 1}{f\lbrack k_{2}\rbrack}$$

**[定理1.5.4]{.underline}** 广义换元定理

$${若g}^{- 1}\lbrack b + 1\rbrack - g^{- 1}\lbrack a\rbrack \in N^{*}$$

$$\sum_{k_{1} = a}^{b}{f\lbrack k_{1}\rbrack} = \sum_{k_{1} = g^{- 1}\lbrack a\rbrack}^{g^{- 1}\lbrack b + 1\rbrack - 1}{K_{f,g}\lbrack k_{1}\rbrack}$$

证明：利用核表示定理1.5.2\"

$$\sum_{k_{1} = g\lbrack a\rbrack}^{g\lbrack b + 1\rbrack - 1}{f\lbrack k_{1}\rbrack} = \sum_{k_{1} = a}^{b}{K_{f,g}\lbrack k_{1}\rbrack}$$

$${a用g}^{- 1}\lbrack a\rbrack 代，{b用g}^{- 1}\lbrack b + 1\rbrack - 1代$$

$$即得到\sum_{k_{1} = a}^{b}{f\lbrack k_{1}\rbrack} = \sum_{k_{1} = g^{- 1}\lbrack a\rbrack}^{g^{- 1}\lbrack b + 1\rbrack - 1}{K_{f,g}\lbrack k_{1}\rbrack}$$

然而目前看来，这是最没用的定理之一。

为了更好理解这抽象的东西，给一个例子。

例1.5.5

$$令a = 8,b = 63,f\lbrack x\rbrack = x^{2},g\lbrack x\rbrack = x^{3}$$

$$\sum_{k_{1} = 8}^{63}{k_{1}}^{2} = \sum_{k_{1} = 2}^{3}{K_{f,g}\lbrack k_{1}\rbrack}$$

$${其中K}_{f,g}\lbrack k_{1}\rbrack = \sum_{k_{2} = {k_{1}}^{3}}^{{(k_{1} + 1)}^{3} - 1}{k_{2}}^{2}$$

可以用平方数求和得出核的函数表达式，

得到一个可以稍微分解的七次多项式；

也可以留着，两个∑展开就回到了左边。

一般来说，当$g$为线性函数时用处会大些，

$$因为设g\lbrack x\rbrack = sx + t,有$$

$$K_{f,g}\lbrack k_{1}\rbrack = \sum_{k_{2} = {sk}_{1} + t}^{{sk}_{1} + s + t - 1}{f\lbrack k_{2}\rbrack} = \sum_{k_{2} = t}^{s + t - 1}{f\lbrack k_{2} + {sk}_{1}\rbrack}$$

$${此时求和上下界与k}_{1}无关，$$

$$易于求出去\sum 表达式或者使用嵌套交换定理。$$

[]{#_Toc507114568 .anchor}1.6 线性合并定理

**[定理1.6.1]{.underline}** 线性合并定理

$$设t_{1},t_{2},\ldots,t_{n} \in \mathbf{R},\ f_{1}\lbrack x\rbrack,f_{2}\lbrack x\rbrack,\ldots,f_{n}\lbrack x\rbrack 保证求和有意义，$$

则有如下等式：

$$t_{1}\sum_{k_{1} = a}^{b}{f_{1}\lbrack k_{1}\rbrack} + t_{2}\sum_{k_{1} = a}^{b}{f_{2}\lbrack k_{1}\rbrack} + \ldots + t_{n}\sum_{k_{1} = a}^{b}{f_{n}\left\lbrack k_{1} \right\rbrack}$$

$$= \sum_{k_{2} = 1}^{n}{{(t}_{k_{2}}\sum_{k_{1} = a}^{b}{f_{k_{2}}\lbrack k_{1}\rbrack})} = \sum_{k_{1} = a}^{b}\left( {\sum_{k_{2} = 1}^{n}t_{k_{2}}f}_{k_{2}}\left\lbrack k_{1} \right\rbrack \right)$$

证明：利用1.4的系数穿透定理和嵌套交换定理即可。

**[应用1.6.2]{.underline}** 逆序求和法

如果$f在\lbrack a,b\rbrack$上具有一定的中心对称性，如最常见的等差数列，

若在1.2.5逆序求和定理中取$m = a + b$,

则$F\lbrack x\rbrack ≔ f\lbrack x\rbrack + f\lbrack m - x\rbrack$会有很好的性质。

$$\sum_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack} = \frac{1}{2}\left( \sum_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack} + \sum_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack} \right)$$

$$= \frac{1}{2}\left( \sum_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack} + \sum_{k_{2} = a}^{b}{f\left\lbrack {a + b - k}_{2} \right\rbrack} \right)$$

应用线性合并定理，得到

$$\sum_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack} = \frac{1}{2}\left( \sum_{k_{1} = a}^{b}\left( f\left\lbrack k_{1} \right\rbrack + f\left\lbrack {a + b - k}_{2} \right\rbrack \right) \right)$$

$$= \frac{1}{2}\sum_{k_{1} = a}^{b}{F\left\lbrack k_{1} \right\rbrack}$$

可以看到，在仅仅提出一个1/2的情况下，

我们就把对$f\lbrack x\rbrack$的求和转化为对具有更好性质的$F\lbrack x\rbrack$的求和。

[]{#_Toc507114569 .anchor}1.7 函数穿透定理

函数穿透定理，是一些具有特殊性质

性质的函数能穿过求和或求积号的能力

**[定理1.7.1]{.underline}** 函数穿透定理

$$对\forall x,y \in \mathbf{Z}\lbrack a,b\rbrack,$$

$$f\lbrack x + y\rbrack = f\lbrack x\rbrack + f\lbrack y\rbrack \Rightarrow \sum_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack} = f\left\lbrack \sum_{k_{1} = a}^{b}k_{1} \right\rbrack$$

$$f\lbrack x + y\rbrack = f\lbrack x\rbrack f\lbrack y\rbrack \Rightarrow \prod_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack} = f\left\lbrack \sum_{k_{1} = a}^{b}k_{1} \right\rbrack$$

$$f\lbrack xy\rbrack = f\lbrack x\rbrack + f\lbrack y\rbrack \Rightarrow \sum_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack} = f\left\lbrack \prod_{k_{1} = a}^{b}k_{1} \right\rbrack$$

$$f\lbrack xy\rbrack = f\lbrack x\rbrack f\lbrack y\rbrack \Rightarrow \prod_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack} = f\left\lbrack \prod_{k_{1} = a}^{b}k_{1} \right\rbrack$$

$$证明：归纳即可。$$

$$具有上面四个性质的典型函数：x;e^{x};\ln x;x^{2}$$

**[推论1.7.2]{.underline}** ∑-∏桥定理

$$\sum_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack} = \ln\left( \prod_{k_{1} = a}^{b}e^{f\left\lbrack k_{1} \right\rbrack} \right)$$

$$证明：由f\lbrack x\rbrack = \ln e^{f\lbrack x\rbrack}得$$

$$\sum_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack} = \sum_{k_{1} = a}^{b}\left( \ln e^{f\left\lbrack k_{1} \right\rbrack} \right) = \ln\left( \prod_{k_{1} = a}^{b}e^{f\left\lbrack k_{1} \right\rbrack} \right)$$

$$通过桥定理，可以将求和换为求积，$$

$$可得到之前大多数定理的\prod 形式。$$

**[例1.7.3]{.underline}** 推导线性合并定理(∏形式)

在1.6.1 中，我们得到了如下线性合并定理：

$$\sum_{k_{2} = 1}^{n}{(t_{k_{2}}\sum_{k_{1} = a}^{b}{f_{k_{2}}\lbrack k_{1}\rbrack})} = \sum_{k_{1} = a}^{b}{(\sum_{k_{2} = 1}^{n}{t_{k_{2}}f_{k_{2}}\lbrack k_{1}\rbrack})}$$

$$将\sum_{k_{1} = a}^{b}{f\lbrack k_{1}\rbrack} = \ln\left( \prod_{k_{1} = a}^{b}e^{f\left\lbrack k_{1} \right\rbrack} \right)代入各式，有$$

$$\ln{\prod_{k_{2} = 1}^{n}{e\hat{}(t_{k_{2}}\ln{(\prod_{k_{1} = a}^{b}e^{f_{k_{2}}\lbrack k_{1}\rbrack})})}} = \ln{\prod_{k_{1} = a}^{b}{e\hat{}(\ln{(\prod_{k_{2} = 1}^{n}e^{t_{k_{2}}f_{k_{2}}\lbrack k_{1}\rbrack})})}}$$

$$化简并用e乘方，得到$$

$$\prod_{k_{2} = 1}^{n}\left( \prod_{k_{1} = a}^{b}e^{f_{k_{2}}\left\lbrack k_{1} \right\rbrack} \right)^{t_{k_{2}}} = \prod_{k_{1} = a}^{b}\left( \prod_{k_{2} = 1}^{n}e^{t_{k_{2}}f_{k_{2}}\left\lbrack k_{1} \right\rbrack} \right)$$

$$设F_{m} ≔ e^{f_{m}\left\lbrack k_{1} \right\rbrack},并定义$$

$$\prod_{k_{1} = a}^{b}{\prod_{k_{2} = c}^{d}{f\left\lbrack k_{1},k_{2} \right\rbrack}} ≔ \prod_{k_{1} = a}^{b}\left( \prod_{k_{2} = c}^{d}{f\left\lbrack k_{1},k_{2} \right\rbrack} \right)$$

得到

$$\prod_{k_{2} = 1}^{n}\left( \prod_{k_{1} = a}^{b}{F_{k_{2}}\lbrack k_{1}\rbrack} \right)^{t_{k_{2}}} = \prod_{k_{1} = a}^{b}{\prod_{k_{2} = 1}^{n}\left( F_{k_{2}}\left\lbrack k_{1} \right\rbrack \right)^{t_{k_{2}}}}$$

这即是∏形式的"线性合并"定理。

**[例1.7.4]{.underline}** 推导嵌套交换定理(∏形式)

#说明：这里的证明比较复杂，看不明白，

也没关系，因为最后的结论并没有什么用处。

在1.4.4 中，我们得到了如下嵌套交换定理：

$$\sum_{k_{1} = a}^{b}{f\lbrack k_{1}\rbrack} \times \sum_{k_{2} = c}^{d}{g\lbrack k_{2}\rbrack}$$

$$= \sum_{k_{1} = a}^{b}{(f\lbrack k_{1}\rbrack\sum_{k_{2} = c}^{d}{g\lbrack k_{2}\rbrack})} = \sum_{k_{2} = c}^{d}{(g\lbrack k_{2}\rbrack\sum_{k_{1} = a}^{b}{f\lbrack k_{1}\rbrack})}$$

$$= \sum_{k_{1} = a}^{b}{\sum_{k_{2} = c}^{d}{f\lbrack k_{1}\rbrack g\lbrack k_{2}\rbrack}} = \sum_{k_{2} = c}^{d}{\sum_{k_{1} = a}^{b}{f\lbrack k_{1}\rbrack g\lbrack k_{2}\rbrack}}$$

$$将\sum_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack} = \ln\left( \prod_{k_{1} = a}^{b}e^{f\left\lbrack k_{1} \right\rbrack} \right)代入各式，有$$

$$\ln\left( \prod_{k_{1} = a}^{b}e^{f\left\lbrack k_{1} \right\rbrack} \right) \times \ln\left( \prod_{k_{2} = c}^{d}e^{g\left\lbrack k_{2} \right\rbrack} \right)$$

$$= \ln{(\prod_{k_{1} = a}^{b}{e\hat{}(f\left\lbrack k_{1} \right\rbrack\ln{(\prod_{k_{2} = c}^{d}e^{g\lbrack k_{2}\rbrack})})})}$$

$$= \ln{(\prod_{k_{2} = c}^{d}{e\hat{}(g\left\lbrack k_{2} \right\rbrack\ln{(\prod_{k_{1} = a}^{b}e^{f\lbrack k_{1}\rbrack})})})}$$

$$= \ln\left( \prod_{k_{1} = a}^{b}{\prod_{k_{2} = c}^{d}e^{g\left\lbrack k_{2} \right\rbrack f\left\lbrack k_{1} \right\rbrack}} \right) = \ln\left( \prod_{k_{2} = c}^{d}{\prod_{k_{1} = a}^{b}e^{f\left\lbrack k_{1} \right\rbrack g\left\lbrack k_{2} \right\rbrack}} \right)$$

$$对中间两式作形如\ e^{x\ln y} = y^{x}的操作，$$

用e乘方所有式子，注意第一式有两种做法，得

$$\left( \prod_{k_{1} = a}^{b}e^{f\left\lbrack k_{1} \right\rbrack} \right)\hat{}\ln\left( \prod_{k_{2} = c}^{d}e^{g\left\lbrack k_{2} \right\rbrack} \right) = \left( \prod_{k_{2} = c}^{d}e^{g\left\lbrack k_{2} \right\rbrack} \right)\ \hat{}\ln\left( \prod_{k_{1} = a}^{b}e^{f\left\lbrack k_{1} \right\rbrack} \right)\ $$

$$= {\prod_{k_{2} = c}^{d}\left( \prod_{k_{1} = a}^{b}e^{f\left\lbrack k_{1} \right\rbrack} \right)}^{g\left\lbrack k_{2} \right\rbrack} = {\prod_{k_{1} = a}^{b}\left( \prod_{k_{2} = c}^{d}e^{g\left\lbrack k_{2} \right\rbrack} \right)}^{f\left\lbrack k_{1} \right\rbrack}$$

$$= \prod_{k_{1} = a}^{b}{\prod_{k_{2} = c}^{d}e^{f\left\lbrack k_{1} \right\rbrack g\lbrack k_{2}\rbrack}} = \prod_{k_{2} = c}^{d}{\prod_{k_{1} = a}^{b}e^{g\lbrack k_{2}\rbrack f\left\lbrack k_{1} \right\rbrack}}$$

$$考虑化简第一式，由\prod_{k_{1} = a}^{b}e^{f\lbrack k_{1}\rbrack} = e\hat{}\sum_{k_{1} = a}^{b}{f\left\lbrack k_{1} \right\rbrack}得$$

$$\left( \prod_{k_{1} = a}^{b}e^{f\left\lbrack k_{1} \right\rbrack} \right)\hat{}\ln\left( \prod_{k_{2} = c}^{d}e^{g\left\lbrack k_{2} \right\rbrack} \right) = \left( \prod_{k_{2} = c}^{d}e^{g\left\lbrack k_{2} \right\rbrack} \right)\hat{}\left( \sum_{k_{1} = a}^{b}{f\lbrack k_{1}\rbrack} \right)$$

$$类似有(\prod_{k_{2} = c}^{d}e^{g\left\lbrack k_{2} \right\rbrack})\hat{}\ln{(\prod_{k_{1} = a}^{b}e^{f\lbrack k_{1}\rbrack})} = (\prod_{k_{1} = a}^{b}e^{f\lbrack k_{1}\rbrack})\hat{}(\sum_{k_{2} = c}^{d}{g\lbrack k_{2}\rbrack})$$

$$得到一串等式：$$

$$(\prod_{k_{2} = c}^{d}e^{g\lbrack k_{2}\rbrack})\hat{}(\sum_{k_{1} = a}^{b}{f\lbrack k_{1}\rbrack}) = (\prod_{k_{1} = a}^{b}e^{f\lbrack k_{1}\rbrack})\hat{}(\sum_{k_{2} = c}^{d}{g\lbrack k_{2}\rbrack})$$

$$= \prod_{k_{2} = c}^{d}\left( \prod_{k_{1} = a}^{b}e^{f\left\lbrack k_{1} \right\rbrack} \right)^{g\left\lbrack k_{2} \right\rbrack} = \prod_{k_{1} = a}^{b}\left( \prod_{k_{2} = c}^{d}e^{g\left\lbrack k_{2} \right\rbrack} \right)^{f\left\lbrack k_{1} \right\rbrack}$$

$$= \prod_{k_{1} = a}^{b}{\prod_{k_{2} = c}^{d}{e^{f\left\lbrack k_{1} \right\rbrack g\lbrack k_{2}\rbrack} =}}\prod_{k_{2} = c}^{d}{\prod_{k_{1} = a}^{b}e^{g\lbrack k_{2}\rbrack f\left\lbrack k_{1} \right\rbrack}}$$

$$如果取含\ e^{f\left\lbrack k_{1} \right\rbrack}的三个式子并令F\left\lbrack k_{1} \right\rbrack ≔ e^{f\lbrack k_{1}\rbrack}，有$$

$$(\prod_{k_{1} = a}^{b}{F\lbrack k_{1}\rbrack})\hat{}(\sum_{k_{2} = c}^{d}{g\lbrack k_{2}\rbrack}) = \prod_{k_{2} = c}^{d}\left( \prod_{k_{1} = a}^{b}{F\left\lbrack k_{1} \right\rbrack} \right)^{g\left\lbrack k_{2} \right\rbrack}$$

$$= \prod_{k_{1} = a}^{b}{\prod_{k_{2} = c}^{d}{F\left\lbrack k_{1} \right\rbrack^{g\left\lbrack k_{2} \right\rbrack}}}$$

其中$F\left\lbrack k_{1} \right\rbrack$自然地大于零防止了负数开根号的可能性。

然而接下去也没什么可做的了。可见由于乘方没有交换律，

最后并没有得到很有价值的结论。

但是正如席南华老师所说："它有意思就行了，说不定哪一天就派上用场。"

所以我还是把它放在这里。

[]{#_Toc507114570 .anchor}2.1 多重求和形式

**[定义2.1.1]{.underline}** 多重求和形式I

$$记\overrightarrow{a},\overrightarrow{b},\overrightarrow{k}为n维向量，如\overrightarrow{a} ≔ (a_{1},a_{2},\ldots,a_{n})$$

$$f为n元函数，f\left\lbrack x_{1},x_{2},\ldots,x_{n} \right\rbrack = :f\left\lbrack \overrightarrow{x} \right\rbrack$$

$$并且对t = 1,2,\ldots,n,成立b_{t} - a_{t} \in \mathbf{N},$$

$其中a_{t},b_{t}与k_{t},\ldots,k_{n}无关$，$则有$

$$\sum_{\overrightarrow{k} = \overrightarrow{a}}^{\overrightarrow{b}}{f\left\lbrack \overrightarrow{k} \right\rbrack} ≔ \sum_{k_{1} = a_{1}}^{b_{1}}{\sum_{k_{2} = a_{2}}^{b_{2}}{\ldots\sum_{k_{n} = a_{n}}^{b_{n}}{f\left\lbrack \overrightarrow{k} \right\rbrack}}}$$

$$: = \sum_{k_{1} = a_{1}}^{b_{1}}{(\sum_{k_{2} = a_{2}}^{b_{2}}\left( ...\left( \sum_{k_{n} = a_{n}}^{b_{n}}{f\left\lbrack \overrightarrow{k} \right\rbrack} \right)... \right)}$$

**[定理2.1.2]{.underline}** 完全分解定理

$$如果所有的a_{t},b_{t}均与k_{t}无关，$$

$$并且f\left\lbrack \overrightarrow{k} \right\rbrack = \prod_{t = 1}^{n}{f_{t}\left\lbrack k_{t} \right\rbrack}，则$$

$$\sum_{\overrightarrow{k} = \overrightarrow{a}}^{\overrightarrow{b}}{f\left\lbrack \overrightarrow{k} \right\rbrack} = \prod_{t = 1}^{n}{\sum_{k_{t} = a_{t}}^{b_{t}}{f_{t}\lbrack k_{t}\rbrack}}$$

证明：在二维情况下

$$若f\left\lbrack k_{1},k_{2} \right\rbrack = g\left\lbrack k_{1} \right\rbrack h\left\lbrack k_{2} \right\rbrack,$$

$$并且a_{2},b_{2}与k_{1},k_{2}无关，$$

则由嵌套交换定理得到

$$\sum_{k_{1} = a_{1}}^{b_{1}}{\sum_{k_{2} = a_{2}}^{b_{2}}{g\left\lbrack k_{1} \right\rbrack h\left\lbrack k_{2} \right\rbrack}} = \left( \sum_{k_{1} = a_{1}}^{b_{1}}{g\left\lbrack k_{1} \right\rbrack} \right)\left( \sum_{k_{2} = a_{2}}^{b_{2}}{h\left\lbrack k_{2} \right\rbrack} \right)$$

对$n维情况$简单归纳即可。

[]{#_Toc507114571 .anchor}2.2 条件求和形式

**[定义2.2.1]{.underline}** 默认求和形式

如果$\overset{⃑}{k}$的限制条件是自然而然的，

不写出也不会引起歧义的，

或者根本不存在限制，[对所有取值求和（不重复）]{.underline}

则默认求和形式记为

$$\sum f\left\lbrack \overset{⃑}{k} \right\rbrack$$

$${如一组数x}_{1},\ldots,x_{n}求和可记为$$

$$\sum x_{k}(甚至\sum x_{n})$$

**[定义2.2.2]{.underline}** 条件求和形式

$$设P\left\lbrack \overset{⃑}{k} \right\rbrack 为关于k_{1},\ldots,k_{n}的命题，$$

$$则对所有满足命题P的\overset{⃑}{k}求和表示为$$

$$\sum_{P\left\lbrack \overset{⃑}{k} \right\rbrack}^{}{f\left\lbrack \overset{⃑}{k} \right\rbrack}$$

$$若\overset{⃑}{k}除命题P外还被限定在\mathbf{Z}\left\lbrack \overset{⃑}{a},\overset{⃑}{b} \right\rbrack 上，$$

$$则此时求和记为$$

$$\sum_{\begin{array}{r}
\overrightarrow{k} = \overrightarrow{a}\  \\
P\left\lbrack \overset{⃑}{k} \right\rbrack
\end{array}}^{\overrightarrow{b}}{f\left\lbrack \overrightarrow{k} \right\rbrack}$$

$$若有多个命题P_{1},\ldots,P_{n}$$

$$则对所有满足所有命题的\overset{⃑}{k}求和表示为$$

$$\sum_{\begin{array}{r}
P_{1}\left\lbrack \overset{\rightharpoonup}{k} \right\rbrack \\
 \vdots \\
P_{n}\left\lbrack \overset{\rightharpoonup}{k} \right\rbrack
\end{array}}^{}{f\left\lbrack \overset{⃑}{k} \right\rbrack}或\underset{P_{1} \land P_{2} \land \ldots \land P_{n}\left\lbrack \overset{⃑}{k} \right\rbrack}{\sum f\left\lbrack \overset{⃑}{k} \right\rbrack}$$

$${取\delta}_{P}\left\lbrack \overset{⃑}{k} \right\rbrack = \begin{matrix}
\left\{ \begin{matrix}
1, & P\left\lbrack \overset{⃑}{k} \right\rbrack 为真 \\
0, & P\left\lbrack \overset{⃑}{k} \right\rbrack 为假
\end{matrix} \right.\  &
\end{matrix}$$

(在不引起歧义的情况下可省略下标)

则可如下定义条件求和：

$$\sum_{P\left\lbrack \overset{⃑}{k} \right\rbrack}^{\ }{f\left\lbrack \overrightarrow{k} \right\rbrack} ≔ \sum\delta\left\lbrack \overrightarrow{k} \right\rbrack f\left\lbrack \overrightarrow{k} \right\rbrack$$

$$\sum_{\begin{array}{r}
\overrightarrow{k} = \overrightarrow{a}\  \\
P\left\lbrack \overset{⃑}{k} \right\rbrack
\end{array}}^{\overrightarrow{b}}{f\left\lbrack \overrightarrow{k} \right\rbrack} ≔ \sum_{\begin{array}{r}
\  \\
\overrightarrow{k} = \overrightarrow{a}
\end{array}}^{\overrightarrow{b}}{\delta\lbrack\overrightarrow{k}\rbrack f\lbrack\overrightarrow{k}\rbrack}$$

$$\sum_{\begin{array}{r}
P_{1}\left\lbrack \overset{\rightharpoonup}{k} \right\rbrack \\
 \vdots \\
P_{n}\left\lbrack \overset{\rightharpoonup}{k} \right\rbrack
\end{array}}^{}{f\left\lbrack \overset{⃑}{k} \right\rbrack} ≔ \sum\left( \prod_{t = 1}^{n}{\delta_{P_{t}}\left\lbrack \overrightarrow{k} \right\rbrack} \right)f\left\lbrack \overrightarrow{k} \right\rbrack$$

$$= \sum\left( \prod\delta_{P_{t}}\left\lbrack \overrightarrow{k} \right\rbrack \right)f\left\lbrack \overrightarrow{k} \right\rbrack$$

**[定理2.2.3]{.underline}** 条件求和容斥原理

设$P,Q为关于\overrightarrow{k}的命题，则$

$$\sum_{P\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack} + \sum_{Q\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack} = \sum_{P \vee Q\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack} + \sum_{P \land Q\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack}$$

证明：

$$左边 = \sum\delta_{P}\left\lbrack \overrightarrow{k} \right\rbrack f\left\lbrack \overrightarrow{k} \right\rbrack + \sum\delta_{Q}\left\lbrack \overrightarrow{k} \right\rbrack f\left\lbrack \overrightarrow{k} \right\rbrack$$

$$= \sum\left( \delta_{P}\left\lbrack \overrightarrow{k} \right\rbrack + \delta_{Q}\left\lbrack \overrightarrow{k} \right\rbrack \right)f\left\lbrack \overrightarrow{k} \right\rbrack$$

由真值表不难得到

$$\delta_{P}\left\lbrack \overrightarrow{k} \right\rbrack + \delta_{Q}\left\lbrack \overrightarrow{k} \right\rbrack = \begin{matrix}
\left\{ \begin{matrix}
0 & P假，Q假 \\
1 & P真，Q假 \\
1 & P假，Q真 \\
2 & P真，Q真
\end{matrix} \right.\  &
\end{matrix}$$

$$= \left\{ \begin{matrix}
0 & P假，Q假 \\
1 & P真，Q假 \\
1 & P假，Q真 \\
1 & P真，Q真
\end{matrix} \right.\  + \left\{ \begin{matrix}
0 & P假，Q假 \\
0 & P真，Q假 \\
0 & P假，Q真 \\
1 & P真，Q真
\end{matrix} \right.\ $$

$$= \left\{ \begin{matrix}
0 & P假且Q假 \\
1 & P真或Q真
\end{matrix} \right.\  + \left\{ \begin{matrix}
0 & P假或Q假 \\
1 & P真且Q真
\end{matrix} \right.\ $$

$$= \delta_{P \vee Q}\lbrack\overrightarrow{k}\rbrack + \delta_{P \land Q}\lbrack\overrightarrow{k}\rbrack$$

因而$左边 = \sum\left( \delta_{P \vee Q}\left\lbrack \overrightarrow{k} \right\rbrack + \delta_{P \land Q}\left\lbrack \overrightarrow{k} \right\rbrack \right)f\left\lbrack \overrightarrow{k} \right\rbrack$

$$= \sum\delta_{P \vee Q}\left\lbrack \overrightarrow{k} \right\rbrack f\left\lbrack \overrightarrow{k} \right\rbrack + \sum\delta_{P \land Q}\left\lbrack \overrightarrow{k} \right\rbrack f\left\lbrack \overrightarrow{k} \right\rbrack$$

$$= 右边$$

**[推论2.2.4]{.underline}** 广义合并定理

$$设关于\overrightarrow{k}的命题P，Q$$

$$满足对\forall\overrightarrow{k},P \land Q\left\lbrack \overrightarrow{k} \right\rbrack 为假，则$$

$$\sum_{P\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack} + \sum_{Q\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack} = \sum_{P \vee Q\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack}$$

证明：由条件求和容斥原理

$$结合\sum_{P \land Q\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack} = 0显然。$$

依照这个定理，可以把满足特定条件的任意多的相同函数的求和式合并为一个。

**[推论2.2.5]{.underline}** 限制定理

$$设R满足P \vee R = Q \vee R,则$$

$$\sum_{P\lbrack\overrightarrow{k}\rbrack}^{}{f\lbrack\overrightarrow{k}\rbrack} = \sum_{Q\lbrack\overrightarrow{k}\rbrack}^{}{f\lbrack\overrightarrow{k}\rbrack} \Leftrightarrow \sum_{\begin{array}{r}
P\lbrack\overrightarrow{k}\rbrack \\
R\lbrack\overrightarrow{k}\rbrack
\end{array}}^{}{f\lbrack\overrightarrow{k}\rbrack} = \sum_{\begin{array}{r}
Q\lbrack\overrightarrow{k}\rbrack \\
R\lbrack\overrightarrow{k}\rbrack
\end{array}}^{}{f\lbrack\overrightarrow{k}\rbrack}$$

$$证明：\sum_{P\lbrack\overrightarrow{k}\rbrack}^{}{f\lbrack\overrightarrow{k}\rbrack} = \sum_{Q\lbrack\overrightarrow{k}\rbrack}^{}{f\lbrack\overrightarrow{k}\rbrack}$$

$$\Leftrightarrow \sum_{P\lbrack\overrightarrow{k}\rbrack}^{}{f\lbrack\overrightarrow{k}\rbrack} + \sum_{R\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack} = \sum_{Q\lbrack\overrightarrow{k}\rbrack}^{}{f\lbrack\overrightarrow{k}\rbrack} + \sum_{R\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack}$$

$$\Leftrightarrow \sum_{P \vee R\lbrack\overrightarrow{k}\rbrack}^{}{f\lbrack\overrightarrow{k}\rbrack} + \sum_{P \land R\lbrack\overrightarrow{k}\rbrack}^{}{f\lbrack\overrightarrow{k}\rbrack} = \sum_{Q \vee R\lbrack\overrightarrow{k}\rbrack}^{}{f\lbrack\overrightarrow{k}\rbrack} + \sum_{Q \land R\lbrack\overrightarrow{k}\rbrack}^{}{f\lbrack\overrightarrow{k}\rbrack}$$

$$\Leftrightarrow \sum_{P \land R\lbrack\overrightarrow{k}\rbrack}^{}{f\lbrack\overrightarrow{k}\rbrack} = \sum_{Q \land R\lbrack\overrightarrow{k}\rbrack}^{}{f\lbrack\overrightarrow{k}\rbrack}$$

$$\Leftrightarrow \sum_{\begin{array}{r}
P\lbrack\overrightarrow{k}\rbrack \\
R\lbrack\overrightarrow{k}\rbrack
\end{array}}^{}{f\lbrack\overrightarrow{k}\rbrack} = \sum_{\begin{array}{r}
Q\lbrack\overrightarrow{k}\rbrack \\
R\lbrack\overrightarrow{k}\rbrack
\end{array}}^{}{f\lbrack\overrightarrow{k}\rbrack}$$

$$注：\sum_{P\lbrack\overrightarrow{k}\rbrack}^{}{f\lbrack\overrightarrow{k}\rbrack} = \sum_{Q\lbrack\overrightarrow{k}\rbrack}^{}{f\lbrack\overrightarrow{k}\rbrack}一般不能推得P = Q$$

此定理得名于它的效果

$$如同给求和加上满足命题R的限制。$$

**[推论2.2.6]{.underline}** 条件求和非定理

$$\delta_{\neg P}\left\lbrack \overrightarrow{k} \right\rbrack = 1 - \delta_{P}\left\lbrack \overrightarrow{k} \right\rbrack$$

$$\sum_{\neg P\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack} = \sum f\left\lbrack \overrightarrow{k} \right\rbrack - \sum_{P\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack}$$

$$证：\delta 的性质可以直接验证。$$

$$求和式证明可利用条件求和容斥原理,$$

$$令P = P,Q = \neg P即可。$$

$$也可利用第一行\delta 的性质证明。$$

$$实际应用还需加上限制，否则\sum f\left\lbrack \overrightarrow{k} \right\rbrack 无意义$$

$$设求和在Q中考虑，即P也在Q中$$

$$P \land Q = P,P \vee Q = Q$$

$$\sum_{\begin{array}{r}
Q\left\lbrack \overrightarrow{k} \right\rbrack \\
\neg P\left\lbrack \overrightarrow{k} \right\rbrack
\end{array}}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack} = \sum_{Q\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack} - \sum_{\begin{array}{r}
Q\left\lbrack \overrightarrow{k} \right\rbrack \\
P\left\lbrack \overrightarrow{k} \right\rbrack
\end{array}}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack}$$

$$证：\sum f\left\lbrack \overrightarrow{k} \right\rbrack = \sum_{P\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack} + \sum_{\neg P\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack} = \sum_{P \vee \neg P\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack}$$

$$应用限制定理，\sum_{Q\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack} = \sum_{\begin{array}{r}
Q\left\lbrack \overrightarrow{k} \right\rbrack \\
P \vee \neg P\left\lbrack \overrightarrow{k} \right\rbrack
\end{array}}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack}$$

$$= \sum_{Q \land (P \vee \neg P)\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack} = \sum_{\left. （Q \land P \right.） \vee (Q \land \neg P)\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack}$$

$$注意到P \land \neg P恒为假，有$$

$$\sum_{\left. （Q \land P \right.） \land (Q \land \neg P)\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack} = \sum_{Q \land (P \land \neg P)\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack} = 0$$

$$因此\sum_{Q\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack} = \sum_{\left. （Q \land P \right.） \vee (Q \land \neg P)\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack} + \sum_{\left. （Q \land P \right.） \land (Q \land \neg P)\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack}$$

$$= \sum_{Q \land P\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack} + \sum_{Q \land \neg P\left\lbrack \overrightarrow{k} \right\rbrack}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack}$$

$$= \sum_{\begin{array}{r}
Q\left\lbrack \overrightarrow{k} \right\rbrack \\
P\left\lbrack \overrightarrow{k} \right\rbrack
\end{array}}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack} + \sum_{\begin{array}{r}
Q\left\lbrack \overrightarrow{k} \right\rbrack \\
\neg P\left\lbrack \overrightarrow{k} \right\rbrack
\end{array}}^{}{f\left\lbrack \overrightarrow{k} \right\rbrack}$$

$$移项即可证得命题。也可利用\delta 证明。$$

[]{#_Toc507114572 .anchor}2.3 任意步长求和形式

**[定义2.3.1]{.underline}** 任意步长求和形式

$$对于d > 0,\frac{b - a}{d} \in \mathbf{N},$$

$$取\delta\left\lbrack k_{1} \right\rbrack = \left\{ \begin{matrix}
1, & k_{1} - a \equiv 0(mod\ d) \\
0, & k_{1} - a ≢ 0(mod\ d)
\end{matrix} \right.\ $$

$$\sum_{\underset{\Delta d}{k_{1} = a}}^{b}{f\left\lbrack k_{1} \right\rbrack} ≔ \sum_{k_{1} = a}^{b}{\delta\left\lbrack k_{1} \right\rbrack f\left\lbrack k_{1} \right\rbrack} = f\lbrack a\rbrack + f\lbrack a + d\rbrack + \ldots + f\lbrack b\rbrack$$

显然当$d = 1$时退化为标准求和式，Δ1可省略。

对于Σ的各种形式，我们试图找到一个等式

来将其化为标准型以便进一步操作。

**[定理2.3.2]{.underline}** 任意步长求和标准化

由于$k_{1}$每自增$d$才会求和一次，

考虑让$k_{1}$和新的求和变量相关，

新的求和变量每自增1，$k_{1}$就自增$d$

显然这个新的求和变量是$k_{2} = k_{1}/d$

而$f\left\lbrack k_{1} \right\rbrack = f\left\lbrack d \cdot k_{2} \right\rbrack$，应用改名定理得

$$\sum_{\underset{\Delta d}{k_{1} = a}}^{b}{f\lbrack k_{1}\rbrack} = \sum_{k_{1} = \frac{a}{d}}^{\frac{b}{d}}{f\lbrack{d \cdot k}_{1}\rbrack}$$

证明：两边求和式应用定义展开写出即可。

**[定义2.3.3]{.underline}** 任意步长的多重求和形式I

$$记\overrightarrow{a},\overrightarrow{b},\overrightarrow{k},\overrightarrow{d}为n维向量,f为n元函数,$$

$$并且对t = 1,2,\ldots,n,\frac{b_{t} - a_{t}}{d_{t}} \in \mathbf{N},$$

$$a_{t},b_{t}{与k}_{t},\ldots,k_{n}无关，$$

$${取\delta}_{t}\lbrack k_{t}\rbrack = \left\{ \begin{matrix}
1, & k_{t} - a_{t} \equiv 0(modd_{t}) \\
0, & k_{t} - a_{t} ≢ 0(modd_{t})
\end{matrix} \right.\ $$

$$\delta\lbrack\overrightarrow{k}\rbrack = \prod_{t = 1}^{n}{\delta_{t}\left\lbrack k_{t} \right\rbrack},则$$

$$\sum_{\underset{\Delta\overrightarrow{d}}{\overrightarrow{k} = \overrightarrow{a}}}^{\overrightarrow{b}}{f\lbrack\overrightarrow{k}\rbrack}: = \sum_{\overrightarrow{k} = \overrightarrow{a}}^{\overrightarrow{b}}{\delta\lbrack\overrightarrow{k}\rbrack f\lbrack\overrightarrow{k}\rbrack} = \sum_{\underset{{\Delta d}_{1}}{k_{1} = a_{1}}}^{b_{1}}{\sum_{\underset{{\Delta d}_{2}}{k_{2} = a_{2}}}^{b_{2}}{...\sum_{\underset{{\Delta d}_{n}}{k_{n} = a_{n}}}^{b_{n}}{f\lbrack\overrightarrow{k}\rbrack}}}$$

$$= \sum_{\underset{{\Delta d}_{1}}{k_{1} = a_{1}}}^{b_{1}}{(\sum_{\underset{{\Delta d}_{2}}{k_{2} = a_{2}}}^{b_{2}}{(...(\sum_{\underset{{\Delta d}_{n}}{k_{n} = a_{n}}}^{b_{n}}{f\lbrack\overrightarrow{k}\rbrack})...)}}$$

$$注意\sum_{\underset{\Delta\overrightarrow{d}}{\overrightarrow{k} = \overrightarrow{a}}}^{\overrightarrow{b}}{f\lbrack\overrightarrow{k}\rbrack} \neq f\lbrack\overrightarrow{a}\rbrack + f\lbrack\overrightarrow{a} + \overrightarrow{d}\rbrack + ... + f\lbrack\overrightarrow{b}\rbrack$$

**[定理2.3.4]{.underline}** 步长替换定理

$$\sum_{\underset{\Delta d}{k_{1} = a}}^{b}{f\lbrack k_{1}\rbrack} = \sum_{\underset{{\Delta d}_{1}}{k_{1} = \frac{d_{1}}{d}a}}^{\frac{d_{1}}{d}b}{f\lbrack\frac{d}{d_{1}}k_{1}\rbrack}$$

证明：由2.3.2,得

$$\sum_{\underset{\Delta d}{k_{1} = a}}^{b}{f\lbrack k_{1}\rbrack} = \sum_{k_{1} = \frac{a}{d}}^{\frac{b}{d}}{f\lbrack{dk}_{1}\rbrack}$$

$$\sum_{\underset{{\Delta d}_{1}}{k_{1} = \frac{d_{1}}{d}a}}^{\frac{d_{1}}{d}b}{f\lbrack\frac{d}{d_{1}}k_{1}\rbrack} = \sum_{k_{1} = \frac{a}{d}}^{\frac{b}{d}}{f\lbrack{dk}_{1}\rbrack}$$

证毕。

**[定理2.3.5]{.underline}** 填坑原理

$$\sum_{\underset{\Delta d}{k_{1} = a}}^{b}{\sum_{\underset{{\Delta d}_{1}}{k_{2} = 0}}^{d - d_{1}}{f\lbrack k_{1} + k_{2}\rbrack}} = \sum_{\underset{{\Delta d}_{1}}{k_{1} = a}}^{b + d - d_{1}}{f\lbrack k_{1}\rbrack}$$

$$其中\frac{d}{d_{1}} \in \mathbf{N}^{\mathbf{*}}$$

$$证明：设b - a = nd,由2\text{.3.2}及换元得$$

$$左边 = \sum_{k_{1} = 0}^{n}{\sum_{\underset{{\Delta d}_{1}}{k_{2} = 0}}^{d - d_{1}}{f\lbrack a + k_{1}d + k_{2}\rbrack}} = \sum_{k_{1} = 0}^{n}{\sum_{\underset{{\Delta d}_{1}}{k_{2} = a + k_{1}d}}^{a + (k_{1} + 1)d - d_{1}}{f\lbrack k_{2}\rbrack}}$$

将它和推论1.3.2$\ $

$$\sum_{k_{2} = 1}^{n}{(\sum_{k_{1} = a_{k_{2}} + 1}^{a_{(k_{2} + 1)}}{f\lbrack k_{1}\rbrack})} = \sum_{k_{1} = a_{1} + 1}^{a_{n + 1}}{f\lbrack k_{1}\rbrack}$$

相对比，有以下一些不同。

对比,有如下一些不同：

1° $k_{1}和k_{2}$位置反了。

但由改名定理这当然是没关系的。

2° 外层求和分别是1到$n$和0到$n$

只要我们明白右边求和的下界是由

左边外层求和下界

代入内层求和下界得到即可。

3° 1.3.2中左边内层上下界

$${分别是a}_{(k_{2} + 1)}{和a}_{k_{2}} + 1$$

而证明中的内层上下界

$分别具有x_{(k_{1} + 1)} - d_{1}$和$x_{1}$的形式。

注意到证明中带了*d*~1~的步长，

这仍然能保持前后连接的完整性。

因此我们仍然能够得到

$$左边 = \sum_{k_{1} = 0}^{n}{\sum_{\underset{{\Delta d}_{1}}{k_{2} = a + k_{1}d}}^{a + (k_{1} + 1)d - d_{1}}{f\lbrack k_{2}\rbrack}} = \sum_{\underset{{\Delta d}_{1}}{k_{1} = a}}^{b + d - d_{1}}{f\lbrack k_{1}}\rbrack$$

证毕。

$$之所以叫填坑原理，是因原来求和步长为d，$$

中间很多项没有加，好像有很多坑。

$${最后得到的求和步长缩小为为d}_{1}，$$

正好似把其中的坑填掉了一部分。

有兴趣的读者可以试试用广义合并定理证明。

$$在证明过程中用到了之前的一堆定理，$$

而之所以在第一章详细论述它们，

$$正是为了打下坚实的基础。$$

$$后面很多证明也都依赖于这些操作。$$

**[应用2.3.6]{.underline}** 证明定理1.3.5

多项相间合并定理：

$$\sum_{k_{2} = 0}^{n - 1}{(\sum_{k_{1} = a}^{b}{f\lbrack{nk}_{1} + k_{2}\rbrack})} = \sum_{k_{1} = na}^{nb + n - 1}{f\lbrack k_{1}\rbrack}$$

证明：

$$左边 = \sum_{k_{2} = 0}^{n - 1}{(\sum_{\begin{array}{r}
k_{1} = na \\
\Delta n
\end{array}}^{nb}{f\lbrack k_{1} + k_{2}\rbrack})}$$

由嵌套交换定理(对步长形式也成立，证略)

$$得到\ 左边 = \sum_{\begin{array}{r}
k_{1} = na \\
\Delta n
\end{array}}^{nb}{(\sum_{k_{2} = 0}^{n - 1}{f\lbrack k_{1} + k_{2}\rbrack})}$$

注意到默认求和有步长为1，应用填坑原理：

$$左边 = \sum_{\begin{array}{r}
k_{1} = na \\
\Delta n
\end{array}}^{nb}{(\sum_{\begin{array}{r}
k_{2} = 0 \\
\Delta 1
\end{array}}^{n - 1}{f\lbrack k_{1} + k_{2}\rbrack})} = \sum_{k_{1} = na}^{nb + n - 1}{f\lbrack k_{1}\rbrack}，证毕。$$

[]{#_Toc507114573 .anchor}2.4 不等求和形式

以下讨论中$a,b,c,d均与k_{1},k_{2}无关。$

只考虑常见的情况：

内外层求和上下界只相差某个整数

$$即对于\sum_{k_{1} = a}^{b}{\sum_{k_{2} = c}^{d}{f\left\lbrack k_{1},k_{2} \right\rbrack}}，有a - c \in \mathbf{Z}$$

**[定义2.4.1]{.underline}** 不等求和形式

$$由kronecker\ \delta_{ij} = \left\{ \begin{matrix}
1, & i = j \\
0, & i \neq j
\end{matrix} \right.\ $$

$$\sum_{k_{1} = a}^{b}{\sum_{\underset{k_{1} \neq k_{2}}{k_{2} = c}}^{d}{f\lbrack k_{1},k_{2}\rbrack}} ≔ \sum_{k_{1} = a}^{b}{\sum_{k_{2} = c}^{d}{(1 - \delta_{k_{1}k_{2}})f\lbrack k_{1},k_{2}\rbrack}}$$

**[定理2.4.2]{.underline}** 不等求和形式标准化

$$当\min\left\{ b,d \right\} < \max\left\{ a,c \right\} 时，$$

$$\sum_{k_{1} = a}^{b}{\sum_{\underset{k_{1} \neq k_{2}}{k_{2} = c}}^{d}{f\lbrack k_{1},k_{2}\rbrack}} = \sum_{k_{1} = a}^{b}{\sum_{k_{2} = c}^{d}{f\lbrack k_{1},k_{2}\rbrack}}$$

$$当\min\{ b,d\} \geq \max\{ a,c\} 时，$$

$$\sum_{k_{1} = a}^{b}{\sum_{\underset{k_{1} \neq k_{2}}{k_{2} = c}}^{d}{f\lbrack k_{1},k_{2}\rbrack}} = \sum_{k_{1} = a}^{b}{\sum_{k_{2} = c}^{d}{f\lbrack k_{1},k_{2}\rbrack}} - \sum_{k_{1} = \max\{ a,c\}}^{\min\{ b,d\}}{f\lbrack k_{1},k_{1}\rbrack}$$

$$证明：第一种情况下，$$

$$注意到a \leq b且c \leq d，有$$

$$a \leq k_{1} \leq b < c \leq k_{2} \leq d或c \leq k_{2} \leq d < a \leq k_{1} \leq b$$

$$可知k_{1} \neq k_{2}恒成立，结论显然。$$

第二种情况下

$$\mathbf{Z}\lbrack a,b\rbrack\bigcap\mathbf{Z}\lbrack c,d\rbrack = \mathbf{Z}\lbrack\max\{ a,c\},\min\{ b,d\}\rbrack$$

$$所以k_{1},k_{2}仅可能在\mathbf{Z}\left\lbrack \max\left\{ a,c \right\},\min\left\{ b,d \right\} \right\rbrack 中相等，于是有$$

$$\sum_{k_{1} = a}^{b}{\sum_{k_{2} = c}^{d}{\delta_{k_{1}k_{2}}f\lbrack k_{1},k_{2}\rbrack}} = \sum_{k_{1} = \max\{ a,c\}}^{\min\{ b,d\}}\left( \sum_{k_{2} = \max\left\{ a,c \right\}}^{\min\left\{ b,d \right\}}{\delta_{k_{1}k_{2}}f\left\lbrack k_{1},k_{2} \right\rbrack} \right)$$

$$= \sum_{k_{1} = \max\{ a,c\}}^{\min\{ b,d\}}{f\lbrack k_{1},k_{1}\rbrack}$$

$$因而$$

$$\sum_{k_{1} = a}^{b}{\sum_{\underset{k_{1} \neq k_{2}}{k_{2} = c}}^{d}{f\lbrack k_{1},k_{2}\rbrack}} = \sum_{k_{1} = a}^{b}{\sum_{k_{2} = c}^{d}{f\lbrack k_{1},k_{2}\rbrack}} - \sum_{k_{1} = a}^{b}{\sum_{k_{2} = c}^{d}{\delta_{k_{1}k_{2}}f\lbrack k_{1},k_{2}\rbrack}}$$

$$= \sum_{k_{1} = a}^{b}{\sum_{k_{2} = c}^{d}{f\lbrack k_{1},k_{2}\rbrack}} - \sum_{k_{1} = \max\{ a,c\}}^{\min\{ b,d\}}{f\lbrack k_{1},k_{1}\rbrack}$$

**[定义2.4.3]{.underline}** 常用不等求和形式

经常遇到的不等求和形式是求和里外层有相同的上下界。

$$定义\sum_{\underset{k_{1} \neq k_{2}}{k_{1},k_{2} = a}}^{b}{f\lbrack k_{1},k_{2}\rbrack} ≔ \sum_{k_{1} = a}^{b}{\sum_{\underset{k_{1} \neq k_{2}}{k_{2} = a}}^{b}{f\lbrack k_{1},k_{2}\rbrack}}$$

由定理2.3.4，显然有

$$\sum_{\underset{k_{1} \neq k_{2}}{k_{1},k_{2} = a}}^{b}{f\lbrack k_{1},k_{2}\rbrack} = \sum_{k_{1},k_{2} = a}^{b}{f\lbrack k_{1},k_{2}\rbrack} - \sum_{k_{1} = a}^{b}{f\lbrack k_{1},k_{1}\rbrack}$$

**[定义2.4.4]{.underline}** 小于求和形式

$$取\delta\lbrack k_{1},k_{2}\rbrack = \left\{ \begin{matrix}
1, & k_{1} < k_{2} \\
0, & k_{1} \geq k_{2}
\end{matrix} \right.\ $$

$$则\sum_{k_{1} = a}^{b}{\sum_{\underset{k_{1} < k_{2}}{k_{2} = c}}^{d}{f\left\lbrack k_{1},k_{2} \right\rbrack}} ≔ \sum_{k_{1} = a}^{b}{\sum_{k_{2} = c}^{d}{\delta\lbrack k_{1},k_{2}\rbrack f\lbrack k_{1},k_{2}\rbrack}}$$

**[定理2.4.5]{.underline}** 小于求和形式标准化

我们考虑以下几种情况。

$$1{^\circ}\ \ b < c$$

$$此时由a \leq k_{1} \leq b < c \leq k_{2} \leq d,{可知k}_{1} < k_{2}恒成立，$$

$$故\sum_{k_{1} = a}^{b}{\sum_{\underset{k_{1} < k_{2}}{k_{2} = c}}^{d}{f\lbrack k_{1},k_{2}\rbrack}} = \sum_{k_{1} = a}^{b}{\sum_{k_{2} = c}^{d}{f\lbrack k_{1},k_{2}\rbrack}}$$

$$2{^\circ}\ \ a \geq d$$

$$此时由c \leq k_{2} \leq d \leq a \leq k_{1} \leq b,{可知k}_{2} \leq k_{1}恒成立$$

$$故\sum_{k_{1} = a}^{b}{\sum_{\underset{k_{1} < k_{2}}{k_{2} = c}}^{d}{f\lbrack k_{1},k_{2}\rbrack}} = 0$$

除去以上两种情况，考虑内层求和。

$${要想让k}_{2} > k_{1}，{只需让k}_{2}{从k}_{1} + 1开始求和。$$

$$\sum_{k_{1} = a}^{b}{\sum_{\underset{k_{1} < k_{2}}{k_{2} = c}}^{d}{f\left\lbrack k_{1},k_{2} \right\rbrack}} = \sum_{k_{1} = a}^{b}\left( \sum_{\underset{k_{1} < k_{2}}{k_{2} = c}}^{d}{f\left\lbrack k_{1},k_{2} \right\rbrack} \right)$$

$$= \sum_{k_{1} = a}^{b}{(\sum_{k_{2} = k_{1} + 1}^{d}{f\lbrack k_{1},k_{2}\rbrack})}$$

$$但是注意到b和d还需要比较。$$

$$3{^\circ}\ \ b \geq c且a < d且b < d$$

$$此时b最大可取到d - 1，k_{1}最大取d - 1$$

$$内层求和仍然成立k_{1} + 1 \leq d$$

$$因此\sum_{k_{1} = a}^{b}{\sum_{\underset{k_{1} < k_{2}}{k_{2} = c}}^{d}{f\lbrack k_{1},k_{2}\rbrack}} = \sum_{k_{1} = a}^{b}{\sum_{k_{2} = k_{1} + 1}^{d}{f\lbrack k_{1},k_{2}\rbrack}}$$

$$4{^\circ}\ \ b \geq c且a < d且b \geq d$$

$$将外层求和拆为两部分。$$

$$\sum_{k_{1} = a}^{b}{\sum_{\underset{k_{1} < k_{2}}{k_{2} = c}}^{d}{f\left\lbrack k_{1},k_{2} \right\rbrack}} = \sum_{k_{1} = a}^{d - 1}{\sum_{\underset{k_{1} < k_{2}}{k_{2} = c}}^{d}{f\left\lbrack k_{1},k_{2} \right\rbrack}} + \sum_{k_{1} = d}^{b}{\sum_{\underset{k_{1} < k_{2}}{k_{2} = c}}^{d}{f\left\lbrack k_{1},k_{2} \right\rbrack}}$$

$$注意到第一项符合情况3，第二项符合情况2$$

$$分别应用结论，得$$

$$\sum_{k_{1} = a}^{b}{\sum_{\underset{k_{1} < k_{2}}{k_{2} = c}}^{d}{f\lbrack k_{1},k_{2}\rbrack}} = \sum_{k_{1} = a}^{d - 1}{\sum_{k_{2} = k_{1} + 1}^{d}{f\lbrack k_{1},k_{2}\rbrack}}$$

$$情况3、4可合并写为$$

$$当b \geq c且a < d时$$

$$\sum_{k_{1} = a}^{b}{\sum_{\underset{k_{1} < k_{2}}{k_{2} = c}}^{d}{f\lbrack k_{1},k_{2}\rbrack}} = \sum_{k_{1} = a}^{\min\{ b,d - 1\}}{\sum_{k_{2} = k_{1} + 1}^{d}{f\lbrack k_{1},k_{2}\rbrack}}$$

**[定义2.4.6]{.underline}** 常用小于求和形式

类似2.4.3，经常遇到的是

内外层求和上下界相同的情况。

规定$b > a$，

$$定义\sum_{\underset{k_{1} < k_{2}}{k_{1},k_{2} = a}}^{b}{f\lbrack k_{1},k_{2}\rbrack} ≔ \sum_{k_{1} = a}^{b}{\sum_{\underset{k_{1} < k_{2}}{k_{2} = a}}^{b}{f\lbrack k_{1},k_{2}\rbrack}}$$

由2.4.5可得

$$\sum_{\underset{k_{1} < k_{2}}{k_{1},k_{2} = a}}^{b}{f\lbrack k_{1},k_{2}\rbrack} = \sum_{k_{1} = a}^{b - 1}{\sum_{k_{2} = k_{1} + 1}^{b}{f\lbrack k_{1},k_{2}\rbrack}}$$

**[定理2.4.7]{.underline}** 对角线切分定理

$$考虑\sum_{k_{1},k_{2} = a}^{b}{f\left\lbrack k_{1},k_{2} \right\rbrack}，其中b > a$$

$$由k_{1} < k_{2},k_{1} > k_{2},k_{1} = k_{2}不能同时存在，$$

并且它们的并组成所有情况，有

$$\sum_{k_{1},k_{2} = a}^{b}{f\left\lbrack k_{1},k_{2} \right\rbrack}$$

$$= \sum_{\begin{array}{r}
k_{1},k_{2} = a \\
k_{1} < k_{2}
\end{array}}^{b}{f\lbrack k_{1},k_{2}\rbrack} + \sum_{\begin{array}{r}
k_{1},k_{2} = a \\
k_{1} > k_{2}
\end{array}}^{b}{f\lbrack k_{1},k_{2}\rbrack} + \sum_{\begin{array}{r}
k_{1},k_{2} = a \\
k_{1} = k_{2}
\end{array}}^{b}{f\lbrack k_{1},k_{2}\rbrack}$$

$$= \sum_{\begin{array}{r}
k_{1},k_{2} = a \\
k_{1} < k_{2}
\end{array}}^{b}{f\lbrack k_{1},k_{2}\rbrack} + \sum_{\begin{array}{r}
k_{1},k_{2} = a \\
k_{1} < k_{2}
\end{array}}^{b}{f\lbrack k_{2},k_{1}\rbrack} + \sum_{k_{1} = a}^{b}{f\lbrack k_{1},k_{1}\rbrack}$$

$$= \sum_{k_{1} = a}^{b - 1}{\sum_{k_{2} = k_{1} + 1}^{b}{(f\lbrack k_{1},k_{2}\rbrack + f\lbrack k_{2},k_{1}\rbrack)}} + \sum_{k_{1} = a}^{b}{f\lbrack k_{1},k_{1}\rbrack}$$

移项并应用2.4.3，得到

$$\sum_{\underset{k_{1} \neq k_{2}}{k_{1},k_{2} = a}}^{b}{f\lbrack k_{1},k_{2}\rbrack} = \sum_{k_{1} = a}^{b - 1}{\sum_{k_{2} = k_{1} + 1}^{b}{(f\lbrack k_{1},k_{2}\rbrack + f\lbrack k_{2},k_{1}\rbrack)}}$$

$$若f具有对称性，即f\lbrack k_{1},k_{2}\rbrack = f\lbrack k_{2},k_{1}\rbrack ，则$$

$$\sum_{\underset{k_{1} \neq k_{2}}{k_{1},k_{2} = a}}^{b}{f\lbrack k_{1},k_{2}\rbrack} = 2\sum_{k_{1} = a}^{b - 1}{\sum_{k_{2} = k_{1} + 1}^{b}{f\left\lbrack k_{1},k_{2} \right\rbrack}}$$

$$若f具有非对角斜对称性，即当k_{1} \neq k_{2}时，有$$

$$f\left\lbrack k_{1},k_{2} \right\rbrack = - f\left\lbrack k_{2},k_{1} \right\rbrack ，则$$

$$\sum_{\underset{k_{1} \neq k_{2}}{k_{1},k_{2} = a}}^{b}{f\lbrack k_{1},k_{2}\rbrack} = 0$$

[]{#_Toc507114574 .anchor}2.5 任选求和形式

定义2.5.1 有序任选求和形式

$$设x_{1},x_{2},\ldots,x_{n}为n个变元,f为r元函数.$$

$\overset{⃑}{t} = \left( t_{1},\ldots,t_{r} \right)为r维向量$，$满足t_{1},t_{2},\ldots,t_{r}互不相等，$

$$并记T = \left\{ t_{1},\ldots,t_{r} \right\},\ \ x_{\overset{⃑}{t}} = \left( x_{t_{1}},\ldots,x_{t_{r}} \right)$$

$$取\delta\lbrack T\rbrack = \left\{ \begin{matrix}
1, & T \subseteq \{ 1,2,\ldots,n\} \\
0, & T \nsubseteq \{ 1,2,\ldots,n\}
\end{matrix} \right.\ $$

$$有序任选求和形式定义为$$

$$\ \ \sum_{T \subseteq \mathbf{Z}\lbrack 1,n\rbrack}^{\ }{f\lbrack x_{\overset{⃑}{t}}\rbrack} ≔ \sum\delta\lbrack T\rbrack f\lbrack x_{\overset{⃑}{t}}\rbrack$$

并为了显示出$r$，形式地记为

$$\sum_{A_{n}^{r} \rightarrow \overset{⃑}{t}}^{\ }{f\lbrack x_{\overset{⃑}{t}}\rbrack} ≔ \sum_{T \subseteq \mathbf{Z}\lbrack 1,n\rbrack}^{\ }{f\lbrack x_{\overset{⃑}{t}}\rbrack}$$

$$此处求和号下的A_{n}^{r}仅仅是一个符号而不是具体的排列数，$$

$$之后求和号下的C_{n}^{r}亦是。$$

**[定理2.5.2]{.underline}** 有序任选求和形式标准化

任选求和实质是以一组数$\left( t_{1},\ldots,t_{r} \right)$为变元的求和，

可通过多重求和及不等求和标准化。

$$\sum_{A_{n}^{r} \rightarrow \overset{⃑}{t}}^{\ }{f\lbrack x_{\overset{⃑}{t}}\rbrack} = \sum_{t_{1} = 1}^{n}{\sum_{\begin{array}{r}
t_{2} = 1 \\
t_{2} \neq t_{1}
\end{array}}^{n}{\ldots\sum_{\begin{array}{r}
t_{r} = 1 \\
t_{r} \neq t_{1} \\
t_{r} \neq t_{2} \\
\ldots \\
t_{r} \neq t_{r - 1}
\end{array}}^{n}{f\lbrack x_{\overset{⃑}{t}}\rbrack}}}$$

证：只需验证右式求和条件满足定义。

由2.4.3常用不等求和形式，

$$\sum_{t_{1} = 1}^{n}{\sum_{\begin{array}{r}
t_{2} = 1 \\
t_{2} \neq t_{1}
\end{array}}^{n}{\ldots\sum_{\begin{array}{r}
t_{r} = 1 \\
t_{r} \neq t_{1} \\
t_{r} \neq t_{2} \\
\ldots \\
t_{r} \neq t_{r - 1}
\end{array}}^{n}{f\lbrack x_{\overset{⃑}{t}}\rbrack}}} = \sum_{\begin{array}{r}
t_{1},\ldots,t_{r} = 1 \\
t_{2} \neq t_{1} \\
t_{3} \neq t_{1} \land t_{3} \neq t_{2} \\
\ldots \\
t_{r} \neq t_{1} \land \ldots \land t_{r} \neq t_{r - 1}
\end{array}}^{n}{f\lbrack x_{\overset{⃑}{t}}\rbrack}$$

求和条件为$t_{1},t_{2},\ldots,t_{r} \in \mathbf{Z}\lbrack 1,n\rbrack 且t_{1},t_{2},\ldots,t_{r}互不相等$

$$显然\left\{ t_{1},t_{2},\ldots,t_{r} \right\} \subseteq \mathbf{Z}\lbrack 1,n\rbrack ，右式求和条件满足定义。$$

因而命题成立。

**[定义2.5.3]{.underline}** 无序任选求和形式

$$设x_{1},x_{2},\ldots,x_{n}为n个变元,f为r元函数.$$

$\overset{⃑}{t} = \left( t_{1},\ldots,t_{r} \right)为r维向量$，$满足t_{1} < t_{2} < \ldots < t_{r}，$

$$并记T = \left\{ t_{1},\ldots,t_{r} \right\},\ \ x_{\overset{⃑}{t}} = \left( x_{t_{1}},\ldots,x_{t_{r}} \right)$$

$$取\delta\lbrack T\rbrack = \left\{ \begin{matrix}
1, & T \subseteq \left\{ 1,2,\ldots,n \right\} \\
0, & T \nsubseteq \{ 1,2,\ldots,n\}
\end{matrix} \right.\ $$

$$无序任选求和形式定义为$$

$$\ \ \sum_{T \subseteq \mathbf{Z}\lbrack 1,n\rbrack}^{\ }{f\lbrack x_{\overset{⃑}{t}}\rbrack} ≔ \sum\delta\lbrack T\rbrack f\lbrack x_{\overset{⃑}{t}}\rbrack$$

并为了显示出$r$，形式地记为

$$\sum_{C_{n}^{r} \rightarrow \overset{⃑}{t}}^{\ }{f\lbrack x_{\overset{⃑}{t}}\rbrack} ≔ \sum_{T \subseteq \mathbf{Z}\lbrack 1,n\rbrack}^{\ }{f\lbrack x_{\overset{⃑}{t}}\rbrack}$$

**[定理2.5.4]{.underline}** 无序任选求和形式标准化

$$\sum_{C_{n}^{r} \rightarrow \overset{⃑}{t}}^{\ }{f\left\lbrack x_{\overset{⃑}{t}} \right\rbrack} = \sum_{t_{1} = 1}^{n - r + 1}{\sum_{t_{2} = t_{1} + 1}^{n - r + 2}{\ldots\sum_{t_{r} = t_{r - 1} + 1}^{n}{f\left\lbrack x_{\overset{⃑}{t}} \right\rbrack}}}$$

证：直接把所有条件写在求和号下，并且拆分小于号。

$$\sum_{C_{n}^{r} \rightarrow \overset{⃑}{t}}^{\ }{f\left\lbrack x_{\overset{⃑}{t}} \right\rbrack} = \sum_{1 \leq t_{1} < t_{2} < \ldots < t_{n} \leq n}^{\ }{f\left\lbrack x_{\overset{⃑}{t}} \right\rbrack} = \sum_{t_{1} = 1}^{n}{\sum_{\begin{array}{r}
t_{2} = 1 \\
t_{1} < t_{2}
\end{array}}^{n}{\ldots\sum_{\begin{array}{r}
t_{r} = 1 \\
t_{r - 1} < t_{r}
\end{array}}^{n}{f\left\lbrack x_{\overset{⃑}{t}} \right\rbrack}}}$$

利用常用小于求和形式并控制上下限即得。

$$\sum_{t_{1} = 1}^{n}{\sum_{\begin{array}{r}
t_{2} = 1 \\
t_{1} < t_{2}
\end{array}}^{n}{\ldots\sum_{\begin{array}{r}
t_{r} = 1 \\
t_{r - 1} < t_{r}
\end{array}}^{n}{f\left\lbrack x_{\overset{⃑}{t}} \right\rbrack}}} = \sum_{t_{1} = 1}^{n - r + 1}{\sum_{t_{2} = t_{1} + 1}^{n - r + 2}{\ldots\sum_{t_{r} = t_{r - 1} + 1}^{n}{f\left\lbrack x_{\overset{⃑}{t}} \right\rbrack}}}$$

在对上文内容进行说明之前，先说明一些概念。

**置换**$\sigma$是有限集合到它自身的双射。

不考虑具体元素，不妨设有限集合为$\mathbf{Z}\lbrack 1,n\rbrack = \left\{ 1,2,\ldots,n \right\}$

$$一般用2 \times n矩阵表示某个置换:\begin{pmatrix}
1 & 2 & \ldots & n \\
\sigma\lbrack 1\rbrack & \sigma\lbrack 2\rbrack & \ldots & \sigma\lbrack n\rbrack
\end{pmatrix}$$

$$对某个n，所有\sigma 组成集合S_{n}$$

$例：当n = 3时$,$S_{n} = \{\begin{pmatrix}
1 & 2 & 3 \\
1 & 2 & 3
\end{pmatrix},\begin{pmatrix}
1 & 2 & 3 \\
1 & 3 & 2
\end{pmatrix},$

$$\begin{pmatrix}
1 & 2 & 3 \\
2 & 1 & 3
\end{pmatrix},\begin{pmatrix}
1 & 2 & 3 \\
2 & 3 & 1
\end{pmatrix},\begin{pmatrix}
1 & 2 & 3 \\
3 & 1 & 2
\end{pmatrix},\begin{pmatrix}
1 & 2 & 3 \\
3 & 2 & 1
\end{pmatrix}\}$$

$$n元函数f\left\lbrack x_{1},\ldots,x_{n} \right\rbrack 称作是\mathbf{对称的}，如果对任意的\sigma \in S_{n}$$

$$有f\left\lbrack x_{1},\ldots,x_{n} \right\rbrack = f\left\lbrack x_{\sigma\lbrack 1\rbrack},\ldots,x_{\sigma\lbrack n\rbrack} \right\rbrack$$

$$例：韦达定理出现的多项式都是对称n元函数。如：$$

$$x_{1} + x_{2} + x_{3},\ \ x_{1}x_{2} + x_{1}x_{3} + x_{2}x_{3},\ \ x_{1}x_{2}x_{3}$$

对比有序和无序求和形式，可以发现仅有一处重要差别。在无序形式中，向量$\overset{⃑}{t}$各分量从互相不等加强为从小到大排列。

这是因为这种形式常用在**函数是对称的**的情况下，选出的$r$个变元的不同排列对函数没有影响，对每种排列求和就造成重复，因此只需选择其中任意一种排列即可。而选中从小到大的排列方式是为了明确起见。

而若函数不是对称的，变元的不同排列得到的结果就不同。一些时候有奇效，但大多数情况不容易分析。

$$例：取n = 4;r = 2;f\left\lbrack x_{\overset{⃑}{t}} \right\rbrack = x_{t_{1}}x_{t_{2}}，此时f是对称的。$$

$$\sum_{A_{4}^{2} \rightarrow \overset{⃑}{t}}^{\ }{x_{t_{1}}x_{t_{2}}} = x_{1}x_{2} + x_{1}x_{3} + x_{1}x_{4} + x_{2}x_{1} + x_{2}x_{3} + x_{2}x_{4} + x_{3}x_{1} + x_{3}x_{2} + x_{3}x_{4} + x_{4}x_{1} + x_{4}x_{2} + x_{4}x_{3}$$

$$\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  = 2\left( x_{1}x_{2} + x_{1}x_{3} + x_{1}x_{4} + x_{2}x_{3} + x_{2}x_{4} + x_{3}x_{4} \right)$$

$$\sum_{C_{4}^{2} \rightarrow \overset{⃑}{t}}^{\ }{x_{t_{1}}x_{t_{2}}} = x_{1}x_{2} + x_{1}x_{3} + x_{1}x_{4} + x_{2}x_{3} + x_{2}x_{4} + x_{3}x_{4}$$

$$取n = 4;r = 3;f\left\lbrack x_{\overset{⃑}{t}} \right\rbrack = x_{t_{1}}x_{t_{2}}，此时f不是对称的。$$

$$\sum_{A_{4}^{3} \rightarrow \overset{⃑}{t}}^{\ }{x_{t_{1}}x_{t_{2}}} = x_{1}x_{2} + x_{1}x_{2} + x_{1}x_{3} + x_{1}x_{3} + x_{1}x_{4} + x_{1}x_{4} + x_{2}x_{1} + x_{2}x_{1} + x_{2}x_{3} + x_{2}x_{3} + x_{2}x_{4} + x_{2}x_{4} + x_{3}x_{1} + x_{3}x_{1} + x_{3}x_{2} + x_{3}x_{2} + x_{3}x_{4} + x_{3}x_{4} + x_{4}x_{1} + x_{4}x_{1} + x_{4}x_{2} + x_{4}x_{2} + x_{4}x_{3} + x_{4}x_{3}$$

$$\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  = 4\left( x_{1}x_{2} + x_{1}x_{3} + x_{1}x_{4} + x_{2}x_{3} + x_{2}x_{4} + x_{3}x_{4} \right)$$

$$\sum_{C_{4}^{3} \rightarrow \overset{⃑}{t}}^{\ }{x_{t_{1}}x_{t_{2}}} = x_{1}x_{2} + x_{1}x_{2} + x_{1}x_{3} + x_{2}x_{3}$$

**[定理2.5.5]{.underline}** 项数计数定理

若把函数$f\lbrack x_{\overset{⃑}{t}}\rbrack$看成一项，则

$$\sum_{A_{n}^{r} \rightarrow \overset{⃑}{t}}^{\ }{f\left\lbrack x_{\overset{⃑}{t}} \right\rbrack}项数为A_{n}^{r} = \frac{n!}{(n - r)!} = (n)_{r}$$

$$\sum_{C_{n}^{r} \rightarrow \overset{⃑}{t}}^{\ }{f\lbrack x_{\overset{⃑}{t}}\rbrack}项数为C_{n}^{r} = \frac{n!}{(n - r)!r!} = \frac{(n)_{r}}{(r)_{r}}$$

证：对于有序任选求和形式而言，

$$求和条件为t_{1},\ldots,t_{r}互不相同且都在\mathbf{Z}\lbrack 1,n\rbrack 内。$$

$$则t_{1}有n种取法，t_{2}有n - 1种取法,\ldots,t_{r}有n - r + 1种取法。$$

$$由乘法计数原理可知总共有\frac{n!}{(n - r)!}种取法。$$

$$对于相同的集合\left. （更贴切地说，值域 \right.）\left\{ t_{1},t_{2},\ldots,t_{r} \right\}$$

在有序形式中共有全排列$r!$种，而在无序形式中只算作1种。

$$因此\frac{n!}{(n - r)!}再除以r!就是无序任选求和形式的项数。$$

**[推论2.5.6]{.underline}** 重复计数定理

若$f\lbrack x_{\overset{⃑}{t}}\rbrack$为对称函数，则

$$\sum_{A_{n}^{r} \rightarrow \overset{⃑}{t}}^{\ }{f\left\lbrack x_{\overset{⃑}{t}} \right\rbrack} = r! \times \sum_{C_{n}^{r} \rightarrow \overset{⃑}{t}}^{\ }{f\lbrack x_{\overset{⃑}{t}}\rbrack}$$

证：由2.5.5的证明可知，对于相同的集合$\left\{ t_{1},t_{2},\ldots,t_{r} \right\}$，由于函数$f$是对称的，因而不论如何排列结果都相同，而在有序形式中共计算了$r!$次，在无序形式中只计算了1次，因此两种求和形式之间相差一个系数。

应用2.5.7

$$\left( \prod_{k = 1}^{n}\left( x - a_{k} \right) \right)^{'} = \sum_{C_{n}^{n - 1} \rightarrow \overset{⃑}{t}}^{\ }{\prod_{k = 1}^{n - 1}{(x - a_{t_{k}})}}$$

$$\left( \prod_{k = 1}^{n}\left( x - a_{k} \right) \right)^{''} = \sum_{C_{n}^{n - 1} \rightarrow \overset{⃑}{t}}^{\ }{\sum_{C_{n - 1}^{n - 2} \rightarrow \overset{⃑}{r}}^{\ }{\prod_{k = 1}^{n - 2}{(x - a_{r_{t_{k}}})}}}$$

[]{#_Toc507114575 .anchor}2.6 置换轮换对称求和形式

**[定义2.6.1]{.underline}** 置换求和形式

$$设\phi\lbrack\sigma\rbrack 是以置换\left. （概念见上节 \right.）集合为定义域的映射，$$

$$取\delta\lbrack\sigma\rbrack = \left\{ \begin{array}{r}
\begin{matrix}
1, & \sigma \in S_{n}
\end{matrix} \\
\begin{matrix}
0, & \sigma \notin S_{n}
\end{matrix}
\end{array} \right.\ $$

则置换求和形式定义为

$$\sum_{\sigma \in S_{n}}^{\ }{\phi\lbrack\sigma\rbrack} ≔ \sum_{}^{}{\delta\lbrack\sigma\rbrack}\phi\lbrack\sigma\rbrack$$

说明：置换$\sigma$是一个函数，而$\delta$是置换到一个数（0或1）的映射，因而事实上$\delta$是一个泛函，求和不再是遍历每个可能的数，而是遍历每种可能的函数。同样地，$\phi$是置换到一个数，或者一个函数，甚至别的事物的映射。在求和中真正变的不是$k_{1}或者x_{1},x_{2}$，而是函数$\sigma.$

由于$\sigma$的特殊性（离散且有限），置换$\sigma$由$n$个数$\sigma\lbrack 1\rbrack,\sigma\lbrack 2\rbrack,\ldots,\sigma\lbrack n\rbrack$唯一确定。因此将$\delta 或者\phi$看作$n$元函数理解也是可以的。

事实上，若$\phi\lbrack\sigma\rbrack$可表为$f\left\lbrack x_{\sigma\lbrack 1\rbrack},x_{\sigma\lbrack 2\rbrack},\ldots,x_{\sigma\lbrack n\rbrack} \right\rbrack 的形式，$

$$则令t_{k} = \sigma\lbrack k\rbrack,k \in \mathbf{Z}\lbrack 1,n\rbrack,$$

$$易证\sum_{\sigma \in S_{n}}^{\ }{\phi\lbrack\sigma\rbrack} = \sum_{A_{n}^{n} \rightarrow \overset{⃑}{t}}^{\ }{f\lbrack x_{\overset{⃑}{t}}\rbrack}$$

在介绍轮换求和形式之前，先引入一类特殊的置换。

$$置换\tau = \begin{pmatrix}
1 & 2 & \ldots & n - 1 & n \\
2 & 3 & \ldots & n & 1
\end{pmatrix} \in S_{n}$$

$$利用复合映射得到\tau^{2} = \begin{pmatrix}
1 & 2 & \ldots & n - 2 & n - 1 & n \\
3 & 4 & \ldots & n & 1 & 2
\end{pmatrix}$$

$$并归纳定义\tau^{k} = \tau \circ \tau^{k - 1}$$

显然有$\tau^{k}\lbrack m\rbrack = \left\{ \begin{array}{r}
\begin{matrix}
m + k & 1 \leq k \leq n - m
\end{matrix} \\
\begin{matrix}
m + k - n & n - m < k \leq 2n - m
\end{matrix}
\end{array} \right.\ ，$

$$\tau^{n} = 恒等映射e$$

**[定义2.6.2]{.underline}** 轮换求和形式

$$设\phi\lbrack\sigma\rbrack 是以\left\{ \tau^{k} \middle| k \in \mathbf{Z}\lbrack 1,n\rbrack \right\} 为定义域的映射，$$

轮换求和形式定义为

$$\sum_{cyc}^{\ }{\phi\lbrack\sigma\rbrack} ≔ \sum_{k = 1}^{n}{\phi\lbrack\tau^{k}\rbrack}$$

此定义式可直接用于计算。

实际计算时，往往让$k从0递增至n - 1，所得结果相同。$

$$例：\sum_{cyc}^{\ }{x_{\sigma\lbrack 1\rbrack}^{2}x_{\sigma\lbrack 2\rbrack}} = x_{1}^{2}x_{2} + x_{2}^{2}x_{3} + \ldots + x_{n - 1}^{2}x_{n} + x_{n}^{2}x_{1}$$

**[定义2.6.3]{.underline}** 对称求和形式

与置换求和形式完全相同。

$$\sum_{sym}^{\ }{\phi\lbrack\sigma\rbrack} ≔ \sum_{\sigma \in S_{n}}^{\ }{\phi\lbrack\sigma\rbrack}$$

注1：对称、置换求和形式从符号上无法得到$n$，如果是具体的数值需要单独注明。

注2：大部分资料给出的轮换、对称求和形式中默认$n = 3$，并将$x_{1},x_{2},x_{3}$换为$x,y,z或a,b,c$表示。本书中不采用这一规定。

[]{#_Toc507114576 .anchor}3 多项式

$$\left( \sum_{k = 1}^{n}x_{k} \right)^{2}$$

$$= \left( \sum_{k = 1}^{n}x_{k} \right)\left( \sum_{k = 1}^{n}x_{k} \right) =^{(1.4)}\sum_{k_{1} = 1}^{n}{\sum_{k_{2} = 1}^{n}{x_{k}}_{1}x_{k_{2}}}$$

$$=^{(2.4.7)}\sum_{k = 1}^{n}x_{k}^{2} + \sum_{\begin{array}{r}
k_{1},k_{2} = 1 \\
k_{1} \neq k_{2}
\end{array}}^{n}{x_{k_{1}}x_{k_{2}}}$$

$$=^{(2.4.7)}\sum_{\begin{array}{r}
k_{1},k_{2} = 1 \\
k_{1} < k_{2}
\end{array}}^{n}{x_{k_{1}}x_{k_{2}}} + \sum_{\begin{array}{r}
k_{1},k_{2} = 1 \\
k_{1} > k_{2}
\end{array}}^{n}{x_{k_{1}}x_{k_{2}}} + \sum_{\begin{array}{r}
k_{1},k_{2} = 1 \\
k_{1} = k_{2}
\end{array}}^{n}{x_{k_{1}}x_{k_{2}}}$$

$$=^{(2.4.7)}\sum_{k = 1}^{n}x_{k}^{2} + 2\sum_{\begin{array}{r}
k_{1},k_{2} = 1 \\
k_{1} > k_{2}
\end{array}}^{n}{x_{k_{1}}x_{k_{2}}}$$

$$=_{(n \geq 2)}^{(2.4.6)}\sum_{k = 1}^{n}x_{k}^{2} + 2\sum_{k_{1} = 1}^{n - 1}{\sum_{k_{2} = 2}^{n}{x_{k_{1}}x_{k_{2}}}}$$

$$\left( \sum_{k = 0}^{n}{a_{k}x^{k}} \right)\left( \sum_{k = 0}^{n}{b_{k}x^{k}} \right)$$

$$= \sum_{k_{1} = 0}^{n}{\sum_{k_{2} = 0}^{n}{b_{k_{2}}x^{k_{2}}}a_{k_{1}}x^{k_{1}}}$$

$$= \sum_{k_{1} = 0}^{n}{\sum_{k_{2} = 0}^{n}{a_{k_{1}}b_{k_{2}}x^{k_{1} + k_{2}}}}$$

$$= \sum_{t = 0}^{2n}{\left( \sum_{\begin{array}{r}
k_{1},k_{2} = 0 \\
k_{1} + k_{2} = t
\end{array}}^{n}{a_{k_{1}}b_{k_{2}}} \right)x^{t}}$$

由$k_{1},k_{2} \in \mathbf{Z}\lbrack 0,n\rbrack,k_{2} = t - k_{1}$

$$得k_{1} \in \lbrack max\{ t - n,0\},min\{ t,n\}\rbrack$$

$$当t \leq n时，k_{1} \in \lbrack 0,t\rbrack;当t \geq n时，k_{1} \in \lbrack t - n,n\rbrack;$$

$$\sum_{t = 0}^{2n}{\left( \sum_{\begin{array}{r}
k_{1},k_{2} = 0 \\
k_{1} + k_{2} = t
\end{array}}^{n}{a_{k_{1}}b_{k_{2}}} \right)x^{t}}$$

$$= \sum_{t = 0}^{n}{\left( \sum_{k = 0}^{t}{a_{k}b_{t - k}} \right)x^{t}} + \sum_{t = n + 1}^{2n}{\left( \sum_{k = t - n}^{n}{a_{k}b_{t - k}} \right)x^{t}}$$

$$=_{②新t = 2n - 旧t}^{①新k = 旧k - t + n}\sum_{t = 0}^{n}{\left( \sum_{k = 0}^{t}{a_{k}b_{t - k}} \right)x^{t}} + \sum_{t = 0}^{n - 1}{\left( \sum_{k = 0}^{t}{a_{k + n - t}b_{n - k}} \right)x^{2n - t}}$$

$$a^{p + 1} - b^{p + 1} = (a - b)\sum_{k = 0}^{p}{a^{p - k}b^{k}}\ \ \ \ \ (p \in \mathbf{N})$$

证明：

$$右边 = \sum_{k = 0}^{p}{a^{p + 1 - k}b^{k}} - \sum_{k = 0}^{p}{a^{p - k}b^{k + 1}}$$

$$= \sum_{k = 0}^{p}{a^{p + 1 - k}b^{k}} - \sum_{k = 1}^{p + 1}{a^{p - k + 1}b^{k}}$$

$$= a^{p + 1} - b^{p + 1}$$

[]{#_Toc507114577 .anchor}4.1 阿贝尔分部求和定理

$$\sum_{k = 1}^{n}{a_{k}b_{k}}$$

$$=^{n \geq 2}a_{1}b_{1} + \sum_{k = 2}^{n}{a_{k}b_{k}}$$

$$= a_{1}b_{1} + \sum_{k_{1} = 2}^{n}{\left( \sum_{k_{2} = 1}^{k_{1}}{a_{k}}_{2} - \sum_{k_{2} = 1}^{k_{1} - 1}a_{k_{2}} \right)b_{k_{1}}}$$

$$= a_{1}b_{1} + \sum_{k_{1} = 2}^{n}\left( b_{k_{1}}\sum_{k_{2} = 1}^{k_{1}}{a_{k}}_{2} \right) - \sum_{k_{1} = 2}^{n}\left( b_{k_{1}}\sum_{k_{2} = 1}^{k_{1} - 1}{a_{k}}_{2} \right)$$

$$= a_{1}b_{1} + \sum_{k_{1} = 2}^{n}\left( b_{k_{1}}\sum_{k_{2} = 1}^{k_{1}}{a_{k}}_{2} \right) - \sum_{k_{1} = 1}^{n - 1}\left( b_{k_{1} + 1}\sum_{k_{2} = 1}^{k_{1}}{a_{k}}_{2} \right)$$

$$= a_{1}b_{1} + \sum_{k_{1} = 1}^{n - 1}\left( b_{k_{1}}\sum_{k_{2} = 1}^{k_{1}}{a_{k}}_{2} \right) + b_{n}\sum_{k_{2} = 1}^{n}{a_{k}}_{2} - b_{1}\sum_{k_{2} = 1}^{1}{a_{k}}_{2} - \sum_{k_{1} = 1}^{n - 1}\left( b_{k_{1} + 1}\sum_{k_{2} = 1}^{k_{1}}{a_{k}}_{2} \right)$$

$$= \sum_{k_{1} = 1}^{n - 1}\left( (b_{k_{1}} - b_{k_{1} + 1})\sum_{k_{2} = 1}^{k_{1}}{a_{k}}_{2} \right) + b_{n}\sum_{k_{2} = 1}^{n}{a_{k}}_{2}$$

$$记\sum_{k = 1}^{m}a_{k} = A_{m},\sum_{k = 1}^{m}b_{k} = B_{m},a_{k + 1} - a_{k} = \alpha_{k},b_{k + 1} - b_{k} = \beta_{k}$$

$$\sum_{k = 1}^{n}{a_{k}b_{k}}$$

$$= A_{n}b_{n} - \sum_{k = 1}^{n - 1}{A_{k}\beta_{k}}$$

$$= a_{n}B_{n} - \sum_{k = 1}^{n - 1}{\alpha_{k}B_{k}}$$

$$= A_{n}b_{n + 1} - \sum_{k = 1}^{n}{A_{k}\beta_{k}}$$

$$= a_{n + 1}B_{n} - \sum_{k = 1}^{n}{\alpha_{k}B_{k}}$$

[]{#_Toc507114578 .anchor}4.2 定义计算积分

闭区间$\lbrack a,b\rbrack(a < b)$的分划$P$指的是由这个区间的有限多个点$x_{0},\ldots,x_{n}$组成的点组，其中$a = x_{0} < x_{1} < \ldots < x_{n} = b.$

$$区间\left\lbrack x_{i - 1},x_{i} \right\rbrack(i = 1,\ldots,n)叫做分划P的区间.$$

$$分划P的最大区间长\lambda(P)叫做分划P的参数.$$

$$\xi_{i} \in \left\lbrack x_{i - 1},x_{i} \right\rbrack(i = 1,\ldots,n)为每个区间中选定的一个点.$$

积分的定义为

$$\int_{a}^{b}{f(x)dx} ≔ \lim_{\lambda(P) \rightarrow 0}{\sum_{i = 1}^{n}{f\left( \xi_{i} \right)\mathrm{\Delta}x_{i}}}$$

以上内容节选自《数学分析》[^1]

$$为了计算上面的求和式，作一些具体的设定。$$

$$确定分划P,令x_{k} - x_{k - 1} = \frac{b - a}{n},k \in \mathbf{Z}\lbrack 1,n\rbrack$$

$$则每个区间长相等，\lambda(P) = \mathrm{\Delta}x_{k} = \frac{b - a}{n}$$

$$此时n \rightarrow + \infty\  \Rightarrow \ \lambda(P) \rightarrow 0$$

$$每个区间的点\xi_{k}选为左端点x_{k} = a + \frac{k}{n}(b - a)$$

于是得到计算式

$$\int_{a}^{b}{f\lbrack x\rbrack dx} = \lim_{n \rightarrow + \infty}{\sum_{k = 1}^{n}{f\left\lbrack a + \frac{k}{n}(b - a) \right\rbrack\frac{b - a}{n}}}$$

$$= (b - a)\lim_{n \rightarrow + \infty}{\sum_{k = 1}^{n}{\frac{1}{n}f\left\lbrack \frac{(b - a)}{n}k + a \right\rbrack}}$$

$$= (b - a)\lim_{n \rightarrow + \infty}{\sum_{\begin{array}{r}
k = (b - a) + na \\
\mathrm{\Delta}(b - a)
\end{array}}^{nb}{\frac{1}{n}f\left\lbrack \frac{k}{n} \right\rbrack}}$$

第二、三行都是可用的计算式，但有时它们其中一种会更简单一些。

下面是一些例子。

$$\int_{1}^{2}{x^{2}dx} = \lim_{n \rightarrow + \infty}{\sum_{k = 1}^{n}{\left( 1 + \frac{k}{n} \right)^{2}\frac{1}{n}}}$$

$$= \lim_{n \rightarrow + \infty}{\sum_{k = 1}^{n}\frac{n^{2} + 2nk + k^{2}}{n^{3}}}$$

$$= \lim_{n \rightarrow + \infty}\frac{n^{3} + n^{2}(n + 1) + \frac{1}{6}n(n + 1)(2n + 1)}{n^{3}}$$

$$= 1 + 1 + \frac{1}{3} = \frac{7}{3}$$

$$\int_{1}^{2}{x^{2}dx} = \lim_{n \rightarrow + \infty}{\sum_{\begin{array}{r}
k = 1 + n \\
\mathrm{\Delta}1
\end{array}}^{2n}{\frac{1}{n}\left( \frac{k}{n} \right)^{2}}} = \lim_{n \rightarrow + \infty}{\frac{1}{n^{3}}\left( \sum_{k = 1}^{2n}k^{2} - \sum_{k = 1}^{n}k^{2} \right)}$$

$$= \lim_{n \rightarrow + \infty}\frac{2n(2n + 1)(4n + 1) - n(n + 1)(2n + 1)}{6n^{3}} = \frac{7}{3}$$

$$求\int_{}^{}{\cos xdx}$$

$$计算\int_{0}^{x}{\cos tdt}，然后将常数用C换掉。$$

$$\int_{0}^{x}{\cos tdt} = \lim_{n \rightarrow + \infty}{\sum_{k = 1}^{n}{{\frac{x}{n}\cos}\frac{xk}{n}}}$$

$$=^{(5.3)}\lim_{n \rightarrow + \infty}\frac{x\cos\left\lbrack \frac{n + 1}{2n}x \right\rbrack\sin\frac{x}{2}}{n\sin\frac{x}{2n}}$$

$$= \frac{\lim_{n \rightarrow + \infty}x\cos\left\lbrack \frac{n + 1}{2n}x \right\rbrack\sin\frac{x}{2}}{\lim_{n \rightarrow + \infty}n\left( \frac{x}{2n} + O\left( \frac{x^{3}}{8n^{3}} \right) \right)}$$

$$= \frac{x\cos\left\lbrack \frac{x}{2} \right\rbrack\sin\frac{x}{2}}{\frac{x}{2}} = \sin x$$

$$于是\int_{}^{}{\cos xdx} = \sin x + C$$

当然这样计算定积分效率很低，一般不会这么算。不过这个公式还有别的用处。

其一是利用积分求和式极限。只要确定了对应的参数，就可以计算定积分来求形如

$$\lim_{n \rightarrow + \infty}{\sum_{k = 1}^{n}{f\lbrack k,n\rbrack}}$$

的极限。

$$例：求\lim_{n \rightarrow + \infty}{\frac{1}{n^{\alpha + 1}}\sum_{k = 1}^{n}k^{\alpha}}$$

对比式子

$$\int_{a}^{b}{f\lbrack x\rbrack dx} = \lim_{n \rightarrow + \infty}{\sum_{k = 1}^{n}{f\left\lbrack a + \frac{k}{n}(b - a) \right\rbrack\frac{b - a}{n}}}$$

$$取a = 0,f\lbrack x\rbrack = x^{\alpha}，得b = 1$$

$$于是\lim_{n \rightarrow + \infty}{\frac{1}{n^{\alpha + 1}}\sum_{k = 1}^{n}k^{\alpha}} = \int_{0}^{1}{x^{\alpha}dx} = \frac{1}{\alpha + 1}$$

$$例：求\lim_{n \rightarrow + \infty}{\frac{1}{n}\sum_{k = 1}^{n}{\ln\left( 1 + \frac{k}{n} \right)}}$$

$$取a = 1,b = 2,f\lbrack x\rbrack = \ln x$$

$$\lim_{n \rightarrow + \infty}{\frac{1}{n}\sum_{k = 1}^{n}{\ln\left( 1 + \frac{k}{n} \right)}} = \int_{1}^{2}{\ln xdx} = 2\ln 2 - 2 - \ln 1 + 1$$

$$= 2\ln 2 - 1$$

$$例：求\lim_{n \rightarrow + \infty}{\sum_{k = 1}^{n}\frac{( - 1)^{k - 1}}{k}}$$

$$取a = 0,b = n,f\lbrack x\rbrack = \frac{( - 1)^{x - 1}}{x}，发现无法计算。$$

事实上，尝试各种$a,b,f\lbrack x\rbrack$组合均以失败告终。怎么办呢？

这里可以用到一个变换消去交错项。

$$\lim_{n \rightarrow + \infty}{\sum_{k = 1}^{n}\frac{( - 1)^{k - 1}}{k}} = \lim_{n \rightarrow + \infty}{\sum_{k = 1}^{2n}\frac{( - 1)^{k - 1}}{k}}$$

$$= \lim_{n \rightarrow + \infty}\left( \sum_{k = 1}^{n}\frac{( - 1)^{2k - 1}}{2k} + \sum_{k = 1}^{n}\frac{( - 1)^{2k - 1 - 1}}{2k - 1} \right)$$

$$= \lim_{n \rightarrow + \infty}\left( \sum_{k = 1}^{n}\frac{1}{2k - 1} - \sum_{k = 1}^{n}\frac{1}{2k} \right)$$

$$= \lim_{n \rightarrow + \infty}\left( \sum_{k = 1}^{n}\frac{1}{2k - 1} + \sum_{k = 1}^{n}\frac{1}{2k} - 2\sum_{k = 1}^{n}\frac{1}{2k} \right)$$

$$= \lim_{n \rightarrow + \infty}\left( \sum_{k = 1}^{2n}\frac{1}{k} - \sum_{k = 1}^{n}\frac{1}{k} \right) = \lim_{n \rightarrow + \infty}{\sum_{k = n + 1}^{2n}\frac{1}{k}} = \lim_{n \rightarrow + \infty}{\sum_{k = 1}^{n}\frac{1}{k + n}}$$

$$取a = 1,b = 2,f\lbrack x\rbrack = \frac{1}{x}$$

$$\lim_{n \rightarrow + \infty}{\sum_{k = 1}^{n}\frac{1}{k + n}} = \int_{1}^{2}{\frac{1}{x}dx} = \ln 2$$

在本节最后，提出三个问题：

1.  是否能归纳出上面利用积分求极限的一般过程，并且找出它的局限性（即什么形式的极限无法求）？

2.  有一些难以计算的积分，是否能通过求和极限简单解决（即公式的第二个用处）？

3.  本节是在划分$P$为均匀划分情况下建立的。对于别的划分$P$，如指数划分，黄金划分等等，情况又会如何呢？

4.3 无穷级数性质

本书中几乎全部其他的讨论都没有涉及无穷求和的内容。这一节

将简要讨论在无穷的情况下一些定理是否还可使用。

本节参考资料：

\[1\]张筑生《数学分析新讲》第三册，第十八章

\[2\]B.A.卓里奇《数学分析》第一卷，第三章

**[定义4.3.1]{.underline}** 无穷级数及其收敛性

$$\sum_{k = a}^{\infty}{f\lbrack k\rbrack} ≔ \lim_{n \rightarrow + \infty}{\sum_{k = a}^{n}{f\lbrack k\rbrack}}$$

$$若存在S，对\forall\varepsilon > 0,\exists N,当n > N时成立$$

$$\left| \sum_{k = a}^{n}{f\lbrack k\rbrack} - S \right| < \varepsilon$$

$$则称无穷级数\sum_{k = a}^{\infty}{f\lbrack k\rbrack}收敛，并记\sum_{k = a}^{\infty}{f\lbrack k\rbrack} = S$$

$$否则称无穷级数\sum_{k = a}^{\infty}{f\lbrack k\rbrack}发散。$$

**[定义4.3.2]{.underline}** 正项无穷级数、绝对收敛和条件收敛

$$对于无穷级数\sum_{k = a}^{\infty}{f\lbrack k\rbrack},若f\lbrack a + t\rbrack > 0对任意t \in \mathbf{N}成立，$$

$$则称无穷级数\sum_{k = a}^{\infty}{f\lbrack k\rbrack}为正项无穷级数。$$

$$若无穷级数\sum_{k = a}^{\infty}\left| f\lbrack k\rbrack \right|收敛，则称\sum_{k = a}^{\infty}{f\lbrack k\rbrack}绝对收敛。$$

绝对收敛蕴含收敛，证明略。

显然，正项级数收敛等价于正项级数绝对收敛。

$$若无穷级数\sum_{k = a}^{\infty}{f\lbrack k\rbrack}收敛，但\sum_{k = a}^{\infty}\left| f\lbrack k\rbrack \right|发散，$$

$$则称\sum_{k = a}^{\infty}{f\lbrack k\rbrack}条件收敛。$$

**[讨论4.3.3]{.underline}** 换元

在有限求和中，常见的换元有$k_{2} = k_{1} + m,k_{2} = m - k_{1}$两种形式。

对无穷级数应用第一种换元。

$$\sum_{k_{1} = a}^{\infty}{f\left\lbrack k_{1} \right\rbrack} = \sum_{k_{2} = a + m}^{\infty}{f\left\lbrack k_{2} - m \right\rbrack}$$

发现实际参与求和的项$(f\lbrack a\rbrack,f\lbrack a + 1\rbrack,\ldots)$没有任何变化。

因此第一种换元是可行的。

$$如\sum_{k = 1}^{\infty}q^{k} = \sum_{k = 0}^{\infty}q^{k + 1} = q\sum_{k = 0}^{\infty}q^{k} = \frac{q}{1 - q}$$

应用第二种换元，

$$\sum_{k_{1} = a}^{\infty}{f\left\lbrack k_{1} \right\rbrack} = \sum_{k_{2} = - \infty}^{m - a}{f\left\lbrack m - k_{2} \right\rbrack}$$

虽然参与求和的项事实上没有变化，但是右端的式子并不容易计算，因此这一种换元在无穷级数中基本不用。

利用换元，我们总能把从$f\lbrack a\rbrack$开始的无穷级数转化为$g\lbrack 1\rbrack$开始的无穷级数。

$$\sum_{k_{1} = a}^{\infty}{f\left\lbrack k_{1} \right\rbrack} =^{(k ≔ k_{1} - a + 1)} = \sum_{k = 1}^{\infty}{f\lbrack k + a - 1\rbrack} =^{g\lbrack k\rbrack ≔ f\lbrack k + a - 1\rbrack}\sum_{k = 1}^{\infty}{g\lbrack k\rbrack}$$

$$函数f的任意性对应函数g的任意性，$$

$$因此讨论无穷级数\sum_{k_{1} = a}^{\infty}{f\left\lbrack k_{1} \right\rbrack}相当于讨论无穷级数\sum_{k = 1}^{\infty}{f\lbrack k\rbrack}$$

简洁起见，下文将不再讨论前一种级数。

\*此段仍存疑

**[讨论4.3.4]{.underline}** 分组求和

分组求和即分配律的应用，对于收敛的级数是确定可行的。

$$在1,2,\ldots 中选无穷个分点，即取b_{0},b_{1},\ldots \in \mathbf{Z}$$

$$且\ \ (1 = b_{0} < b_{1} < \ldots)$$

即$f\lbrack 1\rbrack + f\lbrack 2\rbrack + \ldots$

$$= \left( f\left\lbrack b_{0} \right\rbrack + \ldots + f\left\lbrack b_{1} - 1 \right\rbrack \right) + \left( f\left\lbrack b_{1} \right\rbrack + \ldots + f\left\lbrack b_{2} - 1 \right\rbrack \right) + \ldots$$

写成分组求和形式。

$$\sum_{k = 1}^{\infty}{f\lbrack k\rbrack} = \sum_{k_{1} = 0}^{\infty}{\sum_{k_{2} = b_{k_{1}}}^{b_{k_{1} + 1} - 1}{f\lbrack k_{2}\rbrack}}$$

证明参见参考资料\[1\]。另外，选取有限个分点，令最后一组有无穷项显然也是可行的。

对于发散的级数，一般不能这么操作。如：

$$\sum_{k = 0}^{\infty}( - 1)^{k}是一发散级数，$$

$$若取b_{m} = 2m,则会得到\sum_{k_{1} = 0}^{\infty}{\sum_{k_{2} = b_{k_{1}}}^{b_{k_{1} + 1} - 1}{f\left\lbrack k_{2} \right\rbrack}} = \sum_{k_{1} = 0}^{\infty}{\sum_{k_{2} = 2k_{1}}^{2k_{1} + 1}( - 1)^{k_{2}}}$$

$$= \sum_{k_{1} = 0}^{\infty}\left( ( - 1)^{2k_{1}} + ( - 1)^{2k_{1} + 1} \right) = \sum_{k_{1} = 0}^{\infty}0 = 0$$

这显然是不对的。

**[讨论4.3.5]{.underline}** 乘积嵌套交换

对于两个绝对收敛的级数，乘积嵌套交换成立。

$$柯西定理：若级数\sum_{k = 1}^{\infty}{f\lbrack k\rbrack}，\sum_{k = 1}^{\infty}{g\lbrack k\rbrack}绝对收敛，并且$$

$$\sum_{k = 1}^{\infty}{f\lbrack k\rbrack} = S_{1}，\sum_{k = 1}^{\infty}{g\lbrack k\rbrack} = S_{2},则$$

$f\left\lbrack k_{1} \right\rbrack g\lbrack k_{2}\rbrack(k_{1},k_{2} \in \mathbf{N}^{\mathbf{+}})$按[任意方式]{.underline}排列成的级数都绝对收敛，

并且其和等于$S_{1}S_{2}.$

证明参见参考资料\[1\]。

两种嵌套求和自然也是在"任意方式"中，因而

$$在级数\sum_{k = 1}^{\infty}{f\lbrack k\rbrack}，\sum_{k = 1}^{\infty}{g\lbrack k\rbrack}绝对收敛的条件下，$$

$$\sum_{k_{1} = 1}^{\infty}{\sum_{k_{2} = 1}^{\infty}{f\left\lbrack k_{1} \right\rbrack g\left\lbrack k_{2} \right\rbrack}} = \sum_{k_{2} = 1}^{\infty}{\sum_{k_{1} = 1}^{\infty}{f\left\lbrack k_{1} \right\rbrack g\left\lbrack k_{2} \right\rbrack}}$$

显然如果只有一个是无穷级数，嵌套交换也成立。

$$\sum_{k_{1} = 1}^{\infty}{\sum_{k_{2} = a}^{b}{f\left\lbrack k_{1} \right\rbrack g\left\lbrack k_{2} \right\rbrack}} = \sum_{k_{2} = a}^{b}{\sum_{k_{1} = 1}^{\infty}{f\left\lbrack k_{1} \right\rbrack g\left\lbrack k_{2} \right\rbrack}}$$

[]{#_Toc507114579 .anchor}5.1 一排原子转动惯量

设有质量为$m_{k},k \in \mathbf{Z}\lbrack 1,n\rbrack 的n个原子排列在一条直线上，$坐标为$x_{k},k \in \mathbf{Z}\lbrack 1,n\rbrack$，求绕质心的转动惯量$I.$

$$首先有质心坐标x_{c} = \frac{\sum_{k = 1}^{n}{m_{k}x_{k}}}{\sum_{k = 1}^{n}m_{k}}$$

$$结合转动惯量定义式I = \sum_{k = 1}^{n}{m_{k}\left( x_{k} - x_{c} \right)^{2}}$$

$$记M = \sum_{k = 1}^{n}m_{k}$$

$$得到I = \sum_{k_{1} = 1}^{n}{m_{k_{1}}\left( x_{k_{1}} - \frac{\sum_{k_{2} = 1}^{n}{m_{k_{2}}x_{k_{2}}}}{M} \right)^{2}}$$

下面我们就化简这个式子。

$$I =^{通分}\sum_{k_{1} = 1}^{n}{m_{k_{1}}\left( \frac{x_{k_{1}}M - \sum_{k_{2} = 1}^{n}{m_{k_{2}}x_{k_{2}}}}{M} \right)^{2}}$$

$$=^{提出分母}\sum_{k_{1} = 1}^{n}{\frac{m_{k_{1}}}{M^{2}}\left( Mx_{k_{1}} - \sum_{k_{2} = 1}^{n}{m_{k_{2}}x_{k_{2}}} \right)^{2}}$$

$$=^{平方展开}\sum_{k_{1} = 1}^{n}\frac{m_{k_{1}}}{M^{2}}\left( M^{2}x_{k_{1}}^{2} - 2Mx_{k_{1}}\sum_{k_{2} = 1}^{n}{m_{k_{2}}x_{k_{2}}} + \left( \sum_{k_{2} = 1}^{n}{m_{k_{2}}x_{k_{2}}} \right)^{2} \right)$$

$$=^{分配求和}\sum_{k_{1} = 1}^{n}{m_{k_{1}}x_{k_{1}}^{2}} - \frac{2}{M}\sum_{k_{1} = 1}^{n}{m_{k_{1}}x_{k_{1}}\sum_{k_{2} = 1}^{n}{m_{k_{2}}x_{k_{2}}}} + \frac{1}{M^{2}}\sum_{k_{1} = 1}^{n}{m_{k_{1}}\left( \sum_{k_{2} = 1}^{n}{m_{k_{2}}x_{k_{2}}} \right)^{2}}$$

$$=_{直接求和}^{嵌套交换}\sum_{k_{1} = 1}^{n}{m_{k_{1}}x_{k_{1}}^{2}} - \frac{2}{M}\sum_{k_{1} = 1}^{n}{m_{k_{1}}x_{k_{1}}}\sum_{k_{2} = 1}^{n}{m_{k_{2}}x_{k_{2}}} + \frac{M}{M^{2}}\left( \sum_{k_{2} = 1}^{n}{m_{k_{2}}x_{k_{2}}} \right)^{2}$$

$$=^{嵌套交换}\sum_{k_{1} = 1}^{n}{m_{k_{1}}x_{k_{1}}^{2}} - \frac{2}{M}\left( \sum_{k_{1},k_{2} = 1}^{n}{m_{k_{1}}x_{k_{1}}m_{k_{2}}x_{k_{2}}} \right) + \frac{1}{M}\left( \sum_{k_{1},k_{2} = 1}^{n}{m_{k_{1}}x_{k_{1}}m_{k_{2}}x_{k_{2}}} \right)$$

$$=^{合并}\sum_{k_{1} = 1}^{n}{m_{k_{1}}x_{k_{1}}^{2}} - \frac{1}{M}\sum_{k_{1},k_{2} = 1}^{n}{m_{k_{1}}x_{k_{1}}m_{k_{2}}x_{k_{2}}}$$

$$=_{\ }^{通分}\frac{1}{M}\left( \left( \sum_{k_{1} = 1}^{n}{m_{k_{1}}x_{k_{1}}^{2}} \right)\left( \sum_{k_{2} = 1}^{n}m_{k_{2}} \right) - \sum_{k_{1},k_{2} = 1}^{n}{m_{k_{1}}x_{k_{1}}m_{k_{2}}x_{k_{2}}} \right)$$

$$=_{线性合并}^{嵌套交换}\frac{1}{M}\left( \sum_{k_{1},k_{2} = 1}^{n}{m_{k_{1}}m_{k_{2}}x_{k_{1}}\left( x_{k_{1}} - x_{k_{2}} \right)} \right)$$

$$=_{对换k_{1}k_{2}}^{加倍}\frac{1}{2M}\left( \sum_{\begin{array}{r}
k_{1},k_{2} = 1 \\
k_{1} \neq k_{2}
\end{array}}^{n}{m_{k_{1}}m_{k_{2}}x_{k_{1}}^{2}} + \sum_{\begin{array}{r}
k_{1},k_{2} = 1 \\
k_{1} \neq k_{2}
\end{array}}^{n}{m_{k_{1}}m_{k_{2}}x_{k_{2}}^{2}} - 2\sum_{\begin{array}{r}
k_{1},k_{2} = 1 \\
k_{1} \neq k_{2}
\end{array}}^{n}{m_{k_{1}}x_{k_{1}}m_{k_{2}}x_{k_{2}}} \right)$$

$$=^{线性合并}\frac{1}{2M}\left( \sum_{\begin{array}{r}
k_{1},k_{2} = 1 \\
k_{1} \neq k_{2}
\end{array}}^{n}{m_{k_{1}}m_{k_{2}}\left( x_{k_{1}}^{2} - 2x_{k_{1}}x_{k_{2}} + x_{k_{2}}^{2} \right)} \right)$$

$$= \frac{1}{2M}\left( \sum_{\begin{array}{r}
k_{1},k_{2} = 1 \\
k_{1} \neq k_{2}
\end{array}}^{n}{m_{k_{1}}m_{k_{2}}\left( x_{k_{1}} - x_{k_{2}} \right)^{2}} \right)$$

$$=^{2.4.7}\frac{1}{M}\left( \sum_{\begin{array}{r}
k_{1},k_{2} = 1 \\
k_{1} > k_{2}
\end{array}}^{n}{m_{k_{1}}m_{k_{2}}\left( x_{k_{1}} - x_{k_{2}} \right)^{2}} \right)$$

注：朗道《力学》书上公式相差系数2，原因应当在于朗道书中带有$a \neq b$的求和对相同的$\{ a,b\}$只计算一次，而本书中定义为计算两次。

于是一排原子$\{(x_{k},m_{k})|k \in \mathbf{Z}\lbrack 1,n\rbrack\}$

$$转动惯量I = \frac{1}{M}\left( \sum_{\begin{array}{r}
k_{1},k_{2} = 1 \\
k_{1} > k_{2}
\end{array}}^{n}{m_{k_{1}}m_{k_{2}}\left( x_{k_{1}} - x_{k_{2}} \right)^{2}} \right)$$

$$若记M_{t} = \sum_{k = 1}^{n}{m_{k}x_{k}^{t}}$$

$$I = \sum_{k_{1} = 1}^{n}{m_{k_{1}}x_{k_{1}}^{2}} - \frac{2}{M}\sum_{k_{1} = 1}^{n}{m_{k_{1}}x_{k_{1}}}\sum_{k_{2} = 1}^{n}{m_{k_{2}}x_{k_{2}}} + \frac{M}{M^{2}}\left( \sum_{k_{2} = 1}^{n}{m_{k_{2}}x_{k_{2}}} \right)^{2}$$

$$= \sum_{k_{1} = 1}^{n}{m_{k_{1}}x_{k_{1}}^{2}} - \frac{1}{M}\left( \sum_{k_{2} = 1}^{n}{m_{k_{2}}x_{k_{2}}} \right)^{2}$$

$$= M_{2} - \frac{M_{1}^{2}}{M_{0}} = \frac{M_{2}M_{0} - M_{1}^{2}}{M_{0}}$$

[]{#_Toc507114580 .anchor}5.2 平行轴、垂直轴定理

本节只讨论质点系的情况。

**[定理5.2.1]{.underline}** 平行轴定理

设有$n$个质点在空间直角坐标系中，每个质点$k \in \mathbf{Z}\lbrack 1,n\rbrack,$

$$质量为m_{k},位矢\overset{⃑}{r_{k}} = \left( x_{k},y_{k},z_{k} \right);$$

$$总质量记为M,质心坐标为\overset{⃑}{r_{c}} = \left( x_{c},y_{c},z_{c} \right),$$

$$另有一点T,\overset{⃑}{r_{t}} = \left( x_{t},y_{t},z_{t} \right).$$

$$则绕直线\left\{ \begin{array}{r}
x = x_{c} \\
y = y_{c}
\end{array} \right.\ 的转动惯量I_{c}与绕直线\left\{ \begin{array}{r}
x = x_{t} \\
y = y_{t}
\end{array}的转动惯量I_{t} \right.\ $$

$$有如下关系：$$

$$I_{t} = I_{c} + M\left( \left( x_{c} - x_{t} \right)^{2} + \left( y_{c} - y_{t} \right)^{2} \right) ≔ I_{c} + Md^{2}$$

证明：

$$I_{t} = \sum_{k = 1}^{n}{m_{k}r_{kt}^{2}} = \sum_{k = 1}^{n}{m_{k}\left( \left( x_{k} - x_{t} \right)^{2} + \left( y_{k} - y_{t} \right)^{2} \right)}$$

$$I_{c} = \sum_{k = 1}^{n}{m_{k}\left( \left( x_{k} - x_{c} \right)^{2} + \left( y_{k} - y_{c} \right)^{2} \right)}$$

$$I_{t} - I_{c} = \sum_{k = 1}^{n}{m_{k}\left( \left( x_{k} - x_{t} \right)^{2} + \left( y_{k} - y_{t} \right)^{2} - \left( x_{k} - x_{c} \right)^{2} - \left( y_{k} - y_{c} \right)^{2} \right)}$$

$$= \sum_{k = 1}^{n}{m_{k}\left( (x_{c} - x_{t})(2x_{k} - x_{c} - x_{t}) + (y_{c} - y_{t})(2y_{k} - y_{c} - y_{t}) \right)}$$

$$= \left( x_{c} - x_{t} \right)\left( \sum_{k = 1}^{n}{2m_{k}x_{k}} - (x_{c} + x_{t})\sum_{k = 1}^{n}m_{k} \right) + \left( y_{c} - y_{t} \right)\left( \sum_{k = 1}^{n}{2m_{k}y_{k}} - (y_{c} + y_{t})\sum_{k = 1}^{n}m_{k} \right)$$

我们不把$x_{c}$用质心定义代掉，而是考虑利用质心定义消去恼人的

$$\sum_{k = 1}^{n}{m_{k}x_{k}}项。注意到\sum_{k = 1}^{n}{m_{k}x_{k}} = Mx_{c}$$

$$I_{t} - I_{c} = \left( x_{c} - x_{t} \right)\left( 2Mx_{c} - \left( x_{c} + x_{t} \right)M \right) + \left( y_{c} - y_{t} \right)\left( 2My_{c} - \left( y_{c} + y_{t} \right)M \right)$$

$$= M\left( x_{c} - x_{t} \right)^{2} + M\left( y_{c} - y_{t} \right)^{2}$$

$$= {Md}^{2}.\ \ \ \ \ \ 证毕$$

如果两平行旋转轴不平行于$z$轴，则可旋转坐标系使它们平行于$z$轴。因为上面的讨论对每个质点没有特别的规定，因此旋转之后平行轴定理当然成立。又因为转动惯量是质点系的固有属性，与坐标轴的选取无关，则平行轴定理在原始状态下也成立。此时式中的$d$为两轴间距离。

**[定理5.2.2]{.underline}** 垂直轴定理

设$n$个质点组成的质点系分布在一个平面上，

$$O为该平面上一点，有三条直线互相垂直相交于O，$$

$$其中两条在面内，记为l_{x},l_{y};一条垂直于面,记为l_{z}$$

$$质点系绕轴l_{x},l_{y},l_{z}的转动惯量记为I_{x},I_{y},I_{z}$$

$$则I_{z} = I_{x} + I_{y}$$

证：$取O为坐标原点，l_{x},l_{y},l_{z}分别为x,y,z轴，正方向任意选定，$

$$则得到空间直角坐标系。$$

设质点系各点$\left( k \in \mathbf{Z}\lbrack 1,n\rbrack \right)，$质量为$m_{k}$，$坐标为(x_{k},y_{k},0)$

由转动惯量定义，$
$$$I_{x} = \sum_{k = 1}^{n}{m_{k}y_{k}^{2}},I_{y} = \sum_{k = 1}^{n}{m_{k}x_{k}^{2}},$$

$$I_{z} = \sum_{k = 1}^{n}{m_{k}\left( x_{k}^{2} + y_{k}^{2} \right) =}\sum_{k = 1}^{n}{m_{k}x_{k}^{2}} + \sum_{k = 1}^{n}{m_{k}y_{k}^{2}} = I_{x} + I_{y}$$

证毕。

[]{#_Toc507114581 .anchor}5.3 正余弦等差求和

正余弦等差求和有一套模式化的流程：

乘以半公差正弦→积化和差→相邻相消→（可选）和差化积

$$\sum_{k = 1}^{n}{\sin{\lbrack mk\rbrack}}$$

$$= \frac{1}{\sin\frac{m}{2}}\ \sum_{k = 1}^{n}{\sin{\lbrack mk\rbrack}\sin\frac{m}{2}}$$

$$= \frac{1}{\sin\frac{m}{2}}\ \sum_{k = 1}^{n}{- \frac{1}{2}\left( \cos\left\lbrack \left( k + \frac{1}{2} \right)m \right\rbrack - \cos\left\lbrack \left( k - \frac{1}{2} \right)m \right\rbrack \right)}$$

$$= \frac{- 1}{2\sin\frac{m}{2}}\left( \sum_{k = 1}^{n}{\cos\left\lbrack \left( k + \frac{1}{2} \right)m \right\rbrack - \sum_{k = 1}^{n}{\cos\left\lbrack \left( k - \frac{1}{2} \right)m \right\rbrack}} \right)$$

$$= \frac{- 1}{2\sin\frac{m}{2}}\left( \sum_{k = 1}^{n}{\cos\left\lbrack \left( k + \frac{1}{2} \right)m \right\rbrack - \sum_{k = 0}^{n - 1}{\cos\left\lbrack \left( k + \frac{1}{2} \right)m \right\rbrack}} \right)$$

$$= \frac{- 1}{2\sin\frac{m}{2}}\left( \cos\left\lbrack \left( n + \frac{1}{2} \right)m \right\rbrack - \cos\frac{m}{2} \right)$$

$$= \frac{\sin\left\lbrack \frac{n + 1}{2}m \right\rbrack\sin\left\lbrack \frac{n}{2}m \right\rbrack}{\sin\frac{m}{2}}$$

$$\sum_{k = 1}^{n}{\cos{\lbrack mk\rbrack}}$$

$$= \frac{1}{\sin\frac{m}{2}}\ \sum_{k = 1}^{n}{\cos{\lbrack mk\rbrack}\sin\frac{m}{2}}$$

$$= \frac{1}{\sin\frac{m}{2}}\ \sum_{k = 1}^{n}{\frac{1}{2}\left( \sin\left\lbrack \left( k + \frac{1}{2} \right)m \right\rbrack - \sin\left\lbrack \left( k - \frac{1}{2} \right)m \right\rbrack \right)}$$

$$= \frac{1}{2\sin\frac{m}{2}}\left( \sum_{k = 1}^{n}{\sin\left\lbrack \left( k + \frac{1}{2} \right)m \right\rbrack - \sum_{k = 1}^{n}{\sin\left\lbrack \left( k - \frac{1}{2} \right)m \right\rbrack}} \right)$$

$$= \frac{1}{2\sin\frac{m}{2}}\left( \sum_{k = 1}^{n}{\sin\left\lbrack \left( k + \frac{1}{2} \right)m \right\rbrack - \sum_{k = 0}^{n - 1}{\sin\left\lbrack \left( k + \frac{1}{2} \right)m \right\rbrack}} \right)$$

$$= \frac{1}{2\sin\frac{m}{2}}\left( \sin\left\lbrack \left( n + \frac{1}{2} \right)m \right\rbrack - \sin\frac{m}{2} \right)$$

$$= \frac{\cos\left\lbrack \frac{n + 1}{2}m \right\rbrack\sin\left\lbrack \frac{n}{2}m \right\rbrack}{\sin\frac{m}{2}}$$

$$\sum_{k = 1}^{n}{\sin\lbrack mk\rbrack} = \frac{\sin\left\lbrack \frac{n + 1}{2}m \right\rbrack\sin\left\lbrack \frac{n}{2}m \right\rbrack}{\sin\frac{m}{2}}$$

$$\sum_{k = 1}^{n}{\cos{\lbrack mk\rbrack}} = \frac{\cos\left\lbrack \frac{n + 1}{2}m \right\rbrack\sin\left\lbrack \frac{n}{2}m \right\rbrack}{\sin\frac{m}{2}}$$

[]{#_Toc507114582 .anchor}5.4 1234567×7654321

我们试图找一种方法来计算1234567×7654321（非竖式乘法）

注意，该方法并不比竖式乘法简单。

首先需要把这两个数字表示出来。显然，如果$令a = 1234567,$

$b = 7654321$然后算$a \times b$，并没有从本质上解决问题。

观察这两个数字的特点，注意到数位与该数位上的数有关系，而数位又是由$10^{k}$所控制。因此可将7654321写成下面的形式。

$$7654321 = 7 \times 10^{6} + 6 \times 10^{5} + 5 \times 10^{4} + 4 \times 10^{3} + 3 \times 10^{2} + 2 \times 10^{1} + 1 \times 10^{0}$$

从中归纳出一般项的模板，用求和符号记为

$$7654321 = \sum_{k = 0}^{6}{(k + 1)10^{k}}$$

$$同理，1234567 = \sum_{k = 0}^{6}{(7 - k)10^{k}}$$

现在可以进行乘法了。

$$r = \left( \sum_{k = 0}^{6}{(k + 1)10^{k}} \right)\left( \sum_{k = 0}^{6}{(7 - k)10^{k}} \right)$$

利用多项式乘法的结论

$$\left( \sum_{k = 0}^{n}{a_{k}x^{k}} \right)\left( \sum_{k = 0}^{n}{b_{k}x^{k}} \right)$$

$$= \sum_{t = 0}^{n}{\left( \sum_{k = 0}^{t}{a_{k}b_{t - k}} \right)x^{t}} + \sum_{t = 0}^{n - 1}{\left( \sum_{k = 0}^{t}{a_{k + n - t}b_{n - k}} \right)x^{2n - t}}$$

令$a_{k} = k + 1,b_{k} = 7 - k,n = 6,x = 10$，结果记为$r$

$$r = \sum_{t = 0}^{6}{\left( \sum_{k = 0}^{t}{(k + 1)(7 - t + k)} \right)10^{t}} + \sum_{t = 0}^{5}{\left( \sum_{k = 0}^{t}{(k + 7 - t)(k + 1)} \right)10^{12 - t}}$$

注意到两部分系数恰好一样。（想想是什么原因？）

下面计算系数，也就是求函数

$$f\lbrack t\rbrack ≔ \sum_{k = 0}^{t}{(k + 1)(7 - t + k)}$$

$$= \sum_{k = 0}^{t}\left( k^{2} + (8 - t)k + 7 - t \right)$$

$$= \frac{t(t + 1)(2t + 1)}{6} + \frac{t(t + 1)(8 - t)}{2} + (7 - t)(t + 1)$$

接下来只需要将$t$从0到6逐个代入，求出的值就是对应数位上的数字。化简一下：

$$f\lbrack t\rbrack = \frac{- t^{3} + 18t^{2} + 61t}{6} + 7 = - \frac{1}{6}t^{3} + 3t^{2} + \frac{61}{6}t + 7$$

利用霍纳法求值。以5为例，先打好表格，然后计算。

$$\begin{matrix}
\  & - \frac{1}{6} & 3 & \frac{61}{6} & 7 \\
5 & \  & \  & \  & \  \\
\  & \  & \  & \  & \
\end{matrix}$$

$$\begin{matrix}
\  & - \frac{1}{6} & 3 & \frac{61}{6} & 7 \\
5 & = - \frac{1}{6} & = - \frac{1}{6} \times 5 + 3 & = \frac{13}{6} \times 5 + \frac{61}{6} & = 21 \times 5 + 7 \\
\  & \  & = \frac{13}{6} & = 21 & = 112
\end{matrix}$$

最后得到

$$f\lbrack 0\rbrack = 7;\ \ f\lbrack 1\rbrack = 20;\ \ f\lbrack 2\rbrack = 38;\ \ f\lbrack 3\rbrack = 60;$$

$$f\lbrack 4\rbrack = 85;\ \ f\lbrack 5\rbrack = 112;\ \ f\lbrack 6\rbrack = 140$$

$$r = \sum_{t = 0}^{6}{f\lbrack t\rbrack 10^{t}} + \sum_{t = 0}^{5}{f\lbrack t\rbrack 10^{12 - t}} = \sum_{t = 0}^{6}{f\lbrack t\rbrack 10^{t}} + \sum_{t = 7}^{12}{f\lbrack 12 - t\rbrack 10^{t}}$$

于是$r = \overline{f\lbrack 0\rbrack f\lbrack 1\rbrack f\lbrack 2\rbrack f\lbrack 3\rbrack f\lbrack 4\rbrack f\lbrack 5\rbrack f\lbrack 6\rbrack f\lbrack 5\rbrack f\lbrack 4\rbrack f\lbrack 3\rbrack f\lbrack 2\rbrack f\lbrack 1\rbrack f\lbrack 0\rbrack}$

$$= \overline{7\ 20\ 38\ 60\ 85\ 112\ 140\ 112\ 85\ 60\ 38\ 20\ 7}\ \ (并不规范的写法)$$

利用进位原则，最终得到

$$r = 9449772114007$$

[]{#_Toc507114583 .anchor}5.5 正整数方幂和

$$1^{2} + 2^{2} + \ldots + n^{2}称作正整数的平方和，$$

$$我们知道它等于\frac{n(n + 1)(2n + 1)}{6}$$

$$而\frac{n(n + 1)(2n + 1)}{6} = \frac{1}{3}n^{3} + \frac{1}{2}n^{2} + \frac{1}{6}n是一个三次多项式。$$

$$对于一般的情况，\sum_{m = 1}^{n}m^{p}\ (p \in \mathbf{N})$$

$$我们假设它是一个p + 1次多项式，$$

$$令\sum_{m = 1}^{n}m^{p} = \sum_{r = 0}^{p + 1}a_{p,r}n^{r}，来求系数矩阵\left\{ a_{p,r} \right\}.$$

方法一

以求平方和利用立方差公式为例。

在$a^{3} - b^{3} = (a - b)\left( a^{2} + ab + b^{2} \right)中，$

$$令a = m,b = m - 1$$

$$(m)^{3} - (m - 1)^{3} = \left( m - (m - 1) \right)\left( m^{2} + m(m - 1) + (m - 1)^{2} \right)$$

$$= \left( 3m^{2} - 3m + 1 \right)$$

再令$m$从$1$到$n$,两边求和得

$$n^{3} = 3\sum_{m = 1}^{n}m^{2} - 3\sum_{m = 1}^{n}m + \sum_{m = 1}^{n}1$$

其中零次、一次项求和的结果已经预先知道，代入并移项即得

$$\sum_{m = 1}^{n}m^{2} = \frac{1}{3}\left( n^{3} - n \right) + \frac{n^{2} + n}{2} = \frac{2n^{3} + 3n^{2} + n}{6}$$

$$对于\sum_{m = 1}^{n}m^{p}，我们要利用高次方差公式。$$

$$a^{p + 1} - b^{p + 1} = (a - b)\sum_{k = 0}^{p}{a^{p - k}b^{k}}\ \ \ \ （证明见第三章）$$

仍然令$a = m,b = m - 1$

$$m^{p + 1} - {(m - 1)}^{p + 1} = \sum_{k = 0}^{p}{m^{p - k}{(m - 1)}^{k}}$$

两边$令m从1到n求和$

$$n^{p + 1} = \sum_{m = 1}^{n}{\sum_{k = 0}^{p}{m^{p - k}{(m - 1)}^{k}}}$$

我们只需要找出右边$n$的系数并与左边一一对应即可。

为此，必须先利用$0到p$次的求和公式消去右端的$m.$

先二项展开：

$$\sum_{m = 1}^{n}{\sum_{k = 0}^{p}{m^{p - k}(m - 1)^{k}}}$$

$$= \sum_{m = 1}^{n}{\sum_{k = 0}^{p}{\sum_{t = 0}^{k}{m^{p - k}C_{k}^{t}m^{k - t}( - 1)^{t}}}}$$

求和变量$k,t$不受$m$限制，最外层求和可以换到最里。

$$= \sum_{k = 0}^{p}{\sum_{t = 0}^{k}{\left( \sum_{m = 1}^{n}m^{p - t} \right)C_{k}^{t}( - 1)^{t}}}$$

由之前所作的假定：

$$= \sum_{k = 0}^{p}{\sum_{t = 0}^{k}{\left( \sum_{r = 0}^{p + 1 - t}a_{p - t,r}n^{r} \right)C_{k}^{t}( - 1)^{t}}}$$

$$= \sum_{k = 0}^{p}{\sum_{t = 0}^{k}{\sum_{r = 0}^{p + 1 - t}{a_{p - t,r}C_{k}^{t}( - 1)^{t}n^{r}}}}$$

我们想把$以r$为求和变量的求和号放至最外，以方便寻找系数。

利用三角嵌套交换定理，省略函数。

$$\sum_{t = 0}^{k}{\sum_{r = 0}^{p + 1 - t}\ } = \sum_{t = 0}^{k}{\sum_{r = 0}^{p - k}\ } + \sum_{t = 0}^{k}{\sum_{r = p + 1 - k}^{p + 1 - t}\ }$$

$$= \sum_{r = 0}^{p - k}{\sum_{t = 0}^{k}\ } + \sum_{t = 0}^{k}{\sum_{r - p - 1 + k = 0}^{k - t}\ }$$

这一步用了简略的换元记法，可以如此理解：

$$R ≔ r - p - 1 + k,$$

$$\ r \in \mathbf{Z}\lbrack p + 1 - k,p + 1 - t\rbrack \Rightarrow R \in \mathbf{Z}\lbrack 0,k - t\rbrack$$

$$= \sum_{r = 0}^{p - k}{\sum_{t = 0}^{k}\ } + \sum_{r - p - 1 + k = 0}^{k}{\sum_{t = 0}^{k - (r - p - 1 + k)}\ }$$

$$= \sum_{r = 0}^{p - k}{\sum_{t = 0}^{k}\ } + \sum_{r = p + 1 - k}^{p + 1}{\sum_{t = 0}^{p + 1 - r}\ }$$

这一步将$r$还原:$R \in \mathbf{Z}\lbrack 0,k\rbrack \Rightarrow \ r \in \mathbf{Z}\lbrack p + 1 - k,p + 1\rbrack$

于是

$$\sum_{k = 0}^{p}{\sum_{t = 0}^{k}{\sum_{r = 0}^{p + 1 - t}\ }} = \sum_{k = 0}^{p}{\sum_{r = 0}^{p - k}{\sum_{t = 0}^{k}\ }} + \sum_{k = 0}^{p}{\sum_{r = p + 1 - k}^{p + 1}{\sum_{t = 0}^{p + 1 - r}\ }}$$

再对外层两求和进行交换。

$$\sum_{k = 0}^{p}{\sum_{r = 0}^{p - k}\ } = \sum_{r = 0}^{p}{\sum_{k = 0}^{p - r}\ }$$

$$\sum_{k = 0}^{p}{\sum_{r = p + 1 - k}^{p + 1}\ } = \sum_{k = 0}^{p}{\sum_{r - 1 = p - k}^{p}\ } = \sum_{r - 1 = 0}^{p}{\sum_{k = p - (r - 1)}^{p}\ } = \sum_{r = 1}^{p + 1}{\sum_{k = p + 1 - r}^{p}\ }$$

于是

$$\sum_{k = 0}^{p}{\sum_{t = 0}^{k}{\sum_{r = 0}^{p + 1 - t}\ }} = \sum_{r = 0}^{p}{\sum_{k = 0}^{p - r}{\sum_{t = 0}^{k}\ \ }} + \sum_{r = 1}^{p + 1}{\sum_{k = p + 1 - r}^{p}{\sum_{t = 0}^{p + 1 - r}\ }}$$

即

$$n^{p + 1} = \sum_{r = 0}^{p}{\sum_{k = 0}^{p - r}{\sum_{t = 0}^{k}{a_{p - t,r}C_{k}^{t}( - 1)^{t}n^{r}}\ }}\ \ \ \ \ \ \ \ \ \ \ $$

$$\ \ \ \ \ \ \ \ \ \ \ \ \ \ \  + \sum_{r = 1}^{p + 1}{\sum_{k = p + 1 - r}^{p}{\sum_{t = 0}^{p + 1 - r}{a_{p - t,r}C_{k}^{t}( - 1)^{t}n^{r}}}}$$

此时可以很方便的读出各次项系数，设$n^{r}的系数为f\lbrack r\rbrack$，则有方程

$$f\lbrack 0\rbrack = f\lbrack 1\rbrack = f\lbrack 2\rbrack = \ldots = f\lbrack p\rbrack = 0,f\lbrack p + 1\rbrack = 1$$

考虑$f\lbrack 0\rbrack = 0，即$

$$\sum_{k = 0}^{p}{\sum_{t = 0}^{k}{a_{p - t,0}C_{k}^{t}( - 1)^{t}}\ } = \sum_{t = 0}^{p}{a_{p - t,0}( - 1)^{t}\left( \sum_{k = t}^{p}C_{k}^{t} \right)\ }$$

$$= \sum_{t = 0}^{p}{a_{p - t,0}C_{p + 1}^{t + 1}( - 1)^{t}\ } = \sum_{t = 0}^{p}{a_{t,0}C_{p + 1}^{t}( - 1)^{p - t}\ } = 0$$

此式应对$p = 0,1,2,\ldots 均成立，但代入p = 0得a_{0,0} = 0,$

$$代入p = 1，结合a_{0,0} = 0又可得a_{1,0} = 0$$

如此可知$a_{p,0} = 0$.

考虑$f\lbrack p + 1\rbrack = 1，即$

$$\sum_{k = 0}^{p}{\sum_{t = 0}^{0}{a_{p - t,p + 1}C_{k}^{t}( - 1)^{t}}} = (p + 1)a_{p,p + 1} = 1$$

$$可得a_{p,p + 1} = \frac{1}{p + 1}，$$

$$这说明正整数的p次方求和后p + 1次方的系数为\frac{1}{p + 1}$$

而对$r \in \mathbf{Z}\lbrack 1,p\rbrack$而言，方程表现为

$$\sum_{k = 0}^{p - r}{\sum_{t = 0}^{k}{a_{p - t,r}C_{k}^{t}( - 1)^{t}}\ } + \sum_{k = p + 1 - r}^{p}{\sum_{t = 0}^{p + 1 - r}{a_{p - t,r}C_{k}^{t}( - 1)^{t}}} = 0$$

注意到求和点组成$直角 + 45{^\circ}$梯形，在$k - t$坐标系中四个顶点分别为$(0,0),(p,0),(p,p + 1 - r),(p + 1 - r,p + 1 - r)$

可通过嵌套交换合并。

$$\sum_{t = 0}^{p + 1 - r}{\sum_{k = t}^{p}{a_{p - t,r}C_{k}^{t}( - 1)^{t}}} = \sum_{t = 0}^{p + 1 - r}{a_{p - t,r}C_{p + 1}^{t + 1}( - 1)^{t}} = 0$$

$$\sum_{t = r - 1}^{p}{( - 1)^{p - t}C_{p + 1}^{t}a}_{t,r} = 0$$

来计算一些具体情况，令$r = 1$

$$\sum_{t = 0}^{p}{( - 1)^{p - t}C_{p + 1}^{t}a}_{t,1} = 0$$

也许我们还是想代入$p = 0$，但是注意到$p \geq r$，只能从1开始代。

$$\sum_{t = 0}^{1}{( - 1)^{1 - t}C_{2}^{t}a}_{t,1} = - a_{0,1} + 2a_{1,1} = 0$$

$$其中a_{0,1}只能由a_{p,p + 1} = \frac{1}{p + 1}计算，得a_{0,1} = 1,a_{1,1} = \frac{1}{2}$$

$$再令p = 2，a_{0,1} - 3a_{1,1} + 3a_{2,1} = 0,a_{2,1} = \frac{1}{6}$$

回去看一看平方求和后一次项的系数，确实没错。

这里我们不讨论如何解这个递推方程，因为下面这个方法可以直接得到通项公式，结果显示通项公式中含有第一类斯特林数，而多方查找均未得第一类斯特林数的通项公式，也就是说结果并不是初等的。

方法二

注意，此方法需要用到斯特林数及下降阶乘，不了解的读者请先阅读附录一。

此方法的关键是利用下降阶乘便于求和的特点。

$$\sum_{m = 1}^{n}(m)_{k}$$

$$= \sum_{m = 1}^{n}{\frac{(m + 1) - (m - k)}{k + 1}(m)_{k}}$$

$$= \sum_{m = 1}^{n}{\frac{1}{k + 1}\left( (m + 1)_{k + 1} - (m)_{k + 1} \right)}$$

$$= \frac{1}{k + 1}\left( \sum_{m = 1}^{n}(m + 1)_{k + 1} - \sum_{m = 1}^{n}(m)_{k + 1} \right)$$

$$= \frac{(n + 1)_{k + 1} - (1)_{k + 1}}{k + 1}$$

$$当k \geq 1时，(1)_{k + 1} = 0,因此$$

$$\sum_{m = 1}^{n}(m)_{k} = \frac{(n + 1)_{k + 1}}{k + 1}$$

注：此结论可进一步用于证明组合等式

$$\sum_{k = m}^{n}{C_{k}^{m} = C_{n + 1}^{m + 1}}$$

由第二类斯特林数的性质：

$$x^{n} = \sum_{k = 0}^{n}{S_{2}\lbrack n,k\rbrack(x)_{k}}\ \ \ \ \ \ $$

$$得\sum_{m = 1}^{n}m^{p} = \sum_{m = 1}^{n}{\sum_{k = 0}^{p}{S_{2}\lbrack p,k\rbrack(m)_{k}}}$$

不考虑$p = 0$的情况，则此时$S_{2}\lbrack p,0\rbrack = 0$

$$因此\sum_{m = 1}^{n}m^{p} = \sum_{m = 1}^{n}{\sum_{k = 1}^{p}{S_{2}\lbrack p,k\rbrack(m)_{k}}}$$

现在我们保证了$k \geq 1$，嵌套交换对$(m)_{k}$求和：

$$\sum_{m = 1}^{n}{\sum_{k = 1}^{p}{S_{2}\lbrack p,k\rbrack(m)_{k}}} = \sum_{k = 1}^{p}{S_{2}\lbrack p,k\rbrack\frac{(n + 1)_{k + 1}}{k + 1}}$$

再由第一类斯特林数的性质：

$$(x)_{n} = \sum_{k = 0}^{n}{S_{1}\lbrack n,k\rbrack x^{k}}$$

$$得\sum_{k = 1}^{p}{S_{2}\lbrack p,k\rbrack\frac{(n + 1)_{k + 1}}{k + 1}} = \sum_{k = 1}^{p}\frac{S_{2}\lbrack p,k\rbrack}{k + 1}\sum_{t = 0}^{k + 1}{S_{1}\lbrack k + 1,t\rbrack(n + 1)^{t}}$$

二项展开：

$$= \sum_{k = 1}^{p}\frac{S_{2}\lbrack p,k\rbrack}{k + 1}\sum_{t = 0}^{k + 1}{S_{1}\lbrack k + 1,t\rbrack\sum_{r = 0}^{t}{C_{t}^{r}n^{r}}}$$

$$= \sum_{k = 1}^{p}{\sum_{t = 0}^{k + 1}{\sum_{r = 0}^{t}{\frac{S_{2}\lbrack p,k\rbrack S_{1}\lbrack k + 1,t\rbrack C_{t}^{r}}{k + 1}n^{r}}}}$$

$$= \sum_{k = 2}^{p + 1}{\sum_{t = 0}^{k}{\sum_{r = 0}^{t}{\frac{S_{2}\lbrack p,k - 1\rbrack S_{1}\lbrack k,t\rbrack C_{t}^{r}}{k}n^{r}}}}$$

同样地，我们想把求和变量为$r$的求和号交换到最外层。

$$内二层：\sum_{t = 0}^{k}{\sum_{r = 0}^{t}\ } = \sum_{r = 0}^{k}{\sum_{t = r}^{k}\ }$$

$$外二层：\sum_{k = 2}^{p + 1}{\sum_{r = 0}^{k}\ } = \sum_{r = 0}^{1}{\sum_{k = 2}^{p + 1}\ } + \sum_{r = 2}^{p + 1}{\sum_{k = r}^{p + 1}\ }$$

最终得到

$$\sum_{k = 2}^{p + 1}{\sum_{t = 0}^{k}{\sum_{r = 0}^{t}{\frac{S_{2}\lbrack p,k - 1\rbrack S_{1}\lbrack k,t\rbrack C_{t}^{r}}{k}n^{r}}}}$$

$$= \left( \sum_{r = 0}^{1}{\sum_{k = 2}^{p + 1}{\sum_{t = r}^{k}\ }} + \sum_{r = 2}^{p + 1}{\sum_{k = r}^{p + 1}{\sum_{t = r}^{k}\ }} \right)\frac{S_{2}\lbrack p,k - 1\rbrack S_{1}\lbrack k,t\rbrack C_{t}^{r}}{k}n^{r}$$

很容易读出系数

$$f\lbrack 0\rbrack = \sum_{k = 2}^{p + 1}{\sum_{t = 0}^{k}\frac{S_{2}\lbrack p,k - 1\rbrack S_{1}\lbrack k,t\rbrack}{k}}$$

$$注意到这里k \geq 2,由第一类斯特林数的性质得$$

$$\sum_{t = 0}^{k}{S_{1}\lbrack k,t\rbrack} = 0，\ 因而f\lbrack 0\rbrack = 0$$

$$f\lbrack 1\rbrack = \sum_{k = 2}^{p + 1}{\sum_{t = 1}^{k}\ \frac{S_{2}\lbrack p,k - 1\rbrack S_{1}\lbrack k,t\rbrack C_{t}^{1}}{k}}$$

$$f\lbrack r\rbrack = \sum_{k = r}^{p + 1}{\sum_{t = r}^{k}\frac{S_{2}\lbrack p,k - 1\rbrack S_{1}\lbrack k,t\rbrack C_{t}^{r}}{k}}\ \ \ \ \left( r \in \mathbf{Z}\lbrack 2,p + 1\rbrack \right)$$

经验证对$r = 1亦成立$。

待求的系数矩阵$a_{p,r}即为f\lbrack r\rbrack$

$$a_{p,r} = \left\{ \begin{array}{r}
\begin{matrix}
\sum_{k = r}^{p + 1}{\sum_{t = r}^{k}\frac{S_{2}\lbrack p,k - 1\rbrack S_{1}\lbrack k,t\rbrack C_{t}^{r}}{k}}, & r \in \mathbf{Z}\lbrack 1,p + 1\rbrack
\end{matrix} \\
\begin{matrix}
0, & r = 0
\end{matrix}
\end{array} \right.\ $$

$$令r = p + 1,同样可得a_{p,p + 1} = \frac{1}{p + 1}$$

$$令r = p,a_{p,p} = \sum_{k = p}^{p + 1}{\sum_{t = p}^{k}\frac{S_{2}\lbrack p,k - 1\rbrack S_{1}\lbrack k,t\rbrack C_{t}^{p}}{k}}$$

$$= \sum_{t = p}^{p}\frac{S_{2}\lbrack p,p - 1\rbrack S_{1}\lbrack p,t\rbrack C_{t}^{p}}{p} + \sum_{t = p}^{p + 1}\frac{S_{2}\lbrack p,p\rbrack S_{1}\lbrack p + 1,t\rbrack C_{t}^{p}}{p + 1}$$

$$= \frac{C_{p}^{2}}{p} - \frac{C_{p + 1}^{2}}{p + 1} + \frac{C_{p + 1}^{1}}{p + 1} = \frac{p - 1}{2} - \frac{p}{2} + 1 = \frac{1}{2}$$

$$这意味着正整数p( > 0)次方幂和结果中p次方的系数恒为\frac{1}{2}$$

$$第一个参数表示行数，第二个参数表示列数，$$

$$矩阵\left\{ a_{p,r} \right\} 如下所示。$$

$$\begin{matrix}
0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & \frac{1}{2} & \frac{1}{2} & 0 & 0 & 0 & 0 & 0 \\
0 & \frac{1}{6} & \frac{1}{2} & \frac{1}{3} & 0 & 0 & 0 & 0 \\
0 & 0 & \frac{1}{4} & \frac{1}{2} & \frac{1}{4} & 0 & 0 & 0 \\
0 & - \frac{1}{30} & 0 & \frac{1}{3} & \frac{1}{2} & \frac{1}{5} & 0 & 0 \\
0 & 0 & - \frac{1}{12} & 0 & \frac{5}{12} & \frac{1}{2} & \frac{1}{6} & 0 \\
0 & \frac{1}{42} & 0 & - \frac{1}{6} & 0 & \frac{1}{2} & \frac{1}{2} & \frac{1}{7}
\end{matrix}$$

在之前的步骤中，有

$$\sum_{m = 1}^{n}m^{p} = \sum_{k = 1}^{p}{S_{2}\lbrack p,k\rbrack\frac{(n + 1)_{k + 1}}{k + 1}}$$

$在n > p$的条件下，$(n + 1)_{k + 1}不会为零，可用组合数表示。$

$$\sum_{m = 1}^{n}m^{p} = \sum_{k = 1}^{p}{S_{2}\lbrack p,k\rbrack\frac{(k + 1)!C_{n + 1}^{k + 1}}{k + 1}} = \sum_{k = 1}^{p}{S_{2}\lbrack p,k\rbrack k!C_{n + 1}^{k + 1}}$$

这是正整数方幂和的组合数表示法，如

$$\sum_{m = 1}^{n}m^{3} = \sum_{k = 1}^{3}{S_{2}\lbrack 3,k\rbrack k!C_{n + 1}^{k + 1}} = C_{n + 1}^{2} + 6C_{n + 1}^{3} + 6C_{n + 1}^{4}$$

[]{#_Toc507114584 .anchor}附录一 阶乘与斯特林数

**[Ap1.1]{.underline}** 递升与递降阶乘

**[Ap1.1.1]{.underline}** 定义

递升阶乘$x^{(n)} ≔ x(x + 1)\ldots(x + n - 1),\ n \in \mathbf{N}^{\mathbf{+}}$

$$表示首项为x，末项为x + n - 1，步长为1的n项之积$$

递降阶乘$(x)_{n} ≔ x(x - 1)\ldots(x - n + 1),n \in \mathbf{N}^{\mathbf{+}}$

$$表示首项为x，末项为x - n + 1，步长为 - 1的n项之积$$

$$特别地，当n = 0时，规定x^{(n)} = (x)_{n} = 1$$

**[Ap1.1.2]{.underline}** 表示

$$阶乘：x^{(n)} = \frac{(x + n - 1)!}{(x - 1)!}\ \ \ \ \ (x)_{n} = \frac{(x)!}{(x - n)!}$$

-阶乘表示需要阶乘数为非负整数，而原定义无此限制，即因式中有负数或非整数亦可。

$$排列数：x^{(n)} = A_{x + n - 1}^{n}\ \ \ \ (x)_{n} = A_{x}^{n}$$

-排列数表示的限制与阶乘类似。

$$连乘号：x^{(n)} = \prod_{k = 0}^{n - 1}{(x + k)}\ \ \ \ (x)_{n} = \prod_{k = 0}^{n - 1}{(x - k)}$$

-连乘号表示不能表示$n = 0$的情况。

**[Ap1.1.3]{.underline}** 性质

两种阶乘的联系：

$$x^{(n)} = ( - x)_{n}( - 1)^{n}\ \ \ \ (x)_{n} = {( - x)}^{(n)}( - 1)^{n}$$

递推关系：

$$x{(x)}^{(n)} = {(x)}^{(n + 1)} - n{(x)}^{(n)}\ \ \ \ \ x(x)_{n} = (x)_{n + 1} + n(x)_{n}$$

**[Ap1.2]{.underline}** 第一类斯特林数

**[Ap1.2.1]{.underline}** 定义

无符号第一类斯特林数$\left| S_{1}\lbrack n,m\rbrack \right|$表示$n$个不同元素构成$m$个圆排列的数目,其中$m,n \in \mathbf{N}^{+},n \geq m.$

$$特别地，当m > n时规定\left| S_{1}\lbrack n,m\rbrack \right| = 0,$$

$$当m = 0,n \neq 0时规定\left| S_{1}\lbrack n,m\rbrack \right| = 0,\ \left| S_{1}\lbrack 0,0\rbrack \right| = 1$$

带符号第一类斯特林数$S_{1}\lbrack n,m\rbrack ≔ ( - 1)^{m + n}\left| S_{1}\lbrack n,m\rbrack \right|$

**[Ap1.2.2]{.underline}** 值列表

$$\begin{matrix}
S_{1}\lbrack n,m\rbrack & m = 0 & 1 & 2 & 3 & 4 & 5 & 6 \\
n = 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
1 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
2 & 0 & - 1 & 1 & 0 & 0 & 0 & 0 \\
3 & 0 & 2 & - 3 & 1 & 0 & 0 & 0 \\
4 & 0 & - 6 & 11 & - 6 & 1 & 0 & 0 \\
5 & 0 & 24 & - 50 & 35 & - 10 & 1 & 0 \\
6 & 0 & - 120 & 274 & - 225 & 85 & - 15 & 1
\end{matrix}$$

**[Ap1.2.3]{.underline}** 性质

递推关系：

$$S_{1}\lbrack n + 1,m\rbrack = S_{1}\lbrack n,m - 1\rbrack - n\ S_{1}\lbrack n,m\rbrack,\ 1 \leq m \leq n$$

$$S_{1}\lbrack n,m\rbrack = \sum_{k = m}^{n}{n^{k - m}S_{1}\lbrack n + 1,k + 1\rbrack}$$

$$横行和为零：\sum_{k = 1}^{n}{S_{1}\lbrack n,k\rbrack = 0},n \geq 2$$

利用第一类斯特林数可以分解递升或递降阶乘为多项式形式。

$$x^{(n)} = \sum_{k = 0}^{n}{\left| S_{1}\lbrack n,k\rbrack \right|x^{k}}\ \ \ \ (x)_{n} = \sum_{k = 0}^{n}{S_{1}\lbrack n,k\rbrack x^{k}}$$

**[Ap1.2.4]{.underline}** 特殊值

$$S_{1}\lbrack n,1\rbrack = ( - 1)^{n - 1}(n - 1)!$$

$$S_{1}\lbrack n,n - 1\rbrack = - C_{n}^{2}$$

**[Ap1.3]{.underline}** 第二类斯特林数

**[Ap1.3.1]{.underline}** 定义

第二类斯特林数$S_{2}\lbrack n,m\rbrack$表示将$n$个不同的元素拆分成$m$个集合的方案数，其中$m,n \in \mathbf{N}^{+},n \geq m.$

$$特别地，当m > n时规定S_{2}\lbrack n,m\rbrack = 0,$$

$$当m = 0,n \neq 0时规定S_{2}\lbrack n,m\rbrack = 0,S_{2}\lbrack 0,0\rbrack = 1$$

**[Ap1.3.2]{.underline}** 值列表

$$\begin{matrix}
S_{2}\lbrack n,m\rbrack & m = 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\
n = 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
1 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
2 & 0 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
3 & 0 & 1 & 3 & 1 & 0 & 0 & 0 & 0 & 0 \\
4 & 0 & 1 & 7 & 6 & 1 & 0 & 0 & 0 & 0 \\
5 & 0 & 1 & 15 & 25 & 10 & 1 & 0 & 0 & 0 \\
6 & 0 & 1 & 31 & 90 & 65 & 15 & 1 & 0 & 0 \\
7 & 0 & 1 & 63 & 301 & 350 & 140 & 21 & 1 & 0 \\
8 & 0 & 1 & 127 & 966 & 1701 & 1050 & 266 & 28 & 1
\end{matrix}$$

**[Ap1.3.3]{.underline}** 性质

第二类斯特林数有通项公式：

$$S_{2}\lbrack n,m\rbrack = \frac{1}{m!}\sum_{k = 0}^{m}{( - 1)^{k}C_{m}^{k}(m - k)^{n}} = \frac{1}{m!}\sum_{k = 0}^{m}{( - 1)^{m - k}C_{m}^{k}k^{n}}$$

递推关系：

$$S_{2}\lbrack n,m\rbrack = S_{2}\lbrack n - 1,m - 1\rbrack + m\ S_{2}\lbrack n - 1,m\rbrack$$

$$S_{2}\lbrack n,m\rbrack = \sum_{k = m}^{n}{m^{n - k}S_{2}\lbrack k - 1,m - 1\rbrack}$$

第二类斯特林数可以将方幂拆分为递降阶乘和：

$$x^{n} = \sum_{k = 0}^{n}{S_{2}\lbrack n,k\rbrack(x)_{k}}$$

两类斯特林数形成的等大方阵互为逆矩阵。

本节参考资料：

http://mathworld.wolfram.com/RisingFactorial.html

http://mathworld.wolfram.com/FallingFactorial.html

http://mathworld.wolfram.com/StirlingNumberoftheFirstKind.html

http://mathworld.wolfram.com/StirlingNumberoftheSecondKind.html

https://baike.baidu.com/item/斯特林数

[^1]: (B.A.卓里奇, 2006 页 299-301)
