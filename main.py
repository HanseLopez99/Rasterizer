from gl import Renderer, V2, V3, color
import shaders
import random

width = 1920
height = 1080

rend = Renderer(width, height)

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

rend.glLoadModel(
    "ganesha.obj",
    translate=((width / 2) - 100, height / 2, 0),
    scale=(20, 20, 20),
)

# Poligono 1:
# (165, 380) (185, 360) (180, 330) (207, 345) (233, 330) (230, 360) (250, 380) (220, 385) (205, 410) (193, 383)
polygon1 = [
    V2(165, 380),
    V2(185, 360),
    V2(180, 330),
    V2(207, 345),
    V2(233, 330),
    V2(230, 360),
    V2(250, 380),
    V2(220, 385),
    V2(205, 410),
    V2(193, 383),
]
# Poligono 2:
# (321, 335) (288, 286) (339, 251) (374, 302)
polygon2 = [
    V2(321, 335),
    V2(288, 286),
    V2(339, 251),
    V2(374, 302),
]


# Poligono 3:
# (377, 249) (411, 197) (436, 249)
polygon3 = [V2(377, 249), V2(411, 197), V2(436, 249)]

# Poligono 4:
# (413, 177) (448, 159) (502, 88) (553, 53) (535, 36) (676, 37) (660, 52)
# (750, 145) (761, 179) (672, 192) (659, 214) (615, 214) (632, 230) (580, 230)
# (597, 215) (552, 214) (517, 144) (466, 180)
polygon4 = [
    V2(413, 177),
    V2(448, 159),
    V2(502, 88),
    V2(553, 53),
    V2(535, 36),
    V2(676, 37),
    V2(660, 52),
    V2(750, 145),
    V2(761, 179),
    V2(672, 192),
    V2(659, 214),
    V2(615, 214),
    V2(632, 230),
    V2(580, 230),
    V2(597, 215),
    V2(552, 214),
    V2(517, 144),
    V2(466, 180),
]

# Poligono 5:
# (682, 175) (708, 120) (735, 148) (739, 170)
polygon5 = [V2(682, 175), V2(708, 120), V2(735, 148), V2(739, 170)]

# Draw poligons
rend.glPolygon(polygon1, color(1, 1, 0))
rend.glPolygon(polygon2, color(0, 0, 1))
rend.glPolygon(polygon3, color(1, 0, 0))
rend.glPolygon(polygon4, color(1, 0.5, 0))
rend.glPolygon(polygon5, color(0, 0, 0))

# rend.glRender()

rend.glFinish("output.bmp")
