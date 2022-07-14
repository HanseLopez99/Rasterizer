from gl import Renderer, color
import random

width = 1024
height = 512

rend = Renderer(width, height)

# rend.glClearColor(0, 0.5, 0)
# rend.glColor(1, 1, 0)
# rend.glClear()

# rend.glPoint(100, 100)

# for i in range(512):
#     rend.glPoint(i, i)

# for x in range(width):
#     for y in range(height):
#         if random.random() > 0.1:
#             rend.glPoint(x, y, color(0, 0, 0))
#         else:
#             rend.glPoint(x, y, color(1, 1, 1))

# for x in range(width):
#     for y in range(height):
#         pixelColor = color(random.random(), random.random(), random.random())
#         rend.glPoint(x, y, pixelColor)

# for x in range(width):
#     slope = 1
#     y = int(slope * x)
#     rend.glPoint(x, y)

# for x in range(width):
#     for y in range(height):
#         if random.random() > 0.99:
#             size = random.randrange(1, 3)
#             brighness = random.random() / 2 + 0.5
#             starColor = color(brighness, brighness, brighness)
#             if size == 0:
#                 rend.glPoint(x, y, starColor)
#             elif size == 1:
#                 rend.glPoint(x, y, starColor)
#                 rend.glPoint(x + 1, y, starColor)
#                 rend.glPoint(x + 1, y + 1, starColor)
#                 rend.glPoint(x, y + 1, starColor)
#             elif size == 2:
#                 rend.glPoint(x, y, starColor)
#                 rend.glPoint(x, y + 1, starColor)
#                 rend.glPoint(x, y - 1, starColor)
#                 rend.glPoint(x + 1, y, starColor)
#                 rend.glPoint(x - 1, y, starColor)

rend.glViewport(int(width / 4), int(height / 4), int(width / 2), int(height / 2))

rend.glClearColor(0, 0.5, 0)
rend.glClear()
rend.glClearViewport(color(0.5, 0, 0))

rend.glPointvp(0, 0)

rend.glFinish("output.bmp")
