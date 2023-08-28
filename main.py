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
rend.fragmentShader = shaders.yellowGlowShader

# r-3, 0, -5))end.glCamMatrix(translate=(1, 2, 0))
# rend.glLookAt(camPos=(-3, -1, 0), eyePos=(0, 0, -5))


monkey = Model(
    "models/monkey.obj",
    translate=(-10, -13, -25),
    rotate=(270, 0, 310),
    scale=(0.12, 0.12, 0.12),
)
monkey.LoadTexture("textures/monkey.bmp")
monkey.setShaders(shaders.vertexShader, shaders.thermalVisionShader)

stone = Model(
    "models/stone.obj",
    translate=(5, -5.8, -10),
    rotate=(0, 0, 0),
    scale=(0.4, 0.4, 0.4),
)
stone.LoadTexture("textures/stone.bmp")
stone.setShaders(shaders.vertexShader, shaders.infraredShader)

human = Model(
    "models/human.obj",
    translate=(4.5, -4.4, -9),
    rotate=(0, 0, 0),
    scale=(0.025, 0.025, 0.025),
)
human.LoadTexture("textures/human.bmp")
human.setShaders(shaders.vertexShader, shaders.invertColorShader)

thunderphone = Model(
    "models/thunderphone.obj",
    translate=(4, 2, -10),
    rotate=(0, 0, 0),
    scale=(0.03, 0.03, 0.027),
)
thunderphone.LoadTexture("textures/thunderphone.bmp")
thunderphone.setShaders(shaders.vertexShader, shaders.hologramShader)

thunderphone2 = Model(
    "models/thunderphone.obj",
    translate=(6, 2, -10),
    rotate=(0, 96, 0),
    scale=(0.03, 0.03, 0.027),
)
thunderphone2.LoadTexture("textures/thunderphone.bmp")
thunderphone2.setShaders(shaders.vertexShader, shaders.hologramShader)

table = Model(
    "models/table.obj",
    translate=(1.5, -5.3, -10),
    rotate=(0, 115, 0),
    scale=(1.6, 1.6, 1.6),
)
table.LoadTexture("textures/table.bmp")
table.setShaders(shaders.vertexShader, shaders.chessShader)


rend.glAddModel(monkey)
rend.glAddModel(stone)
rend.glAddModel(human)
rend.glAddModel(thunderphone)
rend.glAddModel(thunderphone2)
rend.glAddModel(table)

rend.glRender()

rend.glFinish("outputWithShaders.bmp")
