---
title: '连续介质力学笔记'
date: 2019-02-25
url: /posts/2019/02/continous
tags:
  - Lecnote
  - Mathematic
  - Physic
  - Mechanics
  - Fluid Mechanics
  - 31-100 Pages
types:
  - lecture-note
topics:
  - mathematics
  - physics
  - mechanics
  - fluid-mechanics
lengths:
  - 31-100-pages
authors:
  - me
---

2019年春季赵亚溥老师《连续介质力学》课程所整理的笔记。

完善度较低。

连续介质力学                                第 1 次课笔记
                                              庄逸

         课程日期：2019 年 2 月 25 日                        最后修改：2019 年 3 月 24 日

  • 经典力学：经过伽利略群变换后不变。

  • 相对论力学：经过洛伦兹群变换后不变。

    固体力学、流体力学、流变学
    Kinetic theory: 动理学，运动机理学                    Dynamics: 动力学
    Multidisciplines, multidisciplinary 横断学科：不仅局限于某一领域，而是横向贯穿于众多
领域。
    作业：看各种空间（书 P11）

                                   1 玻尔兹曼方程
    Boltzmann equation(1872)
                                          ∫
                                   dN =       f (r, v, t)d3 rd3 v             (1)

f : PDF, probablity density function. 无量纲函数，概率密度分布
六维相空间 d3 rd3 v = dxdydzdvx dvy dvz
    牛顿决定性原理：给定初始位置和初速度，轨迹确定。
                                                F
                        df = f (r + vdt, v +      dt, t + dt) − f (r, v, t)   (2)
                                                m
Taylor expansion (1st order)
                               ∂f      ∂f         ∂f F
                                  dt +    · vdt +   · dt = df                 (3)
                               ∂t      ∂r         ∂v m
其中 ∂f , ∂f 是向量。
   ∂r ∂v

---

连续介质力学                                                                           第 1 次课笔记

   利用 p = mv，
                                          (        )
             ∂f                               df
                + v · ∇r f + F · ∇p f =                        = ν (frequency)         (4)
             ∂t                               dt   collision

ν : 碰撞频率，具有频率量纲。
   作业：什么是光滑？

 • 当 M → 0（？zx）时，compressible → imcompressible

 • 当 µ → 0 时，N-S→ Euler

   李雪梅，苏格兰咖啡馆，café，波兰，巴拿赫利沃夫

感谢为本次笔记提供参考的同学：               包雨晨，卢子璇

课程日期：2019 年 2 月 25 日                <| 2 |>                       最后修改：2019 年 3 月 24 日

---

                 连续介质力学                                      第 2 次课笔记
                                                       庄逸

            课程日期：2019 年 2 月 27 日                              最后修改：2019 年 3 月 25 日

                                                    1 复习
1.1 PDF
      f: PDF n is the particle number per unit volume
                                           ∫
                                       n = f dudvdw                                     (1)

If m is the mass of one molecule, then ρ = nm
                                                       ∫
                                              N=            ndxdydz                     (2)

N : total particle numbers.

1.2    玻尔兹曼方程

                         ∫             ∫
                                                   f (q, p, t)dqx dqy dqz dpx dpy dpz   (3)
                             momenta       space

phase space：相空间              dqx ：广义坐标                 dpx ：momenta 广义动量
                                   ∂f   p                     df
                                      +   · ∇q f + F · ∇p f =                           (4)
                                   ∂t   m                     dt
      df
      dt
           : external forces + diffusion + collision，具有频率的量纲

1.3 Others
      NS 方程                   (                         )
                                  ∂v
                          ρ          +v·∇⊗v                 = −∇p + µ∇2 v + ρg          (5)
                                  ∂t

---

连续介质力学                                                                    第 2 次课笔记

µ∇2 v : momentum diffusion，动量扩散
   Lorentz force
                                  F = q(E + v × B)                                (6)

   conjugate: 共轭，如应力和应变

                          2   物理定律可逆性与对称性
   multidisciplinary, hierarchy: 级联
   Kinematics: 运动学        Kinetic theory: 动理学，运动机理学
   Dynamics: 动力学

  • Newtonian(1687)
                                             dp
                                        f=      = mẍ                             (7)
                                             dt
  • Lagrangian(1778)
                                      d ∂L      ∂L
                                              −    =0                             (8)
                                      dt ∂ q̇α ∂qα
  • Hamiltonian(1834,1835)
                                           ∂H             ∂H
                                 p˙α = −          q˙α =                           (9)
                                           ∂qα            ∂pα
  • Schrödiner equation
                                      ~2 2             ∂Ψ
                                  −      ∇ Ψ + vΨ = i~                           (10)
                                      2m               ∂t
这些都是可逆的。
   涨落：fluctuation         CPT symmetry reversal：CPT 对称
   Boltzmann equation 破坏了时间反演不变性
   热力学第二定律：微观保守，宏观耗散。

                       3 BBGKY 级联和量级分类
   见课程讲义。

感谢为本次笔记提供参考的同学：                  包雨晨，卢子璇

课程日期：2019 年 2 月 27 日                    <| 2 |>                 最后修改：2019 年 3 月 25 日

---

            连续介质力学                      第 3 次课笔记
                                    庄逸

        课程日期：2019 年 3 月 4 日             最后修改：2019 年 3 月 25 日

  希尔伯特公理：完备性，相容性 (与一致性？)，独立性。

 • paradiam：范式；paradiam shift：范式转移

 • postulate：公设；axiom：公理

 • 对流导数：convective (advective) derivative

 • aka: also known as

 • steady: 定常的：unsteady: 非定常的

                               1 对流导数
  温度场（标量场）T (r, t)
                        DT   ∂T   ∂T ∂r   ∂T
                           =    +   ·   =    + v · ∇T          (1)
                        Dt   ∂t   ∂r ∂t   ∂t
v · ∇T 称为对流导数，是非线性项。 DT
                     Dt
                        是拉格朗日描述， ∂T
                                 ∂t
                                    是欧拉描述。
  作业：证明 NS 方程的非线性性，参见 P16 例 1.7
  ∇ ⊗ v 二阶张量

感谢为本次笔记提供参考的同学：               包雨晨、卢子璇

---

             连续介质力学                                   第 4 次课笔记
                                                 庄逸

         课程日期：2019 年 3 月 6 日                           最后修改：2019 年 3 月 25 日

                                  1     线性与非线性方程
   ·Schödinger’s equation, Linear equation
                         (           )
                             ~2 2                  ∂Ψ(r, t)
                           −    ∇ + v Ψ(r, t) = i~                            (1)
                             2m                      ∂t
·Principle of superposition 叠加原理
   Gross-pitaevskii equation (Bose-Einstein condensation)
                                                  
                  −   ~2
                                                                 ∂Ψ(r, t)
                          ∇2 + v(r) + g |Ψ(r, t)|  Ψ(r, t) = i~
                                                 2
                                                                              (2)
                       2m               | {z }                     ∂t
                                                nonlinear

   ·N-S Equation             (                   )
                                 ∂v
                         ρ          + (v · ∇)v
                                           ⃗         = −∇p
                                                        ⃗ + µ∇2 v + ρg        (3)
                                 ∂t

                                   2     无量纲数和量纲
   Of the order of magnitude: 具有数量级

2.1 Capillary number
   毛细数，是黏性力与表面张力之比
                             µv/L   µv   danamic viscosity × velocity
                    Ca =          =    =                                      (4)
                             γ/L    γ         surface tension
   表面张力：形成单位新面积需要做的功。
                                              F ·L   F ·L   F
                                      [γ] =        ∼      ∼                   (5)
                                               A      L2    L

---

连续介质力学                                                                       第 4 次课笔记

2.2 Reynolds number

                                   ρv 2   ρvL   vL                 µ
                          Re =          =     =               ν=                     (6)
                                  µv/L     µ     ν                 ρ

2.3 Newtonian fluid

                                                     ∂v
                                        τ = −µ
                                    应力 |{z}                                          (7)
                                                     ∂y
                                          Pa        |{z}
                                                     1/t

   Dynamic Viscocity 动力黏度 → [µ] = [Pa · s]
   Kinematic Viscosity 运动黏度

                                  [ν] = L2 T −1 , [ν] = [D]                          (8)

D: 扩散系数
   Diffusion < r2 >= 6Dt, < x2 >= 2Dt 注: 尖括号表示成正比？
                         (              )
                           ∂v
                       ρ      + (v · ∇v) = −∇p + µ∇2 v + ρg                          (9)
                           ∂t

   作业：证明 [p] = [ρv 2 ] = M L−3 L2 T −2 = . . .
   导数量纲的计算：                   [      ]         [ n ]
                                  dy     [y]    d y    [y]n
                                       =     ,       =                              (10)
                                  dx     [x]    dx n   [x]n

2.4 Deborah number

                               τ    relaxation time
                              De =
                                 =                                                  (11)
                               T   observation time
(Maxwell) relaxation time：施加一个切应力，在介质中能保持的时间。
   De > 1, Solid; De < 1, Liquid; De ∼ 1, 流变体！

2.5 Water, e.g.
   τ ∼ 10−12 s。分子间力程 10−10 m(Å)
   已知
                                        µv                 γ
                                 Ca =      ∼ 1,      v∼                             (12)
                                        γ                  µ

课程日期：2019 年 3 月 6 日                       <| 2 |>                  最后修改：2019 年 3 月 25 日

---

连续介质力学                                                                  第 4 次课笔记

      γ = 0.0738N/m = 7.38 × 10−3 N/m µ ∼ 1.02 × 10−3 Pa · s.
      ∴ v ∼ 72m/s 是水的毛细波速，量级为 102 m/s. Hence,

                                       10−10 m(Å)
                                 τ=               ∼ 10−12 s                    (13)
                                         102 m/s

和已知的结论相符合。
      作业：雷诺数是如何出来的 (见书 P325-326)；动力黏度和运动黏度有什么关系，和扩散
系数又有什么关系？毛细数为什么是粘性力和表面张力的比。

                                3      无源场和涡量场
      涡量
                                     Ω = ∇ × v = curl v                        (14)

      由于
                                    ∇ · Ω = ∇ · (∇ × v) = 0                    (15)

因此涡量场散度为零，为无源场。

3.1    无源场的性质
  1. 涡管中任一横截面上的涡通量保持同一常数值。

  2. 涡管不能在流体中产生或消失。

（《流体力学》吴望一）

感谢为本次笔记提供参考的同学：                      包雨晨，卢子璇

课程日期：2019 年 3 月 6 日                        <| 3 |>            最后修改：2019 年 3 月 25 日

---

                连续介质力学                                  第 5 次课笔记
                                                   庄逸

           课程日期：2019 年 3 月 11 日                          最后修改：2019 年 3 月 25 日

                                    1 拉格朗日方程
      1788 年，Lagrangian Mechanics
      HP: Hamilton’s principle, first principle (1834,1835)

1.1    作用量与动能势能
      action 作用量                          ∫ t2
                                   S=            Ldt     L=T −V                       (1)
                                            t1

L : Lagrangian，是个标量
      Kinetic energy
                                                            1 2
                                          T = T (q̇, t) =     mq̇                     (2)
                                                            2
q̇ : generalized velocity，广义速度
      potential energy for conservative f = −∇V , V (q), q: generalized coordinate

1.2    变分
      HP: δS = 0       stationary value 驻值，一般是最小
                                   ∫ t2
                              S=        L(q, q̇, t)dt                                 (3)
                                    t1
                                   ∫ t2
                        S + δS =          L(q + δq, q̇ + δ q̇, t)dt                   (4)
                                    t1
                                   ∫ t2
                            δS =          [L(q + δq, q̇ + δ q̇, t) − L(q, q̇, t)]dt   (5)
                                    t1

---

连续介质力学                                                                                 第 5 次课笔记

variation 变分；isochronous variation 等时变分
                                    ( )
     derivative dx
                dt
                   , its variation δ dx
                                     dt
      必须要等时变分的原因：
                ( )
                 dx   δ(dx) dx δ(dt)   d(δx) dx d(δt)
              δ     =      −         =      −                                                  (6)
                 dt     dt   (dt)2      dt    (dt)2
                                        (        )
                                            dx           d
                                    δ                =      (δx) ⇒ δt ≡ 0                      (7)
                                            dt           dt
进行泰勒展开：                                  ∫ t2 (                           )
                                                     ∂L        ∂L
                                  δS =                  · δq +      · δ q̇ dt                  (8)
                                            t1       ∂q        ∂ q̇
δ q̇ ：虚速度
      对第二项分部积分，integral by parts.
               ∫ t2                ∫ t2
                    ∂L                   ∂L
                        · δ q̇dt =          d(δq)                                              (9)
                t1 ∂ q̇             t1 ∂ q̇
                                                ∫ t2
                                   ∂L       t2       d ∂L
                                 =      · δq −               · δq                             (10)
                                   ∂ q̇     t1    t1 dt ∂ q̇

      δ q̇ : virtual velcity
      δq : virtual displacement
      ∂L
      ∂ q̇
           : generalized momentum
      结合变分的重要性质，起点和终点变分为零：

                                            δq(t1 ) = δq(t2 ) = 0                             (11)

于是                                      ∫ t2 (                   )
                                                  ∂L   d ∂L
                               δS =                  −               · δqdt = 0               (12)
                                         t1       ∂q   dt ∂ q̇

1.3     拉格朗日方程
      由 δq 任意性，可知拉格朗日方程为
                                                 ∂L   d ∂L
                                                    −         =0                              (13)
                                                 ∂q   dt ∂ q̇

或
                                                 d ∂L      ∂L
                                                         −    =0                              (14)
                                                 dt ∂ q˙i ∂qi

课程日期：2019 年 3 月 11 日                                  <| 2 |>                最后修改：2019 年 3 月 25 日

---

连续介质力学                                                              第 5 次课笔记

   其中由于
                         ∂L        ∂V
                              =−       = Fi                                (15)
                         ∂qi       ∂qi
                         d ∂L       d
                                  = (mq˙i ) = mq¨i = Fi                    (16)
                         dt ∂ q˙i   dt

和牛顿第二定律等价！
   广义坐标可以是角度，广义速度可以是角速度。
   作业：写单摆和双摆的拉格朗日量和拉格朗日方程。

                            2 连续性方程
   Continuity equation
                 ∂p
                    + ∇ · (ρv) = 0                                         (17)
                 ∂t
通过散度展开，前两项合并得到等价形式：
                               Dρ
                                  + ρ divv = 0                             (18)
                               Dt
或者写成相对变化率
                                    1 Dρ
                                −        = divv                            (19)
                                    ρ Dt
在不可压缩时，有
                                           Dρ
                             divv = 0         =0                           (20)
                                           Dt
   sonic boom：音爆
   作业：证明弦振动方程是双曲型方程。

感谢为本次笔记提供参考的同学：              包雨晨，卢子璇

课程日期：2019 年 3 月 11 日                <| 3 |>               最后修改：2019 年 3 月 25 日

---

           连续介质力学                                第 6 次课笔记
                                             庄逸

     课程日期：2019 年 3 月 18 日                         最后修改：2019 年 3 月 25 日

                             1    场论 Field theory
Vorticity Ω = ∇ × u = curl u

                                  ∇ · Ω = ∇ · (∇ × u) ≡ 0                      (1)

∀ϕ as a scalar in soblev space,
                                          ∇ × (∇ϕ) = 0                         (2)

i, j, k: base vectors

                   i    j    k        (                )
                                           ∂2ϕ   ∂2ϕ
                    ∂
                   ∂x
                         ∂
                        ∂y
                              ∂
                             ∂z
                                  =            −           i + ()j + ()k = 0   (3)
                   ∂ϕ   ∂ϕ   ∂ϕ
                                          ∂y∂z ∂z∂y
                   ∂x   ∂y   ∂z

Helmholtz decomposition representation，分解为一个无旋场和无散场

                u = ∇ϕ + ∇ × A             ∇ × (∇ϕ) = 0, ∇ · (∇ × A) = 0       (4)

orthogonal decomposition 正交分解

                                           2 杂项
连续介质假定，适用范围：作用量 S ≫ ~。当 S ∼ ~ 时，假定不适用！
~ = h/2π，h: plank const
近代连续介质力学始于欧拉。哈密顿原理是力学第一性原理。

---

连续介质力学                                                                       第 6 次课笔记

                                3    分析力学解振动方程
                                                                                        √
   [x]-dimension, tension T , [T ] = M LT −2 ; Line density µ, [µ] = M L−1 , Then c ∼       T /µ
（标度关系 scality）
   trig (trigonometric) function 三角函数
   作业：证明弦振动是双曲型偏微分方程。
   书 P29-30
   Kinetic energy; potential energy
   Lagrange equation(L(q, q̇, t) = L(q, qt , t))
                                        d ∂L ∂L
                                                −    =0                                      (5)
                                        dt ∂ q̇   ∂q
   When L(q, qt , qx , t)
                                    ∂ ∂L    ∂ ∂L    ∂L
                                          +       −    =0                                    (6)
                                    ∂t ∂ut ∂x ∂ux   ∂u
   作业：写鼓的膜振动方程（加一项 y)
   双射：bijective; 范式：paradigm; 反对称：antisymmetry
   Epsilon ϵijk , or Levi-civita（奇维塔）symbol, or permutation symbol.

                                    4   麦克斯韦方程组
                                             (        )
                                                  ∂D           ∂ρ
                            ∇ · (∇ × H) = ∇ · J +       =∇·J +                               (7)
                                                   ∂t          ∂t
   作业：证明麦克斯韦方程是线性的。
   用麦克斯韦方程推连续性方程。
   电磁张量，一个矩阵。P70：反对称、无迹、六个独立分量。

感谢为本次笔记提供参考的同学：                         包雨晨，卢子璇

课程日期：2019 年 3 月 18 日                         <| 2 |>          最后修改：2019 年 3 月 25 日

---

               连续介质力学                                      第 7 次课笔记
                                                     庄逸

           课程日期：2019 年 3 月 19 日                             最后修改：2019 年 3 月 24 日

                                            1 诺特定理
      Neother’s theorem (1918), symmetry

1.1    齐次函数
      Homogeneous function 齐次函数，具有以下性质

                            f (λx1 .λx2 , . . . , λxn ) = λm f (x1 , x2 , . . . , xn )    (1)

m: degree of homogeneity. e.g., Kinetic energy T = 1/2mq̇ 2

1.2    欧拉齐次函数定理
      Euler’s homogeneous function theorem
      Taking derivative about λ:
                    ∂f           ∂f                   ∂f
                          x1 +         x2 + · · · +         xn = mλm−1 f (x1 . . . xn )   (2)
                  ∂(λx1 )      ∂(λx2 )              ∂(λxn )
Let λ = 1, then
                                               ∑
                                               n
                                                 ∂f
                                                           = mf                           (3)
                                               i=1
                                                     ∂xi

1.3    能量守恒
      conservation of energy: t-homogeneous

---

连续介质力学                                                                                            第 7 次课笔记

      时间平移不变性：拉格朗日量不显含时间 L(qα , q̇α ). Total differential:
                          (                    )
                  dL ∑ ∂L             ∂L
                      =         q̇α +       q̈                                                          (4)
                   dt   α
                            ∂qα       ∂ q̇α
                                                 d ∂L           ∂L
                                          =               q̇α +        q̈α                              (5)
                                                 dt ∂ q̇α       ∂ q̇α
                                                             (          )
                                                         d ∂L
                                                    =               q̇α                                 (6)
                                                        dt ∂ q̇α

                                          d ∂L      ∂L
                                      ∵           −    =0                                               (7)
                                          dt ∂ q̇α ∂qα
                                  (                       )             (                     )
                        dL   d        ∑ ∂L                      d           ∑ ∂T
                           =                        q̇α       =                         q̇α             (8)
                        dt   dt       α
                                            ∂ q̇α               dt          α
                                                                                ∂ q̇α
(∵ L = T − V )                          (                               )
                                   d        ∑ ∂T
                                 ∴                          q̇α − L         ≡0                          (9)
                                   dt        α
                                                    ∂ q̇α
                             ∂T                      ∂T
                                  = mq̇                   q̇ = mq̇ 2 = 2T                              (10)
                             ∂ q̇                    ∂ q̇

                                                    ∑ ∂T
                                              ∴                       q̇α − L = const                  (11)
                                                      α
                                                              ∂ q̇α

                        2T − (T − V ) = const                         T + V = const                    (12)

                             2     爱因斯坦求和约定
      convention centre: 会展中心
      Einstein summation convention: 约定
                                      ∑
                                      n
                                        ∂L                      ∂L
                                                     q̇α =            q̇α                              (13)
                                      α=1
                                          ∂ q̇α                 ∂ q̇α

Summation is taken over repeated index.

2.1    梯度、散度、旋度算子

                                                        ∂
                                             ∇=            ei                                          (14)
                                                       ∂xi

课程日期：2019 年 3 月 19 日                             <| 2 |>                            最后修改：2019 年 3 月 24 日

---

连续介质力学                                                                                 第 7 次课笔记

  • gradient
                                           ∂ϕ       ∂ϕ    ∂ϕ    ∂ϕ
                                    ∇ϕ =       ei =    i+    j+    k                        (15)
                                           ∂xi      ∂x    ∂y    ∂z
  • divergence
                                    ∂            ∂Aj                             ∂Ai
                      ∇ · A = ei       · Aj ej =     ei · ej = Aj,i δij = Ai,i =            (16)
                                   ∂xi           ∂xi                             ∂xi
      kronecker delta                                   
                                                        1, if i = j
                                      ei · ej = δij =                                       (17)
                                                        0, if i ̸= j

                                                ∂Ax ∂Ay    ∂Az
                                       Ak,k =       +    +                                  (18)
                                                 ∂x   ∂y    ∂z
  • left curl
                                      ∂               ∂Aj           ∂Aj
                        ∇×A=             ei × Aj ej =     ei × ej =     εijk ek             (19)
                                     ∂xi              ∂xi           ∂xi
      Epsilon symbol, Levi-civita. even/odd permutation 123, 231, 312

  • right curl
                                              ∂       ∂Ai
                         A × ∇ = Ai ei ×         ej =     ei × ej = Ai,j εijk ek            (20)
                                             ∂xj      ∂xj

      作业：证明左旋度和右旋度相反。

                             a · b = (ai ei ) · (bj ej ) = ai bj δij = ai bi                (21)

                         F = q(E + v × B)            Fi = q(Ei + εijk vj Bk )               (22)

方程两边都有的: free index.
Repeated indices- dummy index/ silent index

2.2   矩阵和双缩并

                                          
                            A11 A12 A13
                                          
                         A=
                           A 21 A 22 A 23
                                           
                                                          A = Aij ei ⊗ ej ?                (23)
                            A31 A32 A33
trace 迹 tr(A) = Aii

                  trA = A : I         I = δij ei × ej = ei ⊗ ei identity tensor             (24)

课程日期：2019 年 3 月 19 日                            <| 3 |>                  最后修改：2019 年 3 月 24 日

---

连续介质力学                                                                              第 7 次课笔记

colon product
                              z }| {
                A : I = (Aij ei ⊗ ej ) : (ek ⊗ ek ) = Aij δik δjk = Aij δij = Aii        (25)
                                   |      {z   }

(运算方法：相间)
    作业：证明A : I = I : A

2.3 projection tensor of rank two
    n: outward normal
                                fn = (f · n)n = f · (n ⊗ n)                              (26)

                          fτ = f − fn = f · (I − n ⊗ n) = f · P                          (27)

其中点积的点号可去。

感谢为本次笔记提供参考的同学：                      无

课程日期：2019 年 3 月 19 日                        <| 4 |>               最后修改：2019 年 3 月 24 日

---

                  连续介质力学                                     第 7 次课笔记
                                                        庄逸

         课程日期：2019 年 3 月 20 日                                最后修改：2019 年 3 月 24 日

                                        1     诺特定理，动量
    conservation of momentum δq = ε
    variation of Lagrangian, isochronous
                                            ∑
                                            n
                                              ∂L                      ∑
                                                                      n
                                                                        ∂L
                                     δL =               · δqα = ε ·                          (1)
                                            α=1
                                                  ∂qα                 α=1
                                                                            ∂qα
Lagrange equation
                                              d ∂L      ∂L
                                                      −    =0                                (2)
                                              dt ∂ q̇α ∂qα
Hence
            ∑
            n
              d ∂L                 d ∑ ∂L          d ∑                        ∂L
   δL = ε                    =ε·              =ε·        pα = 0 (∵ L = T − V,       = pα )   (3)
            α=1
                  dt ∂ q̇α         dt α ∂ q̇α      dt α                       ∂ q̇α
                                                   ∑
                                        ∴ ptotal =    pα = const                             (4)
                                                         α

                                                  2 张量

                               Prove:       (v · ∇)v = v · ∇v = v · ∇ ⊗ v                    (5)
                                    ∂
                                       ej (vi ei ) = vi,j ej ⊗ ei                            (6)
                                   ∂xj
                                   v · ∇ ⊗ v = (vk ek )(vi,j ej ⊗ ei )                       (7)
                                                                      ∂vi
                                   = vk vi,j δkj ei = vj vi,j ei = vj     ei                 (8)
                                                                      ∂xj
                                     (                                )
                                          ∂v1         ∂v1        ∂v1
                                   = v1          + v2      + v3         e1 + ...             (9)
                                          ∂x1         ∂v2        ∂v3

---

连续介质力学                                                                                 第 7 次课笔记

free index & dummy index

2.1    拉普拉斯算子
      Laplacian (operator)
                               ∂v                1
                                  + v · ∇ ⊗ v = − ∇p + ν∇2 v + g                            (10)
                               ∂t                ρ

                           ρv 2   ρvL   vL
                   Re =         =     =                 [ν] = L2 T−1    < x2 >= 2pt         (11)
                          µv/L     µ     ν
                                        (            ) (       )
                                             ∂            ∂        ∂ ∂          ∂2
                 ∇2 = △ = ∇ · ∇ =               ei    ·      ej =         δij =             (12)
                                            ∂xi          ∂xj      ∂xi ∂xj       ∂x2i

2.2    弹性力学平衡方程

                                                ∇·σ =0                                      (13)
                          (         )
                               ∂                      ∂σij          ∂σij
                                  ek (σij ei ⊗ ej ) =      δki ej =      ej                 (14)
                              ∂xk                     ∂xk           ∂xi
      作业：什么时候 NS 方程中−1/ρ · ∇p项可将系数放入为−∇(p/ρ)

2.3    双缩并与迹

                                 T = Tij ei ⊗ ej          S = Skl ek ⊗ el                   (15)

                                    T : S = Tij Skl δik δjl = Tij Sij                       (16)

                                            A = Alm el ⊗ em                                 (17)

                                 trA = Alm el · em = Alm δlm = All                          (18)

      作业：证明张量 AB 的迹和转置的各种性质。

感谢为本次笔记提供参考的同学：                         无

课程日期：2019 年 3 月 20 日                             <| 2 |>                 最后修改：2019 年 3 月 24 日

---

              连续介质力学                                   第 9 次课笔记
                                                   庄逸

         课程日期：2019 年 3 月 25 日                           最后修改：2019 年 4 月 11 日

                          1       诺特定理（角动量守恒）
    Angular momentum, isotropy, isotropic：各向同性
    infinitesimal rotationδϕ (pseudo vector)

                                  δr = δϕ × r           δv = δϕ × v            (1)

variation of Lagrangian （注意此处 L 表示拉格朗日量）
                              ∑n (                      )
                                   ∂L          ∂L
                         δL =          · δrα +     · δvα = 0                   (2)
                              α=1
                                   ∂rα         ∂vα

∵ L = T − U = mq̇ 2 /2 − U (q), conservative force f = −∇U
                                  ∂L                  ∂L
                                      = pα                = f = ṗα            (3)
                                  ∂vα                 ∂rα
代入Equation 1,Equation 3
                                  ∑
                                  n
                         δL =           [ṗα · (δϕ × rα ) + pα · (δϕ × vα )]   (4)
                                  α=1
                                  ∑n
                              =         [δϕ · (rα × ṗα ) + δϕ · (vα × pα )]   (5)
                                  α=1
                                        ∑
                                        n
                              = δϕ ·          (rα × ṗα + ṙα × pα )           (6)
                                        α=1

                                     d ∑
                                              n
                              = δϕ ·        (rα × pα ) = 0                     (7)
                                     dt α=1

∵ δϕ is arbitrary （注意下面 L 表示角动量）
                                      ∑
                                      n
                                  ∴         (rα × pα ) = L = const             (8)
                                      α=1

---

连续介质力学                                                                                            第 9 次课笔记

                                            2 转动惯量
      recall: moment of inertia, rigid body 注意此处开始斜体 I 表示转动惯量，为二阶张量。

                                                       L = Iω                                           (9)

ω: angular velocity
      contraction, I: identity tensor
      continua (continuum mechanics)
                              ∫                 ∫
                          L = r × (ρv)dV = ρ r × (ω × r)dV                                             (10)
                                ∫
                            = ρ [ω(r · r) − r(r · ω)]dV                                                (11)
                                ∫
                            = ρ ((ωr 2 ) − (r ⊗ r) · ω)dV                                              (12)
                              ( ∫                   )
                            = ρ (r I − r ⊗ r)dV · ω
                                     2
                                                                                                       (13)
                                                   ∫
                                         ∴I=ρ           (r2 I − r ⊗ r)dV                               (14)
                                                   ∫
                                         Iik = ρ       (r2 δik − ri rk )dV                             (15)
                                ∫                                            ∫
                      Ixx = ρ       (x + y + z − x · x)dV = ρ
                                     2      2      2
                                                                                 (y 2 + z 2 )dV        (16)
                                                           ∫
                                             Ixy = −ρ          xydV                                    (17)

In matrix form                                                          
                                                    I    I         Ixz
                                                    xx xy             
                                                   
                                          [Iik ] = Iyx Iyy        Iyz                                (18)
                                                                       
                                                     Izx Izy       Izz

作业：把每个分量写出来，并推导质点系的转动惯量。

2.1    二阶投影张量

                                      fn = (f · n)n = f · (n ⊗ n)                                      (19)

                       fτ = f − fn = f · I − f · (n ⊗ n) = f · (I − n ⊗ n)                             (20)

课程日期：2019 年 3 月 25 日                                   <| 2 |>                     最后修改：2019 年 4 月 11 日

---

连续介质力学                                                                                 第 9 次课笔记

                                  3      双缩并的重要性质

                 A : (BC) = tr(AT (BC)) = tr((AT B)C) = (B T A) : C                         (21)

                                   4      凯莱-哈密顿定理
    caylay-hamilton, 特征多项式零化矩阵本身

                                 XA (λ) = |λI − A|        XA (A) = 0                        (22)

adjoint matrix B = (λI − A)∧ = λ2 B1 + λB2 + B3 , B ∧ B = I |B|

           B(λI − A) = |λI − A| = λ3 B1 + λ2 (B2 − B1 A) + λ(B3 − B2 A) − B3 A              (23)
                                                           = I(λ − λ1 )(λ − λ2 )(λ − λ3 )   (24)

                B1 = I    B2 − B1 A = a1 I       B3 − B2 A = a2 I      − B3 A = a3 I        (25)

                                      0 = A3 + a1 A2 + a2 A + a3 I                          (26)

                 f (A) = a0 I + a1 A + · · · + an An + · · · = b2 A2 + b1 A + b0 I          (27)

任何一个矩阵函数都能用二次以内的矩阵多项式表示。因为这里考虑的矩阵都是三阶的，因此
极小多项式至多为三次。
    作业：整理 C-H 定理
    parallelepiped 平行六面体 [u v w]
    ∀A ∈ Lin Lin:All set of tensors
    作业：查张量的四种定义方式

                                 [Au v w] + [u Av w] + [u v Aw]
                      I1 (A) =                                  = trA                       (28)
                                             [u v w]
                     [Au Av w] + [Au v Aw] + [u Av Aw]  1
          I2 (A) =                                     = (Aii Ajj − Aij Aji )               (29)
                                   [u v w]              2
                                              [Au Av Aw]
                                   I3 (A) =              = |A|                              (30)
                                                [u v w]
作业：为什么可以用 parallelpipied 写成这样的形式？

感谢为本次笔记提供参考的同学：                          无

课程日期：2019 年 3 月 25 日                            <| 3 |>              最后修改：2019 年 4 月 11 日

---

              连续介质力学                                     第 10 次课笔记
                                                    庄逸

           课程日期：2019 年 4 月 1 日                            最后修改：2019 年 4 月 14 日

                                            1 曲线坐标
    或曲纹坐标，curvilinear coordinates. 坐标系 coordinate system.
    直角坐标系，rectangular coordinates, Cartesian coordinates orthogonal.
    坐标线 line of coordinates 都是直线
    曲纹坐标系：至少一个坐标线是曲线。
    triple (x1 , x2 , x3 ), unit bases (e1 , e2 , e3 ), ei · ek = δik
    1637 年，Rene Descartes，《论方法》创立了一套体系，被西方人认为是一套完整的哲学
体系。I think, therefore I am.
    radious vector
                                     r = x1 e1 + x2 e2 + x3 e3 = xi ei                                  (1)

协变基，为矢径对逆变分量求导
                                              ∂r
                                                  ei =                                                  (2)
                                              ∂xi
    1852 年, G. Lamé, spherical surface equations of equilibrium. q 1 , q 2 , q 3 , q i = q i (x1 , x2 , x3 )

    Curvilinear cooedinate (according to Equation 2)
                                                ∂r ∂xk     ∂xk
                                         gi =            =      ek                                      (3)
                                                ∂xk ∂q i   ∂q i

---

连续介质力学                                                                                                第 10 次课笔记

归一化，拉梅系数
                                            √(           )2       (          )2       (          )2
                           gi                    ∂x1                  ∂x2                 ∂x3
                      bi =           Hi =                     +                   +                          (4)
                           Hi                    ∂q i                 ∂q i                ∂q i
（这里没有求和）

Example polar coordinate.

                                x2

                                                    gθ
                                                                  gρ
                                                                         ρ

                                e2

                                                θ
                                          e1                                      x1

                         r = x1 e1 + x2 e2 = ρgρ = ρ cos θe1 + ρ sin θe2                                     (5)
                                        √
                                   ρ = x2 + y 2
                                                                                                             (6)
                                   θ = arctan y = Arg(x, y)
                                                x
Arg: argument.

                   ∂xi    ∂(ρ cos θ)      ∂(ρ sin θ)
               gρ =   ρ
                        =            e1 +            e2 = cos θe1 + sin θe2                                  (7)
                   ∂g        ∂ρ              ∂ρ
                   ∂xi    ∂(ρ cos θ)      ∂(ρ sin θ)
               gθ = θ =              e1 +            e2 = −ρ sin θe1 + ρ cos θe2                             (8)
                   ∂g        ∂θ              ∂θ
Lamé coefficients
                                     √
                            Hρ =         cos2 θ + sin θ2 = 1                 Hθ = ρ                          (9)

                                      1
                                 bρ =    gρ = cos θe1 + sinθ e2                                             (10)
                                      Hρ
                                      1
                                 bθ =    gθ = − sin θe1 + cos θe2                                           (11)
                                      Hθ

课程日期：2019 年 4 月 1 日                             <| 2 |>                            最后修改：2019 年 4 月 14 日

---

连续介质力学                                                                                    第 10 次课笔记

                                 { }             [                     ]{ }
                                  bρ                 cos θ     sin θ     e1
                                             =                                                    (12)
                                    bθ               − sin θ cos θ          e2
bρ · bθ = 1
    velocity in curvilinear coordinates, q i = q i (t)

                                     dr  ∂r dq i
                                v=      = i      = q̇ i gi = q̇ i Hi bi                           (13)
                                     dt  ∂q dt

作业：在极坐标里写成分量。 ρ̇bρ + ρθ̇bθ
    projection of acceleration along bi (注意此处也没有求和)
                                                   dv 1 ∂r         1 dv ∂r
                                             ai =    ·        =                                   (14)
                                                   dt Hi ∂q i     Hi dt ∂q i
                                                     [ (           )           ]
                                                    1 d       ∂r            ∂v
                                                 =        v· i −v· i                              (15)
                                                   Hi dt      ∂q           ∂q
                                                     [ (           )           ]
                             ∂r    ∂v               1 d       ∂v            ∂v
                        (∵        ≡ i)           =        v· i −v· i                              (16)
                             ∂q i  ∂ q̇            Hi dt      ∂ q̇         ∂q

Let T = v 2 /2 = v · v/2                              (                   )
                                         1                d ∂T       ∂T
                                     a = i
                                                                    − i                           (17)
                                         Hi               dt ∂ q̇ i  ∂q

Example polar coordinate
                                          1 2 ρ̇2 + ρ2 θ̇2
                                      T =   |v| =                                                 (18)
                                          2           2
                                        d ∂T      ∂T
                                   aρ =         −    = ρ̈ − ρθ̇2                                  (19)
                                        dt ∂ ρ̇   ∂ρ
                                              1 d 2
                                     aθ =          (ρ θ̇) = 2ρ̇θ̇ + ρθ̈                           (20)
                                              ρ dt
作业：用一年级的方法求加速度

                                             2 度规张量

                                   gij = ġi · gj             gik = gi · g k                      (21)

注：第二式应该是（δik ？）
                                                 ∂r                  ∂r
                                         gi =                 gj =                                (22)
                                                 ∂q i                ∂q j
                                     ds2 = dr · dr = gij dq i dq j                                (23)

课程日期：2019 年 4 月 1 日                                   <| 3 |>                    最后修改：2019 年 4 月 14 日

---

连续介质力学                                                                        第 10 次课笔记

                                 3     惯性坐标系的定义
    inertial coordinate system
                                        ∂L
                                            =0                                        (24)
                                         ∂r
    space is homogeneous & isotropic L = L(v 2 , t)
    time is homogeneous –> L = L(v 2 )
                                         d ∂L        ∂L
                                                  −      =0                           (25)
                                         dt ∂ q̇ α ∂q α
                                                    |{z}
                                                     =0

                                 d ∂L           ∂L
                                           =0 ⇒    = const                            (26)
                                 dt ∂ q̇ α      ∂v
由于 ∂L
   ∂v
      是某个只关于 v 的函数，因此

                                         v = const vector                             (27)

只要是匀速直线运动的坐标系就是惯性坐标系。

                                     4 伽利略变换群

                                     vx = ..., vy = ..., vz = ...                     (28)

t ∈ R,r, v, s ∈ R3

                                        g1 (t, r) = g1 (t, r + vt)                    (29)
                                     g2 (t, r) = g2 (t + τ, r + s)                    (30)
                                           g3 (t, r) = g3 (t, rR)                     (31)

R : 二阶旋转张量
    3+1+3+3：十元伽利略群。

感谢为本次笔记提供参考的同学：                        无

课程日期：2019 年 4 月 1 日                            <| 4 |>               最后修改：2019 年 4 月 14 日

---

           连续介质力学                                第 11 次课笔记
                                               庄逸

        课程日期：2019 年 4 月 2 日                      最后修改：2019 年 4 月 14 日

  Monge 蒙日

                                          1 证明
  注意到 r = r(q1 , q2 , . . . , qn , t)，按照定义，求导得到速度。
                                        dr   ∂r ∑ ∂r dqi
                               v=          =    +                        (1)
                                        dt   ∂t   ∂qi dt

速度对 q̇j 求偏导，得到

                     ∂v       ∂2r      ∑ ∂ 2 r dqi ∑ ∂r ∂
                           =         +               +           q̇i     (2)
                     ∂ q̇j   ∂t∂ q̇j    ∂qi ∂ q̇j dt   ∂qi ∂ q̇j

因为 r 不显含 q̇j ，因此前两项均为零。最后，因为 q̇1 , q̇2 . . . 也互不相关，最后一项的求和只
有在 i = j 时不为零。
                         ∂v      ∑ ∂r ∂                ∂r ∂ q̇j    ∂r
                               =             q̇i δij =           =       (3)
                         ∂ q̇j     ∂qi ∂ q̇j           ∂qj ∂ q̇j   ∂qj

                                   2 第一性原理
  First principles

                                                 dp
                                           F =                           (4)
                                                 dt
  Hamilton’s principle
                                  ∫ t2
                                                 d ∂L       ∂L
                         δS = δ          Ldt              −     =0       (5)
                                   t1            dt ∂ q̇ α ∂q α

  Virtual work principle, virtual displacement principle

---

连续介质力学                                                                                                    第 11 次课笔记

     Real displacement
                                                                  ∂r      ∑n
                                                                              ∂r i
                                  dri (q 1 , . . . , q n , t) =      dt +          dq                            (6)
                                                                  ∂t      i=1
                                                                              ∂q i
q 1 , . . . , q n : generalized coordinates
     virtual displacement
                                                            ∑ ∂r
                                                  δri =                    δq i                                  (7)
                                                                    ∂q i
实质就是等时变分，isochronous variation.

                                                 3 虚功原理

                                                     ∑
                                                           Fi · δri = 0                                          (8)
                                                      i

代入力的分类，作用力 (applied) 和约束力 (constrained).
                                                              (a)              (c)
                                                  Fi = Fi           + fi                                         (9)

得到
                                         ∑         (a)       (c)      ∂r
                                               (Fi        + fi ) ·        δqi = 0                               (10)
                                           i
                                                                      ∂qi
理想约束：约束反力虚功为零。
       ∑ (c) ∂r                                                     (a)        ∂r        ∑
          fi ·     δqi = 0                               Qi = Fi           ·         ∴       Qi δqi = 0         (11)
        i
               ∂qi                                                             ∂qi

把上面的式子代入
                                                             dp
                                                     F−         =0                                              (12)
                                                             dt
得到，
                                 ∑ ( (a)       d2 r
                                                    )
                                                        ∂ri
                                      Fi − m 2 ·             δqi = 0                                            (13)
                                  i
                                               dt       ∂qi
                                 ∑(           d2 r ∂ri
                                                         )
                                      Qi − m 2 ·            δqi = 0                                             (14)
                                              dt     ∂qi
                                                            (           )
                                         d2 r ∂ri        d        ∂r           d ∂r
                                        m 2 ·        =        mv          − mv                                  (15)
                                          dt    ∂qi      dt        ∂q          dt ∂q
                                                            (           )
                                                         d        ∂v           ∂v
                                                     =        mv          − mv                                  (16)
                                                         dt        ∂ q̇        ∂q
                                                         d ∂T       ∂T
                   (∵ kinetic energy T = mv 2 /2) =              −                                              (17)
                                                         dt ∂ q̇    ∂q

课程日期：2019 年 4 月 2 日                                        <| 2 |>                       最后修改：2019 年 4 月 14 日

---

连续介质力学                                                                                      第 11 次课笔记

令 Q = − ∂V
        ∂q
           ,L = T − V
                                     d ∂(T − V ) ∂(T − V )
                                                −          =0                                     (18)
                                     dt   ∂ q̇      ∂q
D’Almbert’s principle.
    虚速度原理，虚加速度原理。

                                 4     张量的现代数学观点
    modern mathematics point of view

                                            f : (V )r × (V ∗ )s                                   (19)
                                                              ∗  ∗
                 | ×V ×
V : vector space V    {z· · · × V}         V ∗ : dual space V      × · · · × V }∗
                                                            | × V {z
                          r                                               s
    位移和力组成对偶空间。
    Catesian product, direct product 笛卡儿积，直积
    Two set X & Y, ordered pair

                                  X × Y = {(x, y)|x ∈ X ∧ y ∈ Y }                                 (20)

    f 是 r + s 重线性映射
                                             T = Tik ei ⊗ ek                                      (21)
                       T = Tik11i2k...i   e ⊗ ei2 ⊗ · · · ⊗ eir ⊗ ej1 ⊗ · · · ⊗ ejs
                                   2 ...ks i1
                                       r
                                                                                                  (22)
    这个张量称为 (r, s) 型，有 r + s 阶，(0, 0) 型 scalar, (1, 0) 型为 ai ei , (0, 1) 型为 bi ei
    作业：写 (1,1),(2,0),(0,2) 类型的张量

                                               trA = I : A                                        (23)
                                       trA2 = I : A2 = AT : A                                     (24)
作业：P86 三缩并
    多重线性是张量的本质, linear map. u ∈ V, v ∈ W, c ∈ K K is a field.

                              f (u + v) = f (u) + f (v)         f (cu) = c(u)                     (25)

homogeneous function of degree 1.

              f (c1 u1 + c2 u2 + · · · + cn un ) = c1 f (u1 ) + c2 f (u2 ) + · · · + cn f (un )   (26)

课程日期：2019 年 4 月 2 日                              <| 3 |>                  最后修改：2019 年 4 月 14 日

---

连续介质力学                                       第 11 次课笔记

感谢为本次笔记提供参考的同学：       无

课程日期：2019 年 4 月 2 日       <| 4 |>   最后修改：2019 年 4 月 14 日

---

           连续介质力学                      第 12 次课笔记
                                   庄逸

         课程日期：2019 年 4 月 3 日             最后修改：2019 年 4 月 14 日

                            1 黎曼度规
1.1    如何获取坐标——逆变基和协变基
                                                  ，
      现在我们的坐标系是笛卡尔斜角坐标系，以二维情况为例，假设我们有基底 g1 , g2（画图）
则一个向量能够进行分解
                             v = v 1 g1 + v 2 g2                (1)

为什么写成上标之后再解释。
      然后我们想要得到这个向量的分量坐标，也就是 v 1 , v 2 。
      想想在笛卡尔直角坐标系中我们的做法：

                              u = ux i + uy j                   (2)

要得到 ux ，我们只需要运算 u · i，因为 i · i = 1, i · j = 0，剩下的自然只有 ux 。
      因此，在斜角坐标系中我们也会想进行运算，结果却得到

                          v · g1 = v 1 + v 2 cos ϕ              (3)

其中 ϕ 是两个基底的夹角。这样就不能方便地得到坐标。为了解决这个问题，我们引入另外两
个向量 g 1 , g 2 ，使得

                        g 1 · g1 = 1      g 1 · g2 = 0          (4)
                        g 2 · g1 = 0      g 2 · g2 = 1          (5)

或者可以简记为
                                gi · g j = δij                  (6)

这个是容易实现的。（Figure 1）

---

连续介质力学                                                                                   第 12 次课笔记

                                        g1
                                                    g2

                                                                   g1

                                                         g2

                                       图 1: 逆变基与协变基

      我们把 g1 , g2 称为协变基，g 1 , g 2 称为逆变基。v 1 , v 2 称为逆变分量。
      显然，我们还有协变分量，因为逆变基也是一组基。

                                             v = v1 g 1 + v2 g 2                                 (7)

因此为了区分协变与逆变分量，并且遵从指标位置规则，就把逆变分量的脚标写成上标。
      这些在三维中可以类似推广。之后在三维中讨论，并且采用爱因斯坦求和约定。

1.2    如何得到曲线微元
      现在考虑长度微元
                                              ds2 = dr · dr                                      (8)

其中 dr = ri gi ，于是

            ds2 = dr · dr = (dri gi ) · (drj g j ) = dri drj gi · g j = dri drj δij = dri dri    (9)

然而，这里的 ri 和 ri 分别是逆变分量和协变分量，就是说这不在一个坐标系中，不好处理。
那么试试在同一个坐标系中求

                        ds2 = dr · dr = (dri gi ) · (drj gj ) = dri drj gi · gj                 (10)

其中出现了 gi · gj 因子，我们直接设其值为 gij ，其张成一个矩阵，称为度量张量的协变分量。
由定义可知这是一个对称矩阵。于是现在曲线长度微分可表示为

                                             ds2 = dri drj gij                                  (11)

课程日期：2019 年 4 月 3 日                               <| 2 |>               最后修改：2019 年 4 月 14 日

---

连续介质力学                                                                       第 12 次课笔记

      事实上，这个量的重要之处还在于它联系着逆变基和协变基。尝试用协变基线性表示逆变
基，设一个系数
                                        gi = hij g j                                 (12)
在上式两端点乘 gk ，得到
                           gi · gk = hij g j · gk = hij δkj = hik                    (13)
可见 h 就是 g。
      另有张量被称为“度量张量的逆变分量”，具体的运算性质都是对称类似的。

1.3   几个例子
欧几里得度量（例 15.1） 欧几里得空间中，ds2 = dx2 + dy 2 + dz 2 ，如果把三个方向的基向
量作为协变基，即 gi = i, j, k，则由于相互垂直，相应的矩阵 gij 为单位矩阵。
                   
              1 0 0
                   
      gij = 
            0 1 0 
                       ds2 = dxi dxj gij = (dxi )2 = dx2 + dy 2 + dz 2              (14)
                  0 0 1

坐标变换的度量（基于例 15.5）                在欧几里得空间的基础上，作变换

                          u = x + 2y       v =x−y              w=z                   (15)

相比原坐标系，新坐标系经历了缩放，两轴也不再垂直，故不能直接用 du2 + dv 2 + dw2 直接
计算长度，而需要用度规。下面算度规张量的协变分量。
      我们已经知道
                                 ds2 = dx2 + dy 2 + dz 2                             (16)
因此考虑作逆变换，将 xyz 换为 uvw。简单计算得到

                      x = (u + 2v)/3       y = (u − v)/3         z=w                 (17)

于是
                                 2 2 2        5
                         ds2 =     du + dudv + dv 2 + dw2                            (18)
                                 9     9      9
利用二次型的表示
                           ds2 = (du dv dw)gij (du dv dw)t                           (19)
可以写出度规张量                                                  
                                           2      1
                                                       0
                                         9       9     
                                   gij = 
                                         9
                                           1      5
                                                  9
                                                       0
                                                                                    (20)
                                              0   0    1

课程日期：2019 年 4 月 3 日                      <| 3 |>                    最后修改：2019 年 4 月 14 日

---

连续介质力学                                                               第 12 次课笔记

      下面我们来计算一个具体的长度。考虑在 xyz 坐标系中，线段 l : (3, −1, 4) → (5, 0, 2) 显
然它的长度是
                          √
                     L=    (5 − 3)2 + (0 − (−1))2 + (2 − 4)2 = 3            (21)

相对应地，在 uvw 坐标系中，它可以对应地表示成 l : (1, 4, 4) → (5, 5, 2)。我们用积分来算。
      首先先写出直线的参数方程

                     u = 1 + 4t v = 4 + t   w = 4 − 2t t ∈ [0, 1]           (22)

然后积分算长度，注意 ds 此时带着度量张量
            ∫       ∫ √         ∫ √
        L = ds =        ds =2         dxi dxj gij                           (23)
            ∫ √
                 2 2 2              5
          =        du + dudv + dv 2 + dw2                                   (24)
                 9       9          9
                √ ( )                         ( )2 (         )2
            ∫ 1            2
                  2 du          2 du dv 5 dv              dw
          =                   +         +             +         dt          (25)
             0    9 dt          9 dt dt    9 dt           dt
            ∫ 1√                                  ∫ 1
                  2          2        5
          =         × 16 + × 4 + + 4 dt =             3dt = 3               (26)
             0    9          9        9            0

      算出的长度相同。

1.4    总结
      顾名思义，度规就是一把尺子。在简单的欧几里得空间中，因为三个基向量具有很好的例
如互相垂直的性质，度规成为单位矩阵，所以计算长度时不需要考虑度规。但是更重要的原因
应该是：现在计算的距离就是在欧几里得空间中简单定义的。
      而在一般的坐标系中计算“在欧几里得空间中定义的距离”，甚至是由度规本身定义的距
离，就需要使用度规，因为此时只有度规才能告诉你在新坐标系中，1 个单位长度等于多少“距
离”。考虑上面的例子，如果在新坐标系中直线被扭成了曲线，仍然可以用类似的方法计算。设
想把曲线划成无数多个 ds，然后拿着尺子去一段一段量。这个尺子就是度规，能告诉你这一
小段应该算多少距离，最后将它们加起来。这就是得出总长度的线积分过程，可以看出度规的
名字是很形象的。
      在上面的例子中，我们先由坐标变换得出了线微元的展开式，然后得到度规，在计算长度
时又将度规代回去得到线微元展开式进行计算。乍看起来求度规有点累赘，但是其实这二者可
以说是等价的，而度规不包含装饰性的微元 dx，能集中反映空间和距离的性质，并且作为一
个张量，和许多量有联系，因此度规本身更有研究的价值。

课程日期：2019 年 4 月 3 日                    <| 4 |>             最后修改：2019 年 4 月 14 日

---

连续介质力学                                                                            第 12 次课笔记

1.5    参考
      赵老师的《理性力学教程》和黄克智《张量分析》

                                          2 球量和偏量
      Cartesian product 笛卡儿积，direct product（直积）
      Newtonian mechanics, Newton’s principle of determinacy

                                   x0 ∈ R3n         ẋ0 ∈ R3n      t∈R                    (27)

R3n × R3n × R → R3n
      spherical devitoric tensor

               1         1           1          1
                 (trA)I = (I : A)I = I(I : A) = (I ⊗ I) : A
                     αI =                                                                 (28)
               3         3           3          3
                           1                  1
       devA = A − αI = A − (I ⊗ I) : A = (I − I ⊗ I) : A = P : A                          (29)
                           3                  3
和二阶投影张量相比。Fτ = F (I − n ⊗ n)
      四阶单位张量 4th order identity tensor

                                       I = δik δjl ei ⊗ ej ⊗ ek ⊗ el                      (30)

口诀：1324（ikjl）。
      和单位矩阵的并矢相区分：（指标 1234）

                                    I ⊗ I = δij δkl ei ⊗ ej ⊗ ek ⊗ el                     (31)

                            I : I = (δik δjl ei ⊗ ej ⊗ ek ⊗ el ) : (δpq ep eq )           (32)
                                   = δik δjl δkp δlq δpq ei ⊗ ej                          (33)
                                   = δip δjq δpq ei ej                                    (34)
                                   = δij ei ⊗ ej                                          (35)

作业：算四阶单位张量和二阶张量的双点积 (P123)，算柯西应力张量
      stress measure 应力度量, strain measure 应变度量

感谢为本次笔记提供参考的同学：                            无

课程日期：2019 年 4 月 3 日                                <| 5 |>               最后修改：2019 年 4 月 14 日

---

            连续介质力学                                第 13 次课笔记
                                              庄逸

         课程日期：2019 年 4 月 8 日                        最后修改：2019 年 4 月 28 日

                                  1 勒让德变换
    Legendre transformation
                                     ∑
                                     n
                               H=          pi q̇i − L                      (1)
                                     i=1
                                     ∑n
                                         ∂T
                                 =             q̇i − L                     (2)
                                     i=1
                                         ∂ q̇i

                                 = 2T − L = 2T − (T − V )                  (3)
                                 =T +V =E                                  (4)

Euler homogeneous function
                                                               1 2
                              f (αu) = αf (u),           T =     mq̇       (5)
                                                               2

                                  2 狄拉克符号
    ⟨态 2|态 1⟩，从右往左读。
          ⟨           ⟩
  1. 拆分：左矢 态 2 和右矢 态 1 。

  2. 组分：⟨3|2⟩, ⟨2|1⟩。

  3. 跳转：⟨2| Q |1⟩。

  4. 前后变换取复数共轭：⟨2|1⟩ = ⟨1|2⟩∗

---

连续介质力学                                                                                                      第 13 次课笔记

证明：
                               ∗
                    ⟨A| = |A⟩               |A⟩ = (a1 , . . . , an )t          ⟨A| = (a∗1 , . . . , a∗n )          (6)
                                   ∗
                            |A⟩ = (a1 , . . . , an )t∗ = (a∗1 , . . . , a∗n ) = ⟨A|                                (7)
                                                                                   ∑
                                                                                   n
                           ⟨B |A⟩ = (b∗1 , . . . , b∗n )(a1 , . . . , an )t =             b∗i ai                   (8)
                                                                                    i=1

                                        ∗
                                                ∑
                                                n                    ∑
                                                                     n
                            ⟨B |A⟩ = (                 b∗i ai )∗ =         a∗i bi = ⟨A| B⟩                         (9)
                                                 i=1                 i=1

bracket:bra-ket
    应用：应力集中（裂尖）、奇点
    作业：N-S 方程（薛定谔方程?）用狄拉克符号写

                                                ~2 2              ∂Ψ
                                            −      ∇ Ψ + V Ψ = i~                                                 (10)
                                                2m                ∂t

                                                   3 谱定理
    3x3 (3 by 3) matrix S, eigenvalue and eigenvector, diagonal, diagonized
    美国最主流的连续介质力学教材：Gurtin M E. An Introduction to continuum mechanics
    Spectral theorem
                                        Se = we ⇒ (S − wI)e = 0                                                   (11)

I: identity tensor of rank two
    nontrivil solution if and only if(iff)

                                       S11 − ω           S12            S13
                                         S21           S22 − ω          S23       =0                              (12)
                                         S31             S32         S33 − ω

characteristic equation ω 3 − I1 ω 2 + I2 ω − I3 = 0, three distinct eigenvalues ω1 ̸= ω2 ̸= ω3 ̸= 0;
two distinct eigenvalues ω1 , ω2 = ω3 .
    Spectral theorem: let S be symmetric. Then thesis on orthonormal basis for V (vector
space) consisting entirely of eigenvectors of S. Moreover, for any such basis e1 , e2 , e3 , the
corresponding eigenvalues ω1 , ω2 , ω3 , when ordered, form the entire spectrum of S，abd(?)
                                                         ∑
                                                 S=            ωi ei ⊗ ei                                         (13)

课程日期：2019 年 4 月 8 日                                      <| 2 |>                       最后修改：2019 年 4 月 28 日

---

连续介质力学                                                                 第 13 次课笔记

                                  4 矩阵的不变量
   principle invariants

                            I1 = trS = I : S = Sii = ω1 + ω2 + ω3              (14)
                  1 2
                    (tr S − trS 2 ) = ω1 ω2 + ω2 ω3 + ω3 ω1
                          I2 =                                                 (15)
                  2
                 1
             I3 = (tr3 S − 3trS trS 2 + 2trS 3 ) = ω1 ω2 ω3                    (16)
                 6
作业：P92 中间，把矩阵写成谱定理的形式
   主应力 T n = σn
   作业：理解 13-10

                                     5 黑森算子
   见书 P95-97
   作业：由 14-13 推 14-14

感谢为本次笔记提供参考的同学：                     无

课程日期：2019 年 4 月 8 日                       <| 3 |>             最后修改：2019 年 4 月 28 日

---

              连续介质力学                            第 14 次课笔记
                                               庄逸

            课程日期：2019 年 4 月 10 日                    最后修改：2019 年 4 月 14 日

    主方向和主应力
                                          Se = ωe                                        (1)

e : unit vector

                           1    Square root theorem
    如果 C 可以进行谱分解，又是 U 的平方
                                               ∑
                                  C = U2 =          ωi ei ⊗ ei                           (2)
                                                i

则
                                          ∑√
                                     U=         ωi ei ⊗ ei                               (3)
                                           i

                    2    Polar decomposition theorem
    There exist positive definite, symmetrical tensors U and V , and a rotation R, such that
(左极分解和右极分解)
                                      F = RU = V R                                       (4)

Moreover, each of these decompositions is unique: in fact
                                     √                    √
                                U=       FTF        V =       FFT                        (5)

Proof.(1)
                           ∵ F = RU        F T = U T RT = U R−1                          (6)

                               ∴ F T F = C = U R−1 RU = U 2                              (7)

---

连续介质力学                                                                                    第 14 次课笔记

类似可证另一个。
      为什么 IT : A = AT ，并且是 2314

      (δjk δil ei ⊗ ej ⊗ ek ⊗ el ) : (Apq ep ⊗ eq ) = δjk δil δkp δlq Apq ei ⊗ ej = Aji ei ⊗ ej = AT    (8)

                                            3 黎曼度规

                                           ẍi + Γikl ẋk ẋl = F i /m                                  (9)
                                              D    d
                                                 =    + Γvv                                            (10)
                                              Dt   dt
作业：看 19-20 讲
      作业：找到黎曼度规张量和拉梅系数的关系（开方？）

3.1     克里斯托费尔符号
      (参考第 16 节 P108)
      协变基 ı̂1 , ı̂2 , ı̂3 ，逆变坐标 x̃1 , x̃2 , x̃3 。在位置 r 基矢为 g1 , g2 , g3 ，其中
                                   ∂r    ∂r ∂ x̃p         ∂ x̃p
                            gi =       =           = ı̂ p                xi = xi (x̃p )
                                   ∂xi   ∂ x̃p ∂xi        ∂xi
      2nd kind Christoff symbol.
                  ∂gj
                      = Γkij gk               (11)
                  ∂xi
对于平直的笛卡儿坐标系而言，为零；但对 Curvilinear 而言不为零。因此克里斯托弗符号不
是张量，因为它在坐标变换下会改变。
      由于 gj = ∂x
              ∂r
                 j
                                             (         )
                                ∂gj    ∂         ∂r             ∂2r       ∂2r
                                    =                      =           =                               (12)
                                ∂xi   ∂xi        ∂xj           ∂xi ∂xj   ∂xj ∂xi
于是 Γkij = Γkji ，是对称的。
      对于非对称三阶张量，共有 33 = 27 个自由度。对于对称的而言，只有 18 个
      作业：证明三阶 n 维对称张量自由度为

                                                  N 2 (N + 1)
                                                                                                       (13)
                                                       2
      逆变基矢量对坐标导数例 16.3
                                               ∂g i
                                                    = −Γijp g p                                        (14)
                                               ∂xj

课程日期：2019 年 4 月 10 日                               <| 2 |>                     最后修改：2019 年 4 月 14 日

---

连续介质力学                                                                    第 14 次课笔记

3.2   加速度

                                      u = ui gi                                    (15)
               i              j       i
                                                         (     i
                                                                            )
       du   du        ∂gm dx   du                            du
          =    gi + um j     =                 i
                                  gi + um v j Γjm gi =          + um v j Γijm gi   (16)
       dt   dt        ∂x dt    dt                            dt
                      Dui
                                          =                                        (17)
                      Dt
（注：按照定义，下标应该是 mj，但是由于是对称的所以没关系。

感谢为本次笔记提供参考的同学：                   无

课程日期：2019 年 4 月 10 日                  <| 3 |>            最后修改：2019 年 4 月 14 日

---

              连续介质力学                           第 15 次课笔记
                                            庄逸

           课程日期：2019 年 4 月 15 日                  最后修改：2019 年 4 月 28 日

                                   1 黑洞无毛定理
      Black hole no-hair theorem (S. Hawkin, 1972)
      hair : complicated informations
      almost no-hair, 3 hairs ：mass, angular momentum, electric charge

                               2   张量标量函数的微分
      scalar-valued function
      strain energy 应变能, extensive quantity w = w(E)，应变能求导能得到应力。

2.1 Banach Space
  （类比社会 = 人群 + 关系）
      Topological space » Metric space (distance) » normed vector space » inner product » Rn
      范数: norm        完备性: completeness
      Banach Space ：完备赋范向量空间
      Soblev Space
      内积：⟨A, B⟩ = |A| |B| cos θ

2.2    一些符号
                (A)
      f (A), ∂f∂A   derivative, 导数。写成偏导的原因是 A 有很多分量。
      Tensor of rank two.

---

连续介质力学                                                                                   第 15 次课笔记

  1. Lin : the set of all tensors. Multi-linearity, linear map

                      f (α1 u1 + α2 u2 + · · · + αn un ) = α1 f (u1 ) + · · · + αn f (un )      (1)

  2. Lin+ : the set of all tensors with detA >0

  3. Sym : Symmetrical tensors

  4. PSym : Symmetrical, positive-definite

  5. orth ：orthogonal tensors. Q−1 = QT

  6. orth+ : rotation det(QQT ) = detQ2 = 1

2.3    矩阵的不变量
      Taylor expansion ∀A, B ∈ Lin, infinitesimal ε ∈ R
                                                     ∂f
                          f (A + αB) = f (A) +          : (αB) + o(α2 B 2 )                     (2)
                                                     ∂A
                   ∂f (A)           f (A + αB) − f (A)   df (A + αB)
                          : B = lim                    =                                        (3)
                    ∂A          α→0         α                 dα     α=0

      ∀A ∈ Lin, characteristic equation 特征方程

                          A11 − ω       A12         A13
             |A − ωI| =     A21      A22 − ω        A23     = −ω 3 + I1 ω 2 − I2 ω + I3 = 0     (4)
                            A31         A32       A33 − ω
      I1 = trA = Aii = I : A = ω1 + ω2 + ω3
                          ∂(trA)           I : (A + εB) − I : A
                                 : B = lim                      =I:B                            (5)
                           ∂A          ε→0           ε
                                                ∂(trA)
                                              ∴         =I                                      (6)
                                                  ∂A
      I2 = 21 [tr2 A − tr(A2 )] = ω1 ω2 + ω1 ω3 + ω2 ω3

                                       ∂(trA)2          ∂trA
                                               = 2(trA)                                         (7)
                                         ∂A              ∂A

课程日期：2019 年 4 月 15 日                              <| 2 |>               最后修改：2019 年 4 月 28 日

---

连续介质力学                                                                                  第 15 次课笔记

                ∂tr(A2 )           I : (A + hB)2 − I : A2
                         : B = lim                                                             (8)
                  ∂A           h→0            h
                                   I : (A2 + hAB + hBA + h2 B 2 ) − I : A2
                             = lim                                                             (9)
                               h→0                     h
                                   I : (h(AB + BA)) + h2 I : B 2
                             = lim                                                            (10)
                               h→0               h
                                   = I : (AB + BA) = I : (AB) + I : (BA)                      (11)
                                        T
                                   = 2A : B                                                   (12)

注意 (A + hB)2 的展开。最后利用了关系式

                                  A : (BC) = (B T A) : C = (AC)T : B                          (13)
                 n            3
作业：计算 ∂(trA)
        ∂A
             和 ∂trA
                ∂A
     I3 = detA = ω1 ω2 ω3
   parallelpiped volume [u v w] = (u × v) · w
   ∀A ∈ Lin, I3 = detA
   考虑性质 det(AB) = det A det B，det(εA) = ε3 det A
                              ∂(detA)           det(A + εB) − detA
                                      : B = lim                                               (14)
                                ∂A          ε→0          ε
其中
            det(A + εB) = det[εA(ε−1 I + A−1 B)] = ε3 det A det(ε−1 I + A−1 B)                (15)
于是
                      ∂(detA)           ε3 det A det(ε−1 I + A−1 B) − det A
                              : B = lim                                                       (16)
                        ∂A          ε→0                    ε
再利用Equation 4

                     det(A−1 B + ε−1 I) = ε−3 + I1 (A−1 B)ε−2 + I2 ()ε−1 + I3 ()              (17)

                     ∂(detA)           ε(det A)I1 (A−1 B) + ε2 (. . . ) + ε3 (. . . )
                             : B = lim                                                        (18)
                       ∂A          ε→0                   ε
                                                 −1
                                 = (det A)(I : (A B))                                         (19)
                                                   −T
                                     = (det A)(A        : B)                                  (20)
                                            ∂(detA)
                                       ∴            = (det A)A−T                              (21)
                                              ∂A

感谢为本次笔记提供参考的同学：                             无

课程日期：2019 年 4 月 15 日                             <| 3 |>               最后修改：2019 年 4 月 28 日

---

         连续介质力学                                第 16 次课笔记
                                            庄逸

     课程日期：2019 年 4 月 17 日                         最后修改：2019 年 4 月 28 日

                                        1 复习
principal stress
复习转动惯量，L = mv × r = m(ω × r) × r
复习四阶投影张量。α = tr/3 = I : A/3, devA = A − αI

                                      ˙    d
                                     A−1 = (A−1 )                        (1)
                                           dt
                                        ˙
                                     A−1 A = İ = 0                      (2)
                                     ˙
                                  ∴ A−1 A + A−1 Ȧ = 0                   (3)
                 ˙
              ∴ A−1 = −A−1 ȦA−1                                         (4)
                             ∑      ∑      ∑
应力方向和大小的特性：满足静力平衡条件，即          Fx =   Fy =   MO = 0
Lin, Lin+ → det A > 0
Sym, Psym positive definite
Orthogonal Q−1 = QT , det QQT = det I = 1 orth+ → det Q > 0
复习左极分解和右极分解。

                              2      克里斯托费符号
期中考题：怎么在曲线坐标系中写运动方程？（16-18)

                                     Dv i   dv i
                              ai =        =      + v m v k Γimk          (5)
                                     Dt     dt
configuration space 位形空间

---

连续介质力学                                                                              第 16 次课笔记

   补充例 16.4
                                                   dq µ dq ν
                                        L = gµν                                            (6)
                                                    dλ dλ
                                         ν          µ
                    ∂L             µk dq         dq              dg ν        dg µ
                           = gµν δ         + gµν      δνk =  gkν      + g µk               (7)
                    ∂ q̇ k            dλ         dλ              dλ          dλ
   Curvature 有了曲率，物体就要运动。时空的弯曲告诉物体如何运动，物体告诉时空如何
弯曲。

                                       3 两种构型
   t = 0 undeformed configuration, initial configuration 初始构形, reference configuration 参
考构型.
  “清华的学生都用‘型’，当我年轻的时候我也用‘型’，现在我坚定地用‘形’。”
   t = t current configuration 当前构形，即时构形
   x : current configuration; X : reference

                                           x = χ(X, t)                                     (8)
                                                            ∂x
                     dx = χ(X + dX, t) − χ(X, t) =             dX = F dX                   (9)
                                                            ∂X

3.1 two-point tensor
   x is current, X is reference.

                                               ∂xi
                                      Fik =        ei ⊗ eK                                (10)
                                              ∂XK
要区分参考构形和当前构形大小写。
   deformation gradient

感谢为本次笔记提供参考的同学：                       无

课程日期：2019 年 4 月 17 日                          <| 2 |>                 最后修改：2019 年 4 月 28 日

---

             连续介质力学                              第 17 次课笔记
                                           庄逸

         课程日期：2019 年 4 月 22 日                    最后修改：2019 年 4 月 24 日

                                       1 运动学
    Kinematics. 区别于 dynamics, kinetics (复习 Bogliubov 的尺度理论)
    固定坐标系 fixed / absolute.
    物质流形 material maniform 流形 continuous media, mechanics of material manifold (M 3 )
         ∑
E3 × R →
    configuration (t = 0 , reference / initial / undeformed configuration, K(X))
    (t = τ , current / deformed configuration)
    bijective 双射，deformation function x = χ(X), X = χ−1 x

                               dx = χ(X + dX, t) − χ(X, t)                           (1)
                                    ∂x
                                  =    dX = F dX                                     (2)
                                    ∂X
                               dx = F dX = dXF T                                     (3)

F is a two-point tensor
                                       ∂x    ∂xi
                                 F =      =      ei ⊗ eK                             (4)
                                       ∂X   ∂XK
                                            ∂xi
                                    FT =        eK ⊗ ei                              (5)
                                           ∂XK
    polar decomposition F ∈ Lin, U , V ∈ Psym , R ∈ orth+ is a rotation.
    F = RU = V R
    P176 切映射场 F (X) : T → τ (?), X ∈ K(B), B : material manifold.
    ∀A ∈ Lin 1st kind, Lagrangian. 2nd kind, Eularian. 3rd king, Mixed (two-point)

---

连续介质力学                                                                 第 17 次课笔记

    (F T F 消除中间两个基后剩余两个基都在参考构形中，因此称为拉格朗日型，可以通过大
小写简单判断。)
         (              )(             )
           ∂xj              ∂xi           ∂xj ∂xi                  ∂xi ∂xi
     T
C=F F =         eA ⊗ ej         ei ⊗ eK =           δij eA ⊗ eK =          eA ⊗ eK
           ∂XA             ∂XK            ∂XA ∂XK                 ∂XA ∂XK
         (              )(             )                                         (6)
            ∂xi             ∂xl             ∂xi ∂xl                  ∂xi ∂xl
       T
B = FF =        ei ⊗ eK         eM ⊗ el =            δKM ei ⊗ el =           ei ⊗ el
           ∂XK             ∂XM             ∂XK ∂XM                  ∂XK ∂XK
                                                                                 (7)
可能是期中考题：证明 c ∈ Psym
    作业：例 26.3, 26.4
    主伸长 λγ = λΓ （书 P180）

                       2     Four definition of Strain
    strain measure, stress measure.

2.1 Green strain
  （现长平方-原长平方）/2 原长平方

                           dx2 − dX 2 = F dX · F dX − dX · dX                    (8)
                                       = dX(F F )dX − dxIdX
                                               T
                                                                                 (9)
                                       = dX(F F − I)dX
                                               T
                                                                                (10)
                                       = dX(2E)dX                               (11)
                                       = dX 2 2E T                              (12)

                                      1 T          1
                              ET =      (F F − I) = (C − I)                     (13)
                                      2            2
为对称矩阵，因此
                                      1 T          1
                               E=       (F F − I) = (C − I)                     (14)
                                      2            2
作业/可能是期末考题，可参考 P252

                                         ∂ω    ∂ω
                                            =2                                  (15)
                                         ∂E    ∂C

课程日期：2019 年 4 月 22 日                       <| 2 |>            最后修改：2019 年 4 月 24 日

---

连续介质力学                                                                    第 17 次课笔记

2.2 Almansi strain
  （现长平方-原长平方）/2 现长平方

                         dx2 − dX 2 = dx · dx − F −1 dxF −1 dx                  (16)
                                        = dxIdx − dxF −T F −1 dx                (17)
                                        = dx(2e)dx                              (18)

同理，
                                         1
                                   e=      (I − F −T F −1 )                     (19)
                                         2

2.3 Logarithmic strain
   infinitesimal
                                  ∫ l
                        dl           dl     l                  ε2
                   de =    → e=         = ln = ln(1 + ε) = ε −    + ...         (20)
                         l         L l      L                  2

2.4 Cauchy strain

                                             ∆l   l−L
                                        ε=      =                               (21)
                                             L     L

感谢为本次笔记提供参考的同学：                    无

课程日期：2019 年 4 月 22 日                         <| 3 |>          最后修改：2019 年 4 月 24 日

---

             连续介质力学                 第 18 次课笔记
                                  庄逸

        课程日期：2019 年 4 月 24 日            最后修改：2019 年 4 月 28 日

   (53-8)
               1                  1
                 (v ⊗ ∇ + ∇ ⊗ v) = ((∇ ⊗ v)T + ∇ ⊗ v)
                 S=                                            (1)
               2                  2
作业：用矩阵形式表示 12-24
   书 P180-182
   Linear elastic 线弹性：忽略掉二阶项。
   (27-25)

                        1 Theory of elastic
   elasticity 弹性力学    plasticity 塑性力学
   作业：例 27.5，27.6

感谢为本次笔记提供参考的同学：             无

---

             连续介质力学                                第 19 次课笔记
                                               庄逸

           课程日期：2019 年 5 月 6 日                       最后修改：2019 年 5 月 6 日

                                           1 复习
1.1 almansi strain
      Dirac symbol
                            (current length)2 − (original length)2
                                                                                     (1)
                                      2(current length)2

                     ⟨dx|dx⟩ − ⟨dX|dX⟩ = ⟨dx|dx⟩ − ⟨F −1 dx|F −1 dx⟩                 (2)
                                             = ⟨dx|dx⟩ − ⟨dxF −T |F −1 dx⟩           (3)
                                                            −T     −1
                                            = ⟨dx|I − F F |dx⟩                       (4)
                                              1
                                        ∴ e = (I − F −T F −1 )                       (5)
                                              2

1.2    测地线方程

                                     d2 q r        dq µ dq ν
                                            + Γrµν           =0                      (6)
                                     dλ  2         dλ dλ
λ: proper time τ , q - generalized coordinate, r - free index, µ, ν - dummy index.
                                        d2 q r
                                    m          + Γrµν · · · = ma                     (7)
                                        dτ 2

1.3 Basics
  1. Neother’s theorem, field equations.

  2. superposition → Linear → Taylor expension (1st)

  3. Dimensional analysis, (rough) order-of-magnitude estimate.

---

连续介质力学                                                                       第 19 次课笔记

                              2 Dimensional analysis
      model, prototype, dimension number
      fine structure const, α = e2 /4επ~c, c : speed of light.
      作业：有一张有名的图片，杨振宁和李政道的老师 Enrico Fermi 在上课时把精细结构参
数写成了~2 /ec
      Lederman, Rabi

2.1 foundamental and derived
      physical quantitles: foundamental (M, L, T, I, Θ, N, J) / derived
                                                    m 1 m2
                                           F = −G          r̂                         (8)
                                                     r2
inverse square rule.
      Point sorce, area of surface 4πr2
      In Rn , F ∝ r−(n−1)

2.2 intensive and extensive
      intensive ρ, T, . . .
      extensive m, S, V

2.3     量纲
      universal, primary, dimensional homogeneity.
                                                GM m
                                       F =−          r̂ = ma                          (9)
                                                 r2
                                              M2
                              M LT −2 = [G]           [G] = M −1 L3 T −2             (10)
                                              L2
Kepler’s 3rd law, 1618
                                                  a3            GM
                              M [G] = L3 T −2       2
                                                      = const =                      (11)
                                                  T             4π 2
                                                    L
                                           [M G] = ( )2 L                            (12)
                                                    T
L/T : velocity. Second velocity
                                           2GM                  GM
                                    v2 =              v2 ∼                           (13)
                                            R                    R

课程日期：2019 年 5 月 6 日                             <| 2 |>              最后修改：2019 年 5 月 6 日

---

连续介质力学                                                                                 第 19 次课笔记

black hole, RS ∼ 2GM /c2
      plank length
                                                    √
                                             lp =    ~G/c3                                   (14)

量子引力 quantum gravity
                                       [E] = [mc2 ] = M L2 T −2                              (15)

                                     [~] = M L2 T −2 T = M L2 T −1                           (16)
                                                                L
                      [G] = M −1 L3 T −2      [G~] = L5 T −3 = ( )3 L2 = [c3 ][lp2 ]         (17)
                                                                T
                                                 √
                                             lp ∼ ~G/c    3                                  (18)

∼: order of magnitude
                                 √
      plank time, tp = lp /c ∼    ~G/c5 ∼ 10−44 s

2.4    无量纲数
      Bernoulli eqn
                                     1
                                 p + ρv 2 + ρgh = const                                      (19)
                                     2
dimension homogeneity, additive term

                                  [ρv 2 ] = M L−3 L2 T −2 = M L−1 T −2                       (20)

n terms, n − 1 dimenionless.
                                           1 v2   p
                                                +   = ...                                    (21)
                                           2 gh ρgh
Froude number
                                                    V
                                              Fr = √                                         (22)
                                                     gh

2.5

                                               ∇·u=0                                         (23)

mass conservation,
                                           Dρ
                                              + ρdivu = 0                                    (24)
                                           Dt
incompressible Dρ
               Dt
                  =0
                                  ∂u
                             ρ(      + u · ∇ ⊗ u) = −∇p + µ∇2 u + ρg                         (25)
                                  ∂t

课程日期：2019 年 5 月 6 日                             <| 3 |>                  最后修改：2019 年 5 月 6 日

---

连续介质力学                                                                        第 19 次课笔记

  1.                                      /
                                     ρV       ρV 2    L   fL
                                                   ∼    ∼    = St                     (26)
                                      T        L     TV    v
  2.                                           /
                                          ∆p       ρV 2  ∆p
                                                        ∼ 2 = Eu                      (27)
                                          L         L    ρv
  3.                                           /
                                       ρV 2        µV   ρV L
                                                    2
                                                      ∼      = Re                     (28)
                                        L          L     µ

  4. froude number，留作作业                                        /
                                                        ρV 2
                                           F r = sqrt           ρg                    (29)
                                                         L

       Komlogoror, 1941
                              ⟨|v(x + r, t) − v(x, t)|2 ⟩ = cE 2/3 r2/3               (30)
                                                          2    −2
                                   energy          ML T
                            [E] =               =          = L2 T −3                  (31)
                                 mass x time         MT
       Spectrum E(k), k → wave number, [k] = L−1
                                                      ∫ ∞
                              1
                                ⟨v(x, t) · b(x, t)⟩ =     E(k)dk                      (32)
                              2                        0

self-correlated function
       作业：计算[E(k)] cE 2/3 k −5/3
       Fermi: better be approximately right than precisely wrong.

感谢为本次笔记提供参考的同学：                        无

课程日期：2019 年 5 月 6 日                            <| 4 |>                最后修改：2019 年 5 月 6 日

---

           连续介质力学                               第 20 次课笔记
                                             庄逸

        课程日期：2019 年 5 月 8 日                       最后修改：2019 年 6 月 19 日

                                      1 积分的量纲
                      [∫          ]
                           E(k)dk = [E(k)][k] = [E(k)]L−1 = L3 T −2         (1)

作业：推积分的量纲表达式

                                   2 plank mass
  plank length lp ，plank time lτ ，quantum gravity ~, G, c

                           [~] = M L2 T −1 [G] = M −1 L3 T −2               (2)
                        [ ]                                 √
                         ~       M L2 T −1   2T               ~c
                             = −1 3 −2 = M       ⇒ lm =                     (3)
                         G      M L T          L              G

                                  3    Buckingham
  Edgar Buckingham (1914) Π-theorem.
  Variables x1 , . . . xn , primary dimension k, n − k
 semi-infinite bar, longituclinal wave cL , transverse wave cT

                   σ = Eε, [E] = [σ] = [ρv 2 ] = [p] = [ρgh] = M L−1 T −2   (4)
                                        [ ]                   √
                                                    2
                                         E        L             E
                         [ρ] = M L−3           = 2        c∼                (5)
                                         ρ        T             ρ
                        σ(x, t) − σ(x + dx, t) = ρdxAutt = −σx dxA          (6)

---

连续介质力学                                                                    第 20 次课笔记

                             ∂(−Eε)    ∂ε
                         −          =E    = ρutt E           ε = ux                (7)
                               ∂x      ∂x
                                                         √
                                                             E
                              ∴ Euxx = ρutt       cL =                             (8)
                                                             ρ
hyperbolic.
                                      Tt = x∇2 T                                   (9)

轶事 anecdote
    作业：P316-317

                               4 dirac notation

                  2edx2 = ⟨dx|dx⟩ − ⟨dX|dX⟩                                       (10)
                        = ⟨dx|dx⟩ − ⟨(I − u ⊗ ∇) dx| (I − u ⊗ ∇) dx⟩              (11)
                                                     T
                        = ⟨dx|dx⟩ − ⟨dx| (I − u ⊗ ∇) (I − u ⊗ ∇) |dx⟩             (12)
                                              T
                        = ⟨dx|I − (I − u ⊗ ∇) (I − u ⊗ ∇) |dx⟩                    (13)

                                          5

                           ∂u                 1
                               + (u · ∇)u = − ∇p + ν∇2 u + g                      (14)
                            ∂t                ρ
ν: diffusivity momentum, kinematic viscosity.
                                       ρV L      vL
                                   Re =       =                                   (15)
                                        µ         ν
                                                 [     ]
                                    ∂u              FT
                               τ =µ       [τ ] =                                  (16)
                                    ∂y              AT
τ : flux of momentum.

                    6   Thickness of boundary layer
    (laminar).                           √
                                            x
                                      δ=c ν                                       (17)
                                            u0

课程日期：2019 年 5 月 8 日                     <| 2 |>                  最后修改：2019 年 6 月 19 日

---

连续介质力学                                                                                  第 20 次课笔记

                                       [u0 ] = LT −1       [x/u0 ] = T                        (18)

adiabatic shear, non-slip boundary 作业：用雷诺数表示

                                  7 Schrödiner equation

                                              ~2
                                          −      Ψxx + V Ψ = i~Ψt                             (19)
                                              2m
Ψ: wave funcation, non-dimensional.
     Let t = τ t̂, τ : characteristic time, x = Lx̂, L : length. Ψ(x, t) = Ψ(x̂, t̂)

                                             ~2                i~
                                        −       2
                                                  Ψx̂x̂ + V Ψ = Ψt̂                           (20)
                                            2mL                τ
divided by 21 m( Lτ )2

                              ~2 τ 2               V           i~τ 2           i~τ
                         −             Ψ x̂x̂ +    (  )  Ψ =           Ψt̂ = 1     Ψ          (21)
                                2
                             4m L    4          1
                                                  m L
                                                       2       1
                                                             τ 2 mL  2
                                                                             2
                                                                               mL2 t̂
                                              2    τ

                                              ε2
                                          −      Ψx̂x̂ + V̂ Ψ = 2iεΨt̂                        (22)
                                              4

感谢为本次笔记提供参考的同学：                             无

课程日期：2019 年 5 月 8 日                                 <| 3 |>               最后修改：2019 年 6 月 19 日

---

         连续介质力学                                第 21 次课笔记
                                             庄逸

     课程日期：2019 年 5 月 13 日                          最后修改：2019 年 6 月 18 日

                             1     量纲和普朗克量
力学讲义表 8.1

                                 基本力类型             力的强度
                                    引力                 10−39
                                    弱力                 10−6
                                   电磁力                 1/137
                                    强力                   1

                          [M G] = L3 T −2      [G] = M −1 L3 T −2                 (1)
                                  Gm2p
                                         = 5.91 × 10−39                           (2)
                                   ~c
Boltzmann constant S = kB ln Ω

                              [kB ] = J/K = M L2 T −2 Θ−1                         (3)

Planck length lP , Planck time tP , planck mass mP
Planck temperature TP = mp c2 /kB 作业：查一下普朗克温度
bijection, strain compatibility equation.

                              εij,st + εst,ij = εis,jt + εjt,is                   (4)

4πε0 ，高斯制，CGS: centimeter, Gram, second.

                [e2 ] = [E][L] = M L3 T −2         [~c] = [E · T ][V ] = [E][L]   (5)

planck charge
                                        √          √
                                 qP =       ~c =     4πε0 ~c                      (6)

---

连续介质力学                                                                     第 21 次课笔记

作业：如果世界毁灭了，只能有一条信息留下来，那么。。。
   类比 analogy, 不完全相似？

                                      2 韦伯数
   Weber number, γ, σ. surface tension.

                         [γ] = J/A = F LL−2 = F L−1 = M T −2                       (7)
                                                    2
                                              ρv
                                      We =                                         (8)
                                              γ/L

                                      3 邦德数
                                                        √
                                      ρgl                   γ
                               Bo =       1 ⇒ L=                                   (9)
                                       γ                    ρg
作业：分析液滴的毛细特征尺寸，什么时候可以忽略重力？小虫子在水上为什么能站住?
   作业：估算水的弛豫时间，毛细特征速度。 让无量纲量等于 1                                      10−12 m/s
   Better be approximately right than precisely wrong. 解方程不注意限制条件，会得到错
误的结果，还不如粗略估计。

感谢为本次笔记提供参考的同学：                   无

课程日期：2019 年 5 月 13 日                      <| 2 |>                最后修改：2019 年 6 月 18 日

---

            连续介质力学                           第 22 次课笔记
                                          庄逸

         课程日期：2019 年 5 月 15 日                  最后修改：2019 年 6 月 18 日

                              1   估算山的最大高度
    guesstimation, Enrico Fermi
    作业：maximum height of a mountain on earth；思路：熔解热，太高的话底部会发生塑
性变形
    Mount Everest σ = ρgh, E : Young’s moculus, [E] = [p]
    strain ε = σ/E = ρgh/E, plastic strain εy = 6.977/1000, Let ε = εy , h → hmax
    density ρ = 4 × 103 kg/m2 , E = 64.5GPa, hmax = 11.6km
    M = 106 , G = 109 , mega-Å
    Method II. σ = ρgh, σY = 450MPa , hmax = . . .
    Method III.

                                    2 牛顿炒股
    quant 宽克（矿工）
    royal mint 金本位 gold standard system , 牛顿 1720 stock.
    股票走势图见课件（45-46）
    先赚了 7000 英镑，又赔了 20000 英镑。
    year 1717 金本位 Ounce 盎司 gold = 3 磅 17 先令 10 便士
    作业：估算今天牛顿赔的钱的数量级
    “I could calculate the orbits of heavily bodied, but could not calculate the madness of
people “ ——Sir Issac Newton

---

连续介质力学                                                                   第 22 次课笔记

                                      3 Others
   作报告第一句话很重要

               ∑        ∑
         R=                        bγ ⊗ Nγ = n1 ⊗ NI + n2 ⊗ NII + n3 ⊗ NIII     (1)
              γ=1,2,3 Γ=I,II,III

R 是联系当前构形和初始构形的两点张量。
   strech ratio, 赛斯应变度量见书。

感谢为本次笔记提供参考的同学：                      无

课程日期：2019 年 5 月 15 日                      <| 2 |>           最后修改：2019 年 6 月 18 日

---

             连续介质力学                              第 23 次课笔记
                                             庄逸

         课程日期：2019 年 5 月 20 日                     最后修改：2019 年 6 月 18 日

大作业     渗流力学, Darcy’s law, (Darcy-) Stokes-Brinkman equation, 应用：石油、天然气
    正则: kenadical？

弛豫时间       水 10−12 s，钢铁则是十的几次方。德博拉数约为 1 的时候是流变体，大于 1 则是
固体。
    Navier，1822 年方程。1820+ Suspension bridge
    对称张量和非对称张量双内积，先把它对称化

                                         1 功共轭
    物质流形 material manifold
    Refernce configuration, t = 0; current configuration, t = t
                                                      dx
    deformation gradient tensor. two-point tensor F = dX

                                         ∂x
                                   F =      = FaB ea ⊗ eB                (1)
                                         ∂X
    determinant of F
                                            ∂x   ∂x   ∂x
                                            ∂X   ∂Y   ∂Z
                                            ∂y   ∂y   ∂y
                                  det F =   ∂X   ∂Y   ∂Z
                                                           =J            (2)
                                            ∂z   ∂z   ∂z
                                            ∂X   ∂Y   ∂Z
                  dv
J : Jacobian, J = dV ; dv = dx · da = dx(da)n
    dV = dX · dA
    stress = d(force) / d(area)
    Cauchy stress σ = df /da

                       JdX · dA = dx · da = F dX · da = dXF T da         (3)

---

连续介质力学                                                                                         第 23 次课笔记

                                       dX(JdA − F T da) = 0                                                (4)

由 dX 任意性，JdA = F T da
                                                da = JF −T dA                                              (5)

1.1 PK1
    Piola-Kirchhoff stress of the first kind (PK1) df = σda = JσF −T dA
                                            df
                                   P =         = JσF −T = τ F −T                                           (6)
                                            dA
where τ = Jσ in current configuration, τ : kirchhoff stress
                                            ∂XM                   ∂XM
                  P = (Jσkl ek ⊗ el ) · (        en ⊗ eM ) = Jσkl      δln ek ⊗ em                         (7)
                                             ∂xn                   ∂xn

                                                P = JσF −T                                                 (8)

1.2 PK2
    S = S T ,S = JF −1 σF −T , (JF −1 σF −T )T = JF −1 σF −T

1.3 velocity gradient tensor

                                                                                  
                    ∂v    ∂            ∂x          ∂       ∂x       ∂X   ∂        ∂x       ∂X
       l = v ⊗ ∇x =    =                        =                      =                      = Ḟ F −1    (9)
                    ∂x   ∂x            ∂t         ∂X       ∂t       ∂x   ∂t       ∂X       ∂x
    strain rate
                                                       l + lT
                                                 d=                                                       (10)
                                                          2
symmetrical d = dT ,l = d + ω
    spin
                                                       l − lT
                                                 ω=                                                       (11)
                                                          2

1.4 work conjugate

        ẇ = Jσ : d = Jσ : (l − ω) = Jσ : l = Jσ : (Ḟ F −1 ) = (JσF −T ) : Ḟ = P : Ḟ                   (12)

课程日期：2019 年 5 月 20 日                               <| 2 |>                最后修改：2019 年 6 月 18 日

---

连续介质力学                                                           第 23 次课笔记

   Green strain
                                      1 T
                              E=        (F F − I)                        (13)
                                      2
                                  1 T
                           Ė =     (Ḟ F + F T Ḟ )                     (14)
                                  2

                       ẇ = (JσF −T ) : Ḟ                               (15)
                         = JF −1 F σF −T : Ḟ                            (16)
                         = (JF −1 σF −T ) : (F T Ḟ )                    (17)
                                  T          T
                                F Ḟ + Ḟ F
                         =S:                = S : Ė                     (18)
                                     2

Summary
                  ẇ = Jσ : d = Jσ : l = P : Ḟ = S : Ė                 (19)

感谢为本次笔记提供参考的同学：             无

课程日期：2019 年 5 月 20 日                  <| 3 |>           最后修改：2019 年 6 月 18 日

---

                连续介质力学                                   第 24 次课笔记
                                                     庄逸

              课程日期：2019 年 5 月 22 日                           最后修改：2019 年 6 月 30 日

                         [eV ] = [kB T ] = [RT /NA ] = [hν] = [~ω] = [hc/λ]                              (1)

[e2 ] = [E][L], ae = e2 /me c2

                                 1     鸵鸟飞不起来的原因
     mg : gravity;     CAρair v 2 : lift;       L : characteristic length;     m : ρbird L3 ;   A : L2

                                                                    ρbird
                                 CAρair v 2 ∼ mg             v2 ∼         gL                             (2)
                                                                    Cρair
     √
v∼       gL

                                  2         无量纲数·达西数
     solid-like liquid 类固体。达西定律：
                                           κ                 µv  [κ]p
                                      v = − ∇p                  ∼ 2                                      (3)
                                           µ                 L    L

κ ∼ L2
     类比，analogy，热传导方程，扩散方程，通量 flux

                                            3      Jacobian
     f (x), x(t)                            Z            Z
                                                                 dx
                                                f dx =       f      dt                                   (4)
                                                                 dt

---

连续介质力学                                                                                           第 24 次课笔记

                        ZZ                     ZZ
                             f (x, y)dxdy =          f (x(u, v), y(u, v)) |J| dudv                      (5)

                                               ∂x        ∂x
                                                                   ∂(x, y)
                                     |J2 | =   ∂u
                                               ∂y
                                                         ∂v
                                                         ∂y
                                                               =                                        (6)
                                                                   ∂(u, v)
                                               ∂u        ∂v

                                                    ∂x        ∂x    ∂x
                                                    ∂u        ∂v    ∂w
                                        |J3 | =     ∂y
                                                    ∂u
                                                              ∂y
                                                              ∂v
                                                                    ∂y
                                                                    ∂w
                                                                                                        (7)
                                                    ∂z        ∂z    ∂z
                                                    ∂u        ∂v    ∂w

                                               |Jn | = . . .                                            (8)
                                               ∂x
                                        F =       = x ⊗ ∇X                                              (9)
                                               ∂X
    作业：求球坐标的雅可比和球的体积
    Professor, Reader, Lecturer
    原创

                                         4 速度梯度
    deformation gradient F , Jacobian J = det F

                                    d    d            ∂J
                                J˙ = J =    det(F ) =    : Ḟ                                          (10)
                                    dt   dt           ∂F
velocity gradient l
                                                                                   
                                     ∂v    ∂             dx        ∂X   d        ∂x
                      l = v ⊗ ∇x =      =                             =                   F −1         (11)
                                     ∂x   ∂X             dt        ∂x   dt       ∂X

                                     l = Ḟ F −1         ⇒         Ḟ = lF                             (12)

                 C = FTF         B = FFT                 det C = det(F T F ) = (det F )2               (13)

作业：验证 trC=trB?

课程日期：2019 年 5 月 22 日                              <| 2 |>                    最后修改：2019 年 6 月 30 日

---

连续介质力学                                                                                 第 24 次课笔记

                              5       行列式对矩阵的导数

                           ∂ det F           det(F + εA) − det F
                                   : A = lim                                                 (14)
                             ∂F          ε→0          ε
                       ∵ det(F + λI) = λ + I1 (F )λ + I2 (F )λ + I3 (F )
                                         3         2
                                                                                             (15)

         ∂ det F            det[εF (ε−1 I + F −1 A)]
                 : A = lim                                                                   (16)
           ∂F          ε→0             ε
                            det(εF ) det (ε−1 I + F −1 A) − J
                     = lim                                                                   (17)
                       ε→0                   ε
                            ε3 J[ε−3 + I1 (F −1 A)ε−2 + I2 (F −1 A)ε−1 + I3 (F −1 A)]
                     = lim                                                                   (18)
                       ε→0                              ε
                               −1              −1
                     = JI1 (F A) = Jtr(F A) = JI : (F −1 A) = JF −T : A                      (19)

                                          ∂J   ∂ det F
                                      ∴      =         = JF −T                               (20)
                                          ∂F     ∂F
    Volume strain
                (1 + ε11 )dx1 (1 + ε22 )dx2 (1 + ε33 )dx3 − dx1 dx2 dx3
         εV =                                                           ≈ ε11 + ε22 + ε33    (21)
                                      dx1 dx2 dx3
作业：29-45，5.1？
    Spectral decomposition

                                  6       常用张量的谱分解

                            x1 = λ1 X1        x2 = λ2 X2    x3 = λ3 X3                       (22)
                                  X
                                  3                        X
                                                           3
                            F =         λi ni ⊗ Ni    R=         ni ⊗ Ni                     (23)
                                  i=1                      i=1
                               X                                    X
                 C = FTF =            λ2i Ni ⊗ Ni    B = FFT =           λ2i ni ⊗ ni         (24)
                                  i                                  i
                        √ X                   √     X
                  U=  C=       λi Ni ⊗ Ni V = B=         λi ni ⊗ ni                          (25)
                      X1                      1
                   E=    (λ2i − 1)Ni ⊗ Ni  e = (1 − 1/λ2i )ni ⊗ ni                           (26)
                       2                      2
principal stretch 作业：写比奥应变，物质亨奇应变，空间比奥应变

感谢为本次笔记提供参考的同学：                           无

课程日期：2019 年 5 月 22 日                           <| 3 |>              最后修改：2019 年 6 月 30 日

---

            连续介质力学                              第 25 次课笔记
                                             庄逸

         课程日期：2019 年 5 月 27 日                       最后修改：2019 年 6 月 18 日

                          1     无量纲数·磁流体力学
    lorentz force，magenetic field
                      [              ]
                        ∂u
                    ρ      + (u · ∇)u = −∇p + µ∇2 u + ρg + j × B            (1)
                        ∂t

where, j - current density, ohm’s law. j = σ(E + B × u)
    j × B ∼ σB 2 V     µ∇2 u ∼ µV /L2
                         √                     √                    √
                             Lorentz force         σB 2 V L2            σ
                                           =                 = BL           (2)
                             viscous force           µV                 µ
Hartman number
    作业：用 N-S 方程推各种无量纲数？

                               2      体积的时间变化率
    Time derivative
                                     ∂J
                               J˙ =      : Ḟ = JF −T : Ḟ                  (3)
                                    ∂F
                                                ( )
                                    ∂v       ∂   dx ∂X
                      l = v ⊗ ∇x =      =                  = Ḟ F −1        (4)
                                    ∂x      ∂X dt ∂x
l=d+w
                                   ∴ J˙ = Jtrl = Jtrd = J∇ · v              (5)

                              ˙ = JdV
                             dv    ˙  = J(∇ · v)dV = ∇ · vdv                (6)

---

连续介质力学                                                                     第 25 次课笔记

区分速度和体积？
    Truesdell, Noll, NLFT: Nonlinear field theory, field equations
    杨振宁：宁拙勿巧
    推 30-4

                                    3 连续性方程
    mass continuity equation
                                     ∂ρ
                                        + ∇ · (ρv) = 0                              (7)
                                     ∂t
    charge
                                   ∂ρ
                                      +∇·j =0           j = ρvd                     (8)
                                   ∂t
j ：漂移速度
    diffusion
                                         ∂c
                                            +∇·J =0                                 (9)
                                         ∂t
Fick’s law, J = −D∇c
    thermal conduction
                                             ∂θ
                                        ρc      +∇·q =0                            (10)
                                             ∂t
q = −κ∇θ
    wave function Ψ
                               2
    probability density ρ = |Ψ|
                                         ∂ρ
                                            +∇·J =0                                (11)
                                         ∂t
probability density flux
                   ~
                      (Ψ∗ ∇Ψ − Ψ∇Ψ∗ )
                                   J=                                              (12)
                   mi
    可能是期末考题：用一句话说明为什么克里斯托弗符号不是张量。

感谢为本次笔记提供参考的同学：                     无

课程日期：2019 年 5 月 27 日                          <| 2 |>             最后修改：2019 年 6 月 18 日

---

                连续介质力学                         第 26 次课笔记
                                            庄逸

              课程日期：2019 年 5 月 29 日               最后修改：2019 年 6 月 18 日

     CPI - Corruption perception index 清廉指数

                                     1 无量纲数

                                  ∂c              c    c
                                     = D∇2 c        ∼D 2                (1)
                                  ∂t              τ   L
     √
L∼       Dτ
     oscillatory flow, pulsatile flow （脉动）, Womersley number 沃姆斯莱数
                                              √
                                                ξω
                                        Wo = L                          (2)
                                                 ν
L : character length; ω : frequency; ν : Kinematic viscosity

                                 Du    1
                                    = − ∇p + ν∇2 u + f                  (3)
                                 Dt    ρ
Du
Dt
     → v/τ = vω , ν∇2 u → νv/L2
                           √          √        √
                              vω        ω        inertial force
                                   =L                                   (4)
                             νv/L2      ν        viscous force
                                      √
                                        transient force
                                 W0 =                                   (5)
                                         viscous force
     stokes boundary layer          √
                                      ν
                                         − length                       (6)
                                      ω

                               L        characteristic length
                        Wo =     =                                      (7)
                               δ   Stokesboundarylayerthickness
     Roshko number
                                     Ro = St · Re = Wo2                 (8)

---

连续介质力学                                                          第 26 次课笔记

                                      2 Others
   二阶投影张量
                                          P =I−n⊗n                       (9)

   Cauchy’s stress principle (1822)
   traction force tn = σn
   n · σ · n = σij ni nj
   固体中（？）质量守恒，ρdv = dm，求导可以跳过（书 P216）
   可能是期末考题：参考构形中的平衡方程怎么写？（32-12)

                                          ∇X · P = 0                    (10)

感谢为本次笔记提供参考的同学：                       无

课程日期：2019 年 5 月 29 日                       <| 2 |>     最后修改：2019 年 6 月 18 日

---

        连续介质力学                     第 27 次课笔记
                                 庄逸

       课程日期：2019 年 6 月 3 日           最后修改：2019 年 6 月 17 日

                            1 连续性方程
• 质量守恒
                            ∂ρ
                               +∇·J =0        J = ρv             (1)
                            ∂t
• 电荷守恒
                        ∂ρ
                           +∇·J =0          J = ρvd              (2)
                        ∂t
• 量子力学概率密度
                 ∂ρ                       ~
                    +∇·J =0        J=        (ψ ∗ ∇ψ − ψ∇ψ ∗ )   (3)
                 ∂t                      2mi
• 扩散
                       ∂c
                          +∇·J =0          J = −D∇c              (4)
                       ∂t
• 热传导和热扩散
                            ∂θ
                      ρcp      +∇·q =0        q = −κ∇θ           (5)
                            ∂t
• 动量扩散，momentun diffusion
                    ∂(ρv)
                          +∇·τ =0                                (6)
                     ∂t    (                             )
                                          2
                    τ = −µ ∇ ⊗ v + v ⊗ ∇ − (∇ · v)I              (7)
                                          3

                                 ∂v
                                    = ν∇2 v                      (8)
                                 ∂t
  不可压缩条件：∇ · v = 0

---

连续介质力学                                                                       第 27 次课笔记

  • 对流热扩散方程
                                        ∂θ
                                           + v̇ · ∇[θ] = α∇2 θ                        (9)
                                        ∂t

类比，Analogy
    Kinematic viscosity
                                         µ
                                  [ν] = [ ] = L2 T −1 = [D]                          (10)
                                         ρ

                                 2      推导 N-S 方程
    conservation equation
                                       ∂(ρv)
                                             +∇·τ =0                                 (11)
                                        ∂t
    shear stress
                            τ = −[µ(∇ ⊗ v + v ⊗ ∇) + λ(∇ · v)I]                      (12)

                                  σ = −ρI + λ(trd)I + 2µd                            (13)

λ : bulk viscosity; µ : dynamic viscosity

Stokes’ hypothesis
                                        2            2
                                     λ + µ = 0, λ = − µ                              (14)
                                        3            3

                                                       2
                        ∇ · τ = −µ[∇2 v + (∇ · v) ⊗ ∇ − ∇ · (∇ · v)I]                (15)
                                                       3
for incompressible fluid, ∇ · v = 0
                                        ∇ · τ = −µ∇2 v                               (16)
                                    ∂v               ∂v
                               ∴ρ       = µ∇2 v          = ν∇2 v                     (17)
                                     ∂t              ∂t
                                    [α] = [D] = [ν] = L2 T −1                        (18)

    diffusion tensor
                                        xi xj             ⟨x ⊗ x⟩
                                Dij =               D=                               (19)
                                          t                  2t

课程日期：2019 年 6 月 3 日                             <| 2 |>             最后修改：2019 年 6 月 17 日

---

连续介质力学                                                                  第 27 次课笔记

                                     3 无量纲数
    普朗特数，施密特数
                                           ν           ν
                                  Pr =          Sc =                            (20)
                                           α           D
    无量纲化
                                  ∂c
                                     + (v · ∇)c = D∇2 c                         (21)
                                  ∂t
t = ατ, dx = dβL, v = dx
                      dt
                         = dβ L
                           dα τ
                                     (          )
                              ∂c         dβ         τD
                                 +          · ∇β c = 2 ∇2β c                    (22)
                              ∂α         dα         L

作业：推导不可压缩 NS 方程
    Péclet number, Pe 佩克莱数
                                                 LV   LV ν
                             P e = Re · P r         =                           (23)
                                                  α    ν α
    [v ⊗ v]
    作业：推导 33-8

感谢为本次笔记提供参考的同学：                   无

课程日期：2019 年 6 月 3 日                        <| 3 |>             最后修改：2019 年 6 月 17 日

---

              连续介质力学                            第 28 次课笔记
                                             庄逸

           课程日期：2019 年 6 月 5 日                    最后修改：2019 年 6 月 17 日

    无量纲化方程

                              1   无量纲数·傅里叶数
    Fourier number （Fo）傅里叶数
                                           ∂θ
                                     ρcp      +∇·q =0                                      (1)
                                           ∂t
Fourier’s heat transfer
                                           q = −κ∇T                                        (2)

k-thermal diffusivity
                                   q = h∆T = h(T2 − T1 )                                   (3)

h-heat transfer coefficient
                                           L[h] = [κ]                                      (4)

努塞尔特数，毕奥数。作业：它们的物理意义？除了书上的解释还有没有？
    q-热通量，单位面积单位时间通过的热量
    thermal diffusion:
                                                  αt
                                           Fo =                                            (5)
                                                  L2
mass diffusion:
                     Dt
                                           Fo =                                            (6)
                     L2
无量纲化不能把算子去了，这和数量级估计不一样。 ∂θ
                        ∂t
                           ∼ θ/τ ，α∇2 θ ∼ αθ/L2
    characteristic time for thermal conduction τ ∼ L2 /α, so F o = t/τ , Fo–dimensionless time

---

连续介质力学                                                                           第 28 次课笔记

                                       2 PDE 的类型
    PDE-partial differential equations

  • hyperbolic, 双曲, wave motion, 引力波方程？

  • parabolic, 抛物, flux

  • elliptic, 椭圆

    毕奥-萨伐尔定律在流体中的类比。（？）

                                   3      热通量变换公式
    q0 : heat flux at reference configuration. (per dA)
    q: heat flux at current configuration. (per da)

                                           q0 · dA = q · da                               (7)

南森公式 da = JF −T dA
                                       q0 = JqF −T = JF −1 q                              (8)
重要：当前构形和参考构形的热流变化。
    对于各向异性，则要用张量。
    isotropic
                                          1
                                  εik =     α∆T δik ⇒ εkk = α∆T                           (9)
                                          3
anisotropic
                                                    1
                                            εik =     αik ∆T                             (10)
                                                    3
αik - thermal expansion tensor;

                                  q = −k∇T           qi = −kik Tk (?)                    (11)

                                           4 Others
    作业：独立分量个数。αik , kik = 1；高级晶系：立方；= 2；中级晶系：四方、六方、三方；
= 3；低级晶系：单斜、三斜、正交。朗道解释：椭球张量
    诺特定理推能量守恒。复习等时变分。
    作业：推 34-6

课程日期：2019 年 6 月 5 日                            <| 2 |>                  最后修改：2019 年 6 月 17 日

---

连续介质力学                                       第 28 次课笔记

感谢为本次笔记提供参考的同学：       无

课程日期：2019 年 6 月 5 日       <| 3 |>   最后修改：2019 年 6 月 17 日

---

             连续介质力学                             第 29 次课笔记
                                            庄逸

          课程日期：2019 年 6 月 10 日                     最后修改：2019 年 6 月 17 日

                     1   无量纲数·奥内佐格数·水的振动
    Ohnesorge number
    水的特征速度，Capillary number
                                                  µv
                                          Ca =                                  (1)
                                                  γ
Capillary velocity
                                                 γ
                                            v∼                                  (2)
                                                 µ
γ : surface tension. Capillary time (viscous)
                                                L   Lµ
                                       tvis ∼     =                             (3)
                                                v    γ
Lord Rayleigh 写了一本关于振动的好书 The theory of sound
                      √       √     √       √
                        ρR3     m     m        γ
                   τ∼       ∼     ∼     ω∼                                      (4)
                         γ      γ     k       ρR3

弹簧振子振动方程。谐振子 simple harmonic oscillator

                                         ẍ + ω 2 x = 0                         (5)

                         [γ] = M L2 T −2 L−2 = M T −2     [k] = M T −2          (6)

analogy between (coefficient of stiffness of spring) & (surface tension). 液滴表面相当于一个
小弹簧。可能是期末考题：求液滴的杨氏模量
                                                  γ
                                            E∼                                  (7)
                                                  r
                                                 √
                                          tvis     We
                                     Oh =      =                                (8)
                                           τ      Re

---

连续介质力学                                                           第 29 次课笔记

                             2 散度分配律

                          (ρv) · ∇ = ρdivv + v · ∇ρ                       (9)

                      (vσ) · ∇ = v · (σdiv) + (v ⊗ ∇) : σ                (10)

                         3    无滑移边界条件
   流体的无滑移边界条件：速度沿着边界面切线方向为零，二阶投影张量。uP = 0
   完全滑移边界条件 impermeability condition v · n = 0

                                 4 others
   作业：推热力学第一第二定律，推 (34-8)(34-12,13)(35-14,15)(35-20)(35-24)(35-26)
   固体，free body diagram。流体：contour volume 控制体积。作业：查什么是流体的控制
体积？
   雷诺输运定理 RTT

感谢为本次笔记提供参考的同学：              无

课程日期：2019 年 6 月 10 日               <| 2 |>              最后修改：2019 年 6 月 17 日

---

            连续介质力学                           第 30 次课笔记
                                        庄逸

         课程日期：2019 年 6 月 12 日                最后修改：2019 年 6 月 17 日

                                      1 复习
    NS 方程及指标形式，q, q0 之间关系

                                 2 无量纲数

                       ∂ui      ∂ui    1 ∂p     ∂ 2 ui
                           + uk     =−      +ν         + fi                  (1)
                        ∂t      ∂xk    ρ ∂x    ∂xk ∂xk
                                     √
                                       We     µ
                               Oh =       =√                                 (2)
                                      Re     ργL
拉普拉斯数 laplace，Suratman number Su
                                γL       ργL   ργL
                      La =             =      = 2 = Oh−2                     (3)
                             µv/L · L2   µρvL   µ

                                 3    Invariance
    Galilean transformation, classical mechanics, continuum mechanics. 伽利略变换在经典力
学和连续介质力学下适用。
                              r ′ = r − vt   t′ = t − τ                      (4)

v : uniform motion.

                             4       inertial frame
    惯性坐标系的性质

---

连续介质力学                                                                               第 30 次课笔记

  1. space is isotropic and homogenous.

  2. time is homogenous.

  3. Simplicity

L(q, q̇, t) → L(q̇ 2 , t) → L(q̇ 2 )
                          d ∂L ∂L                         ∂L
                                  −    =0          →           = const q̇ = const             (5)
                          dt ∂ q̇   ∂q                    ∂ q̇
(?)
                                                d2 r               d2 r ′
                                       f =m               f′ = m                              (6)
                                                dt2                dt2

                                       5      流体力学客观性
       Take divergence ∇ onto N-S equations
                (                )
                    1                   1
            ∇ · − ∇p + ν∇2 u = − ∇2 p + ν∇2 (∇ · u)                                           (7)
                    ρ                   ρ
                  (              )
                    ∂u                ∂
               ∇·       + u · ∇u = (∇ · u) + (∇ ⊗ u) : (u ⊗ ∇) + (u · ∇)(∇ · u)               (8)
                     ∂t               ∂t
                                      D
                                    =    (∇ · u) + (∇ ⊗ u) : (u ⊗ ∇)                          (9)
                                      Dt
                               ∇2 p = −ρ(∇ ⊗ u) : (u ⊗ ∇)                                    (10)

注意
                                                               ∂uj ∂ui
                                   (∇ ⊗ u) : (u ⊗ ∇) =                                       (11)
                                                               ∂xi ∂xj
原因是后面没东西，所以是右散度。
                                              ∂2p      ∂uj ∂ui
                                                2
                                                  = −ρ                                       (12)
                                              ∂xi      ∂xi ∂xj
L length, u velocity.
                                              x           u            u
                                       x∗ =        u∗ =       t∗ = t                         (13)
                                              L           y            L
  1.
                                                  ∇∗
                              ∇·u=0 ⇒                · (u∗ u) = 0 → ∇∗ u∗ = 0                (14)
                                                  L
  2.
                               ∂(uu∗ )        ∗      ∇∗ ∗        ∇∗
                                        +  (u   u) ·   (u u) = −    (pu2 p∗ )                (15)
                              ∂(t∗ u/L)              L           L
                              ∂u∗                              1 ∗2 ∗2 ∗
                                    + u∗ · ∇∗ u∗ = −∇∗ p∗ +      ∇ ∇ u                       (16)
                               ∂t∗                            Re

课程日期：2019 年 6 月 12 日                               <| 2 |>                  最后修改：2019 年 6 月 17 日

---

连续介质力学                                                              第 30 次课笔记

  3. 作业：把第三个方程无量纲化 (11) 式

1. Re similarity 雷诺相似性. 2. 时空 (space and time) 3. Time reversal（时间反演）
   t∗ = −t∗ , u∗ = −u∗ , Re 项（黏性项）不满足时间反演！
   4. 旋转 rotation (fixed angle) & reflection

                                  ei · êj = cos θ = aij                    (17)

                                  x̂ = ax      û = au                      (18)

感谢为本次笔记提供参考的同学：                   syj

课程日期：2019 年 6 月 12 日                    <| 3 |>            最后修改：2019 年 6 月 17 日

---

            连续介质力学                                     第 31 次课笔记
                                                     庄逸

        课程日期：2019 年 6 月 17 日                              最后修改：2019 年 6 月 17 日

                                               1 复习
   麦克斯韦方程组，推电荷密度守恒方程，埃尔曼西应变，格林应变张量，客观性，NS 方
程无量纲化，？的散度。
   连续性方程：电荷、浓度、热、动量扩散、概率密度，甚至交通流等。
                                        ˙ = (∇ · u)dv
   速度的散度的意义是什么？∇ · v = 0。位移的散度是体积微元变化率 dv

                               2 Galiliean invariance

                              r ′ = r − vt       v = const        t′ = t + α     (1)

惯性参考系中牛顿第二定律也不发生变化，因为求导两次。

2.1 Extended Galiliean invariance
   v = v(t) is rectilinear

                             ∂ui      ∂ui    1 ∂p      ∂ 2 ui
                                 + uk     =−       +ν         − Ai               (2)
                             ∂t       ∂xk    ρ ∂xi    ∂xk ∂xk
                             1 ∂p           1 ∂                     1 ∂
                       −           − Ai = −       (p + ρxj Aj ) = −       p̂     (3)
                             ρ ∂xi          ρ ∂xi                   ρ ∂xi
                                                     p + ρxj Aj
                                             p̂∗ =                               (4)
                                                        ρu2
如果在加速系中做实验，只需要把加速度修正到上面这项即可。

                                             p̂ = p + ρx · A                     (5)

---

连续介质力学                                                                    第 31 次课笔记

2.2 rotation invariance
   转动的情况
                                        aij = ei · êj                             (6)
                                        dei
                                            = Ωij ej                               (7)
                                        dt
Ω : spin, Ωij = −Ωji ，Ω = ΩT 反对称
   frame acceleration
                                                              dωji
                            Aij = xj Ωjk Ωki + 2vj Ωji + xj                        (8)
                                                               dt
欧拉力
   时间反演不满足：粘性项。标架旋转不满足：科氏加速度和角加速度

                                3    欧几里得客观性
   §36
                                    x∗ − x∗0 = Q(x − x0 )                          (9)

                        x∗ = x∗0 + Q(x − x0 )x − x0 = QT (x ∗ −x∗0 )              (10)

作业：解 (36-4)

                                     4 无量纲数
   凑伽利略数：重力/粘性力

感谢为本次笔记提供参考的同学：                     无

课程日期：2019 年 6 月 17 日                      <| 2 |>                最后修改：2019 年 6 月 17 日

---

           连续介质力学                            第 32 次课笔记
                                          庄逸

         课程日期：2019 年 6 月 19 日                   最后修改：2019 年 6 月 19 日

                                       1 复习
      εijk ，无量纲数，黏性力是哪个 nian？功共轭，现代张量的数学定义：多重线性映射

                         2    张量的欧几里得客观性
      见书 37 节
      首先定义 n 阶张量的客观性。一个 n 阶张量 u1 ⊗ u2 ⊗ · · · ⊗ un ，当更换观察者时，所对
应的变换满足下式：

                (u1 ⊗ u2 ⊗ · · · ⊗ un )∗ = (Qu1 ) ⊗ (Qu2 ) ⊗ · · · ⊗ (Qun )    (1)

对于二阶张量，上式退化为

           (u1 ⊗ u2 )∗ = (Qu1 ) ⊗ (Qu2 ) = (Qu1 ) ⊗ (u2 QT ) = Q(u1 ⊗ u2 )QT   (2)

亦即，满足上式的二阶张量就是满足欧几里得客观性。

2.1    变形梯度张量的欧几里得客观性
      可从两种途径判断变形梯度的客观性。其一，从其基本定义出发：F = ∂x/∂X，对于另
外一个观察者而言，有
                ∂x∗   ∂(Qx) ∂x
                    =        F∗ =
                               = QF     (3)
                ∂X      ∂x ∂X
上式反映出，变形梯度的变换就像一个矢量一样，它作为两点张量场，不满足欧几里得客观性
的要求。其原因之一，是参考构形中的矢量 X 是不变的，亦即：X ∗ = X，换句话说，X 和
观察者无关。

---

连续介质力学                                                                    第 32 次课笔记

      判断变形梯度是否满足客观性要求的途径是由当前构形和参考构形中线段的联系：dx =
F dX，由于：dx∗ = Qdx，(dx)∗ = (F dX)∗ = F ∗ dX，因此上式成立。
      由于雅可比 J = det F 作为一个反映体积变化的标量毫无疑问是满足欧几里得客观性的，
现利用上式证明如下：

                 J ∗ = det F ∗ = det(QF ) = (det Q)(det F ) = det F = J          (4)

      下面我们来看“右柯西-格林”和“左柯西-格林”(Finger) 变形张量的客观性：
            
            C ∗ = (F T F )∗ = (QF )T QF = F T QT QF = F T F = C
                                                                                 (5)
                B ∗ = (F F T )∗ = QF (QF )T = QF F T QT = QBQT

2.2    柯西应力的欧几里得客观性
      柯西面力 (traction) 矢量 t 是柯西应力 σ 和截面外法线 n 的点积：t = σn。两个矢量 t
和 n 均满足客观性：t∗ = Qt，n∗ = Qn，因此有

        t∗ = Qt = (σn)∗ = σ ∗ n∗ = σ ∗ Qn ⇒ Qt = Qσn = σ ∗ Qn ⇒ σ ∗ = QσQT       (6)

上式说明，柯西应力作为欧拉型的当前构形中的张量，是满足欧几里得客观性要求的。
      基尔霍夫应力由于和可惜盈利之间满足：τ = Jσ，显然也是客观的应力张量。

2.3 PK1 和 PK2 应力张量的欧几里得客观性
      PK1 应力的定义式 P = JσF −T ，应用 (37-6) 和 (12-13) 两式，故有

               P ∗ = J ∗ σ ∗ (F ∗ )−T = JQσQT (QF )−T = JQσQT Q−T F −T           (7)
                  = JQσF −T = QP                                                 (8)

上式说明，作为两点张量的 PK1 的变换关系和另外一个两点张量——变形梯度张量的变换关
系一致，不满足二阶张量的欧几里得客观性要求。
      PK2 应力的定义式：T = F −1 P ，变换观察者时，其变换关系为

                    T ∗ = (QF )−1 QP = F −1 Q−1 QP = F −1 P = T                  (9)

和右柯西-格林变形张量 C 类似，PK2 作为参考构形中的应力张量，其变换关系和标量一样，
不满足张量的欧几里得客观性要求。

课程日期：2019 年 6 月 19 日                    <| 2 |>             最后修改：2019 年 6 月 19 日

---

连续介质力学                                                             第 32 次课笔记

                             3 张量的客观率
3.1    速度梯度、应变率、旋率张量的欧几里得客观性
      首先看速度梯度张量的客观性。由于 l = Ḟ F −1 ，故，速度梯度的变换关系为
               ˙ (QF )−1 = (Q̇F + QḞ )F −1 Q−1 = Q̇QT + QlQT = Ω + QlQT
         l∗ = QF                                                           (10)

在上式中，已经利用了正交张量的基本性质 (20-13) 式，利用 (36-6) 式中的 Ω = −ΩT ，有
            
            
                  l∗ + l∗T        l + lT T
             d∗ =             =Q        Q = QdQT
                        2             2              (11)
            
                  l ∗
                       −  l ∗T
            ω =
               ∗
                               = Ω + QωQ  T
                        2
上式表明，应变率作为当前构形的欧拉型张量是满足欧几里得客观性要求的；而，旋率的转换
关系和速度梯度相同，均不满足张量的客观性要求。
      从 (38-2) 式中的第二式：ω ∗ = Q̇QT + QωQT 中容易得到：
                           
                            Q̇ = ω ∗ Q − Qω
                                                                           (12)
                              Q̇T = −QT ω ∗ + ωQT

3.2    客观矢量率的定义
                                       ˙ = Q̇u + Qu̇，将 (38-3) 式中的
      由客观矢量的定义 (36-1) 式，对时间求导，有：u̇∗ = Qu
第一式代入，得到如下关系：

                       u̇∗ = Q̇u + Qu̇ = (ω ∗ Q − Qω)u + Qu̇
                                                                           (13)
                          = ω ∗ u∗ + Qu̇ − Qωu

由上式整理得到：
                             (u̇ − ωu)∗ = Q(u̇ − ωu)                       (14)

通过上式可定义满足矢量客观性要求的共旋率 (co-rotational rate):

                                   ū = u̇ − ωu                            (15)

3.3    客观张量率的定义
      对于任意满足客观性要求的二阶张量 A，有 A∗ = QAQT ，其时间导数：

                         Ȧ∗ = Q̇AQT + QȦQT + QAQ̇T                       (16)

课程日期：2019 年 6 月 19 日                 <| 3 |>             最后修改：2019 年 6 月 19 日

---

连续介质力学                                                 第 32 次课笔记

将 (38-3) 式代入上式，整理得到：
                (            )∗
                 Ȧ − ωA + Aω = Q(Ȧ − ωA + Aω)QT              (17)

上式便定义了连续介质力学中最为常用的尧曼-扎伦巴 (Jaumann-Zaremba) 客观率：

                          Â = Ȧ − ωA + Aω                    (18)

特别地，当 A 取柯西应力 σ，得到连续介质力学中常用的柯西应力的尧曼-扎伦巴客观率：

                          σ̂ = σ̇ − ωσ + σω                    (19)

                           4 Others
   连续性方程是客观的，因为是标量方程？

                   5   无量纲数·阿基米德数
   比较伽利略数和阿基米德数

感谢为本次笔记提供参考的同学：           无

课程日期：2019 年 6 月 19 日           <| 4 |>        最后修改：2019 年 6 月 19 日

---

           连续介质力学                         第 33 次课笔记
                                      庄逸

         课程日期：2019 年 6 月 25 日              最后修改：2019 年 6 月 25 日

                                      1

                                B = α(trA)I + βA                    (1)
                                                         1
                   trB = 3α trA + β trA   ⇒    trA =          trB   (2)
                                                       3α + β
                                   α
                             B=        (trB)I + βA                  (3)
                                3α + β
                                 (                    )
                              −1          α
                          A=β     B−           (trB)I               (4)
                                        3α + β

                                      2
   Constitutive relation. constitution-宪法. paradigm-范式
   理性力学范式：八条公理 axiom
   rheology 流变学；theology 神学
   注意：NS 方程的不变性，无量纲，雷诺相似性

                          ∂vx ∂vy   ∂vz
                  ∇·v =      +    +     = εxx + εyy + εkk = trε     (5)
                          ∂x   ∂y   ∂z
应变 (?)

                                      3
   杆拉伸 tension 压缩 compression. 纵向 longituclinal. 横向 transverse.
   拉伸纵向伸长 longituclinal extension

---

连续介质力学                                                                   第 33 次课笔记

   作业：查泊松比的详细定义。
   线弹性 linear elastic. 叠加原理 superposition principle
   作业：应变是对称的
   体模量：施加一个静水压强，水的体积变化率
   Stress-strain relation
                                       σ = 2µε + λ(trε)I                          (6)
                                       σ
                                      ∆ = λ(trd)I + 2µd                           (7)

                                           S = C −1                               (8)

                                     4 格拉晓夫数
   Grashof number
                                                     1
                            εkk = α(T − T0 )      εik =α(T − T0 )δik              (9)
                                                     3
                                   buoyancy      gL3 β(Twall − T∞ )
                            Gr =               =                                 (10)
                                 viscous force           ν2
β = α 是热膨胀系数。

感谢为本次笔记提供参考的同学：                       无

课程日期：2019 年 6 月 25 日                           <| 2 |>          最后修改：2019 年 6 月 25 日

---

            连续介质力学                            第 34 次课笔记
                                           庄逸

        课程日期：2019 年 6 月 26 日                     最后修改：2019 年 6 月 26 日

    王文标教授；Joseph John Thomoson, four to seven courses per year; Geim

                                    s = 2µε + λ(trε)I                   (1)

力、化耦合的胡克定律，JCM Li，(james) 李振民
                                1                            CΩ
                        εij =     [(1 + ν)σij − νσkk δij ] +    δij     (2)
                                E                             3
通过类比法得到。
                   1
                     α(T − T0 )δik εik =                                (3)
                   3
每当你创立一个新学科的时候首先要考虑公理体系和范式。
    作业：求 s8-1 的逆，对比 s8-2,3

                                1 弹性体的分类
  • Cauchy elastic, 胡克定律

  • hyperelastic, hyper: to a higher degree 超弹性

  • hypoelastic, to a lesser degree 次弹性，低弹性

低弹性本构关系
                 ∆
    Jaumann rate σ = σ̇ − ωσ + σω
                                    ∆
                                    σ = 2µd + λ(trd)I                   (4)

work conjugacy
                         ω̇ = Jσ : d = τ : d = P : Ḟ = T : Ė          (5)

---

连续介质力学                                                      第 34 次课笔记

spin
                            l − lT        l + lT
                       ω=            d=                              (6)
                               2             2
理论上讲这个是对的：
                        ∆
                        τ = 2µd + λ(trd)I                            (7)

感谢为本次笔记提供参考的同学：        无

课程日期：2019 年 6 月 26 日           <| 2 |>             最后修改：2019 年 6 月 26 日

---

          连续介质力学              第 35 次课笔记
                           庄逸

       课程日期：2019 年 6 月 27 日     最后修改：2019 年 8 月 1 日

                          1 复习
 stretch ratio λi
 超弹性：有势，potential
 超弹性是处理非线性弹性的。
 材料可压缩–要有 J − 1

感谢为本次笔记提供参考的同学：       无

---

       连续介质力学              第 36 次课笔记
                        庄逸

     课程日期：2019 年 7 月 1 日   最后修改：2019 年 8 月 1 日

                       1 复习
 转动惯量的表达、格林应变张量、二维板、轴的一维振动 ∇ · σ = ρa
 波动方程记得写波速
 ∇ · σ = 0 的物理意义
 什么是惯性系？伽利略变换，空间均匀各向同性，时间均匀，简单性（二次方）

感谢为本次笔记提供参考的同学：    无

---

         连续介质力学                                 第 37 次课笔记
                                            庄逸

      课程日期：2019 年 7 月 3 日                        最后修改：2019 年 7 月 3 日

                                        1 复习
质量守恒，连续性方程，雷诺输运定理的推导。
event observer
                                   ρ = ρ∗        J = J∗                     (1)

continuity equation, Lagrangian viewpoint, ρ∗0 = J ∗ ρ∗
obvious, mathematical humor, scale 标尺

             2 objectivity of continuity equation

                 ∂ρ∗                             ∂ρ∗   ∂
                     + ∇∗ · (ρv)∗ = 0       ⇒        + ∗ (ρ∗ Qlk vk ) = 0   (2)
                 ∂t∗                             ∂t∗  ∂xl
                             ∂ρ    ∂            ∂xp
                                +     (ρQlk vk ) ∗ = A                      (3)
                             ∂t   ∂xp           ∂xl
                                 x∗ − x∗0 = Q(t)(x − x0 )                   (4)
                                            ∂x
                                        Q       =I                          (5)
                                            ∂x∗
                               ∂xp
                                    = Qlp       det Q = ±1                  (6)
                               ∂x∗l
                                    ∂ρ    ∂
                              A=       +     (ρvk )Qlk Qlp                  (7)
                                    ∂t   ∂xp
                                                ∂ρ        ∂
                     ∵ Qlk Qlp = δkp    ⇒          + δkp     (ρvk ) = 0     (8)
                                                ∂t       ∂xp
                                 ∂xp            ∂ρ    ∂
                       ∵ δkp =          ⇒          +     (ρvk ) = 0         (9)
                                 ∂xk            ∂t   ∂xk

---

连续介质力学                                                                      第 37 次课笔记

[div(ρv)]∗k ，v ∗ = Qv
    动量方程客观性, equations of equlibrium

                                            ∇·σ =0                                  (10)
                                                       ∂ ∗
                                         ∇∗ · σ ∗ =        σ                        (11)
                                                      ∂x∗l
                                           σ ∗ = QσQT                               (12)

                                       ∂
                        (∇∗ · σ ∗ )k =     (Qlr σrs Qks )                           (13)
                                      ∂x∗l
                                       ∂                  ∂xq
                                    =      (Qlr σrs Qks ) ∗                         (14)
                                      ∂xq                 ∂xl
                                                  ∂σrs             ∂σrs
                                    = Qlr Qks Qlq        = Qks δrq                  (15)
                                                   ∂xq             ∂xq

                                               ∂σrs
                             ∇∗ · σ ∗ = Qsk         = Q · (∇ · σ)                   (16)
                                               ∂xr
    Duhem 迪昂

                                          1
                                   ε=       (∇ ⊗ u + u ⊗ ∇)                         (17)
                                          2
作业：证明 s10-1
    柱坐标的变形张量？26-6，黎曼度规

                                               F →                                  (18)

感谢为本次笔记提供参考的同学：                     无

课程日期：2019 年 7 月 3 日                          <| 2 |>                最后修改：2019 年 7 月 3 日

---

         连续介质力学                               第 38 次课笔记
                                          庄逸

       课程日期：2019 年 7 月 3 日                      最后修改：2019 年 7 月 3 日

                 1     其他坐标的变形梯度和黎曼度规

                                X = Rg R + Θg Θ + Zg Z                                 (1)

                                  x = rg r + θg θ + zg z                               (2)
                                                        
                                         ∂r   1 ∂r     ∂r
                                       ∂R    R ∂θ     ∂z 
                               [F ] =   ∂θ
                                      r ∂R
                                              r ∂θ
                                              R ∂Θ
                                                        ∂θ 
                                                      r ∂z                            (3)
                                        ∂z    1 ∂z     ∂z
                                        ∂R    R ∂Θ     ∂Z

                            ds2 = gµν dxµ dxν = g µν dxµ dxν                           (4)
                                                    
                                           1
                                                    
                                 [gµν ] = 
                                             r 2    
                                                                                      (5)
                                                     1

                                          2

                      ∂ρ
                         + ∇ · (ρv) = 0                                                (6)
                      ∂t
满足时间反演 t · −t。NS 方程不满足时间反演

                          Q = Qij ei ⊗ ej     QT = Qji ei ⊗ ej                         (7)

       QQT = (Qij ei ⊗ ej ) · (Qsr er ⊗ es ) = δjr Qij Qsr ei ⊗ es = δis ei ⊗ es = I   (8)

                                      1
                                 ε=     (∇ ⊗ u + u ⊗ ∇)                                (9)
                                      2

---

连续介质力学                                                                       第 38 次课笔记

                                   ∂ 2 εxy   ∂ 2 εxx ∂ 2 εyy
                               2           =        +                              (10)
                                   ∂x∂y       ∂y 2    ∂x2
                                        ∇×ε×∇=0                                    (11)
                 ∂                 ∂             ∂ 2 εjk
                    ei × ej εjk ⊗     ek × el =          εijm εkln em ⊗ en         (12)
                ∂xi               ∂xl           ∂xi ∂xl
                                     εjk,il εijm εkln = 0                          (13)

有限变形、大变形 finite deformation, compability condition

                                        F × ∇X = 0                                 (14)
                               ∂ 2 xi
                                      εKLM ei ⊗ eM = 0                             (15)
                             ∂XK ∂XL

感谢为本次笔记提供参考的同学：                     无

课程日期：2019 年 7 月 3 日                       <| 2 |>               最后修改：2019 年 7 月 3 日

---

        连续介质力学                       第 39 次课笔记
                                  庄逸

      课程日期：2019 年 7 月 5 日              最后修改：2019 年 8 月 1 日

                                F × ∇X = 0                   (1)

 测地线方程
 非线性经典场论 non-linear classical field theory
 公理化和客观性，公理化起码要知道一两个，哥德尔不完备定理

感谢为本次笔记提供参考的同学：             无

---
