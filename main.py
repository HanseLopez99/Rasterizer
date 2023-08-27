from gl import Renderer, Model
import shaders
import random

width = 1000
height = 600

rend = Renderer(width, height)

rend.glClearColor(0.2, 0.2, 0.2)
rend.glBackgroundTexture("backgrounds/bosque.bmp")
rend.glClearBackground()

rend.vertexShader = shaders.vertexShader
# rend.fragmentShader = shaders.fragmentShader
# rend.fragmentShader = shaders.flatShader
# rend.fragmentShader = shaders.gouradShader
rend.fragmentShader = shaders.yellowGlowShader

# r-3, 0, -5))end.glCamMatrix(translate=(1, 2, 0))
# rend.glLookAt(camPos=(-3, -1, 0), eyePos=(0, 0, -5))

model1 = Model(
    "models/monkey.obj",
    translate=(-5, -2.8, -10),
    rotate=(270, 0, 0),
    scale=(0.12, 0.12, 0.12),
)
model1.LoadTexture("textures/monkey.bmp")
model1.setShaders(shaders.vertexShader, shaders.chessShader)

model2 = Model(
    "models/monkey.obj",
    translate=(0, -2.8, -10),
    rotate=(270, 0, 0),
    scale=(0.12, 0.12, 0.12),
)
model2.LoadTexture("textures/monkey.bmp")
model2.setShaders(shaders.vertexShader, shaders.thermalVisionShader)

model3 = Model(
    "models/monkey.obj",
    translate=(5, -2.8, -10),
    rotate=(270, 0, 0),
    scale=(0.12, 0.12, 0.12),
)
model3.LoadTexture("textures/monkey.bmp")
model3.setShaders(shaders.vertexShader, shaders.sketchedToonShader)


rend.glAddModel(model1)
rend.glAddModel(model2)
rend.glAddModel(model3)

rend.glRender()

rend.glFinish("output.bmp")
