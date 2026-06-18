---
title: 'nabla 算子运算规则的作用对象修正'
date: 2019-03-25
url: /posts/2019/03/nabla/
tags:
  - Blogpost
  - Mathematic
  - Vector calculus
  - 6-10 Pages
types:
  - blogpost
topics:
  - mathematics
  - vector-calculus
lengths:
  - 6-10-pages
authors:
  - me
---

在套用向量运算规则对nabla算子进行计算时，需要注意哪些问题？
## 小结

### 什么时候 nabla 算符不能简单套用向量运算规则？
对于一个完整的表达式（v · ∇ 等不算，它们只能作为一个算符），如果牵扯到了两个及以上的向量（相同的也算），并且使用了一些矢量运算公式，使得 nabla 算符 从括号内移至括号外（不指明作用对象的话，受到 nabla 算符作用的向量数量可能增加。从括号外移至括号内，则此时简单套用向量运算规则会导致作用对象发生转移，因此不能简单套用。

### 如何做？
只需要记住 nabla 算符有作用对象即可。可以通过加费曼脚标以标明，然后可依照向量运算规则。对于表达式中有向量相同的情况，先用不同符号代替区分，最
再将它们都代回原来的符号。当然，也可以直接采用张量和爱因斯坦求和约定，直接按照运算顺序一步步来，但也需要注意作用对象。

\vspace{1em}

# 背景和动机：不能总作为向量的算符

众所周知，nabla算子$\nabla$的运算规则，可以把它当做向量，套用向量的运算规则，即令 $$\nabla=\brack{\pp{}{x},\pp{}{y},\pp{}{z}}=\pp{}{x}\bm{i}+\pp{}{y}\bm{j}+\pp{}{z}\bm{k}$$ 对于标量场$\phi$的梯度，向量场$\bm{A}$的散度、旋度，甚至旋度的散度一些复合，用向量的运算规则都能 fit very well. 例如： $$\div \curl \bm{A}=\nabla\cdot(\nabla\times A)=
  \nabla \cdot
  \begin{vmatrix}
    \bm{i}&\bm{j}&\bm{k} \\
    \pp{}{x}&\pp{}{y}&\pp{}{z} \\
    A_x&A_y&A_z
  \end{vmatrix}
  =\begin{vmatrix}
    \pp{}{x}&\pp{}{y}&\pp{}{z} \\
    \pp{}{x}&\pp{}{y}&\pp{}{z} \\
    A_x&A_y&A_z
  \end{vmatrix}
  =0$$

但是，在一些情况下，简单套用矢量运算法会产生一些问题。本篇文章的目的即为解决以下两个问题

1.  什么时候nabla算符不能套用矢量运算法？

2.  当不能套用矢量运算法的时候，我们该如何做？

# 关键点A：无简单交换律 {#sec:pointa}

先提一个简单的。

众所周知，向量点积是可交换的，即$\bm{a}\cdot \bm{b}=\bm{b}\cdot \bm{a}$。 但是，nabla算符的点积是不可交换的，其表达的意义不同。例如： $$\nabla\cdot \bm{v}=\pp{v_x}{x}+\pp{v_y}{y}+\pp{v_z}{z}$$ 而 $$\bm{v}\cdot\nabla=v_x\pp{}{x}+v_y\pp{}{y}+v_z\pp{}{z}$$ 这并不是一个确切的数值，而仍然是一个算符。考虑其对$\bm{u}$进行作用，取其结果的$x$分量为例 $$\brack{(\bm{v}\cdot\nabla)\bm{u}}_x=v_x\pp{u_x}{x}+v_y\pp{u_x}{y}+v_z\pp{u_x}{z}$$ 作为对比，有 $$\brack{(\nabla \cdot \bm{v})\bm{u}}_x=u_x\pp{v_x}{x}+u_x\pp{v_y}{y}+u_x\pp{v_z}{z}$$

同理，梯度也是不可交换的，即$\nabla \phi$和$\phi \nabla$不同，但是遇到的不多，迷惑性也不如点积的大。 旋度即使用向量反交换律法则也不成立，即$\nabla \times \bm{v}$和$-\bm{v}\times\nabla$不同。 从性质上来说，nabla置于前的式子，都是一个[具体的向量或数]{.underline}，而nabla置于后的式子，都还只是一个[算符]{.underline}， 不能将nabla之前的向量或标量**直接放入偏导数内**。

在解决问题B之后，可以很直观地理解这里的关键原因，并重建良好的交换律。见`\nameref{sec:reasona}`{=latex}

# 问题B引入：隐藏的错误

下面这个表达式是正确的。 $$(\nabla \times \bm{v})\times \bm{v}=-\frac{1}{2}\nabla(\bm{v}^2)+(\bm{v}\cdot\nabla)\bm{v}$$

请试着用公式 $$\label{eq:backcab}
  \bm{a}\times(\bm{b}\times \bm{c})=\bm{b}(\bm{a}\cdot \bm{c})-\bm{c}(\bm{a}\cdot \bm{b})$$ 对左端展开以验证。

你将很有可能得到： $$\begin{aligned}
  (\nabla \times \bm{v})\times \bm{v}&=-\bm{v}\times(\nabla \times \bm{v})
  \\
                                     &=-\nabla(\bm{v}\cdot \bm{v})+\bm{v}(\bm{v}\cdot\nabla)&\\
  &=-\nabla(\bm{v}^2)+(\bm{v}\cdot\nabla)\bm{v}
\end{aligned}$$

你可能会经历以下心路历程。

1.  发现得到的结果，和前面所谓正确的公式差了一半。

2.  于是你开始检查你的推导过程。

3.  很有可能你在很多地方见过`\autoref{eq:backcab}`{=latex}[^1]，因此不会怀疑它的正确性。

4.  在对照了十几遍之后，仍然找不出推导过程半点不对劲的地方。

5.  你开始对我给你所谓的正确方程产生严重的怀疑。

请相信我。我给你的方程是完全正确的，而你的推导过程确实存在问题。这确实非常隐蔽，可能看个几十遍都看不出来。 于是你打算直接拿行列式进行一通爆算来找问题到底出在哪儿。但是为了极大地节约你的时间，我还是直接告诉你结论。

# 关键点B：作用对象

\begin{centering}
\huge\textbf{nabla算符有固定作用对象}

\textbf{nabla算符有固定作用对象}

\textbf{nabla算符有固定作用对象}

\end{centering}
\vspace{1em}

`\normalsize `{=latex}意思是，在$\nabla\times \bm{v} \times \bm{v}$中，nabla算符只对一个向量$\bm{v}$ 产生作用。而在$\nabla (\bm{v}\cdot \bm{v})$中，nabla算符相当于对两个向量都进行了一次作用。因此，要注意区分。

# 解决办法B：费曼脚标和默认约定

引入"费曼脚标算符"[^2]，以**指示nabla算符的作用对象**。例如 $$\nabla(\bm{a}\cdot \bm{b})=\nabla_a(\bm{a}\cdot \bm{b})+\nabla_b(\bm{a}\cdot \bm{b})$$ 等号左边的nabla算符表示对两个向量都进行作用，右边的第一项表示只对$\bm{a}$向量作用，把$\bm{b}$视为常数（常向量）。 第二项则相反。其原理类似于乘法求导法则。 $$\pp{}{x}(ab)=b\pp{a}{x}+a\pp{b}{x}$$

然后我们再来进行运算。在最开始的式子中，nabla后接哪个向量，下标就标上哪个向量。即**默认约定：**nabla算符作用对象就是其后的向量或标量。为了清晰起见，先用 $\bm{v}_1=\bm{v}_2=\bm{v}$区分。(其实不区分也行，只需要牢记有下标时只对其中一个$\bm{v}$进行运算即可。) $$\begin{aligned}
  (\nabla\times \bm{v}_1) \times \bm{v}_2&=-\bm{v}_2\times(\nabla_1\times \bm{v}_1)\\
                             &=-\nabla_1(\bm{v}_2\cdot \bm{v}_1)+\bm{v}_1(\bm{v}_2\cdot \nabla_1)\\
  (\because \bm{v}_1=\bm{v}_2)\quad  &=-\frac{1}{2}\brack{\nabla_1(\bm{v}_2\cdot \bm{v}_1)+\nabla_2(\bm{v}_2\cdot \bm{v}_1)}+\bm{v}_1(\bm{v}_2\cdot\nabla_1)\\
&=-\frac{1}{2}\nabla(\bm{v}_1\cdot \bm{v}_2)+(\bm{v}_2\cdot\nabla_1)\bm{v}_1\\
  &=-\frac{1}{2}\nabla(\bm{v}^2)+(\bm{v}\cdot \nabla)\bm{v}
\end{aligned}$$

可以看到，这次的式子是正确的。其中最后一步第二项的处理，注意到$\bm{v}_2\cdot\nabla_1$去掉脚标后（只要不瞎用交换律，见`\nameref{sec:pointa}`{=latex}）也不会产生"算符作用到前面一个向量上"的歧义即可。

# 原理解释A：重建交换律 {#sec:reasona}

现在可以解释`\nameref{sec:pointa}`{=latex}中内在的原因。根据**默认约定**：nabla算符作用的对象就是其后跟着的向量或标量，即 $$\nabla\phi=\nabla_{\phi}\phi \qquad \nabla\cdot \bm{v}=\nabla_{\bm{v}}\cdot \bm{v} \qquad \nabla \times \bm{v}=\nabla_{\bm{v}}\times \bm{v}$$

但是将nabla算符后置时，其后的作用对象可能暂时还未给出。例如 $$\bm{v}\cdot\nabla=\bm{v}\cdot\nabla_{?}$$

因此，考虑任意向量$\bm{u}$，我们有 $$(\nabla\cdot \bm{v})\bm{u}=(\nabla_{\bm{v}}\cdot \bm{v})\bm{u} \qquad (\bm{v}\cdot\nabla)\bm{u}=(\bm{v}\cdot \nabla_{\bm{u}})\bm{u}$$

在用下标指定作用对象后，利用向量的运算规则（梯度、散度交换律，旋度反交换律）理论上是被[允许]{.underline}的，因为它们表达的意义很明确， 即作用对象之外的向量或标量都被**明确禁止进入偏导数内**。 $$\nabla_{\bm{v}}\cdot \bm{v}=\bm{v}\cdot\nabla_{\bm{v}} \qquad \nabla_{\bm{u}}\cdot \bm{v}=\bm{v}\cdot\nabla_{\bm{u}}$$

显然，对$\bm{u}\neq \bm{v}$，由于$\nabla_{\bm{v}}\neq \nabla_{\bm{u}}$，可知$\nabla_{\bm{v}}\cdot \bm{v} \neq \nabla_{\bm{u}}\cdot \bm{v}$ $(\bm{v}\neq \bm{0})$，于是显然有$\nabla_{\bm{v}}\cdot \bm{v} \neq \bm{v}\cdot\nabla_{\bm{u}}$。 这就是为什么一般默认记法$\nabla\cdot \bm{v}\neq \bm{v}\cdot\nabla$。

特殊的情况，考虑"左右旋度"，虽然nabla算符置于不同的位置，但是可以理解成已经显式指明作用的对象（就是你要求旋度的那个矢量，偏导数都是对它求），就可以套用反交换律了。 $$\nabla_{\bm{v}}\times \bm{v}=-\bm{v}\times\nabla_{\bm{v}}$$

# 注意点：向量规则和默认约定

在上面的运算过程中，考虑$(\bm{v}_2\cdot\nabla_1)\bm{v}_1$一项。既然$\nabla_1$对$\bm{v}_2$是完全不理睬的，那么**似乎**能把$\bm{v}_2$独立出来，然后nabla算符和后面的$\bm{v}_1$粘上，即 $$(\bm{v}_2\cdot\nabla_1)\bm{v}_1=\bm{v}_2(\nabla_1 \cdot \bm{v}_1)=(\nabla \cdot \bm{v})\bm{v}$$ 而正确的项为$(\bm{v}\cdot\nabla)\bm{v}$。如果不注意区分，会误解为是因为交换律而引起的问题，但事实上就算强行交换，意义也不对。

进行区分，正确的答案为$(\bm{v}_2\cdot\nabla_1)\bm{v}_1$，上面最后一项为$(\nabla_1\cdot \bm{v}_1)\bm{v}_2$。注意默认约定， $$(\nabla_1 \cdot \bm{v}_1)\bm{v}_2=(\bm{v}_1 \cdot \nabla_1)\bm{v}_2\neq (\bm{v}_1 \cdot \nabla)\bm{v}_2=(\bm{v}_1 \cdot \nabla_2)\bm{v}_2$$ 在$\bm{v}_1=\bm{v}_2$的条件下，上式最右端轮换指标可以化为正确答案。两端根本的不同之处在于$\nabla$的作用对象，[一个是在括号外，一个是在括号内]{.underline}。这使得即使$\bm{v}_1=\bm{v}_2=\bm{v}$也无济于事。

根源是第一步就出了错。其实，写成普通向量形式是好理解的，即一般 $$\bm{a}(\bm{b}\cdot \bm{c})\neq(\bm{a}\cdot \bm{b}) \bm{c}$$ 即使指明了作用对象，nabla的运算相对"自由"了一些，但仍然不能为所欲为，由于指出了nabla算符和向量的不同之处，就发明不符合向量基本运算规则的nabla运算规则，强行去粘作用对象。脚标和作用对象的引入，目标是**使得将nabla算符能够适用向量运算的规则，而不是让nabla算符超越现有的规则。**

# 一劳永逸的解决方案：张量与求和约定

以后不学张量的非数学物理力学系同学其实大概可以跳过此段。

## 爱因斯坦求和约定

首先引入爱因斯坦求和约定：凡是成对出现的指标，都认为是要从$1$到$3$进行求和。于是向量可以表为 $$\bm{a}=a_1\bm{e}_1+a_2\bm{e}_2+a_3\bm{e}_3=\sum_{i=1}^3a_i\bm{e}_i=a_i\bm{e}_i$$

## 两个符号

再引入kronecker和levi-civita符号 $$\delta_{ij}=
  \left\{
    \begin{aligned}
      &1&i=j\\
      &0&i\neq j
    \end{aligned}
  \right.\qquad
  \varepsilon_{ijk}=
  \left\{
    \begin{aligned}
      &1&ijk=123,231,312\\
      &-1&ijk=132,213,321\\
      &0&other\\
    \end{aligned}
  \right.$$ 它们分别具有以下性质 $$f(i,j)\delta_{i,j}=f(i,i)$$ 证明： $$\begin{aligned}
  left=\sum_{i=1}^3\sum_{j=1}^3f(i,j)\delta_{i,j}&=\sum_{\substack{i,j=1\\ i=j}}^3f(i,j)\delta_{i,j}+\sum_{\substack{i,j=1\\ i\neq j}}^3f(i,j)\delta_{i,j}
  \\ (\mathrm{use~definition})\quad&=\sum_{\substack{i,j=1\\ i=j}}^3f(i,j)=\sum_{i=1}^3f(i,i)=right
\end{aligned}$$ 以及 $$\varepsilon_{ijk}=\varepsilon_{kij}=\varepsilon_{jki}=-\varepsilon_{ikj}=-\varepsilon_{kji}=-\varepsilon_{jik}$$ 证明：只需要理解$\varepsilon_{ijk}$只返回$ijk$的排列性质（偶排列为1，奇排列为-1）即可，因此交换奇数次下标会改变符号，交换偶数次下标不改变符号。

## 基矢运算

定义基矢的点乘和叉乘分别为 $$\bm{e}_i\cdot \bm{e}_j=\delta_{ij}\qquad \bm{e}_i\times \bm{e}_j=\varepsilon_{ijk}\bm{e}_k$$ 于是我们就有了向量的点乘和叉乘 $$\bm{a}\cdot \bm{b}=(a_i\bm{e}_i)\cdot(b_j\bm{e}_j)=a_ib_j(\bm{e}_i\cdot \bm{e}_j)=a_ib_j\delta_{ij}=a_ib_i$$ $$\bm{a}\times \bm{b}=(a_i\bm{e}_i)\times(b_j\bm{e}_j)=a_ib_j(\bm{e}_i\times \bm{e}_j)=a_ib_j\varepsilon_{ijk}\bm{e}_k$$ 其中叉乘的$\bm{e}_1$方向分量为$a_ib_j\varepsilon_{ij1}=a_2b_3-a_3b_2$，和行列式传统定义计算结果相同。

另外还有基矢的并矢计算，得到的是一个只在i行j列为1的矩阵。 $$A_{ij}\bm{e}_i\otimes \bm{e}_j=\sum_{i=1}^3\sum_{j=1}^3A_{ij}\bm{e}_i\otimes \bm{e}_j=\bm{A}$$ 其他高级的张量计算等在此不作介绍。

## nabla算子及运算

现在，只要把$x,y,z$三个方向记为$x_1,x_2,x_3$三个方向，令nabla算子为 $$\nabla=\pp{}{x_i}\bm{e}_i$$ 即可像正常向量一样参与运算。例如 $$\nabla\cdot \bm{v}=\pp{}{x_i}\bm{e}_i\cdot v_j\bm{e}_j=\pp{v_i}{x_i}\qquad
  \nabla\times \bm{v}=\pp{}{x_i}\bm{e}_i\times v_j\bm{e}_j=\pp{v_j}{x_i}\varepsilon_{ijk}\bm{e}_k$$

此时也需要注意作用对象。作用对象和非作用对象的区别，在此很明显地体现为在偏导数中是视为常数直接提出，还是需要参与偏导运算。 $$\bm{v}\times\nabla=v_i\bm{e}_i\times \pp{}{x_j}\bm{e}_j=\varepsilon_{ijk}v_i\pp{}{x_j}\bm{e}_k$$ $$\nabla(\bm{a}\cdot \bm{b})=\pp{(a_jb_j)}{x_i}\bm{e}_i=\brack{a_j\pp{b_j}{x_i}+b_j\pp{a_j}{x_i}}\bm{e}_i$$ $$\nabla_a(\bm{a}\cdot \bm{b})=\pp{_a(a_jb_j)}{x_i}\bm{e}_i=b_j\pp{a_j}{x_i}\bm{e}_i$$ 可见，写在nabla算符之前的向量，其写成这种形式时也位于偏导左边，因此一般粘在偏导左边作为系数。而写在算符之后的向量， 位于偏导右边，而粘在偏导右边的量一般就被认为是需要进行偏导运算。这也许就是默认约定的来源。

## 对前面问题的解释

现在再计算前面产生问题的式子，就不会产生问题。 $$\begin{aligned}
  (\nabla\times \bm{v})\times \bm{v}&=\brack{\pp{}{x_i}\bm{e}_i\times v_j\bm{e}_j}\times \bm{v}\\
                                    &=\pp{v_j}{x_i}\varepsilon_{ijk}\bm{e}_k\times v_l\bm{e}_l\\
                                    &=v_l\pp{v_j}{x_i}\varepsilon_{ijk}\varepsilon_{klm}\bm{e}_m\\
                                    &=v_l\pp{v_j}{x_i}\varepsilon_{ijk}\varepsilon_{lmk}\bm{e}_m
\end{aligned}$$ 然后我们来考察一下两个Levi-civita符号的乘积。注意到它们下标$ijk$和$lmk$中，在相同的位置出现了$k$。 那么，要使得它们都不为零，$i,j$和$l,m$都分别只能在除$k$外的两个数中选。于是，要么$i=l,j=m$，要么$i=m,j=l$。 $$f(i,j,k,l,m)\varepsilon_{ijk}\varepsilon_{lmk}=f(i,j,k,i,j)\varepsilon_{ijk}\varepsilon_{ijk}+f(i,j,k,j,i)\varepsilon_{ijk}\varepsilon_{jik}$$ 交换最后一个符号的$ij$下标，由于$\varepsilon_{jik}=-\varepsilon_{ijk}$，增加一个负号。 $$f(i,j,k,l,m)\varepsilon_{ijk}\varepsilon_{lmk}=(f(i,j,k,i,j)-f(i,j,k,j,i))\varepsilon_{ijk}^2$$ 由于出现了平方，$\varepsilon_{ijk}^2$在三个下标都互不相等的情况下总为$1$，即有 $$\varepsilon_{ijk}^2=(1-\delta_{ij})(1-\delta_{jk})(1-\delta_{ki})$$ 考虑$\delta_{ij}$项， $$(f(i,j,k,i,j)-f(i,j,k,j,i))\delta_{ij}=f(i,i,k,i,i)-f(i,i,k,i,i)=0$$ 于是这一项可以去掉。 $$f(i,j,k,l,m)\varepsilon_{ijk}\varepsilon_{lmk}=(f(i,j,k,i,j)-f(i,j,k,j,i))(1-\delta_{jk})(1-\delta_{ki})$$ 要使得表达式不为零，必须要$i,j\neq k$。之前已经证明$i=j$的情况会得到无用的零，因此此处可以认为$i\neq j$。如果前面的函数不含$k$，即可以用四元函数$g$表示$f$，$f(i,j,k,l,m)=g(i,j,l,m)$，那么每次求和，$k$就可以不受影响地选且只能选$i,j$之外的那一个值，使得表达式不为零。也就是 $$g(i,j,l,m)\varepsilon_{ijk}\varepsilon_{lmk}=g(i,j,i,j)-g(i,j,j,i)$$ 回到最开始的计算，我们有 $$(\nabla\times \bm{v})\times \bm{v}=v_l\pp{v_j}{x_i}\varepsilon_{ijk}\varepsilon_{lmk}\bm{e}_m$$ 此处两个$k$位置对齐，且没有在别的地方出现，因此有 $$\begin{aligned}
  (\nabla\times \bm{v})\times \bm{v}&=v_i\pp{v_j}{x_i}\bm{e}_j-v_j\pp{v_j}{x_i}\bm{e}_i\\
                                    &=v_i\pp{}{x_i}v_je_j-\frac{1}{2}\pp{}{x_i}e_i(v_j\cdot v_j)\\
  &=(\bm{v}\cdot\nabla)\bm{v}-\frac{1}{2}\nabla \bm{v}^2
\end{aligned}$$

按照爱因斯坦求和约定进行推算，一路都很顺利，没有遇到什么坎（两个$\varepsilon$乘积那个理解了就很容易）。

# 总结：when&how

回到开头提出的两个问题。

#### 什么时候nabla算符不能简单套用向量运算规则？

对于一个**完整的表达式**（$\bm{v}\cdot\nabla$等不算，它们只能作为一个算符）， 如果牵扯到了**两个及以上**的向量（相同的也算），并且使用了一些矢量运算公式，使得nabla算符 **从括号内移至括号外**（不指明作用对象的话，受到nabla算符作用的向量数量可能增加，如

$$\bm{a}\cdot(\nabla\times \bm{b})= \nabla_b\cdot(\bm{b}\times \bm{a})\neq \nabla\cdot(\bm{b}\times \bm{a})$$

从括号外移至括号内，则此时简单套用向量运算规则会导致**作用对象发生转移**，因此不能简单套用。

显然，如果式子中只有一个向量的话，无论怎么变，作用对象都是明确的。有多个向量，甚至是相同向量时，具有较大迷惑性， 需要小心。

#### 应该怎么办？

只需要记住nabla算符有**作用对象**即可。可以通过加费曼脚标以标明，然后可依照向量运算规则。 对于表达式中有向量相同的情况，先用不同符号代替区分，最后再将它们都代回原来的符号。

当然，也可以直接采用张量和爱因斯坦求和约定，直接按照运算顺序一步步来，但也需要 注意作用对象。

[^1]: 此式由于其类似"bac(k)-cab"而得名"后面的出租车"，是使用非常频繁的三重矢积公式。

[^2]: 可在《费曼物理学讲义》第二卷§27-3中找到
