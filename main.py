from gl import Renderer, V2, V3, color
import shaders
import random

width = 1000
height = 600

rend = Renderer(width, height)

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

rend.glLoadModel(
    "monkey.obj",
    "monkey.bmp",
    translate=(35, 120, 0),
    rotate=(90, 90, 90),
    scale=(5, 5, 5),
)

rend.glLoadModel(
    "monkey.obj",
    "monkey.bmp",
    translate=(150, 250, 0),
    rotate=(90, 180, 90),
    scale=(5, 5, 5),
)

rend.glLoadModel(
    "monkey.obj",
    "monkey.bmp",
    translate=(850, 250, 0),
    rotate=(90, 180, 270),
    scale=(5, 5, 5),
)

rend.glLoadModel(
    "monkey.obj",
    "monkey.bmp",
    translate=(500, 120, 0),
    rotate=(180, 360, 360),
    scale=(5, 5, 5),
)


rend.glLoadModel(
    "monkey.obj",
    "monkey.bmp",
    translate=(630, 250, 0),
    rotate=(90, 180, 0),
    scale=(5, 5, 5),
)

rend.glLoadModel(
    "monkey.obj",
    "monkey.bmp",
    translate=(370, 250, 0),
    rotate=(90, 180, 180),
    scale=(5, 5, 5),
)

rend.glLoadModel(
    "monkey.obj",
    "monkey.bmp",
    translate=(960, 120, 0),
    rotate=(270, 270, 90),
    scale=(5, 5, 5),
)

rend.glRender()

# triangle = [(130, 50), (250, 500), (500, 10)]

# triangle2 = [(10, 500), (100, 500), (60, 450)]

# rend.glTriangle(triangle[0], triangle[1], triangle[2])
# rend.glTriangle(triangle2[0], triangle2[1], triangle2[2])

# triangle = [(100, 100), (450, 180), (250, 500)]

# rend.glTriangle_bc(triangle[0], triangle[1], triangle[2])

rend.glFinish("output.bmp")
