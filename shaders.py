import numpy as np


def vertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    vpMatrix = kwargs["vpMatrix"]

    vt = [vertex[0], vertex[1], vertex[2], 1]

    vt = vpMatrix * projectionMatrix * viewMatrix * modelMatrix @ vt

    vt = [vt[0, 0], vt[0, 1], vt[0, 2], vt[0, 3]]

    vt = [vt[0] / vt[3], vt[1] / vt[3], vt[2] / vt[3]]

    return vt


def fragmentShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]

    if texture != None:
        color = texture.getColor(texCoords[0], texCoords[1])
    else:
        color = (1, 1, 1)
    return color


def flatShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    dLight = kwargs["dLight"]
    normal = kwargs["normals"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture != None:
        textureColor = texture.getColor(texCoords[0], texCoords[1])
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    dLight = np.array(dLight)
    intensity = np.dot(normal, -dLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return [0, 0, 0]


def gouradShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture != None:
        tU = u * tA[0] + v * tB[0] + w * tC[0]
        tV = u * tA[1] + v * tB[1] + w * tC[1]

        textureColor = texture.getColor(tU, tV)
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    normal = [
        u * nA[0] + v * nB[0] + w * nC[0],
        u * nA[1] + v * nB[1] + w * nC[1],
        u * nA[2] + v * nB[2] + w * nC[2],
    ]

    dLight = np.array(dLight)
    intensity = np.dot(normal, -dLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return [0, 0, 0]


def toonShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture != None:
        tU = u * tA[0] + v * tB[0] + w * tC[0]
        tV = u * tA[1] + v * tB[1] + w * tC[1]

        textureColor = texture.getColor(tU, tV)
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    normal = [
        u * nA[0] + v * nB[0] + w * nC[0],
        u * nA[1] + v * nB[1] + w * nC[1],
        u * nA[2] + v * nB[2] + w * nC[2],
    ]

    dLight = np.array(dLight)
    intensity = np.dot(normal, -dLight)

    if intensity <= 0.25:
        intensity = 0.2
    elif intensity <= 0.5:
        intensity = 0.45
    elif intensity <= 0.75:
        intensity = 0.7
    elif intensity <= 1:
        intensity = 0.95

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return [0, 0, 0]


def redShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture != None:
        tU = u * tA[0] + v * tB[0] + w * tC[0]
        tV = u * tA[1] + v * tB[1] + w * tC[1]

        textureColor = texture.getColor(tU, tV)
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    normal = [
        u * nA[0] + v * nB[0] + w * nC[0],
        u * nA[1] + v * nB[1] + w * nC[1],
        u * nA[2] + v * nB[2] + w * nC[2],
    ]

    dLight = np.array(dLight)
    intensity = np.dot(normal, -dLight)

    b *= intensity
    g *= intensity
    r *= intensity

    red = (1, 0, 0)

    b *= red[2]
    g *= red[1]
    r *= red[0]

    if intensity > 0:
        return r, g, b
    else:
        return [0, 0, 0]


def yellowGlowShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]
    camMatrix = kwargs["camMatrix"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture != None:
        tU = u * tA[0] + v * tB[0] + w * tC[0]
        tV = u * tA[1] + v * tB[1] + w * tC[1]

        textureColor = texture.getColor(tU, tV)
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    normal = [
        u * nA[0] + v * nB[0] + w * nC[0],
        u * nA[1] + v * nB[1] + w * nC[1],
        u * nA[2] + v * nB[2] + w * nC[2],
    ]

    dLight = np.array(dLight)
    intensity = np.dot(normal, -dLight)

    if intensity <= 0:
        intensity = 0

    b *= intensity
    g *= intensity
    r *= intensity

    camForward = (camMatrix.item(0, 2), camMatrix.item(1, 2), camMatrix.item(2, 2))

    glowAmount = 1 - np.dot(normal, camForward)

    if glowAmount <= 0:
        glowAmount = 0

    yellow = (1, 1, 0)

    b += glowAmount * yellow[2]
    g += glowAmount * yellow[1]
    r += glowAmount * yellow[0]

    if b > 1:
        b = 1
    if g > 1:
        g = 1
    if r > 1:
        r = 1

    return r, g, b
