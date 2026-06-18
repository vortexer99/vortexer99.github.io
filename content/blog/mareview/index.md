---
title: '数学分析2期末复习'
date: 2018-07-01
url: /posts/2018/07/mareview/
tags:
  - Blogpost
  - Mathematic
  - Mathematical Analysis
  - Vector calculus
  - 6-10 Pages
types:
  - blogpost
topics:
  - mathematics
  - mathematical-analysis
  - vector-calculus
lengths:
  - 6-10-pages
authors:
  - me
---

矢量分析，曲线和曲面积分，极限过渡

-   矢量分析

场的分类：数量场$u(x,y,z)$,矢量场$\overrightarrow{u}(x,y,z) = P\left. （x,y,z \right.）\overrightarrow{i} + Q(x,y,z)\overrightarrow{j} + R(x,y,z)\overrightarrow{k}$

后请注意区分

Nabla算符 $\nabla$ 若记为向量$\frac{\partial}{\partial x}\overrightarrow{i} + \frac{\partial}{\partial y}\overrightarrow{j} + \frac{\partial}{\partial z}\overrightarrow{k} = \left( \frac{\partial}{\partial x},\frac{\partial}{\partial y},\frac{\partial}{\partial z} \right),$则各运算法则与矢量运算相同

方向导数：数量场$u(x,y,z)$沿某一方向$\overrightarrow{l} = (\cos\alpha,\cos\beta,\cos\gamma)$的增减情况和速度

$$\frac{\partial u}{\partial\overrightarrow{l}} = \frac{\partial u}{\partial x}\cos\alpha + \frac{\partial u}{\partial y}\cos\beta + \frac{\partial u}{\partial z}\cos\gamma$$

梯度：数量场→矢量场，方向表示该点方向导数最大的方向（增加最快的方向），大小表示增加最快方向导数的值（增加的速度）

$${grad}u = \nabla u = \left( \frac{\partial u}{\partial x},\frac{\partial u}{\partial y},\frac{\partial u}{\partial z} \right)\ $$

$$注：\frac{\partial u}{\partial\overrightarrow{l}} = \nabla u \cdot \overrightarrow{l} = |\nabla u|\left| \overrightarrow{l} \right|\cos\theta,\left| \overrightarrow{l} \right| = 1,\cos\theta \in \lbrack - 1,1\rbrack$$

$$\therefore\nabla u与l方向相同时方向导数有最大值\left( \frac{\partial u}{\partial\overrightarrow{l}} \right)_{M} = |\nabla u| = \sqrt{\left( \frac{\partial u}{\partial x} \right)^{2} + \left( \frac{\partial u}{\partial y} \right)^{2} + \left( \frac{\partial u}{\partial z} \right)^{2}}$$

$$方向相反时有负的最大值,垂直时\frac{\partial u}{\partial\overrightarrow{l}} = 0$$

散度：矢量场→数量场，定义为通量与体积比的极限（定义了解即可）

$${div}\overrightarrow{u} = \nabla \cdot \overrightarrow{u} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z},{div}\overrightarrow{u} \equiv 0的场称为无源场$$

旋度：矢量场→矢量场

方向旋量：取定一点及一个方向$\overrightarrow{n} = (\cos\alpha,\cos\beta,\cos\gamma)$，在过该点的垂面上作闭路环绕该点，环量与面积比的极限称为该点绕该方向的方向旋量。（定义了解即可）

$$设\overrightarrow{u} = \left( P(x,y,z),Q(x,y,z),R(x,y,z) \right)$$

$$R_{n} = \left| \begin{matrix}
\cos\alpha & \cos\beta & \cos\gamma \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
P & Q & R
\end{matrix} \right| = \overrightarrow{n} \cdot (\nabla \times \overrightarrow{u})$$

旋度的方向定义为使方向旋量达到最大的方向，大小为此时的方向旋量

$${rot}\overrightarrow{u} = \nabla \times \overrightarrow{u} = \left| \begin{matrix}
\overrightarrow{i} & \overrightarrow{j} & \overrightarrow{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
P & Q & R
\end{matrix} \right|若{rot}\overrightarrow{u} \equiv 0,称\overrightarrow{u}为无旋场$$

$$注：R_{n} = \overrightarrow{n} \cdot {rot}\overrightarrow{u},故\ \overrightarrow{n}与{rot}\overrightarrow{u}方向相同时R_{n}有最大值\left| {rot}\overrightarrow{u} \right|\ $$

保守场：沿任一闭路的环量为零。

在单连通区域内，保守场与无旋场等价。

-   例1

$$u = 2x + 3y + 4z$$

$${grad}u = \nabla u = \left( \frac{\partial u}{\partial x},\frac{\partial u}{\partial y},\frac{\partial u}{\partial z} \right) = (2,3,4) = 2\overrightarrow{i} + 3\overrightarrow{j} + 4\overrightarrow{k}$$

$${div}{{grad}u} = \nabla \cdot (\nabla u) = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z},其中P = \frac{\partial u}{\partial x} = 2，Q = \frac{\partial u}{\partial y} = 3，R = \frac{\partial u}{\partial z} = 4$$

$$于是{div}{{grad}u} = 0 + 0 + 0 = 0$$

$${div}{{grad}u} = \nabla \cdot (\nabla u),记为\Delta u = \frac{\partial^{2}u}{\partial x^{2}} + \frac{\partial^{2}u}{\partial z^{2}} + \frac{\partial^{2}u}{\partial z^{2}}$$

$${rot}{{grad}u} = \nabla \times (\nabla u) = \left| \begin{matrix}
\overrightarrow{i} & \overrightarrow{j} & \overrightarrow{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
\frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} & \frac{\partial u}{\partial z}
\end{matrix} \right| = 0$$

$$此式对任意数量场均成立，即梯度场是无旋场$$

-   例2

$$\overrightarrow{u} = (x + y)\overrightarrow{i} + (y + z)\overrightarrow{j} + (z + x)\overrightarrow{k}$$

$${div}\overrightarrow{u} = \nabla \cdot \overrightarrow{u} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z} = 1 + 1 + 1 = 3$$

$${rot}\overrightarrow{u} = \nabla \times \overrightarrow{u} = \left| \begin{matrix}
\overrightarrow{i} & \overrightarrow{j} & \overrightarrow{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
P & Q & R
\end{matrix} \right| = ( - 1, - 1, - 1)$$

$${div}{{rot}\overrightarrow{u}} = \nabla \cdot \left( \nabla \times \overrightarrow{u} \right) = \left| \begin{matrix}
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
P & Q & R
\end{matrix} \right| = 0$$

此式对任意矢量场均适用，即旋度场是无源场。

梯度，散度，旋度的复合运算，可依照矢量运算和求导法则推导

$$以下函数f为从数量到数量的函数,u,v为数量场函数,\overrightarrow{u},\overrightarrow{v}为矢量场函数,a,b为常数$$

线性性质：

$$a1)\nabla(au + bv) = a\nabla u + b\nabla v\ $$

$$b1)\nabla \cdot \left( a\overrightarrow{u} + b\overrightarrow{v} \right) = a\nabla \cdot \overrightarrow{u} + b\nabla \cdot \overrightarrow{v}$$

$$c1)\nabla \times \left( a\overrightarrow{u} + b\overrightarrow{v} \right) = a\nabla \times \overrightarrow{u} + b\nabla \times \overrightarrow{v}$$

数量函数乘法性质：

$$a2)\nabla(uv) = v(\nabla u) + u(\nabla v)$$

$$b2)\nabla \cdot \left( u\overrightarrow{v} \right) = u\nabla \cdot \overrightarrow{v} + \overrightarrow{v} \cdot \nabla u$$

$$c2)\nabla \times \left( u\overrightarrow{v} \right) = u\left( \nabla \times \overrightarrow{v} \right) + (\nabla u) \times \overrightarrow{v}$$

注：可直接按照乘法求导的微分法记，注意验证最后的结果是矢量还是数量。

复合性质：

$$a3)\nabla\left( f(u) \right) = f^{'}(u)\nabla u$$

矢量函数乘法性质：

$$b3)\nabla \cdot \left( \overrightarrow{u} \times \overrightarrow{v} \right) = \overrightarrow{v} \cdot \left( \nabla \times \overrightarrow{u} \right) - \overrightarrow{u} \cdot \left( \nabla \times \overrightarrow{v} \right)$$

$$c3)\nabla \times \left( \overrightarrow{u} \times \overrightarrow{v} \right) = \left( \nabla \cdot \overrightarrow{v} \right)\overrightarrow{u} - \left( \nabla \cdot \overrightarrow{u} \right)\overrightarrow{v}$$

推导示范：

$$b2)\nabla \cdot \left( u\overrightarrow{v} \right) = u\nabla \cdot \overrightarrow{v} + \overrightarrow{v} \cdot \nabla u$$

$$证:设\overrightarrow{v} = \left( v_{x},v_{y},v_{z} \right),其中v_{x},v_{y},v_{z}均是x,y,z的数量函数$$

$$\nabla \cdot \left( u\overrightarrow{v} \right) = \frac{\partial uv_{x}}{\partial x} + \frac{\partial uv_{x}}{\partial y} + \frac{\partial uv_{z}}{\partial z} = \left( \frac{\partial u}{\partial x}v_{x} + \frac{\partial v_{x}}{\partial x}u \right) + \left( \frac{\partial u}{\partial y}v_{y} + \frac{\partial v_{y}}{\partial y}u \right) + \left( \frac{\partial u}{\partial z}v_{z} + \frac{\partial v_{z}}{\partial z}u \right)$$

$$= \left( \frac{\partial v_{x}}{\partial x}u + \frac{\partial v_{y}}{\partial y}u + \frac{\partial v_{z}}{\partial z}u \right) + \left( \frac{\partial u}{\partial x}v_{x} + \frac{\partial u}{\partial y}v_{y} + \frac{\partial u}{\partial z}v_{z} \right)$$

$$= u\nabla \cdot \overrightarrow{v} + \overrightarrow{v} \cdot (\nabla u)$$

$$\ c3)\nabla \times \left( \overrightarrow{u} \times \overrightarrow{v} \right) = \left( \nabla \cdot \overrightarrow{v} \right)\overrightarrow{u} - \left( \nabla \cdot \overrightarrow{u} \right)\overrightarrow{v}$$

$证:需要用到公式\ \overrightarrow{a} \times \left( \overrightarrow{b} \times \overrightarrow{c} \right) = \left( \overrightarrow{a} \cdot \overrightarrow{c} \right)\overrightarrow{b} - \left( \overrightarrow{a} \cdot \overrightarrow{b} \right)\overrightarrow{c},此式证略$（其实是不会）

$$代入即可得到\nabla \times \left( \overrightarrow{u} \times \overrightarrow{v} \right) = \left( \nabla \cdot \overrightarrow{v} \right)\overrightarrow{u} - \left( \nabla \cdot \overrightarrow{u} \right)\overrightarrow{v}$$

-   例3

$$\overrightarrow{c}为常向量,\overrightarrow{r} = x\overrightarrow{i} + y\overrightarrow{j} + z\overrightarrow{k},r = \left| \overrightarrow{r} \right|$$

$${div}\left. （\overrightarrow{c} \times f(r)\overrightarrow{r} \right.） = \nabla \cdot \left( \overrightarrow{c} \times \left( f(r)\overrightarrow{r} \right) \right) = \left( f(r)\overrightarrow{r} \right) \cdot \left( \nabla \times \overrightarrow{c} \right) - \overrightarrow{c} \cdot \left( \nabla \times \left( f(r)\overrightarrow{r} \right) \right)$$

$$= \left( f(r)\overrightarrow{r} \right) \cdot \overrightarrow{0} - \overrightarrow{c} \cdot \left( f(r)\left( \nabla \times \overrightarrow{r} \right) + \overrightarrow{r} \times \left( \nabla f(r) \right) \right)\ \ $$

$$\nabla \times \overrightarrow{r} = \nabla \times (x,y,z) = \overrightarrow{0}$$

$$\nabla f(r) = f^{'}(r)\nabla(r)$$

$$\nabla r = \nabla\left( \sqrt{x^{2} + y^{2} + z^{2}} \right) = \left( \frac{x}{r},\frac{y}{r},\frac{z}{r} \right) = \frac{\overrightarrow{r}}{r}$$

$$原式 = \overrightarrow{c} \cdot \left( \overrightarrow{r} \times \left( f^{'}(r)\frac{\overrightarrow{r}}{r} \right) \right) = 0\ \ \ \ \ \ \left\lbrack \because\overrightarrow{r} \times \overrightarrow{r} = \overrightarrow{0} \right\rbrack$$

$$注：一些重要结论$$

$$\nabla r = \left( \frac{x}{r},\frac{y}{r},\frac{z}{r} \right) = \frac{\overrightarrow{r}}{r}$$

$$\nabla \times \overrightarrow{r} = \nabla \times (x,y,z) = \overrightarrow{0}$$

$$\nabla \times \overrightarrow{c} = \overrightarrow{0}$$

-   各类积分

<!-- -->

-   第一型曲线积分

$$L:\left( x(t),y(t),z(t) \right),a \leq t \leq b$$

$$\int_{L}^{}{f(x,y,z)}ds = \int_{a}^{b}{f\left\lbrack x(t),y(t),z(t) \right\rbrack}\sqrt{x^{'2}(t) + y^{'2}(t) + z^{'2}(t)}dt$$

$$即ds = \sqrt{x^{'2}(t) + y^{'2}(t) + z^{'2}(t)}dt\ \ \ \ \ \ \left\lbrack \because ds = \sqrt{dx^{2} + dy^{2} + dz^{2}} \right\rbrack$$

-   第二型曲线积分

$$\overrightarrow{f} = P(x,y,z)\overrightarrow{i} + Q(x,y,z)\overrightarrow{j} + R(x,y,z)\overrightarrow{k}$$

$$\int_{\widehat{AB}}^{}{Pdx + Qdy + Rdz} = \int_{a}^{b}{\left\lbrack Px^{'}(t) + Qy^{'}(t) + Rz^{'}(t) \right\rbrack dt}\ $$

$$即dx = x^{'}(t)dt,dy = y^{'}(t)dt,dz = z^{'}(t)dt$$

-   第一型曲面积分

$$S:\left( x(u,v),y(u,v),z(u,v) \right),(u,v) \in \Omega$$

$$\overrightarrow{r_{u}^{'}} = \left( \frac{\partial x}{\partial u},\frac{\partial y}{\partial u},\frac{\partial z}{\partial u} \right)\ \ \ \overrightarrow{r_{v}^{'}} = \left( \frac{\partial x}{\partial v},\frac{\partial y}{\partial v},\frac{\partial z}{\partial v} \right)$$

$$A = \frac{\partial(y,z)}{\partial(u,v)},B = \frac{\partial(z,x)}{\partial(u,v)},C = \frac{\partial(x,y)}{\partial(u,v)}$$

$$E = \overrightarrow{r_{u}^{'}} \cdot \overrightarrow{r_{u}^{'}},F = \overrightarrow{r_{u}^{'}} \cdot \overrightarrow{r_{v}^{'}},G = \overrightarrow{r_{v}^{'}} \cdot \overrightarrow{r_{v}^{'}}$$

$$\iint_{S}^{}{f(x,y,z)dS} = \iint_{\Omega}^{}{f\left( x(u,v),y(u,v),z(u,v) \right)\sqrt{EG - F^{2}}}dudv$$

$$注:\sqrt{EG - F^{2}}其实就是\left| \overrightarrow{r_{u}^{'}} \times \overrightarrow{r_{v}^{'}} \right| = \left| \overrightarrow{r_{u}^{'}} \right|\left| \overrightarrow{r_{v}^{'}} \right|\sin\theta$$

-   第二型曲面积分

$$\overrightarrow{f} = P(x,y,z)\overrightarrow{i} + Q(x,y,z)\overrightarrow{j} + R(x,y,z)\overrightarrow{k}$$

$$\iint_{S}^{}{Pdydz + Qdzdx + Rdxdy} = \pm \iint_{\Omega}^{}{(PA + QB + RC)dudv}$$

正负号由取定曲面的侧决定。

$$注:\iint_{S}^{}{Pdydz + Qdzdx + Rdxdy}可拆成三个积分之和$$

$$\iint_{S}^{}{Pdydz}可化为在S的yOz面上投影区域上的积分,并用y,z表示x,即$$

$$\iint_{S}^{}{Pdydz} = \pm \iint_{S_{x}}^{}{P\left( x(y,z),y,z \right)dydz}\ $$

-   例1

$$计算\int_{L}^{}(xy + yz + zx)ds,L为球面x^{2} + y^{2} + z^{2} = a^{2}与平面x + y + z = 0的交线$$

$$联立可得2x^{2} + 2xy + 2y^{2} = a^{2} \Rightarrow \left. （\sqrt{2}x + \frac{y}{\sqrt{2}} \right.）^{2} + \left( \sqrt{\frac{3}{2}}y \right)^{2} = a^{2}$$

$$设\sqrt{2}x + \frac{y}{\sqrt{2}} = a\cos\theta,\sqrt{\frac{3}{2}}y = a\sin\theta$$

$$\left\{ \begin{aligned}
 & x = \frac{a\left( \sqrt{3}\cos\theta - \sin\theta \right)}{\sqrt{6}} \\
 & y = \frac{a\sin\theta\sqrt{2}}{\sqrt{3}} \\
 & z = - \frac{a\left( \sqrt{3}\cos\theta + \sin\theta \right)}{\sqrt{6}}
\end{aligned} \right.\ ,\left\{ \begin{aligned}
 & x' = \frac{a\left( - \sqrt{3}\sin\theta - \cos\theta \right)}{\sqrt{6}} \\
 & y' = \frac{a\cos\theta\sqrt{2}}{\sqrt{3}} \\
 & z' = - \frac{a\left( - \sqrt{3}\sin\theta + \cos\theta \right)}{\sqrt{6}}
\end{aligned} \right.\ $$

$$原式 = \int_{0}^{2\pi}{- \frac{a^{2}}{2}\sqrt{a^{2}}d\theta} = - \pi a^{3}$$

-   例2

$$计算\oint_{}^{}{\left( x^{2} + y^{2} \right)dx + (x + y)^{2}dy},积分路径L为x^{2} + y^{2} = ax,逆时针方向$$

$$极坐标换元,r^{2} = ar\cos\theta \Rightarrow r = a\cos\theta \Rightarrow \left\{ \begin{aligned}
 & x = a\cos^{2}\theta \\
 & y = a\cos\theta\sin\theta
\end{aligned} \right.\ \ $$

$$原式 = \int_{- \frac{\pi}{2}}^{\frac{\pi}{2}}{\left( - 2a^{3}\cos^{3}\theta\sin\theta + a^{3}\cos^{2}\theta\left( 1 + 2\sin\theta\cos\theta \right)\left( \cos^{2}\theta - \sin^{2}\theta \right) \right)d\theta}$$

$$= a^{3}\int_{- \frac{\pi}{2}}^{\frac{\pi}{2}}{\left( - 2\cos^{3}\theta\sin\theta + \cos^{4}\theta + 2\cos^{5}\theta\sin\theta - \cos^{2}\theta\sin^{2}\theta - 2\cos^{3}\theta\sin^{3}\theta \right)d\theta}$$

$$= \frac{1}{4}\pi a^{3}$$

-   例3

$$计算\iint_{D}^{}{|xyz|dS},S为曲面z = x^{2} + y^{2}被平面z = 1截下的部分$$

$$参数化表示\left\{ \begin{aligned}
 & x = u \\
 & y = v \\
 & z = u^{2} + v^{2}
\end{aligned} \right.\ ,\sqrt{EG - F^{2}} = \sqrt{4u^{2} + 4v^{2} + 1}$$

$$原式 = 4\iint_{D}^{}{\left( u^{3}v + uv^{3} \right)\sqrt{4u^{2} + 4v^{2} + 1}dudv},可知投影D为四分之一圆$$

$$再用极坐标换元得原式 = 4 \times \int_{0}^{\frac{\pi}{2}}{\cos\theta\sin\theta d\theta}\int_{0}^{1}r^{5}\sqrt{4r^{2} + 1}dr = \frac{125\sqrt{5} - 1}{420}$$

-   例4

$$计算\iint_{S}^{}{x^{3}dydz + y^{3}dzdx + z^{3}dxdy},S为球面x^{2} + y^{2} + z^{2} = R^{2}的外侧$$

$$先算\iint_{S}^{}{z^{3}dxdy} = 2\iint_{D}^{}{z^{3}dxdy} = 2\iint_{D}^{}{\left( R^{2} - x^{2} - y^{2} \right)^{\frac{3}{2}}dxdy},投影D为x^{2} + y^{2} = R^{2}圆$$

$$极坐标换元得到\iint_{D}^{}{\left( R^{2} - x^{2} - y^{2} \right)^{\frac{3}{2}}dxdy} = \int_{0}^{2\pi}{d\theta}\int_{0}^{R}{\left( R^{2} - r^{2} \right)^{\frac{3}{2}}rdr} = \frac{2}{5}\pi R^{5}$$

$$由对称性得到原式 = 3 \times 2 \times \frac{2}{5}\pi R^{5} = \frac{12}{5}\pi R^{5}$$

-   三个公式

$$格林公式:P,Q连续可微\int_{\partial D^{+}}^{}{Pdx + Qdy} = \iint_{D}^{}{\left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right)dxdy} = \iint_{D}^{}{\left| \begin{matrix}
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} \\
P & Q
\end{matrix} \right|dxdy}\ $$

$$或\int_{\partial D^{+}}^{}{\left. （P\cos\left. \ \left\langle \overrightarrow{n},x \right\rangle \right.\  + Q\cos\left. \ \left\langle \overrightarrow{n},y \right\rangle \right.\  \right.）ds} = \iint_{D}^{}{\left( \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} \right)dxdy},\overrightarrow{n}为外法线方向\ $$

$$\partial D^{+}正方向的规定:沿着曲线行进时区域在左边$$

$$高斯公式:\iint_{\partial V}^{}{Pdydz + Qdzdx + Rdxdy} = \iiint_{V}^{}{\left( \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z} \right)dxdydz} = \iiint_{V}^{}{{div}\overrightarrow{u}dxdydz}$$

$$斯托克斯公式:\int_{\partial S}^{}{Pdx + Qdy + Rdz} = \iint_{S}^{}\left| \begin{matrix}
dydz & dzdx & dxdy \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
P & Q & R
\end{matrix} \right|$$

$$\partial S的方向由S的定向通过右手螺旋准则确定$$

-   例1

$$计算\iint_{S}^{}{x^{3}dydz + y^{3}dzdx + z^{3}dxdy},S为球面x^{2} + y^{2} + z^{2} = R^{2}的外侧$$

$$利用高斯公式,原式 = \iiint_{V}^{}{3\left( x^{2} + y^{2} + z^{2} \right)dV},V为球x^{2} + y^{2} + z^{2} = R^{2}$$

$$于是原式 = 3 \times 2\pi\int_{0}^{R}{r^{4}dr}\int_{0}^{\pi}{\sin\theta d\theta} = \frac{12}{5}\pi R^{5}$$

-   例2

$$计算\int_{L}^{}{(y - z)dx + (z - x)dy + (x - y)dz},L为x^{2} + y^{2} = R^{2}与\frac{x}{a} + \frac{z}{h} = 1的交线$$

$$从Ox轴正向看去,椭圆是逆时针方向进行的$$

$$利用斯托克斯公式,原式 = - 2\iint_{S}^{}{dydz + dzdx + dxdy},取S为该椭圆$$

$$利用投影计算\iint_{S}^{}{dydz} = \pi\frac{Rh}{a}R = \frac{\pi R^{2}h}{a},\iint_{S}^{}{dzdx} = 0,\iint_{S}^{}{dxdy} = \pi R^{2}$$

$$原式 = - 2\pi R^{2}\frac{h + a}{a}$$

-   极限过渡

$$(a1)F_{t}在B_{t}上一致收敛\ \ (a2)F_{t}在B_{x}上极限存在 \Rightarrow \lim_{B_{x}}{\lim_{B_{t}}{F_{t}(x)}} = \lim_{B_{t}}{\lim_{B_{x}}{F_{t}(x)}}$$

$$(b1)F_{t}在B_{t}上一致收敛\ \ (b2)F_{t}在x_{0}连续 \Rightarrow F在x_{0}连续$$

$$(c1)F_{t}在B_{t}上一致收敛\ \ (c2)F_{t}在某区间上可积 \Rightarrow F在该区间上也可积$$

$$(d1)\mathbf{F}_{\mathbf{t}}^{\mathbf{'}}在B_{t}上一致收敛于g\ \ (d2)F_{t}至少在一点x_{0}收敛 \Rightarrow F_{t}一致收敛于F,且F^{'} = g$$

-   另外两个例子

<!-- -->

-   例1

$$求曲面围成的体积x^{2} + y^{2} + z^{2} = a^{2},x^{2} + y^{2} \leq a|x|\ $$

$$r^{2}\sin^{2}\theta \leq ar\sin\theta\cos\varphi \Rightarrow r\sin\theta \leq a\cos\varphi$$

$$V = 8\int_{0}^{\frac{\pi}{2}}{d\theta}\left( \int_{\frac{\pi}{2} - \theta}^{\frac{\pi}{2}}{d\varphi}\int_{0}^{\frac{a\cos\varphi}{\sin\theta}}{r^{2}\sin\theta dr} + \int_{0}^{\frac{\pi}{2} - \theta}{d\varphi}\int_{0}^{a}{r^{2}\sin\theta dr} \right)$$

$$= 8\int_{0}^{\frac{\pi}{2}}{d\theta}\left( \int_{\frac{\pi}{2} - \theta}^{\frac{\pi}{2}}{\frac{a^{3}\cos^{3}\varphi}{3\sin^{2}\theta}d\varphi} + \int_{0}^{\frac{\pi}{2} - \theta}{\frac{1}{3}a^{3}\sin\theta d\varphi} \right)\ $$

$$= 8\int_{0}^{\frac{\pi}{2}}\left( \frac{a^{3}(\frac{2}{3} - \cos\theta + \frac{1}{3}\cos^{3}\theta)}{3\sin^{2}\theta} + \frac{1}{3}a^{3}\left( \frac{\pi}{2} - \theta \right)\sin\theta \right)d\theta$$

$$= \frac{8}{3}a^{3}\int_{0}^{\frac{\pi}{2}}\left( \frac{\frac{2}{3} - \cos\theta + \frac{1}{3}\cos^{3}\theta}{\sin^{2}\theta} + \frac{\pi}{2}\sin\theta - \theta\sin\theta \right)d\theta$$

$$= \frac{8}{3}a^{3}\left( \left( - \frac{2}{3}\cot\theta + \frac{1}{\sin{\theta\ }} - \frac{1}{3\sin\theta} - \frac{\sin\theta}{3} \right)│_{0}^{\frac{\pi}{2}} + \frac{\pi}{2} - \left( - \theta\cos\theta │_{0}^{\frac{\pi}{2}} + \int_{0}^{\frac{\pi}{2}}{\cos\theta d\theta} \right) \right)$$

$$= \frac{8}{3}a^{3}\left( \left( \frac{2\left( 1 - \cos\theta \right)}{3\sin\theta} \right)│_{0}^{\frac{\pi}{2}} - \frac{1}{3} + \frac{\pi}{2} - 1 \right)$$

$$= \frac{8}{3}a^{3}\left( \frac{2}{3} - \frac{1}{3} + \frac{\pi}{2} - 1 \right)$$

$$= \frac{8}{3}a^{3}\left( \frac{\pi}{2} - \frac{2}{3} \right)$$

-   例2

$$I = \int_{0}^{1}{dx}\int_{x}^{1}{dy}\int_{y}^{1}{y\sqrt{1 + z^{4}}dz} = \int_{0}^{1}{dz}\int_{0}^{z}{dy}\int_{0}^{z}{y\sqrt{1 + z^{4}}}dx$$

$$= \int_{0}^{1}{dz}\int_{0}^{z}{zy\sqrt{1 + z^{4}}dy}$$

$$= \int_{0}^{1}{\frac{1}{2}z^{3}\sqrt{1 + z^{4}}dz}$$

$$= \frac{1}{8}\int_{1}^{2}{\sqrt{1 + z^{4}}d\left( 1 + z^{4} \right)} = \frac{1}{12}\left( 1 + z^{4} \right)^{\frac{3}{2}}│_{0}^{1} = \frac{1}{12}(2\sqrt{2} - 1)$$

-   反常积分极限过渡

$$(a1)f(x,y)在B_{y}上一致收敛于g(x)$$

$$(a2)f(x,y)关于x反常积分一致收敛$$

$$\Rightarrow g(x)反常可积，\lim_{B_{y}}{\int_{a}^{w}{f(x,y)}dx} = \int_{a}^{w}{g(x)dx}$$

$$(b1)f(x,y)连续$$

$$(b2)f(x,y)关于x反常积分一致收敛$$

$$\Rightarrow f可积且f(x,y) = \int_{a}^{w}{dx}\int_{c}^{d}{f(x,y)dy}$$

$$(c1)f(x,y),f_{y}^{'}(x,y)连续$$

$$\left. （c2 \right.）f_{y}^{'}(x,y)关于x反常积分一致收敛$$

$$\left. （c3 \right.）f(x,y)关于x反常积分至少在一点y_{0}收敛$$

$$\Rightarrow f(x,y)关于x反常积分收敛于F\left. （y \right.）且F^{'}(y) = \int_{a}^{w}{f_{y}^{'}(x,y)}dx$$

$$(d1)f\left. （x,y \right.）连续$$

$$(d2)f(x,y)关于每个变量的反常积分都一致收敛$$

$$(d3)\int_{a}^{w}{dx}\int_{c}^{\widetilde{w}}{\left| f(x,y) \right|dy}或\int_{c}^{\widetilde{w}}{dy}\int_{a}^{w}{\left| f(x,y) \right|dx}存在$$

$$\Rightarrow \int_{a}^{w}{dx}\int_{c}^{\widetilde{w}}{f(x,y)dy} = \int_{c}^{\widetilde{w}}{dy}\int_{a}^{w}{\left| f(x,y) \right|dx}反常积分可交换$$
