from gl import Renderer, V2, V3, color
import shaders
import random

width = 1280
height = 1280

rend = Renderer(width, height)

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

rend.glLoadModel(
    "ganesha.obj",
    translate=((width / 2) - 100, height / 2, 0),
    scale=(20, 20, 20),
)

rend.glRender()

rend.glFinish("output.bmp")
