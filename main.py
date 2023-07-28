from gl import Renderer, V2, V3, color
import shaders
import random

width = 1000
height = 1000

rend = Renderer(width, height)

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

rend.glLoadModel(
    "ganesha.obj",
    translate=((width / 2) + 75, height / 2, 0),
    rotate=(0, 180, 0),
    scale=(20, 20, 20),
)

rend.glRender()

# triangle = [(130, 50), (250, 500), (500, 10)]

# triangle2 = [(10, 500), (100, 500), (60, 450)]

# rend.glTriangle(triangle[0], triangle[1], triangle[2])
# rend.glTriangle(triangle2[0], triangle2[1], triangle2[2])

# triangle = [(100, 100), (450, 180), (250, 500)]

# rend.glTriangle_bc(triangle[0], triangle[1], triangle[2])

rend.glFinish("output.bmp")
