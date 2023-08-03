import mathLib as ml


def vertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]

    vt = [vertex[0], vertex[1], vertex[2], 1]

    # Operate @ for: 'list' and 'list'
    vt = ml.matmul4(modelMatrix, vt)

    vt = [vt[0], vt[1], vt[2]]

    return vt


def fragmentShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]

    if texture != None:
        color = texture.getColor(texCoords[0], texCoords[1])
    else:
        color = (1, 1, 1)
    return color
