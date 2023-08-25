from gl import Renderer, V2, V3, color
import shaders
import random

width = 1000
height = 600

rend = Renderer(width, height)

rend.glClearColor(0.5, 0.5, 0.5)
rend.glClear()

rend.vertexShader = shaders.vertexShader
# rend.fragmentShader = shaders.fragmentShader
# rend.fragmentShader = shaders.flatShader
rend.fragmentShader = shaders.gouradShader

# r-3, 0, -5))end.glCamMatrix(translate=(1, 2, 0))
# rend.glLookAt(camPos=(-3, -1, 0), eyePos=(0, 0, -5))

rend.glLoadModel(
    fileName="models/model.obj",
    textureName="textures/model.bmp",
    translate=(0, 0, -5),
    rotate=(0, 0, 0),
    scale=(1.5, 1.5, 1.5),
)

rend.glRender()

rend.glFinish("output.bmp")
