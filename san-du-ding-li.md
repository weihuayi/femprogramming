# 散度定理

散度定理是有限元理论和算法中经常用到一个定理。 但很多学过数学分析的学生， 你如果问他这个定理， 很少有人能答出来。

给定向量函数 $$\mathbf F(x)$$， 其定义域为 $$\Omega\in\mathbb R^n$$， $$\mathbf n$$ 是 $$\Omega$$ 边界 $$\partial \Omega$$ 上的单位外法线向量.

$$
\int_{\Omega} \nabla\cdot\mathbf F~ \mathrm d \mathbf x = \int_{\partial \Omega}\mathbf  F\cdot\mathbf n ~\mathrm d s
$$

在一维情形下， 散度定理等价于微积分第二基本定理或“牛顿-莱布尼茨公式”， 它的内容如下：
设 $$a, b\in \mathbb R$$, 设 $$f, F:[a, b]\rightarrow \mathbb R$$， 且满足：

* $$F$$ 连续，
* $$f$$ 是 $$F$$ 的原函数， 即 $$\forall x \in (a, b)$$, $$F'(x) = f(x)$$,

那么， 若 $$f$$ 黎曼可积， 则有
$$
\int_a^b f(t) \mathrm d t = F(b) - F(a)
$$

在二维情形下， 散度定理等价于格林公式。

散度定理在数值计算的理论和算法中非常有用， 你一定要牢记它。 

比如， 它可以用来计算多边形的面积和多面体的体积。 以多边形的面积计算为例， 给定一个多边形 $$\Omega$$， 假设它有 $$n$$ 个按逆时针排序的顶点 $$\{\mathbf x_i \}_{i=0}^{n-1}$$， $$n$$ 条边 $$\{e_i:=(\mathbf x_i, \mathbf x_{i+1})\}_{i=0}^{n-1}$$(注意这里假定 $$\mathbf x_n = \mathbf x_0$$)， 第 $$i$$ 条边 $$e_i$$ 的单位外法线向量记为 $$\mathbf n_i$$。 下面利用散度定理给出多边形面积的计算公式：

$$
\begin{align}
\int_\Omega \mathrm d\mathbf x = &\frac{1}{2}\int_\Omega\nabla\cdot\mathbf x \mathrm d\mathbf x \\
=& \int_{\partial\Omega} (\mathbf x\cdot \mathbf n) \mathrm ds\\
=& \sum_{e_i\in\partial \Omega}\int_{e_i} (\mathbf x\cdot \mathbf n_i)  \mathrm ds\\
=& \sum_{e_i\in\partial\Omega}\int_{e_i} [(\mathbf x - \mathbf x_i + \mathbf x_i)\cdot \mathbf n_i]\mathrm ds\\
=& \sum_{e_i\in\partial\Omega}\int_{e_i} (\mathbf x_i\cdot \mathbf n_i)  \mathrm ds\\
=& \sum_{e_i\in\partial \Omega}(\mathbf x_i\cdot \mathbf n_i)\int_{e_i} \mathrm ds\\
\end{align}
$$

推广一下， 还可以把一些特殊一点的函数在高维区域函数积分， 转化为低维区域积分的问题。 

还可以把高阶的微分算子变成低阶的微分算子。 比如 Laplace 算子：
$$
\Delta u(x, y) =\nabla\cdot\nabla u =   \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2}~~~(2D),
$$

$$
\Delta u(x, y, z) =\nabla\cdot\nabla u =   \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2}~~~(3D),
$$
给定两个适当

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