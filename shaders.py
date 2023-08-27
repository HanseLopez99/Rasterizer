import numpy as np


def vertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    vpMatrix = kwargs["vpMatrix"]

    vt = [vertex[0], vertex[1], vertex[2], 1]

    vt = vpMatrix * projectionMatrix * viewMatrix * modelMatrix @ vt

    vt = vt.tolist()[0]

    vt = [vt[0] / vt[3], vt[1] / vt[3], vt[2] / vt[3]]

    return vt


def fatVertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    vpMatrix = kwargs["vpMatrix"]
    normal = kwargs["normal"]

    blowAmount = 0.2

    vt = [
        vertex[0] + (normal[0] * blowAmount),
        vertex[1] + (normal[1] * blowAmount),
        vertex[2] + (normal[2] * blowAmount),
        1,
    ]

    vt = vpMatrix * projectionMatrix * viewMatrix * modelMatrix @ vt

    vt = vt.tolist()[0]

    vt = [vt[0] / vt[3], vt[1] / vt[3], vt[2] / vt[3]]

    return vt


def fragmentShader(**kwargs):
    tA, tB, tC = kwargs["texCoords"]
    texture = kwargs["texture"]
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
    return r, g, b


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
    modelMatrix = kwargs["modelMatrix"]

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
        0,
    ]

    normal = modelMatrix @ normal
    normal = normal.tolist()[0]
    normal = [normal[0], normal[1], normal[2]]

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


def chessShader(**kwargs):
    tA, tB, tC = kwargs["texCoords"]
    u, v, w = kwargs["bCoords"]
    size = 10  # Adjust for checker size

    tU = u * tA[0] + v * tB[0] + w * tC[0]
    tV = u * tA[1] + v * tB[1] + w * tC[1]

    if (int(tU * size) % 2) ^ (int(tV * size) % 2):
        return (1, 1, 1)  # white
    else:
        return (0, 0, 0)  # black


def sketchedToonShader(**kwargs):
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

    if intensity < 0.2:
        return [0, 0, 0]  # Dark color for the outlines

    # Toon shading bands
    if intensity < 0.5:
        intensity = 0.4
    elif intensity < 0.8:
        intensity = 0.7
    else:
        intensity = 1.0

    b *= intensity
    g *= intensity
    r *= intensity

    # Adding a little noise for the "sketched" effect.
    noiseAmount = 0.05 * np.random.randn()
    r += noiseAmount
    g += noiseAmount
    b += noiseAmount

    return r, g, b


def thermalVisionShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]

    if texture != None:
        tU = u * tA[0] + v * tB[0] + w * tC[0]
        tV = u * tA[1] + v * tB[1] + w * tC[1]
        textureColor = texture.getColor(tU, tV)
    else:
        textureColor = [1, 1, 1]

    normal = [
        u * nA[0] + v * nB[0] + w * nC[0],
        u * nA[1] + v * nB[1] + w * nC[1],
        u * nA[2] + v * nB[2] + w * nC[2],
    ]

    dLight = np.array(dLight)
    intensity = np.dot(normal, -dLight)

    # Convert the intensity to a thermal color based on a gradient.
    if intensity < 0.25:
        color = [0, 0, 0.5 + intensity]  # Dark blue to light blue
    elif intensity < 0.5:
        color = [0, 4 * intensity - 1, 1]  # Blue to green
    elif intensity < 0.75:
        color = [4 * intensity - 2, 1 - (4 * intensity - 2), 0]  # Green to yellow
    else:
        color = [1, 4 * intensity - 3, 0]  # Yellow to red

    # Modulate with the texture color if present
    color[0] *= textureColor[0]
    color[1] *= textureColor[1]
    color[2] *= textureColor[2]

    return color
