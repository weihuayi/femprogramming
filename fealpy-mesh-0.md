# FEALPy 中的网格对象

在偏微分方程数值计算程序设计中， 网格是最核心的数据结构，是下一步实现数值离散方法的
基础。用节点数组 `node` 和单元数组 `cell`, 就可以表示一个网格，其它的如边数
组 `edge`、 面数组 `face` 及拓扑关系数组都可以由 `cell` 生成。在这里我们把
`node`、`edge`、`face` 和 `cell` 通称为网格的实体 `entity`。 关于网格数据结构的
数组化表示与生成核心算法，请参见下面的两篇文章：

* [网格数据结构的数组化表示：node 和 cell]()
* [网格数据结构的数组化表示：edge]()

下面将着重介绍 FEALPy 中的 `mesh` 模块。`mesh` 模块中实现了偏微分方程数值计算
中常见网格类型，包括：

| 网格类名           |代表网格类型 |
| :-----------       | :-----|
| `IntervalMesh`     | 区间网格|
| `TriangleMesh`     | 三角形网格|
| `QuadrangleMesh`   | 四边形网格|
| `TetrahedronMesh`  | 四面体网格|
| `HexahedronMesh`   | 六面体网格|
| `PolygonMesh`      | 多边形网格|
| `PolyhedronMesh`   | 多面体网格|
| `StructureQuadMesh`| 结构四边形网格|
| `StructureHexMesh` | 结构六面体体网格|
| `Tritree`          | 三角形树结构网格|
| `Quadtree`         | 四边形树结构网格，即四叉树|
| `Octree`           | 六面体树结构网格，即八叉树|


上面的网格类都可以通过类似于下面的语法导入：

```
from fealpy.mesh import TriangleMesh
from fealpy.mesh import QuadrangleMesh
from fealpy.mesh import Tritree
```

注意上面的 `StructureQuadMesh` 和 `StructureHexMesh` 的实现与其它非结构网格类的
内部实现是完全不同的，它们的实现充分考虑了结构网格的特点。但它们的接口和其它非结
构网格基本是一样的，在使用过程中用户不用关心底层的实现。 


FEALPy 中的所有网格类的成员变量和成员函数都遵循同样的命名约定，尽量做到与维数和
网格类型无关。基本成员变量的约定为：

| 变量名 | 含义 |
| :----- | :----- |
| `NN`   | 节点的个数 
| `NC`   | 单元的个数 
| `NE`   | 边的个数 
| `NF`   | 面的个数 
| `NCV`  | 单元顶点的个数
| `NFV`  | 面的顶点的个数
| `GD`   | 空间维数
| `TD`   | 拓扑维数
| `node` | 节点数组， 形状为 `(NN, GD)`
| `cell` | 单元数组， 形状为 `(NC, NCV)` 
| `edge` | 边数组， 形状为 `(NE, 2)`
| `face` | 面数组， 形状为 `(NF, NFV)`
| `ds`   | 网格的拓扑数据结构对象， 所有的拓扑关系数据都由其管理和获取 
| `nodedata` | 字典数组， 存储定义在节点上的数据， 默认为空字典 `{}`
| `celldata` | 字典数组， 存储定义在单元上的数据， 默认为空字典 `{}`
| `edgedata` | 字典数组， 存储定义在边上的数据， 默认为空字典 `{}`
| `facedata` | 字典数组， 存储定义在面上的数据， 默认为空字典 `{}`
| `itype`    | 存储网格所用的整型数据类型
| `ftype`    | 存储网格所有的浮点型数据类型

因为多边形网格的每个单元顶点个数不一样，所以 `PolygonMesh` 中的 `cell` 数组
`cell` 数组是一个一维数组， 另外还多增加了一个长度为 `NC+1` 一维数组
`cellLocation`, `cell[cellLocation[i]:cellLocation[i+1]]` 存储第 `i` 个单元的顶
点编号， 注意这里的顶点编号是按逆时针排序。


假设有网格对象 `mesh`, 它一般都有如下接口：

| 成员函数名 | 功能 
| :--------- | :------
| `mesh.geo_dimension()` | 获得网格的几何维数 
| `mesh.top_dimension()` | 获得网格的拓扑维数 
| `mesh.number_of_nodes()` | 获得网格的节点个数 
| `mesh.number_of_cells()` | 获得网格的单元个数 
| `mesh.number_of_edges()` | 获得网格的边个数 
| `mesh.number_of_faces()` | 获得网格的面的个数 
| `mesh.number_of_entities(etype)` | 获得 `etype` 类型实体的个数 
| `mesh.entity(etype)`  | 获得 `etype` 类型的实体
| `mesh.entity_measure(etype)` | 获得 `etype` 类型的实体的测度 
| `mesh.entity_barycenter(etype)` | 获得 `etype` 类型的实体的重心
| `mesh.integrator(i)` | 获得该网格上的第 `i` 个积分公式  
| `mesh.bc_to_points(bc)` | 转换重心坐标 `bc` 到实际单元上的点


上面的 `etype` 可以取 0, 1, 2, 3 或者字符串 `cell`, `node`, `edge`, `face`
， 当然对于二维网格 `etype` 就不能取 3 或者 `face`。 

网格对象 `mesh` 的成员变量 `ds` 有如下的接口：

| 成员函数名 | 功能 
| :--------- | :------
| `cell2cell = mesh.ds.cell_to_cell(...)`   | 单元与单元的邻接关系
| `cell2face = mesh.ds.cell_to_face(...)`   | 单元与面的邻接关系 
| `cell2edge = mesh.ds.cell_to_edge(...)`   | 单元与边的邻接关系 
| `cell2node = mesh.ds.cell_to_node(...)`   | 单元与节点的邻接关系 
| `face2cell = mesh.ds.face_to_cell(...)`   | 面与单元的邻接关系 
| `face2face = mesh.ds.face_to_face(...)`   | 面与面的邻接关系 
| `face2edge = mesh.ds.face_to_edge(...)`   | 面与边的邻接关系 
| `face2node = mesh.ds.face_to_node(...)`   | 面与节点的邻接关系 
| `edge2cell = mesh.ds.edge_to_cell(...)`   | 边与单元的邻接关系 
| `edge2face = mesh.ds.edge_to_face(...)`   | 边与面的邻接关系 
| `edge2edge = mesh.ds.edge_to_edge(...)`   | 边与边的邻接关系 
| `edge2node = mesh.ds.edge_to_node(...)`   | 边与节点的邻接关系 
| `node2cell = mesh.ds.node_to_cell(...)`   | 节点与单元的邻接关 
| `node2face = mesh.ds.node_to_face(...)`   | 节点与面的邻接关系
| `node2edge = mesh.ds.node_to_edge(...)`   | 节点与边的邻接关系
| `node2node = mesh.ds.node_to_node(...)`   | 节点与节点的邻接关
| `isBdNode = mesh.ds.boundary_node_flag()` | 一维逻辑数组，标记边界节点 
| `isBdEdge = mesh.ds.boundary_edge_flag()` | 一维逻辑数组，标记边界边 
| `isBdFace = mesh.ds.boundary_face_flag()` | 一维逻辑数组，标记边界面
| `isBdCell = mesh.ds.boundary_cell_flag()` | 一维逻辑数组，标记边界单元
| `bdNodeIdx = mesh.ds.boundary_node_index()` | 一维整数数组，边界节点全局编号
| `bdEdgeIdx = mesh.ds.boundary_edge_index()` | 一维整数数组，边界边全局编号
| `bdFaceIdx = mesh.ds.boundary_face_index()` | 一维整数数组，边界面全局编号
| `bdCellIdx = mesh.ds.boundary_cell_index()` | 一维整数数组，边界单元全局编号

注意，上面接口中的 `...` 表示有默认的参数，可以根据需要来设定。也要注意返回的
实体间邻接关系， 默认可能是二维数组， 也可能是稀疏矩阵。 在使用过程中，用户要根
据网格的类型或者实际需要， 来控制返回邻接关系的数据类型。

如果 `mesh` 是一个三角形网格类 `TriangleMesh` 的对象， 则 

```
# 下面的语句 cell2cell 为形状为 (NC, 3) 
# 的数组。 注意， 如果 cell2cell[i, j] == i,
# 则表示第 i 个单元的第 j 个邻居是区域外部
cell2cell = mesh.ds.cell_to_cell()

# 下面语句 cell2cell 为形状为 (NC, NC) 的稀疏矩阵
cell2cell = mesh.ds.cell_to_cell(return_sparse=True) 

# 下面的语句返回的 cell2cell 是一个一维数组
# 再加一个 cell2cellLocation, 则第 i 个单元
# 邻接单元的编号为 cell2cell[cell2cellLocation[i]:cell2cellLocation[i+1]]
cell2cell， cell2cellLocation = mesh.ds.cell_to_cell(return_array=True) 
```

当然上面介绍的接口只是一部分常用接口，更多接口可以自己去代码中探索发现。 

最后， 还是以一个例子为结尾， 你可以在 ipython3 中一行行测试下 面的命令， 可以先
把网格画出来， 再获取网格中的各种数据，并和网格图进行对比。 这样可以帮助你更快
更好理解 FEALPy 中网格的用法。 

```
import numpy as np
import matplotlib.pyplot as plt
from fealpy.mesh import TriangleMesh

# [0, 1]^2 区域上的网格
node = np.array([
    (0, 0), 
    (1, 0), 
    (1, 1),
    (0, 1)], dtype=np.float)
cell = np.array([
    (1, 2, 0),
    (3, 0, 2)], dtype=np.int)

# 建立三角形网格对象
tmesh = TriangleMesh(node, cell) 

# 一致加密一次
tmesh.uniform_refine()


# 获得节点数组
node = tmesh.entity('node')

# 获得边数组
edge = tmesh.entity('edge')      

# 获得单元数组
cell = tmesh.entity('cell')

# 获得单元的面积
cellArea = tmesh.entity_measure('cell')

# 获得边的长度
edgeLength = tmesh.entity_measure('edge')  

# 获得单元的重心
cellBC = tmesh.entity_barycenter('cell')

# 获得边的重心
edgeBC = tmesh.entity_barycenter('edge')

# 获得每条边的单位法向和切向
n, t = tmesh.edge_frame() 

# 获得单元的邻接关系数组, 形状为 (NE, 3)
cell2cell = tmesh.ds.cell_to_cell() 

# 获得边与单元的邻接关系数组，形状为 (NE, 4)
edge2cell = tmesh.ds.edge_to_cell()

# 打印网格的信息
tmesh.print() 

# 建立画图对象
fig = plt.figure() 
# 获得坐标系
axes = fig.gca()   
# 在坐标系中画网格
tmesh.add_plot(axes) 
# 显示所有节点编号
tmesh.find_node(axes, showindex=True) 
# 显示所有边的编号
tmesh.find_edge(axes, showindex=True)
# 显示所有单元的编号
tmesh.find_cell(axes, showindex=True)
plt.show()
```
