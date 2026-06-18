---
title: '组合数，阶乘与幂，对称多项式等一些问题'
date: 2018-01-08
url: /posts/2018/01/xuanshang
tags:
  - Blogpost
  - Mathematic
  - Combinatorics
  - Mathematical Analysis
  - Linear Algebra
  - 11-30 Pages
types:
  - blogpost
topics:
  - mathematics
  - combinatorics
  - mathematical-analysis
  - linear-algebra
lengths:
  - 11-30-pages
authors:
  - me
---

最早是在公众号上发我感兴趣的问题，看看有没有人能解答的，后来开摆了。包括以下几个问题

1. 证明幂可以线性表达阶乘（已有解）
1. 证明第二类斯特林数矩阵的右上角均为零
1. 倒数的对称多项式之和如何表达？（已有解）
1. 证明下降多项式的二项式定理
1. 找方程f(f(x))=x^2+x的解
1. 为了提高经济效益，某商场设置了一台抽奖机器，规则如下：（1）每一次抽奖的初始中奖概率为零。（2）每投入一个币，当次中奖概率就增加 α。（3）一个人抽奖的次数和硬币数不限，机器能吞的硬币不限。为了省钱，是否有合理的投币策略？（直觉上倾向于都一样，但是还没证明）

# 【悬赏001】

求证：

$$\sum_{k = 0}^{n}{( - 1)^{n - k}C_{n}^{k}k^{n}} = n!\ \ (n \in \mathbf{N}^{\mathbf{*}})$$

请找出纯代数证法。

【等价命题】

$$A:\sum_{k = 1}^{n}{( - 1)^{n - k}C_{n}^{k}k^{n}} = n!\ \ (n \in \mathbf{N}^{\mathbf{*}})$$

$$B:\sum_{k = 0}^{n}{( - 1)^{k}C_{n}^{k}{(n - k)}^{n}} = n!\ \ (n \in \mathbf{N}^{\mathbf{*}})$$

$$C:\sum_{k = 0}^{n}\frac{( - 1)^{n - k}k^{n}}{k!(n - k)!} = 1\ \ (n \in \mathbf{N}^{\mathbf{*}})$$

【说明】

很神奇，利用正整数的幂次和组合数表示出了阶乘。

举几个例子：$1! = C_{1}^{1}1^{1} = 1$

$$2! = - C_{2}^{1}1^{2} + C_{2}^{2}2^{2} = - 2 + 4 = 2$$

$$3! = C_{3}^{1}1^{3} - C_{3}^{2}2^{3} + C_{3}^{3}3^{3} = 3 - 24 + 27 = 6$$

$$4! = - C_{4}^{1}1^{4} + C_{4}^{2}2^{4} - C_{4}^{3}3^{4} + C_{4}^{4}4^{4}$$

$$\ \ \ \ \  = - 4 + 96 - 324 + 256 = 24$$

【问题背景】

1.  m个不同的球放进n个不同的盒子里，\
    要求每个盒子至少有一个球，方案总数\
    $$f(m,n) = \sum_{k = 0}^{n}{( - 1)^{n - k}C_{n}^{k}k^{m}}
    $$当m=n时，每个盒子里只能装一个球，\
    显然方案总数为n!，于是\
    $$f(n,n) = \sum_{k = 0}^{n}{( - 1)^{n - k}C_{n}^{k}k^{n}} = n!
    $$注：这是一种证法，但比较好奇有没有\
    不构造实际情景，纯代数的证法。

2.  一号数学研究指出，n次幂可以分解成阶乘和\
    $$n^{m} = \sum_{s = 0}^{m - 1}{x_{m,s}\prod_{q = 0}^{s}(n - q)}
    $$其中$x_{m,s}$为第二类斯特林数\
    $$x_{m,s} = \frac{1}{s!}\sum_{k = 0}^{s}( - 1)^{k}C_{s}^{k}(s - k)^{m}
    $$命题等价于求证$x_{m,m} = 1$

3.  一号数学研究指出，n次幂可以分解成阶乘和\
    而所需证明的等式是用阶乘和合成n次幂，\
    似乎有互逆关系。

# 【悬赏001解】

【证】

引理

$$范德蒙行列式\left| \begin{matrix}
1 & 1 & \cdots & 1 \\
x_{1} & x_{2} & \cdots & x_{n} \\
 \vdots & \vdots & \ddots & \vdots \\
x_{1}^{n - 1} & x_{2}^{n - 1} & \cdots & x_{n}^{n - 1}
\end{matrix} \right| = \prod_{1 \leq i < j \leq n}^{}\left( x_{j} - x_{i} \right)$$

证略。

$$断言\ \sum_{j = 0}^{n}{( - 1)^{j}f\left( b_{j} \right)C_{n}^{j}} = ( - 1)^{n}a_{n}n!d^{n}$$

$$其中\ f(x) = a_{n}x^{n} + \ldots + a_{0},\left\{ b_{n} \right\} 是公差为d的等差数列,d \neq 0$$

$$令f(x) = x^{n},b_{n} = n,则d = 1$$

$$即得到\sum_{j = 0}^{n}{( - 1)^{j}j^{n}C_{n}^{j}} = ( - 1)^{n}n!$$

断言的证明：

$$记D = \left| \begin{matrix}
1 & 1 & \cdots & 1 \\
b_{1} & b_{2} & \cdots & b_{n + 1} \\
 \vdots & \vdots & \ddots & \vdots \\
b_{1}^{n} & b_{2}^{n} & \cdots & b_{n + 1}^{n}
\end{matrix} \right|,由引理,D = \prod_{1 \leq i < j \leq n + 1}^{}\left( b_{j} - b_{i} \right)$$

$$记D第n + 1行j列位置\left. （即b_{j}^{n} \right.）的余子式为D_{j}（非代数余子式）$$

$$D_{j} = \left| \begin{matrix}
1 & \cdots & \widehat{1} & \cdots & 1 \\
b_{1} & \cdots & \widehat{b_{j}} & \cdots & b_{n + 1} \\
 \vdots & & \vdots & & \vdots \\
b_{1}^{n - 1} & \cdots & \widehat{b_{j}^{n - 1}} & \cdots & b_{n + 1}^{n - 1}
\end{matrix} \right|,其中\begin{pmatrix}
\widehat{1} \\
\widehat{b_{j}} \\
 \vdots \\
\widehat{b_{j}^{n - 1}}
\end{pmatrix}表示行列式中除去这一列$$

$$由引理可知D_{j} = \prod_{\begin{array}{r}
1 \leq s < t \leq n + 1 \\
s,t \neq j
\end{array}}^{}\left( b_{t} - b_{s} \right) = \frac{( - 1)^{n + 1 + j}\prod_{\begin{array}{r}
1 \leq s < t \leq n + 1
\end{array}}^{}\left( b_{t} - b_{s} \right)}{\prod_{\begin{array}{r}
1 \leq s < t \leq n + 1 \\
s = j
\end{array}}^{}\left( b_{t} - b_{s} \right)\prod_{\begin{array}{r}
1 \leq s < t \leq n + 1 \\
t = j
\end{array}}^{}\left( b_{t} - b_{s} \right)}$$

$$= \frac{D}{\prod_{\begin{array}{r}
j < t \leq n + 1
\end{array}}^{}\left( b_{t} - b_{j} \right)\prod_{\begin{array}{r}
1 \leq s < j
\end{array}}^{}\left( b_{j} - b_{s} \right)}$$

$$由b_{n}的等差数列性质可知,b_{t} - b_{j} = (t - j)d,b_{j} - b_{s} = (j - s)d,$$

$$\prod_{\begin{array}{r}
j < t \leq n + 1
\end{array}}^{}\left( b_{t} - b_{j} \right) = \prod_{t = j + 1}^{n + 1}{(t - j)d} = (n + 1 - j)!\ d^{n + 1 - j}$$

$$\prod_{\begin{array}{r}
1 \leq s < j
\end{array}}^{}\left( b_{j} - b_{s} \right) = \prod_{s = 1}^{j - 1}{(j - s)d} = (j - 1)!\ d^{j - 1}$$

$$于是D_{j} = \frac{D}{(n + 1 - j)!\ d^{n + 1 - j}(j - 1)!\ d^{j - 1}} = \frac{C_{n}^{j - 1}D}{n!\ d^{n}}$$

$$考虑D^{'} = \left| \begin{matrix}
1 & 1 & \cdots & 1 \\
b_{1} & b_{2} & \cdots & b_{n + 1} \\
 \vdots & \vdots & \ddots & \vdots \\
f\left( b_{1} \right) & f\left( b_{2} \right) & \cdots & f\left( b_{n + 1} \right)
\end{matrix} \right|$$

$$注意到D^{'}与D仅有最后一行不同,将D^{'}由最后一行展开,得到$$

$$D^{'} = \sum_{j = 1}^{n + 1}{( - 1)^{n + 1 + j}f\left( b_{j} \right)D_{j}} = \sum_{j = 1}^{n + 1}{( - 1)^{n + 1 + j}f\left( b_{j} \right)\frac{C_{n}^{j - 1}D}{n!\ d^{n}}}$$

$$另一方面,由行列式的行变换,可将f\left( b_{j} \right)次数低于n的项全部消去$$

$$可知D^{'} = \left| \begin{matrix}
1 & 1 & \cdots & 1 \\
b_{1} & b_{2} & \cdots & b_{n + 1} \\
 \vdots & \vdots & \ddots & \vdots \\
a_{n}b_{1}^{n} & a_{n}b_{2}^{n} & \cdots & a_{n}b_{n + 1}^{n}
\end{matrix} \right| = a_{n}D$$

$$于是\sum_{j = 1}^{n + 1}{( - 1)^{n + 1 + j}f\left( b_{j} \right)\frac{C_{n}^{j - 1}D}{n!\ d^{n}}} = a_{n}D$$

$$由d \neq 0可知\left\{ b_{n} \right\} 互不相同,由引理可知D \neq 0$$

$$约去D,整理得到\sum_{j = 1}^{n + 1}{C_{n}^{j - 1}( - 1)^{n + 1 + j}f\left( b_{j} \right)} = n!a_{n}\ d^{n}$$

$$即\sum_{j = 0}^{n}{C_{n}^{j}( - 1)^{j}f\left( b_{j} \right)} = \left. （ - 1 \right.）^{n}n!a_{n}\ d^{n}\ \ \ \ \ \ \ \blacksquare$$

【思考】

$$\sum_{j = 0}^{n}{( - 1)^{j}f\left( b_{j} \right)C_{n}^{j}} = ( - 1)^{n}a_{n}n!d^{n}是一个很有用的式子，从几方面考量它的意义。$$

$$首先,待定量是多项式f(x)和等差数列b_{n},这个式子将它们联系起来。$$

$$其次，公式可以变形为a_{n} = \frac{1}{n!d^{n}}\left( \sum_{j = 0}^{n}{( - 1)^{n - j}f\left( b_{j} \right)C_{n}^{j}} \right)$$

$$这就是说我们能通过多项式在n + 1个等间隔点的值确定出多项式的首项系数。$$

$$不过这是比插值公式相对较弱的一个结论。$$

$$再者，对于形如\sum_{j = 0}^{n}{( - 1)^{j}C_{n}^{j}y_{n}}的式子，今后也有办法可以计算。$$

$$只需要找f(x),使得f在一系列等差点b_{0},\ldots,b_{n}上分别取到y_{0},\ldots,y_{n}$$

由于取等差点的目的只是为了求得首项系数，可以考虑$0,1,\ldots,n$

通过插值公式，能得到$f(x)$的首项系数，则该式的值为$\left. （ - 1 \right.）^{n}n!a_{n}\ d^{n}$

【一个推论】

$$\sum_{j = 0}^{n}{C_{n}^{j}( - 1)^{j}f\left( b_{j} \right)} = \left. （ - 1 \right.）^{n}n!a_{n}\ d^{n}$$

$$当f(x)最高次系数为k,k < n时,a_{n} = 0$$

$$此时\sum_{j = 0}^{n}{C_{n}^{j}( - 1)^{j}f\left( b_{j} \right)} = 0$$

$$特别地,取f(x) = x^{k},k < n,b_{j} = j,\sum_{j = 0}^{n}{C_{n}^{j}( - 1)^{j}j^{k}} = 0$$

这是悬赏002的主题。

更多应用可见参考文献相关内容。

【说明】

这个解法已经十分巧妙，并且也算是符合了代数证法的要求。当然，如果你有其他更巧妙的方法，也欢迎分享给我。

【参考文献】

历届美国大学生数学竞赛试题集------第一卷（1938\~1949）:152-156

# 【悬赏002】

$$函数f(m,n) = \sum_{k = 0}^{n}{( - 1)^{n - k}C_{n}^{k}k^{m}}\ \ (m,n \in \mathbf{N}^{\mathbf{*}})$$

请从代数角度证明：

$$当m < n时f(m,n) \equiv 0$$

【等价命题】

A:函数f中到底是什么结构决定了这么一个性质？

B:能否构造出一个"正常"（如不间断，不分段，不单独定义，

解析式不复杂，可描点，无高等函数等）的二元函数

也具有类似的性质？

如果能，它们有什么共同点？

【说明】

看一下函数值表。

$$\begin{matrix}
1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
1 & 2 & 0 & 0 & 0 & 0 & 0 & 0 \\
1 & 6 & 6 & 0 & 0 & 0 & 0 & 0 \\
1 & 14 & 36 & 24 & 0 & 0 & 0 & 0 \\
1 & 30 & 150 & 240 & 120 & 0 & 0 & 0 \\
1 & 62 & 540 & 1560 & 1800 & 720 & 0 & 0 \\
1 & 126 & 1806 & 8400 & 16800 & 15120 & 5040 & 0 \\
1 & 254 & 5796 & 40824 & 126000 & 191520 & 141120 & 40320
\end{matrix}$$

注意到左下角都是一般的正数，右上角却全为0

划重点，刚好全是0，而不是别的什么。

举几个例子：

$$f(1,2) = \sum_{k = 0}^{2}{{( - 1)}^{2 - k}C_{2}^{k}k^{1}} = - 2 + 2 = 0$$

$$f(3,4) = \sum_{k = 0}^{4}{( - 1)^{4 - k}C_{4}^{k}k^{3}} = - 4 + 48 - 108 + 64 = 0$$

$$f(3,5) = \sum_{k = 0}^{5}{{( - 1)}^{5 - k}C_{5}^{k}k^{3}} = 5 - 80 + 270 - 320 + 125 = 0$$

$$f(4,7) = \sum_{k = 0}^{7}{( - 1)^{7 - k}C_{7}^{k}k^{4}}$$

$$= 7 - 336 + 2835 - 8960 + 13125 - 9072 + 2401 = 0$$

每一项数字有比十小的个位数，也有成百上千，

然而到底是什么魔力使得它们之和总刚好为0？

【问题背景】

4.  $f(m,n)$为m个不同的球放进n个不同的盒子，\
    要求每个盒子至少有一个球的方案总数，显然\
    当m\<n时，找不到满足要求的方案。\
    注：这是一种证法，但比较好奇有没有\
    不构造实际情景，纯代数的证法。

5.  第二类斯特林数S也有类似的性质。\
    它与f的关系如下\
    $$S(m,n) = \frac{1}{n!}f(m,n)
    $$

【进展】

在【悬赏001·解】中，利用

$$\sum_{j = 0}^{n}{C_{n}^{j}( - 1)^{j}f\left( b_{j} \right)} = \left. （ - 1 \right.）^{n}n!a_{n}\ d^{n}$$

$$得到了k < n时$$

$$\sum_{j = 0}^{n}{C_{n}^{j}( - 1)^{j}j^{k}} = 0$$

# 【悬赏003】

$$定义p_{k} ≔ \sum_{t = 1}^{n}x_{t}^{k}\ (k \in \mathbf{Z})$$

试用初等对称多项式$s_{1},s_{2},\ldots,s_{n},$

$$表示出p_{k} ≔ \sum_{t = 1}^{n}x_{t}^{k}\ (k < 0时)$$

递推式亦可。

$$【等价命题】$$

$$A:试用初等对称多项式表示出\sum_{t = 1}^{n}{\prod_{\begin{array}{r}
r = 1 \\
r \neq t
\end{array}}^{n}x_{r}^{k}}$$

$$【说明】$$

$$初等对称多项式形式与韦达定理相同。$$

$$s_{1} = x_{1} + x_{2} + \ldots + x_{n}$$

$$s_{2} = x_{1}x_{2} + x_{1}x_{3} + \ldots + x_{n - 1}x_{n}$$

...

$$s_{n} = x_{1}x_{2}\ldots x_{n}$$

$$当k = - 1时，事情还比较简单。$$

$$p_{- 1} = \frac{1}{x_{1}} + \frac{1}{x_{2}} + \ldots + \frac{1}{x_{n}} = \frac{s_{n - 1}}{s_{n}}$$

$$当k = - 2时，就十分困难了。$$

$$p_{- 2} = \frac{1}{x_{1}^{2}} + \frac{1}{x_{2}^{2}} + \ldots + \frac{1}{x_{n}^{2}}$$

$$= \frac{x_{2}^{2}x_{3}^{2}\ldots x_{n}^{2} + \ldots + x_{1}^{2}x_{2}^{2}\ldots x_{n - 1}^{2}}{s_{n}^{2}}$$

经由电脑计算找规律得到

$$p_{- 2} = \frac{s_{n - 1}^{2} - 2s_{n - 2}s_{n}}{s_{n}^{2}}$$

$$p_{- 3} = \frac{s_{n - 1}^{3} - 3s_{n - 2}s_{n - 1}s_{n} + 3s_{n - 3}s_{n}^{2}}{s_{n}^{3}}$$

$$【背景】$$

$${关于s_{k}和p_{k}的联系，有如下的牛顿公式
}{p_{k} - s_{1}p_{k - 1} + s_{2}p_{k - 2} + \ldots + ( - 1)^{k - 1}s_{k - 1}p_{1} + ( - 1)^{k}s_{k}k = 0,\ \ 1 \leq k \leq n}$$

$$p_{k} - s_{1}p_{k - 1} + s_{2}p_{k - 2} + \ldots + ( - 1)^{n - 1}s_{n - 1}p_{k - n + 1} + ( - 1)^{n}s_{n}p_{k - n} = 0,\ \ k \geq n$$

结合克拉默公式有

$$p_{k} = \left| \begin{matrix}
s_{1} & 1 & 0 & 0 & \cdots & 0 \\
2s_{2} & s_{1} & 1 & 0 & \cdots & 0 \\
3s_{3} & s_{2} & s_{1} & 1 & \cdots & 0 \\
 \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
(k - 1)s_{k - 1} & s_{k - 2} & s_{k - 3} & s_{k - 4} & \cdots & 1 \\
ks_{k} & s_{k - 1} & s_{k - 2} & s_{k - 3} & \cdots & s_{1}
\end{matrix} \right|$$

$$s_{k} = \frac{1}{k!}\left| \begin{matrix}
p_{1} & 1 & 0 & 0 & \cdots & 0 \\
p_{2} & p_{1} & 1 & 0 & \cdots & 0 \\
p_{3} & p_{2} & p_{1} & 1 & \cdots & 0 \\
 \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
p_{k - 1} & p_{k - 2} & p_{k - 3} & p_{k - 4} & \cdots & 1 \\
p_{k} & p_{k - 1} & p_{k - 2} & p_{k - 3} & \cdots & p_{1}
\end{matrix} \right|$$

$$在证明牛顿公式的过程中\left. （非标准证法 \right.），$$

$$设x_{1},x_{2},\ldots,x_{n}为方程x^{n} + a_{1}x^{n - 1} + \ldots + a_{n} = 0的n个互不相同的根。$$

$$则s_{1} = - a_{1},\ s_{k} = ( - 1)^{k}a_{k}\ \ ,因而a_{k} = ( - 1)^{k}s_{k}$$

$$于是x^{n} - s_{1}x^{n - 1} + \ldots + ( - 1)^{n}s_{n} = 0$$

$$在k \geq n时，方程两边乘x^{k - n}，并代入x_{1},x_{2},\ldots,x_{n}求和后得到$$

$$p_{k} - s_{1}p_{k - 1} + s_{2}p_{k - 2} + \ldots + ( - 1)^{n - 1}s_{n - 1}p_{k - n + 1} + ( - 1)^{n}s_{n}p_{k - n} = 0$$

$$在k \leq n时，先考虑k = n - 1,方程两边除以x，并代入x_{1},x_{2},\ldots,x_{n}求和后得到$$

$$p_{n - 1} - s_{1}p_{n - 2} + s_{2}p_{n - 3} + \ldots + ( - 1)^{n - 1}s_{n - 1}p_{0} + ( - 1)^{n}s_{n}p_{- 1} = 0,$$

$$利用p_{- 1} = \frac{s_{n - 1}}{s_{n}}，p_{0} = n得到$$

$$p_{n - 1} - s_{1}p_{n - 2} + s_{2}p_{n - 3} + \ldots + ( - 1)^{n - 1}(n - 1)s_{n - 1} = 0,$$

命题成立。

$$在k = n - r时，做类似的操作，则需要考虑p_{- 1},p_{- 2},\ldots,p_{- r}$$

由于$p_{k}(k < 0)表达式难以求得，因而这样无法证明牛顿公式第一式。$

但是牛顿公式可以用别的方法证得，也许能由牛顿公式去反推$p_{- 1},p_{- 2},\ldots,p_{- r}$

\*我觉得这样至少能摆弄个递推公式出来，把这个机会留给读者。

# $$\mathbf{【悬赏}\mathbf{003}\mathbf{解】}$$

$$设x_{1},x_{2},\ldots,x_{n}的初等对称多项式$$

$$s_{1} = x_{1} + x_{2} + \ldots + x_{n}$$

$$s_{2} = x_{1}x_{2} + x_{1}x_{3} + \ldots + x_{n - 1}x_{n}$$

$$\ldots$$

$$s_{n} = x_{1}x_{2}\ldots x_{n}$$

$$再类似地，$$

$$设y_{1},y_{2},\ldots,y_{n}的初等对称多项式为$$

$t_{1},t_{2},\ldots,t_{n}$，$并且规定$

$$y_{k} = \frac{1}{x_{k}}\ ,k = 1,2,\ldots,n$$

$$设p_{k} = \sum_{t = 1}^{n}x_{n}^{k}\ ,q_{k} = \sum_{t = 1}^{n}y_{n}^{k}$$

$$则p_{- k} = q_{k}$$

$$当k > 0时$$

$$由牛顿公式等知$$

$$q_{k}可用q_{1},\ldots,q_{k - 1}和t_{1},\ldots,t_{k}递推表示$$

$$或可直接用t_{1},\ldots,t_{k}表示。$$

$$因此要想用s_{1},\ldots,s_{n}表达p_{- k},$$

只需用$s_{1},\ldots,s_{n}表示t_{r},\ r = 1,2,\ldots,k$

$$作一些试验：$$

$$t_{1} = \frac{1}{x_{1}} + \frac{1}{x_{2}} + \ldots + \frac{1}{x_{n}}$$

通分后分母显然为$s_{n}\ ,分子为n项之和，$

$$每一项都是x_{1}到x_{n}缺一项的乘积$$

$$刚好为s_{n - 1},于是t_{1} = \frac{s_{n - 1}}{s_{n}}$$

$$t_{2} = \frac{1}{x_{1}x_{2}} + \frac{1}{x_{1}x_{3}} + \ldots + \frac{1}{x_{n - 1}x_{n}}$$

$$通分后分母仍然为s_{n}$$

分子的每一项是$x_{1}到x_{n}缺两项的乘积$

$$刚好为s_{n - 2}$$

$$以此类推，可得$$

$$t_{k} = \frac{s_{n - k}}{s_{n}}$$

在牛顿公式中，将$p换为q,s换为t，k换为k^{'},即$

$$q_{k'} - t_{1}q_{k^{'} - 1} + t_{2}q_{k^{'} - 2} + \ldots + ( - 1)^{k^{'} - 1}t_{k^{'} - 1}q_{1} + ( - 1)^{k^{'}}t_{k^{'}}k' = 0,\ \ 1 \leq k' \leq n$$

$$q_{k'} - t_{1}q_{k^{'} - 1} + t_{2}q_{k^{'} - 2} + \ldots + ( - 1)^{n - 1}t_{n - 1}q_{k^{'} - n + 1} + ( - 1)^{n}t_{n}q_{k^{'} - n} = 0,\ \ k' \geq n$$

并代入$
$$$t_{k'} = \frac{s_{n - k'}}{s_{n}}\ ,\ q_{k'} = p_{- k'}\ ,k^{'} = - k$$

得到

$$p_{k} - \frac{s_{n - 1}}{s_{n}}p_{k + 1} + \frac{s_{n - 2}}{s_{n}}p_{k + 2} + \ldots + ( - 1)^{k - 1}\frac{s_{n + k + 1}}{s_{n}}p_{- 1} + ( - 1)^{k}\frac{s_{n + k}}{s_{n}}( - k) = 0,\ \  - n \leq k \leq - 1$$

$$p_{k} - \frac{s_{n - 1}}{s_{n}}p_{k + 1} + \frac{s_{n - 2}}{s_{n}}p_{k + 2} + \ldots + ( - 1)^{n - 1}\frac{s_{1}}{s_{n}}p_{n + k - 1} + ( - 1)^{n}\frac{s_{0}}{s_{n}}p_{n + k} = 0,\ \ k \leq - n$$

关于行列式，类似有

$$q_{k'} = \left| \begin{matrix}
\frac{s_{n - 1}}{s_{n}} & 1 & 0 & 0 & \cdots & 0 \\
2\frac{s_{n - 2}}{s_{n}} & \frac{s_{n - 1}}{s_{n}} & 1 & 0 & \cdots & 0 \\
3\frac{s_{n - 3}}{s_{n}} & \frac{s_{n - 2}}{s_{n}} & \frac{s_{n - 1}}{s_{n}} & 1 & \cdots & 0 \\
 \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
(k' - 1)\frac{s_{n - k^{'} + 1}}{s_{n}} & \frac{s_{n - k' + 2}}{s_{n}} & \frac{s_{n - k' + 3}}{s_{n}} & \frac{s_{n - k' + 4}}{s_{n}} & \cdots & 1 \\
k'\frac{s_{n - k'}}{s_{n}} & \frac{s_{n - k' + 1}}{s_{n}} & \frac{s_{n - k' + 2}}{s_{n}} & \frac{s_{n - k' + 3}}{s_{n}} & \cdots & \frac{s_{n - 1}}{s_{n}}
\end{matrix} \right|$$

$$= \frac{1}{s_{n}^{k'}}\left| \begin{matrix}
s_{n - 1} & s_{n} & 0 & 0 & \cdots & 0 \\
2s_{n - 2} & s_{n - 1} & s_{n} & 0 & \cdots & 0 \\
3s_{n - 3} & s_{n - 2} & s_{n - 1} & s_{n} & \cdots & 0 \\
 \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
(k' - 1)s_{n - k' + 1} & s_{n - k' + 2} & s_{n - k' + 3} & s_{n - k' + 4} & \cdots & s_{n} \\
ks_{n - k'} & s_{n - k' + 1} & s_{n - k' + 2} & s_{n - k' + 3} & \cdots & s_{n - 1}
\end{matrix} \right|$$

$$于是p_{k} = s_{n}^{k}\left| \begin{matrix}
s_{n - 1} & s_{n} & 0 & 0 & \cdots & 0 \\
2s_{n - 2} & s_{n - 1} & s_{n} & 0 & \cdots & 0 \\
3s_{n - 3} & s_{n - 2} & s_{n - 1} & s_{n} & \cdots & 0 \\
 \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
( - k - 1)s_{n + k + 1} & s_{n + k^{'} + 2} & s_{n + k^{'} + 3} & s_{n + k^{'} + 4} & \cdots & s_{n} \\
 - ks_{n + k} & s_{n + k^{'} + 1} & s_{n + k^{'} + 2} & s_{n + k^{'} + 3} & \cdots & s_{n - 1}
\end{matrix} \right|(k < 0)$$

作为验算，考虑

$$p_{- 2} = \frac{1}{s_{n}^{2}}\left| \begin{matrix}
s_{n - 1} & s_{n} \\
2s_{n - 2} & s_{n - 1}
\end{matrix} \right| = \frac{s_{n - 1}^{2} - 2s_{n - 2}s_{n}}{s_{n}^{2}}$$

$$p_{- 3} = \frac{1}{s_{n}^{3}}\left| \begin{matrix}
s_{n - 1} & s_{n} & 0 \\
2s_{n - 2} & s_{n - 1} & s_{n} \\
3s_{n - 3} & s_{n - 2} & s_{n - 1}
\end{matrix} \right| = \frac{s_{n - 1}^{3} + 3s_{n}^{2}s_{n - 3} - 3s_{n}s_{n - 1}s_{n - 2}}{s_{n}^{3}}$$

$$与之前电脑计算得到的结果相同。$$

# 【悬赏004】

$$定义运算(x)_{0} = 1$$

$$(x)_{n} = x(x - 1)\ldots(x - n + 1),n \in \mathbf{N}^{\mathbf{*}}$$

$$证明：$$

$$\left. （a + b \right.）_{n} = \sum_{k = 0}^{n}{C_{n}^{k}\ (a)_{n - k}(b)_{k}}$$

【高级目标】

利用$(x)_{n}和x^{n}$的相似性证明上面的命题。

【说明】

长得特别像二项式定理，

结合悬赏001还有之前的一号数学研究，

似乎可以说$(x)_{n}和普通的幂x^{n}$有相似的性质。

不知道有没有可能找一个群同构，

或者类似的东西来帮助证明以上命题？

【例子】

$$\left. （a + b \right.）_{1} = \sum_{k = 0}^{1}{C_{1}^{k}\ (a)_{1 - k}(b)_{k}} = a + b$$

$$\left. （a + b \right.）_{2} = (a + b)^{2} - (a + b) = a^{2} + 2ab + b^{2} - a - b$$

$$\sum_{k = 0}^{2}{C_{2}^{k}\ (a)_{2 - k}(b)_{k}} = (a)_{2} + 2ab + (b)_{2} = a^{2} - a + 2ab + b^{2} - b$$

$$(a + b)_{3} = (a + b)^{3} - 3(a + b)^{2} + 2(a + b)$$

$$= a^{3} + 3a^{2}b + 3ab^{2} + b^{3} - 3a^{2} - 6ab - {3b}^{2} + 2a + 2b$$

$$\sum_{k = 0}^{3}{C_{3}^{k}\ (a)_{3 - k}(b)_{k}} = (a)_{3} + 3(a)_{2}(b)_{1} + 3(a)_{1}(b)_{2} + (b)_{3}$$

$$= a^{3} - 3a^{2} + 2a + 3a^{2}b - 3ab + 3ab^{2} - 3ab + b^{3} - 3b^{2} + 2b$$

【背景】

1.  $(x)_{n}$称为Pochhammer函数，在维基百科它的词条\
    （亦'Falling and rising factorials'）中记载了需要证明的等式，*\
    *但似乎没有直接给出证明。

2.  在维基百科'Binomial type'词条中，满足关系式\
    ![](media/media/image2.svg){width="2.21875in" height="0.4375in"}\
    的多项式序列$p_{n}$被称作具有二项式性质，\
    它们形成一个集合，除了$(x)_{n}$外，\
    阿贝尔多项式$p_{n}(x) = x(x - an)^{n - 1}$等也在其中。

3.  一号数学研究指出\
    $${x^{n} = \sum_{t = 1}^{n}{S_{n,t - 1}(x)_{t}}，其中S_{n,m}为第二类斯特林数
    }{满足S_{n,m} = \frac{1}{m!}\sum_{k = 0}^{m}( - 1)^{k}C_{m}^{k}(m - k)^{n}}$$

4.  $无符号的第一类斯特林数c_{n,m}，$\
    $$表示n个不同元素构成m个圆排列的数目
    $$带符号的第一类斯特林数$s_{n,k} = ( - 1)^{n - k}c_{n,k}$\
    $${(x)_{n} = \sum_{k = 0}^{n}{s_{n,k}x^{k}},\
    }{和上面的相反，把阶乘拆成了幂次和。}$$

# 【悬赏005】

结合极限严格证明：

$$f(x) = ``\lim_{a \rightarrow 0}"\frac{a}{x^{2} + x}$$

$$是方程f\left( f(x) \right) = x^{2} + x的解$$

或$
$$$f(x) = ``\lim_{a \rightarrow 0}"\frac{a}{x^{2} + x}$$

$$不是方程f\left( f(x) \right) = x^{2} + x的解$$

【必由之路】

$$请给f(x) = ``\lim_{a \rightarrow 0}"\frac{a}{x^{2} + x}\ $$

$$下一个准确的定义。$$

【说明】

$$我们先对\frac{a}{x^{2} + x}复合，得到$$

$$\frac{a}{\left( \frac{a}{x^{2} + x} \right)^{2} + \frac{a}{x^{2} + x}} = \frac{\left( x^{2} + x \right)^{2}}{a + \left( x^{2} + x \right)}$$

$$再令a趋向于0，就得到x^{2} + x$$

$$乍一看，似乎f(x) = \lim_{a \rightarrow 0}\frac{a}{x^{2} + x}就是解。$$

但是这样一来，$f(x)就直接成为0了。$

$$那么，我们让a不等于0，$$

$$a取1,\ 0.01,\ 0.00001\ldots\ldots$$

则此时$f(x)不是0，可以正常复合，$

$$由复合后为\frac{\left( x^{2} + x \right)^{2}}{a + \left( x^{2} + x \right)}可知$$

$$结果会越来越趋向于x^{2} + x$$

$$所以就有两个问题：$$

1.  $结合极限的定义，到底应该如何定义$\
    $$这样的f(x)？$$

2.  判断这个$f(x)到底是不是方程的解。$

最头疼的是第一个问题，有了定义之后

第二个问题就不足为惧了。

【背景】

知乎有"f(f(x))=x\^2+x，如何求 f(x)？"的问题，

讨论十分丰富，甚至有一大类类似方程的可解性。

不过似乎没有和这个悬赏相关的内容。

# 【悬赏007】

$$\alpha \in (0,1),\ \ x_{0} = 0,x_{k} \in \left( 0,\frac{1}{\alpha} \right),k = 1,2,\ldots\ $$

$$设\ S = \sum_{k = 1}^{\infty}\left( \left( \prod_{l = 0}^{k - 1}\left( 1 - \alpha\ x_{l} \right) \right)\alpha x_{k}\left( \sum_{l = 0}^{k}x_{l} \right) \right)$$

$$满足\sum_{k = 1}^{\infty}\left( \left( \prod_{l = 0}^{k - 1}\left( 1 - \alpha\ x_{l} \right) \right)\alpha x_{k} \right) = 1$$

$$求一个\ x_{n}\ 的通项公式，使得\ S\ 最小。$$

【背景】

为了提高经济效益，某商场设置了一台抽奖机器，规则如下：

（1）每一次抽奖的初始中奖概率为零。

（2）每投入一个币，当次中奖概率就增加$\ \alpha\ \ \left. （\alpha \in (0,1) \right.）\ \ $。

（3）一个人抽奖的次数和硬币数不限，机器能吞的硬币不限。

这里计算的时候可以任意给定概率，不受整数限制。

然而概率当然不能比0低或者比1大。

小明非常想要中奖的礼物，他拿着用了毕生心血攒下来的无穷多的硬币去抽奖。虽然硬币有无穷多，但是小明还是希望能够节约一些。于是他开始苦恼应该投多少硬币。

小张说："当然是一次投多一些了，虽然花的多，但是几率大，没几次就有很大概率中奖。"

然而小红觉得不对："一次投太多感觉很浪费，少投一些，花的硬币就会少一点。"

$$听了两个知心好友的话，小明决定相信数学。他在心里盘算着：$$

我要算一下每种方案平均我要花的硬币数量。

因为失败几率总存在，所以理论上我有可能要投无限次硬币。

$$考虑直到第\ k\ 次抽奖我才中，这说明前面已经失败了\ k - 1\ 次$$

$$之前第\ t\ 次我投了\ x_{t}\ 个硬币，那一次失败概率是\left( 1 - x_{t}\alpha \right)$$

$$所以我连跪\ k - 1\ 局的概率是\ \prod_{t = 1}^{k - 1}\left( 1 - \alpha\ x_{t} \right)$$

$$为了\ k = 1\ 的时候这个式子也能用，引入\ x_{0} = 0，$$

$$连跪\ k - 1\ 局的概率是\ \prod_{t = 0}^{k - 1}\left( 1 - \alpha\ x_{t} \right)$$

$$这一次我投了\ x_{k}\ 个硬币，成功概率是\ x_{k}\alpha$$

$$总的来说，我在第\ k\ 次中奖的概率为\prod_{t = 0}^{k - 1}\left( 1 - \alpha\ x_{t} \right)x_{k}\alpha$$

$$我在第\ k\ 次中奖，总共已经给机器喂了\sum_{t = 0}^{k}x_{t}个硬币$$

于是就能算出中奖所需要的硬币数数学期望。

$$S = \sum_{k = 1}^{\infty}\left( \left( \prod_{t = 0}^{k - 1}\left( 1 - \alpha\ x_{t} \right) \right)\alpha x_{k}\left( \sum_{t = 0}^{k}x_{t} \right) \right)$$

这一串玩意儿似乎在瞪着眼嘲笑小明。

虽然小明能拿着无穷多的硬币，然而当他尝试着对这个有无穷多变量的函数，每个变量求了一遍导，发现并不能拿着这无穷个方程对这一串玩意儿做什么事情。

小张见了这个式子，说："要求最小值？那不是让$\ x$全取零就OK? 这就最小了。"

小明："这样还怎么中奖？"

小张："反正你本来也是失败无穷多次，不一样嘛？"

小明：......（一定有哪儿不对劲）

于是小明写了一个条件把小张拍了回去。

$$\sum_{k = 1}^{\infty}\left( \left( \prod_{l = 0}^{k - 1}\left( 1 - \alpha\ x_{l} \right) \right)\alpha x_{k} \right) = 1$$

小明："只要满足这个条件，我就有必胜的信心。我先试试每次扔固定数量的硬币。"

他掏出了两根无限长的棍子把无穷多个变量串在了一起：

$$设x = x_{1} = x_{2} = x_{3} = \ldots$$

$$于是\ S = \sum_{k = 1}^{\infty}\left( (1 - \alpha\ x)^{k - 1}k\alpha x^{2} \right)$$

这个式子开始瑟瑟发抖，因为小明的差比数列技能是S+级的。

只见他顺手就抄起了$(1 - \alpha\ x)\ 戳在了\ S\ 的复制品身上$

$$(1 - \alpha\ x)S = \sum_{k = 1}^{\infty}\left( (1 - \alpha\ x)^{k}k\alpha x^{2} \right) = \sum_{k = 2}^{\infty}\left( (1 - \alpha\ x)^{k - 1}(k - 1)\alpha x^{2} \right)$$

和$\ S\ $本体一比较，

$$\alpha x\ S = \sum_{k = 2}^{\infty}\left( (1 - \alpha\ x)^{k - 1}\alpha x^{2} \right) + \alpha x^{2} = \frac{(1 - \alpha x)\alpha x^{2}}{1 - (1 - \alpha x)} + \alpha x^{2} = x$$

胜利就在眼前了！只要求出$S(x),求最值就容易了！！但是，似乎哪儿有点不对\ldots\ldots$

$$S = \frac{x}{\alpha x} = \frac{1}{\alpha} = Const$$

小明：？？？？

$$S:就算我被你化简了，求出了具体的表达式，我还是要对你发出诡异的\ldots\ldots$$

S的话还没说完就被小明拍在了桌子上。他打算研究更一般的情况，并且猜想如果S对所有x的取值都是这个结果，那也一定很有意思。
