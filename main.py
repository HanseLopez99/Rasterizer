from gl import Renderer, V2, V3, color
import shaders
import random

width = 1000
height = 600

rend = Renderer(width, height)

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

# rend.glCamMatrix(translate=(0, 2.5, -6))
rend.glLookAt(camPos=(0, 7, -6.5), eyePos=(0, 0.7, -10))

rend.glLoadModel(
    fileName="models/monkey.obj",
    textureName="textures/monkey.bmp",
    translate=(0, -2.8, -10),
    rotate=(270, 0, 0),
    scale=(0.12, 0.12, 0.12),
)


rend.glRender()

rend.glFinish("shots/high-angle.bmp")
