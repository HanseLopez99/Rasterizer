from math import isclose


# Create all matrix and vector operations


# Degress to radians
def degToRad(deg):
    return deg * 3.141592653589793 / 180


# Alternative to numpy.linalg.norm
def norm(vector):
    return (vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2) ** 0.5


def div(vector: tuple, normal: float):
    return tuple(map(lambda item: item / normal, vector))


# Alternative to numpy.cross
def cross(vector1, vector2):
    return [
        vector1[1] * vector2[2] - vector1[2] * vector2[1],
        vector1[2] * vector2[0] - vector1[0] * vector2[2],
        vector1[0] * vector2[1] - vector1[1] * vector2[0],
    ]


def dot(vector1, vector2):  # manage for all types: list, tuple, etc.
    if type(vector1) == tuple and type(vector2) == tuple:
        return (
            vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]
        )
    elif type(vector1) == list and type(vector2) == list:
        return (
            vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]
        )


# Add two matrices
def addMatrix(matrix1, matrix2):
    # Check if the matrices are the same sizes
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None
    return [
        [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))]
        for i in range(len(matrix1))
    ]


# Subtract two matrices
def subtract(*vectors):
    return tuple(map(lambda i, j: i - j, *vectors))


def colsToRows(matrix):
    aT = [[], [], [], []]

    for n in range(4):
        aT[n] = [matrix[0][n], matrix[1][n], matrix[2][n], matrix[3][n]]

    return aT


# Multiply two 4X4 matrices
def multiplyMatrix4X4(m1, m2):
    m2T = colsToRows(m2)
    mF = []

    for n in range(4):
        temp = []

        for j in range(4):
            res = 0
            for i in range(4):
                res += m1[n][i] * m2T[j][i]
            temp.append(res)
        mF.append(temp)

    return mF


def multiplyMatrix4x4AndVector(matrix, vector):
    return [
        sum([matrix[i][j] * vector[j] for j in range(len(vector))])
        for i in range(len(matrix))
    ]


# Inverse of a matrix by Gauss-Jordan method
def inverseMatrix(matrix):
    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        return None
    # Create the identity matrix of the same size as the input matrix
    identity = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
    for i in range(len(matrix)):
        identity[i][i] = 1
    # Create the augmented matrix
    augmented = [matrix[i] + identity[i] for i in range(len(matrix))]
    # Perform the Gauss-Jordan elimination
    for i in range(len(augmented)):
        # Search for the maximum value in the column
        maxValue = 0
        for j in range(i, len(augmented)):
            if abs(augmented[j][i]) > maxValue:
                maxValue = abs(augmented[j][i])
                maxRow = j
        # Swap the rows if necessary
        if maxRow != i:
            augmented[i], augmented[maxRow] = augmented[maxRow], augmented[i]
        # Divide the row by the max value
        augmented[i] = [
            augmented[i][j] / augmented[i][i] for j in range(len(augmented[i]))
        ]
        # Subtract the row from the other rows to zero out the column
        for j in range(len(augmented)):
            if j != i:
                augmented[j] = [
                    augmented[j][k] - augmented[j][i] * augmented[i][k]
                    for k in range(len(augmented[j]))
                ]
    # Return the inverse matrix
    return [
        augmented[i][len(augmented[0]) - len(matrix) :] for i in range(len(augmented))
    ]


# Operate @ for: 'list' and 'list'
def matmul4(matrix, vector):
    return [
        sum([matrix[i][j] * vector[j] for j in range(len(vector))])
        for i in range(len(matrix))
    ]


def barycentricCoords(A, B, C, P):
    # ========================= METHOD 1 =========================
    areaPCB = (B[1] - C[1]) * (P[0] - C[0]) + (C[0] - B[0]) * (P[1] - C[1])

    areaACP = (C[1] - A[1]) * (P[0] - C[0]) + (A[0] - C[0]) * (P[1] - C[1])

    areaABP = (A[1] - B[1]) * (P[0] - A[0]) + (B[0] - A[0]) * (P[1] - A[1])

    areaABC = (C[1] - A[1]) * (B[0] - C[0]) + (A[0] - C[0]) * (B[1] - C[1])

    # ========================= METHOD 2 =========================
    # areaPCB = abs(
    #     (P[0] * C[1] + C[0] * B[1] + B[0] * P[1])
    #     - (P[1] * C[0] + C[1] * B[0] + B[1] * P[0])
    # )

    # areaACP = abs(
    #     (A[0] * C[1] + C[0] * P[1] + P[0] * A[1])
    #     - (A[1] * C[0] + C[1] * P[0] + P[1] * A[0])
    # )

    # areaABP = abs(
    #     (A[0] * B[1] + B[0] * P[1] + P[0] * A[1])
    #     - (A[1] * B[0] + B[1] * P[0] + P[1] * A[0])
    # )

    # areaABC = abs(
    #     (A[0] * B[1] + B[0] * C[1] + C[0] * A[1])
    #     - (A[1] * B[0] + B[1] * C[0] + C[1] * A[0])
    # )

    if areaABC == 0:
        return None

    u = areaPCB / areaABC
    v = areaACP / areaABC
    w = areaABP / areaABC

    if 0 <= u <= 1 and 0 <= v <= 1 and 0 <= w <= 1 and isclose(u + v + w, 1.0):
        return u, v, w
    else:
        return None
