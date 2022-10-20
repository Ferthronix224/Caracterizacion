import math

# Métodos requeridos para la realización del modelo matemático
def Math(alpha, k):
    sqrt = (asignacion((-1.0 * alpha), k) * math.pow(-1.0, k)) / asignacion(1.0, k)
    return sqrt


def asignacion(alpha, k):
    valor = 1.0
    if k == 0:
        valor = 1.0
    else:
        for i in range(1, k + 1):
            valor = valor * ((alpha + i) - 1)
    return valor
