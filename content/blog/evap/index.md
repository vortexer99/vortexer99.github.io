---
title: '三维矩阵不变量与平行六面体体积'
date: 2019-05-02
url: /posts/2019/05/evap/
tags:
  - Blogpost
  - Mathematic
  - Linear Algebra
  - 6-10 Pages
types:
  - blogpost
topics:
  - mathematics
  - linear-algebra
lengths:
  - 6-10-pages
authors:
  - me
---

矩阵不变量为何可以通过矩阵对任意不共面矢量uvw的运算推出？特征值与特征分解。

## 混合积和体积

对于三维空间中三个不共面的向量$\bm{u},\bm{v},\bm{w}$而言，其混合积$\bm{u}\cdot(\bm{v}\times \bm{w})$ 表示三个向量（经过平移使其共起点）张成的平行六面体体积。将其简记为$\left[
    \bm{u}~\bm{v}~\bm{w}
  \right]$ ，其计算方法可用行列式表示。 $$\label{eq:triprod}

  \left[
    \bm{u}~\bm{v}~\bm{w}
  \right]=
  \begin{vmatrix}
    u_x&u_y&u_z\\
    v_x&v_y&v_z\\
    w_x&w_y&w_z
  \end{vmatrix}$$

## 矩阵的不变量

对于三维矩阵$\bm{A}$而言，其三个不变量为 $$\begin{aligned}
  I_1(\bm{A})&=\tr\bm{A}\\
  I_2(\bm{A})&=\frac{1}{2}(\tr^2\bm{A}-\tr\bm{A}^2)\\
  I_3(\bm{A})&=\det{\bm{A}}=\frac{1}{6}(\tr^3\bm{A}-3(\tr\bm{A})(\tr \bm{A}^2)+2\tr \bm{A}^3)
\end{aligned}$$

## 问题

矩阵的不变量可以如下计算。对于任意不共面矢量$\bm{u},\bm{v},\bm{w}$，有 $$\begin{aligned}
  I_1(\bm{A})&=\frac{
  \left[
    \bm{Au}~\bm{v}~\bm{w}
  \right]+
  \left[
    \bm{u}~\bm{Av}~\bm{w}
  \right]+
  \left[
    \bm{u}~\bm{v}~\bm{Aw}
  \right]}{
  \left[
    \bm{u}~\bm{v}~\bm{w}
  \right]}\\
  I_2(\bm{A})&=\frac{
  \left[
    \bm{Au}~\bm{Av}~\bm{w}
  \right]+
  \left[
    \bm{Au}~\bm{v}~\bm{Aw}
  \right]+
  \left[
    \bm{u}~\bm{Av}~\bm{Aw}
  \right]}{
  \left[
    \bm{u}~\bm{v}~\bm{w}
  \right]}\\
  I_3(\bm{A})&=\frac{
  \left[
    \bm{Au}~\bm{Av}~\bm{Aw}
  \right]}{
  \left[
    \bm{u}~\bm{v}~\bm{w}
  \right]}
\end{aligned}$$ 为什么？

# 证明

其实矩阵的不变量就是特征值的对称多项式。而如果$\bm{u},\bm{v},\bm{w}$刚好是$\bm{A}$的特征向量，结论是显然的。 因此，对一般向量，可用特征向量分解，得到类似的结论。

## 不变量的来龙去脉

依照求特征值的方法，三维矩阵$\bm{A}$的三个特征值$\lambda_1,\lambda_2,\lambda_3$能使得 $$\abs{\bm{A}-\lambda \bm{E}}=0$$ 成立。其中$\bm{E}$为单位矩阵。而上式左端可以看作以$\lambda$为变量的三次多项式。事实上，正有 $$\label{eq:1}
  \abs{\bm{A}-\lambda \bm{E}}=-\lambda^3+I_1(\bm{A})\lambda^2-I_2(\bm{A})\lambda+I_3(\bm{A})=0$$ 证明略，根据对应的$\lambda$次数，算一下余子式即可。于是，根据韦达定理可知 $$\begin{aligned}
  \label{eq:2}
  I_1(\bm{A})&=\lambda_1+\lambda_2+\lambda_3\\
  I_2(\bm{A})&=\lambda_1\lambda_2+\lambda_1\lambda_3+\lambda_2\lambda_3\\
  I_3(\bm{A})&=\lambda_1\lambda_2\lambda_3
\end{aligned}$$

## 特征分解

取矩阵的三个特征向量$\bm{e}_1,\bm{e}_2,\bm{e}_3$，对$\bm{u},\bm{v},\bm{w}$进行特征分解。利用求和约定（**省去$1$至$3$的求和号**） （且上标不表示次数） $$\bm{u}=u^i\bm{e}_i\qquad \bm{v}=v^i\bm{e}_i \qquad \bm{w}=w^i\bm{e}_i$$ 于是 $$\left[
    \bm{u}~\bm{v}~\bm{w}
  \right]=u^iv^jw^k\bm{e}_i\cdot(\bm{e_j}\times \bm{e}_k)=u^iv^jw^k
  \left[
    \bm{e}_i~\bm{e}_j~\bm{e}_k
  \right]=u^iv^jw^kV(i,j,k)$$ 其中$V(i,j,k)=
  \left[
    \bm{e}_i~\bm{e}_j~\bm{e}_k
  \right]$。显然，由混合积的性质，只要$i,j,k$中有任意两个相等，$V(i,j,k)$就等于$0$。

然后看第一项。根据特征向量的性质 $$\bm{A} \bm{e}_i=\lambda_i \bm{e}_i \qquad i=1,2,3$$ 有 $$\bm{A}\bm{u}=\bm{A}u^i\bm{e}_i=\lambda_iu^i\bm{e}_i$$ 于是 $$\left[
    \bm{A}\bm{u}~\bm{v}~\bm{w}
  \right]=\lambda_iu^iv^jw^kV(i,j,k)$$ 那么，类似的有 $$\left[
    \bm{Au}~\bm{v}~\bm{w}
  \right]+
  \left[
    \bm{u}~\bm{Av}~\bm{w}
  \right]+
  \left[
    \bm{u}~\bm{v}~\bm{Aw}
  \right]=(\lambda_i+\lambda_j+\lambda_k)u^iv^jw^kV(i,j,k)$$ 根据前面的讨论，求和时$i,j,k$有任意两个相等时，求和项因为$V(i,j,k)=0$而为零。因此有贡献的项是$i,j,k$互不相等时的项。 而$i,j,k$互不相等时，显然$\lambda_i+\lambda_j+\lambda_k=I_1(\bm{A})$，于是 $$\begin{aligned}

  \left[
    \bm{Au}~\bm{v}~\bm{w}
  \right]+
  \left[
    \bm{u}~\bm{Av}~\bm{w}
  \right]+
  \left[
    \bm{u}~\bm{v}~\bm{Aw}
  \right]&=I_1(\bm{A})u^iv^jw^kV(i,j,k)\\
  &=I_1(\bm{A})
  \left[
    \bm{u}~\bm{v}~\bm{w}
  \right]
\end{aligned}$$ 这就证得了第一式。对于第二、第三式，做法是类似的。考虑第二式中某项， $$\left[
    \bm{Au}~\bm{Av}~\bm{w}
  \right]=\lambda_i\lambda_ju^iv^jw^kV(i,j,k)$$ 最后得到的系数是$\lambda_i\lambda_j+\lambda_i\lambda_k+\lambda_j\lambda_k$，当$i,j,k$互不相等时显然就是$I_2(\bm{A})$。

# 细枝末节的东西

## 如果矩阵不满秩

如果矩阵$\bm{A}$不满秩会怎么样？这也就是说对应的线性映射$\mathcal{A}$像空间不是全空间$V$， 即核空间维数不为零，会将一些非零向量映射为零向量。

此时像空间中的$r$个向量及其特征值没有影响。对于核空间，取$3-r$个基向量，作为特征向量，并令其对应特征值为零即可。

这样既保证了任何向量都能被特征向量分解，又使得$\bm{A}\bm{e}_i=\lambda_i\bm{e}_i$成立。

## 混合积的线性性质

将任意向量按照特征向量分解时，利用了混合积的线性性质。由于混合积是行列式运算，行列式又是多重线性函数，这一点是显然的。

一个简单的证明是，点积是线性的，即 $$(a_1\bm{u}_1+a_2\bm{u}_2)\cdot (\bm{v}\times \bm{w})=a_1\bm{u}_1\cdot(\bm{v} \times \bm{w})+a_2\bm{u}_2\cdot(\bm{v}\times \bm{w})$$ 然后利用混合积的轮换性质（可通过行列式表示证明，但是通过行列式性质亦可直接证得混合积是线性的），可知$\bm{v},\bm{w}$也是线性项。

## 为何称作不变量

矩阵的不变量之所以被称为不变量，是因为它们在坐标变换下不变。

考虑坐标变换（正交）矩阵$\bm{S}$，矩阵$\bm{A}$经变换后得到矩阵$\bm{B}=\bm{S}^{-1}\bm{A}\bm{S}$。计算$\bm{B}$的特征多项式， 利用正交矩阵和行列式的性质， $$\label{eq:3}
  \abs{\bm{B}-\lambda \bm{E}}=\abs{\bm{S}^{-1}\bm{A}\bm{S}-\bm{S}^{-1}\lambda\bm{S}}=\abs{\bm{S}^{-1}(\bm{A}-\lambda\bm{E})\bm{S}}
  =\abs{\bm{S}^{-1}}\abs{\bm{A}-\lambda \bm{E}}\abs{\bm{S}}=\abs{\bm{A}-\lambda \bm{E}}$$ 可见$\bm{A}$和$\bm{B}$的特征多项式相同，因此由`\autoref{eq:1}`{=latex}和`\autoref{eq:2}`{=latex}的推导可知$\bm{A}$和$\bm{B}$的不变量也相同。

## 一个简便证法

对于第三式，可以通过写成矩阵相乘的形式发现 $$\left[
    \bm{A}\bm{u}~\bm{Av}~\bm{Aw}
  \right]=\abs{
    \bm{A}\begin{pmatrix}
      u_x&u_y&u_z\\
      v_x&v_y&v_z\\
      w_x&w_y&w_z
    \end{pmatrix}
  }=\abs{\bm{A}}
  \left[
    \bm{u}~\bm{v}~\bm{w}
  \right]$$ 于是便很显然了。

# \*粗暴展开硬核做法及反推结论

注：最初我是这么做的，但是卡在了一些关键步骤的证明上。现在倒过来可以证明那些关键步骤。

将点乘和叉乘全部利用求和展开，得到 $$\left[
    \bm{u}~\bm{v}~\bm{w}
  \right]=u^iv^jw^k\varepsilon_{ijk}$$ 此处$\bm{u}=u^i\bm{b}_i$，$\bm{b}_i,\bm{b}_j,\bm{b}_k$为笛卡尔直角坐标系的三个基向量。Levi-Civita符号$\varepsilon_{ijk}$在$ijk$中有任意两个相同时取$0$，全不相同时为$\pm 1$，符号由$ijk$的置换奇偶性决定（例如$\varepsilon_{123}=1$）

由于$\bm{A}\bm{u}=A_{ij}\bm{e}_i\otimes \bm{e}_j\cdot u^k\bm{e}_k=A_{ij}u^j\bm{e}_i$，因此 $$\left[
    \bm{Au}~\bm{v}~\bm{w}
  \right]=A_{li}u^iv^jw^k\varepsilon_{ljk}$$ 同理，有 $$\left[
    \bm{u}~\bm{Av}~\bm{w}
  \right]=A_{lj}u^iv^jw^k\varepsilon_{ilk}$$ $$\left[
    \bm{u}~\bm{v}~\bm{Aw}
  \right]=A_{lk}u^iv^jw^k\varepsilon_{ijl}$$ 由于我们已经证明了等式，这也就是说 $$u^iv^jw^k(A_{li}\varepsilon_{ljk}+A_{lj}\varepsilon_{ilk}+A_{lk}\varepsilon_{ijl})=\tr \bm{A}u^iv^jw^k\varepsilon_{ijk}$$ 可以从中提取出一般性的抽象规律（注意对$i,j,k,l$求和) $$f(i,j,k)[g(l,i)\varepsilon_{ljk}+g(l,j)\varepsilon_{ilk}+g(l,k)\varepsilon_{ijl}]=f(i,j,k)g(l,l)\varepsilon_{ijk}$$ 这个还是容易证明的。首先，可以证明$i,j,k$有一组相等时左边求和项为零。例如$i=j$时，中括号里为 $$[g(l,i)\varepsilon_{lik}+g(l,i)\varepsilon_{ilk}+g(l,k)\varepsilon_{iil}]$$ 由于$\varepsilon_{iil}=0$，$\varepsilon_{lik}=-\varepsilon_{ilk}$，因此上式为零。

对于$i,j,k$互不相等的情况，因为$i,j,k,l$只能取$1,2,3$，$l$必须与其中一个相等。如果$l=i$，则$\varepsilon_{ilk}=\varepsilon_{ijl}=0$。 那么总共只有一项 $$f(i,j,k)g(i,i)\varepsilon_{ijk}$$ 注意此处求和限制$l=i$。注意到只对互不相等的$i,j,k$进行求和，对任意函数$F$有 $$\sum_{i,j,k}(F(i,j,k,i)+F(i,j,k,j)+F(i,j,k,k))=\sum_{i,j,k}\sum_lF(i,j,k,l)$$ 也就是令$l=i,l=j,l=k$得到的三项加起来，结果就是 $$f(i,j,k)(g(i,i)+g(j,j)+g(k,k))\varepsilon_{ijk}=f(i,j,k)g(l,l)\varepsilon_{ijk}$$

对于另外两个等式，相应也可得到两个结论 $$\begin{gathered}
  f(i,j,k)[g(l,i)g(m,j)\varepsilon_{lmk}+g(l,j)g(m,k)\varepsilon_{lmi}+g(l,k)g(m,i)\varepsilon_{lmj}]\\
  =f(i,j,k)\varepsilon_{ijk}\frac{1}{2}[g(l,l)g(m,m)-g(l,m)g(m,l)]
\end{gathered}$$ $$f(i,j,k)[g(l,i)g(m,j)g(n,k)\varepsilon_{lmn}]=f(i,j,k)\varepsilon_{ijk}\abs{g}$$ 其中$\abs{g}$表示对写成函数形式的矩阵$g$求行列式。
