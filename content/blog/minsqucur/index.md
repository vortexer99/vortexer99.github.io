---
title: '固定两端最小面积的旋转曲面'
date: 2019-06-26
url: /posts/2019/06/minsqucur/
tags:
  - Blogpost
  - Mathematic
  - 1-5 Pages
types:
  - blogpost
topics:
  - mathematics
lengths:
  - 1-5-pages
authors:
  - me
---

设绕 x 轴旋转的曲线，在 xy 平面内由函数 y = f(x) 和两端点决定，求曲面面积最小值。

设绕$x$轴旋转的曲线，在$xy$平面内由函数$y=f(x)$和两端点$(x_1,y_1),(x_2,y_2)$决定$(x_1<x_2,\;\forall x\in (x_1,x_2)f(x)>0)$， 则旋转而成的曲面面积为 $$S=\int_{x_1}^{x_2}2\pi y \;\mathrm{d}s=2\pi\int_{x_1}^{x_2}f(x)\sqrt{f'^2(x)+1}\;\mathrm{d}x$$ 我们要求曲面面积的最小值。这是一个比较简单的泛函问题。

# 解

由于两端点固定，所以可由Euler-lagrange方程求得曲面面积的最小值。令泛函 $$F:=f(x)\sqrt{f'^2(x)+1}$$ 对EL方程 $$\frac{\mathrm{d}}{\mathrm{d} x}\frac{\partial F}{\partial f'}-\frac{\partial F}{\partial f}=0$$ 先作一些变换，以节省计算量（这是一个较为常用的技巧）。由于 $$\frac{\mathrm{d} F}{\mathrm{d} x}=\frac{\partial F}{\partial f}f'+\frac{\partial F}{\partial f'}\frac{\mathrm{d} f'}{\mathrm{d} x}+\frac{\partial F}{\partial x}$$ 由于$F$不显含$x$，故最后一项为零。对中间一项，把对$x$全导数提到最外面，即分部积分 $$\frac{\mathrm{d} F}{\mathrm{d} x}=\frac{\partial F}{\partial f}f'+\frac{\mathrm{d}}{\mathrm{d} x}\left(\frac{\partial F}{\partial f'}f'\right)-f'\frac{\mathrm{d}}{\mathrm{d} x}\frac{\partial F}{\partial f'}$$ 注意到首尾两项即是EL方程。把中间一项移到左边合并导数，得到 $$\frac{\mathrm{d}}{\mathrm{d} x}\left(F-f'\frac{\partial F}{\partial f'}\right)=f'\left(\frac{\mathrm{d}}{\mathrm{d} x}\frac{\partial F}{\partial f'}-\frac{\partial F}{\partial f}\right)=0$$ 那么显然有 $$f'\frac{\partial F}{\partial f'}-F=c$$ 其中$c$是常数。于是 $$f\left(f'^2(f'^2+1)^{-1/2}-(f'^2+1)^{1/2}\right)=c$$ 化简得到 $$f^2=c^2(f'^2+1)$$ 设$f(x)=c\cosh u(x),\;f'=c\sinh u(x)\cdot u'(x)$，得 $$\cosh^2u=c^2\sinh^2u\cdot u'^2+1$$ 利用$\cosh^2u=\sinh^2u+1$，$f>0,\cosh x>0\;\Rightarrow\; u>0\;\Rightarrow\;\sinh u>0$，化简得 $$u'c=\pm 1 \quad\Rightarrow \quad u=\pm\frac{x}{c}+c_2=\pm c_1x+c_2\quad (c_1=1/c)$$ 由于$\cosh x$是偶函数，$\cosh(\pm c_1x+c_2)=\cosh(c_1x\pm c_2)$，又因为$c_2$是任意常数，可以直接用正号代替正负号。 于是结果为 $$f=\frac{1}{c_1}\cosh(c_1x+c_2)\qquad (c_1>0)$$ 注意到其中决定形状的只有双曲余弦函数，自由常数$c_1$表征$xy$坐标等比例缩放对解无影响，$c_2$表征左右平移坐标对解无影响。 考虑到形成最小面积的曲线形状不依赖于坐标架选取的客观性，以及固定的两点限制条件可以解出两常数，这是合情合理的。

由于这曲线由双曲余弦函数决定，因此又称这条曲线为悬链线，其名称来源于将一根绳子两端悬挂固定，受重力自然下垂所形成的形状。
