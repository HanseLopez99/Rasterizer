from gl import Renderer, V2, V3, color
import shaders
import random

width = 1000
height = 600

rend = Renderer(width, height)

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

# r-3, 0, -5))end.glCamMatrix(translate=(1, 2, 0))
# rend.glLookAt(camPos=(-3, -1, 0), eyePos=(0, 0, -5))

rend.glLoadModel(
    fileName="models/model.obj",
    textureName="textures/model.bmp",
    translate=(-3, 0, -5),
    rotate=(0, 0, 0),
    scale=(2, 2, 2),
)

rend.glLoadModel(
    fileName="models/model.obj",
    textureName="textures/model.bmp",
    translate=(0, 0, -5),
    rotate=(0, 0, 0),
    scale=(1.5, 1.5, 1.5),
)

rend.glLoadModel(
    fileName="models/model.obj",
    textureName="textures/model.bmp",
    translate=(3, 0, -10),
    rotate=(0, 0, 0),
    scale=(2, 2, 2),
)

rend.glRender()

# triangle = [(130, 50), (250, 500), (500, 10)]

# triangle2 = [(10, 500), (100, 500), (60, 450)]

# rend.glTriangle(triangle[0], triangle[1], triangle[2])
# rend.glTriangle(triangle2[0], triangle2[1], triangle2[2])

# triangle = [(100, 100), (450, 180), (250, 500)]

# rend.glTriangle_bc(triangle[0], triangle[1], triangle[2])

rend.glFinish("output.bmp")
