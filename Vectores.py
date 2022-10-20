# Operaciones aplicadas para los vectores


def matrizUnidimensional(filas):
    matriz = []
    for i in range(filas):
        matriz.append([])
    return matriz


def suma(v, u):
    lst = matrizUnidimensional(len(u))
    for i in range(len(u)):
        result = v[i] + u[i]
        lst[i] = result

    return lst


def resta(v, u):
    lst = matrizUnidimensional(len(u))

    for i in range(len(u)):
        result = v[i] - u[i]
        lst[i] = result

    return lst


def productoPunto(u, v):
    result = 0

    for i in range(len(u)):
        result += u[i] * v[i]

    return result


def productoEscalar(escalar, u):
    lst = matrizUnidimensional(len(u))

    for i in range(len(u)):
        result = u[i] * escalar
        lst[i] = result

    return lst
