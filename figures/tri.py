import numpy as np 
from fealpy.mesh import TriangleMesh
import matplotlib.pyplot as plt

node = np.array([[0.0, 0.0],
                 [1.0, 0.0],
                 [1.0, 1.0],
                 [0.0, 1.0]], dtype=np.float)
cell = np.array([[1, 2, 0],
                 [3, 0, 2]], dtype=np.int32)

mesh = TriangleMesh(node, cell)
fig = plt.figure()
axes = fig.gca()
mesh.add_plot(axes)
mesh.find_node(axes, showindex=True)
mesh.find_cell(axes, showindex=True)
plt.show()
