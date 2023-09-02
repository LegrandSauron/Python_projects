import pyvista as pv
import numpy as np
def draw_heart():
    t = pv.PolyData()
    t.points = [[0, 0, 0]]

    theta = np.linspace(0, 2 * np.pi, 100)
    x = 16 *np.sin(theta) ** 3
    y = 13 * np.cos(theta) - 5 * np.cos(2 * theta) - 2 * np.cos(3 * theta) - np.cos(4 * theta)
    z = np.zeros_like(theta)
    heart_points = np.column_stack((x, y, z))

    t.points = heart_points
    heart_mesh = t.delaunay_2d()
    p = pv.Plotter()
    p.add_mesh(heart_mesh, color="red")
    p.show()
draw_heart()


