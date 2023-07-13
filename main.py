from gl import Renderer, V2, color
import random

width = 1920
height = 1080

rend = Renderer(width, height)

# rend.glClearColor(0, 0.5, 0)
# rend.glColor(1, 1, 0)
# rend.glClear()

# rend.glPoint(100, 100, rend.glColor(1, 0, 0))

# for x in range(0, width, 10):
#     for y in range(0, height, 10):
#         rend.glLine(V2(0, 0), V2(x, height - 1))
#         rend.glLine(V2(0, 0), V2(width - 1, y))

# for x in range(width):
#     for y in range(height):
#         pixelColor = rend.glColor(random.random(), random.random(), random.random())
#         rend.glPoint(x, y, pixelColor)

# Stars
for x in range(width):
    for y in range(height):
        if random.random() > 0.99:
            size = random.randrange(1, 3)
            brighness = random.random() / 2 + 0.5
            starColor = color(brighness, brighness, brighness)
            if size == 0:
                rend.glPoint(x, y, starColor)
            elif size == 1:
                rend.glPoint(x, y, starColor)
                rend.glPoint(x + 1, y, starColor)
                rend.glPoint(x + 1, y + 1, starColor)
                rend.glPoint(x, y + 1, starColor)
            elif size == 2:
                rend.glPoint(x, y, starColor)
                rend.glPoint(x, y + 1, starColor)
                rend.glPoint(x, y - 1, starColor)
                rend.glPoint(x + 1, y, starColor)
                rend.glPoint(x - 1, y, starColor)


rend.glFinish("output.bmp")
