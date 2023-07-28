from math import isclose


def barycentricCoords(A, B, C, P):
    areaPCB = (B[1] - C[1]) * (P[0] - C[0]) + (C[0] - B[0]) * (P[1] - C[1])

    areaACP = (C[1] - A[1]) * (P[0] - C[0]) + (A[0] - C[0]) * (P[1] - C[1])

    areaABC = (C[1] - A[1]) * (B[0] - C[0]) + (A[0] - C[0]) * (B[1] - C[1])

    # areaPCB = abs(
    #     (P[0] * C[1] + C[0] * B[1] + B[0] * P[1])
    #     - (C[1] * B[0] + B[1] * P[0] + P[1] * C[0])
    # )

    # areaACP = abs(
    #     (A[0] * P[1] + C[0] * P[1] + P[0] * A[1])
    #     - (P[0] * C[1] + P[1] * A[0] + A[1] * C[0])
    # )

    # areaABC = abs(
    #     (A[0] * B[1] + B[0] * C[1] + C[0] * A[1])
    #     - (B[0] * A[1] + C[0] * B[1] + A[0] * C[1])
    # )

    if areaABC == 0:
        return None

    u = areaPCB / areaABC
    v = areaACP / areaABC
    w = 1 - u - v

    if 0 <= u <= 1 and 0 <= v <= 1 and 0 <= w <= 1 and isclose(u + v + w, 1.0):
        return u, v, w
    else:
        return None

    return u, v, w
