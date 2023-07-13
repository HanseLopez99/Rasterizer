import struct
from collections import namedtuple

V2 = namedtuple("Point2", ["x", "y"])


def char(c):
    # 1 byte
    return struct.pack("=c", c.encode("ascii"))


def word(w):
    # 2 bytes
    return struct.pack("=h", w)


def dword(d):
    # 4 bytes
    return struct.pack("=l", d)


def color(r, g, b):
    return bytes([int(b * 255), int(g * 255), int(r * 255)])


class Renderer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.clearColor = color(0, 0, 0)
        self.currentColor = color(1, 1, 1)
        # default color white
        self.color = color(1, 1, 1)

        self.glClear()

    def glClearColor(self, r, g, b):
        self.clearColor = color(r, g, b)

    def glColor(self, r, g, b):
        self.currentColor = color(r, g, b)

    def glPoint(self, x, y, clr=None):
        if (0 <= x < self.width) and (0 <= y < self.height):
            self.pixels[x][y] = clr or self.currentColor

    def glClear(self):
        self.pixels = [
            [self.clearColor for y in range(self.height)] for x in range(self.width)
        ]

    def glLine(self, v0, v1, clr=None):
        # Bresenham's line algorithm
        # y = mx + b

        # m = (v1.y - v0.y) / (v1.x - v0.x)
        # y = v0.y

        # for x in range(v0.x, v1.x + 1):
        #     self.glPoint(x, int(y), clr)

        x0 = int(v0.x)
        x1 = int(v1.x)
        y0 = int(v0.y)
        y1 = int(v1.y)

        # Si el punto 0 es igual al punto 1, solo dibujar un punto
        if x0 == x1 and y0 == y1:
            self.glPoint(x0, y0)
            return

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        steep = dy > dx

        # Si la linea tiene pendiente mayor a 1 o menor a -1
        # intercambiar el eje x por el y
        # Dibujar de manera vertical en vez de horizontal
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        # Si el punto inicial en x es mayor al punto final en x,
        # intercambiar los puntos para siempre dibujar de izquierda a derecha
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        offset = 0
        limit = 0.5

        m = dy / dx
        y = y0

        for x in range(x0, x1 + 1):
            if steep:
                # Dibujar de manera vertical
                self.glPoint(y, x, clr or self.currentColor)
            else:
                # Dibujar de manera horizontal
                self.glPoint(x, y, clr or self.currentColor)

            offset += m

            if offset >= limit:
                if y0 < y1:
                    y += 1
                else:
                    y -= 1

                limit += 1

    def glFinish(self, fileName):
        with open(fileName, "wb") as file:
            # Header
            file.write(bytes("B".encode("ascii")))
            file.write(bytes("M".encode("ascii")))
            file.write(dword(14 + 40 + self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(14 + 40))

            # Info header
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            # Color table
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])
