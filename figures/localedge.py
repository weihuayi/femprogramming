import numpy as np 
from fealpy.mesh import TriangleMesh
import matplotlib.pyplot as plt

node = np.array([[0.0, 0.0],
                 [1.0, 0.0],
                 [0.5, np.sqrt(3)/2.0]], dtype=np.float)
cell = np.array([[0, 1, 2]], dtype=np.int32)

localEdge = np.array([[1, 2], [2, 0], [0, 1]], dtype=np.int32)

bc = (node[localEdge[:, 0]] + node[localEdge[:, 1]])/2.0

mesh = TriangleMesh(node, cell)
fig = plt.figure()
axes = fig.gca()
mesh.add_plot(axes)
mesh.find_node(axes, showindex=True)
#mesh.find_cell(axes, showindex=True)
mesh.find_node(axes, node=bc, index=np.array([0, 1, 2], dtype=np.int32), showindex=True, markersize=150, color='g')
plt.savefig('localedge.png')
plt.show()
