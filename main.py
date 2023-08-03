from gl import Renderer, V2, V3, color
import shaders
import random

width = 1000
height = 500

rend = Renderer(width, height)

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

rend.glLoadModel(
    "model.obj",
    "model.bmp",
    translate=(250, 250, 0),
    rotate=(0, 180, 0),
    scale=(200, 200, 200),
)

rend.glLoadModel(
    "model.obj",
    "model.bmp",
    translate=(750, 250, 0),
    rotate=(0, 90, 0),
    scale=(200, 200, 200),
)

rend.glRender()

# triangle = [(130, 50), (250, 500), (500, 10)]

# triangle2 = [(10, 500), (100, 500), (60, 450)]

# rend.glTriangle(triangle[0], triangle[1], triangle[2])
# rend.glTriangle(triangle2[0], triangle2[1], triangle2[2])

# triangle = [(100, 100), (450, 180), (250, 500)]

# rend.glTriangle_bc(triangle[0], triangle[1], triangle[2])

rend.glFinish("output.bmp")
