---
title: '满群同态证明技巧'
date: 2019-08-16
url: /posts/2019/08/manquntongtai/
tags:
  - Blogpost
  - Mathematic
  - Linear Algebra
  - 1-5 Pages
types:
  - blogpost
topics:
  - mathematics
  - linear-algebra
lengths:
  - 1-5-pages
authors:
  - me
---

一道题，证明自然同态 Z → Zp 诱导的群同态 SLn(Z) → SLn(Zp) 是满同态，其中 p 是素数。

自然同态$\mathbb{Z}\rightarrow \mathbb{Z}_p$诱导的群同态$\mathrm{SL}_n(\mathbb{Z})\rightarrow \mathrm{SL}_n(\mathbb{Z}_p)$是满同态，其中$p$是素数。

# 直接定义证明满射

同态是易证的，这里的关键是要证明$\phi:\mathrm{SL}_n(\mathbb{Z})\rightarrow \mathrm{SL}_n(\mathbb{Z}_p)$是满射。

容易想到的一种方法是：对每个$\mathrm{SL}_n(\mathbb{Z}_p)$中的矩阵，都有$\mathrm{SL}_n(\mathbb{Z})$中的一个矩阵与之对应。

也就是，对于$\mathrm{SL}_n(\mathbb{Z}_p)$中的矩阵$A_p=(\overline{a_{ij}})$(其中$0\le a_{ij}<p$)，要找一个系数矩阵$N=(n_{ij})(n_{ij}\in \mathbb{Z})$，得到对应矩阵$A=(a_{ij})+p\cdot N$ 利用已知的$\det (\overline{a_{ij}})=\overline{1}$的条件(即$\det (a_{ij})=x\cdot p+1$($x$为某确定整数但并不知道))使得$\det A=1$。

举个二维情况的例子： 对$\mathrm{SL}_2(\mathbb{Z}_p)$中的某矩阵$\left( \begin {matrix}\overline{a}&\overline{b}\\ \overline{c}&\overline{d} \end{matrix} \right)$ 已知$\overline{a}\overline{d}-\overline{b}\overline{c}=\overline{1}$，即$ad-bc\equiv1(\mathrm{mod}\; p)$ 要找四个整数$n_1，n_2，n_3，n_4$让 $\det \left(\begin{matrix}a+n_1p&b+n_2p\\c+n_3p&d+n_4p\end{matrix}\right)=1$。这显然是十分头大的。

# 利用生成元和同态性质间接证明满射

所以有另一种想法。我们只要证明群$\mathrm{SL}_n(\mathbb{Z}_p)$有生成元，并且这些生成元有对应的矩阵即可。这样我们就不用考虑全部元素。只需考虑几个生成元是否有对应的矩阵，其他$\mathrm{SL}_n(\mathbb{Z}_p)$中的矩阵都可以根据群同态的性质推出存在对应的矩阵。什么样的生成元呢？很容易想到可爱的初等矩阵。并且，我们发现

1.  $\mathrm{SL}_n(\mathbb{Z}_p)$中单位矩阵 $\left(\begin{matrix}\overline{1}\\ &\overline{1}\\  &&\ddots\\ &&&\overline{1}\end{matrix}\right)$ 对应的矩阵$\left(\begin{matrix} 1\\ &1\\  &&\ddots\\ &&&1 \end{matrix}\right)$

    在$\mathrm{SL}_n(\mathbb{Z})$中；

2.  $\mathrm{SL}_n(\mathbb{Z}_p)$中倍加矩阵\
    $\left(\begin{matrix}
    \overline{1}\\ &\ddots \\&&\overline{\color{red}{1}}&\dots&\overline{a}\\&&&\ddots&\vdots\\&&&&\overline{\color{red}{1}}\\&&&&&\ddots\\&&&&&&\overline{1}
    \end{matrix}\right)$ 对应的矩阵$\left(\begin{matrix}
    1\\ &\ddots \\&&1&\dots&a\\&&&\ddots&\vdots\\&&&&1\\&&&&&\ddots\\&&&&&&1
    \end{matrix}\right)$ 在$\mathrm{SL}_n(\mathbb{Z})$中；

3.  $\mathrm{SL}_n(\mathbb{Z}_p)$中交换矩阵(稍有些不同，为了使行列式值为1必须加个负号)\
    $\left(\begin{matrix}
    \overline{1}\\&\ddots\\&&\overline{0}&\dots&\overline{1}\\&&\vdots&\ddots&\vdots\\&&\overline{-1}&\dots&\overline{0}\\&&&&&\ddots\\&&&&&&\overline{1}
    \end{matrix}\right)$对应的矩阵 $\left(\begin{matrix}
    1\\&\ddots\\&&0&\dots&1\\&&\vdots&\ddots&\vdots\\&&-1&\dots&0\\&&&&&\ddots\\&&&&&&1
    \end{matrix}\right)$\
    也在$\mathrm{SL}_n(\mathbb{Z})$中

OK，then，对于$\mathrm{SL}_n(\mathbb{Z}_p)$中任意矩阵$(\overline{a_{ij}})$， 因为它行列式等于1所以可逆，从而可以被分解而写成$\mathrm{SL}_n(\mathbb{Z}_p)$中单位矩阵和像上面这样的初等矩阵的乘积。

注意，少了一个提出倍数的初等矩阵也没有关系，可以通过倍加解决。考虑如下情况：

如果$(\overline{a_{ij}})$最后化到了$\left(\begin{matrix}
\overline{x_{11}}\\&\overline{x_{22}}\\&&\ddots\\&&&\overline{x_{nn}}
\end{matrix}\right)$的形式，考虑左上$2\times 2$矩阵$\left(\begin{matrix}
\overline{x_{11}}&\overline{0}\\
\overline{0}&\overline{x_{22}}
\end{matrix}\right)$， 注意到$\mathbb{Z}_p$中每个元素均有逆，将第二行的$(x_{22})^{-1}$倍加到第一行，得到$\left(\begin{matrix}
\overline{x_{11}}&\overline{1}\\
\overline{0}&\overline{x_{22}}
\end{matrix}\right)$； 把第二列的$1-\overline{x_{11}}$倍加到第一列，得到$\left(\begin{matrix}
\overline{1}&\overline{1}\\
(\overline{1}-\overline{x_{11}})\overline{x_{22}}&\overline{x_{22}}
\end{matrix}\right)$。 用左上角的$1$消去副对角线，得到$\left(\begin{matrix}
\overline{1}&\overline{1}\\
\overline{0}&\overline{x_{11}} \ \overline{x_{22}}
\end{matrix}\right)$ 重复操作，可把$\left(\begin{matrix}
\overline{x_{11}}\\&\overline{x_{22}}\\&&\ddots\\&&&\overline{x_{nn}}
\end{matrix}\right)$变为$\left(\begin{matrix}
1\\&1\\&&\ddots\\&&&\overline{x_{11}}\ \overline{x_{22}}\ \dots\overline{x_{nn}}
\end{matrix}\right)$ 注意到由条件得到连乘积为$\overline{1}$，则它就是单位矩阵。

# 结论

我们证明了群$\mathrm{SL}_n(\mathbb{Z}_p)$有生成元，也说明了生成元都有原像。那么既然$\mathrm{SL}_n(\mathbb{Z}_p)$中每个矩阵都能通过生成元运算得到，每个矩阵也都就利用同态，通过生成元的原像得到。于是就成功证明了满射。

# 后记 {#后记 .unnumbered}

整理自大胡子的习题课

感谢zx的人工ocr
