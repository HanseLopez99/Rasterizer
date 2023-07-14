from gl import Renderer, V2, V3, color
import shaders
import random

width = 1920
height = 1080

rend = Renderer(width, height)

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

verts = [V3(0, 0, 0), V3(50, 0, 0), V3(25, 40, 0)]

rend.glAddVertices(verts)

rend.glModelMatrix(translate=(width / 2, height / 2, 0), scale=(5, 3, 1))

rend.glRender()

rend.glFinish("output.bmp")
