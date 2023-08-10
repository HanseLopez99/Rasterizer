import mathLib as ml


def vertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    vpMatrix = kwargs["vpMatrix"]

    vt = [vertex[0], vertex[1], vertex[2], 1]

    # vt = vpMatrix * projectionMatrix * viewMatrix * modelMatrix @ vt

    # Use multiplyMatrix4X4 instead and matmul4 istead of @
    vt = ml.matmul4(
        ml.multiplyMatrix4X4(
            ml.multiplyMatrix4X4(
                ml.multiplyMatrix4X4(vpMatrix, projectionMatrix), viewMatrix
            ),
            modelMatrix,
        ),
        vt,
    )

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
