import numpy as np 
from fealpy.mesh import QuadrangleMesh 
import matplotlib.pyplot as plt

node = np.array([[0.0, 0.0],
                 [0.5, 0.0],
                 [1.0, 0.0],
                 [0.0, 0.5],
                 [0.5, 0.5],
                 [1.0, 0.5],
                 [0.0, 1.0],
                 [0.5, 1.0],
                 [1.0, 1.0]], dtype=np.float)

cell = np.array([[0, 1, 4, 3],
                 [3, 4, 7, 6],
                 [1, 2, 5, 4],
                 [4, 5, 8, 7]], dtype=np.int32)

mesh = QuadrangleMesh(node, cell)
fig = plt.figure()
axes = fig.gca()
mesh.add_plot(axes)
mesh.find_node(axes, showindex=True)
mesh.find_cell(axes, showindex=True)
plt.show()
