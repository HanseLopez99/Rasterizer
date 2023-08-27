from gl import Renderer, Model
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
# rend.fragmentShader = shaders.gouradShader
rend.fragmentShader = shaders.yellowGlowShader

# r-3, 0, -5))end.glCamMatrix(translate=(1, 2, 0))
# rend.glLookAt(camPos=(-3, -1, 0), eyePos=(0, 0, -5))

model1 = Model(
    "models/model.obj", translate=(-3, 0, -5), rotate=(0, 0, 0), scale=(1.5, 1.5, 1.5)
)
model1.LoadTexture("textures/model.bmp")
model1.setShaders(shaders.vertexShader, shaders.yellowGlowShader)

model2 = Model(
    "models/model.obj", translate=(0, 0, -5), rotate=(0, 0, 0), scale=(1.5, 1.5, 1.5)
)
model2.LoadTexture("textures/model.bmp")
model2.setShaders(shaders.vertexShader, shaders.toonShader)

model3 = Model(
    "models/model.obj", translate=(3, 0, -5), rotate=(0, 0, 0), scale=(1.5, 1.5, 1.5)
)
model3.LoadTexture("textures/model.bmp")
model3.setShaders(shaders.vertexShader, shaders.redShader)

rend.glAddModel(model1)
rend.glAddModel(model2)
rend.glAddModel(model3)

rend.glRender()

rend.glFinish("output.bmp")
