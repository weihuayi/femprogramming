# 多维数组与网格数据结构

本文将介绍如何用 Numpy 中的多维数组对象 `ndarray` 来表示存储一个三角形网格。

首先， 表示一个三角形网格需要两个基本数组

* `node`： 网格节点坐标数组， 形状为 `(NN, 2)`, 即一个 `NN` 行 `2` 列的二维矩阵。 `node[i, j]` 存储的是第 `i` 个节点的第 `j` 个坐标分量， 其中 `0<= i < NN`, `0<= j < 2`。
* `cell`： 网格单元顶点编号数组， 形状为 `(NC, 3)`, 即一个 `NC` 行 `2` 列的二维矩阵。 `cell[i, j]` 存储的是第 `i` 个单元的第 `j` 个顶点编号(即 `node` 的行号)， 其中 `0<= i < NC`, `0 <= j < 3`。注意， **这里约定三个顶点编号在 `cell[i, :]` 中存储顺序保证对应三个顶点在二维空间中是按逆时针排列的**， 这样可以保证以后计算三角形面积时一定为正的。

下面给出一个 [0,1]^2 区域的三角形网格和例子，其中有 4 个顶点、 2 个单元

```
import numpy as np 
node = np.array([[0.0, 0.0],
                 [1.0, 0.0],
                 [1.0, 1.0],
                 [0.0, 1.0]], dtype=np.float)
cell = np.array([[1, 2, 0],
                 [3, 0, 2]], dtype=np.int32)
```
代码第一行导入 `numpy` 模块， 并且用 `as` 语法重新把模块简写为 `np`。 这是一个**约定俗成的习惯**， 你平时最好也这样写, 方便大家阅读你的代码。 

接着用数组创建函数 `np.array` 创建两个数组： `node` 和 `cell`， 存储的数据类型分别指定为 `np.float`(64 位浮点型） 和 `np.int32` (32 位整型). 

在 IPython 中用运行上述代码后， 用 `type` 函数可以检查 `node` 和 `cell` 的数据类型， 都为 `numpy.ndarray` 多维数组对象。

```
In [10]: type(node)
Out[10]: numpy.ndarray

In [11]: type(cell)
Out[11]: numpy.ndarray
```

`ndarray` 对象有很多属性， 常用的有 `shape` 属性， 它是一个 `tuple` 对象， 存储了 `ndarray` 对象的形状。 `shape[i]` 就存储的是 `ndarray` 对象的第 `i` 轴 (axis) 长度。 另外， `ndarray` 还有另一个属性 `ndim`, 存储了多维数组的维数。

```
In [12]: print(node.ndim, node.shape)
2 (4, 2) # node 是 2 维数组， 第 0 轴长度为 4 ， 第 1 轴长度为 2

In [13]: print(cell.shape)
(2, 3) # cell 是 2 维数组， 第 0 轴长度为 2, 第 1 轴长度为 3
```

下面上一个 `ndarray` 的图片(来自： https://www.oreilly.com/library/view/elegant-scipy/9781491922927/assets/elsp_0105.png)， 让大家直观感受一下多维数组中**轴**的概念。
![](./figures/ndarray.png)


