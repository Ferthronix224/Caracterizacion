from Matrices import Matrices

salidas = []


def ejecucion(datos, grado, alpha, beta):
    # Generación de A, indice de error, coeficientes y salidas

    matriz = Matrices(datos, grado, alpha, beta)
    A = matriz.getA()
    matrizR = matriz.matricesTotales(datos, A)
    error = matriz.error(datos, matrizR, grado)

    print(f'\nCoeficientes: {len(A) - 1}')
    for i in range(len(A)):
        print(A[i])

    print('\nSalida:')
    for j in range(len(matrizR)):
        for k in range(len(matrizR[0])):
            print(f'{matrizR[j][k]}', end=' ')
            if k == 1:
                salidas.append(matrizR[j][1])
        print()
    print(error)


def getSalidas():
    return salidas
