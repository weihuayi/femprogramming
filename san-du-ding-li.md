# 散度定理

散度定理是有限元理论和算法中经常用到一个定理。 但很多学过数学分析的学生， 你如果问他这个定理， 很少有人能答出来。

给定向量函数 $\mathbf F(x)$， 其定义域为 $\Omega\in\mathbb R^n$， $\mathbf n$ 是 $\Omega$ 边界 $\partial \Omega$ 上的单位外法线向量.

$$
\int_{\Omega} \nabla\cdot\mathbf F~ \mathrm d \mathbf x = \int_{\partial \Omega}\mathbf  F\cdot\mathbf n ~\mathrm d s
$$

这就是**散度定理**.

散度定理是微积分第二基本定理或“牛顿-莱布尼茨公式”的推广



$$
\begin{aligned}
\int_{\Omega} \nabla\cdot(v\nabla u)~\mathrm d \mathbf x &= \int_{\partial\Omega} v\nabla u\cdot\mathbf n~\mathrm d \mathbf s\\
\int_{\Omega} v\Delta u~\mathrm d \mathbf x + \int_{\Omega}\nabla u\cdot\nabla v~\mathrm d \mathbf x &= \int_{\partial\Omega} v\nabla u\cdot\mathbf n~\mathrm d \mathbf s
\end{aligned}
$$

$$
\int_\Omega v_x \mathrm d \mathbf x = \int_\Omega \nabla\cdot \begin{pmatrix}
v\\0
\end{pmatrix} \mathrm d \mathbf x = 
\int_{\partial \Omega} v\mathbf n_x \mathrm d \mathbf s
$$

$$
\int_\Omega v_y \mathrm d \mathbf x = \int_\Omega \nabla\cdot \begin{pmatrix}
v\\0
\end{pmatrix} \mathrm d \mathbf x = 
\int_{\partial \Omega} v\mathbf n_y \mathrm d \mathbf s
$$

利用散度定理： 
* 求多边形的面积 
* 求多面体的体积