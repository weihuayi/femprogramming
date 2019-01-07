import numpy as np

from fealpy.mesh import TriangleMesh
import matplotlib.pyplot as plt
# 网格节点数组
node = np.array([[0.0, 0.0],
                 [1.0, 0.0],
                 [1.0, 1.0],
                 [0.0, 1.0]], dtype=np.float)
# 网格单元数组
cell = np.array([[1, 2, 0],
                 [3, 0, 2]], dtype=np.int32)
NN = node.shape[0] # 网格中的节点个数
NC = cell.shape[0] # 网格中的单元个数

localEdge = np.array([[1, 2],
                      [2, 0],
                      [0, 1]], dtype=np.int32)

totalEdge = cell[:, localEdge] # shape 为 (NC, 3, 2)
totalEdge = totalEdge.reshape(-1, 2) # shape 变为 (3*NC, 2)
print('totalEdge:\n', totalEdge)

totalEdge0 = np.sort(totalEdge, axis=1)
print('totalEdge0:\n', totalEdge0)

edge0, i0, j = np.unique(totalEdge0, return_index=True, return_inverse=True, axis=0)
print('j:\n', j)

cell2edge = j.reshape(NC, 3)
print('cell2edge:\n', cell2edge)

edge = totalEdge[i0] # 最终的边数组
print('edge:\n', edge)

E = 3 # 每个三角形有 3 条边
NE = edge.shape[0] # 获得网格中边的个数, 即 `edge` 的行数
i1 = np.zeros(NE, dtype=np.int32) # 分配空间
i1[j] = range(3*NC) # totalEdge0 的行数是 3*NC, j 的长度也是 3*NC

print('i0:\n', i0)
print('i1:\n', i1)

edge2cell = np.zeros((NE, 4), dtype=np.int32)
edge2cell[:, 0] = i0//E # 得到每条边的左边单元
edge2cell[:, 1] = i1//E # 得到每条边的右边单元
edge2cell[:, 2] = i0%E  # 得到每条边的在左边单元中的局部编号
edge2cell[:, 3] = i1%E  # 得到每条边在其右边单元中的局部编号

print('edge2cell:\n', edge2cell)



mesh = TriangleMesh(node, cell)
mesh.print()
fig = plt.figure()
axes = fig.gca()
mesh.add_plot(axes)
mesh.find_node(axes, showindex=True)
mesh.find_cell(axes, showindex=True)
mesh.find_edge(axes, showindex=True)
plt.savefig('numpy-mesh-edge.png')
plt.show()
