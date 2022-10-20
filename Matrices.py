import Operaciones as operaciones
import math
from Ortogonal import Ortogonal as ort


class Matrices:
    def __init__(self, datos, grado, alpha, beta):
        self.datos = datos
        self.grado = grado
        self.alpha = alpha
        self.beta = beta
        self.matrizA = []
        self.matrizB = []
        self.h = []
        self.A = []
        self.dOrtho = []
        self.dV = []
        self.MatrizDatos()

    def getMatrizA(self):
        return self.matrizA

    def getMatrizB(self):
        return self.matrizB

    def getH(self):
        return self.h

    def getA(self):
        return self.A

    def matrizUnidimensional(self, filas):
        matriz = []
        for i in range(filas):
            matriz.append([])
        return matriz

    def matrizBidimensional(self, filas, columnas):
        matriz = []
        for i in range(filas):
            matriz.append([])
            for j in range(columnas):
                matriz[i].append([])
        return matriz

    def calculaMatrizA(self):
        self.matrizA = self.matrizUnidimensional(len(self.h))
        for i in range(len(self.h)):
            self.matrizA[i] = self.matrizB[i] / self.h[i]

    def calculaMatrizB(self, orth):
        self.matrizB = self.matrizUnidimensional(self.grado + 1)

        for k in range(self.grado + 1):
            dSuma = 0.0
            for i in range(len(self.datos)):
                dSuma += self.datos[i][0] * orth[k][i] * self.datos[i][2]
            self.matrizB[k] = dSuma

    def h_k(self, orth):
        self.h = self.matrizUnidimensional(self.grado + 1)
        for k in range(self.grado + 1):
            suma = 0.0
            for i in range(len(self.datos)):
                suma += self.datos[i][0] * (math.pow(orth[k][i], 2))
            self.h[k] = suma

    def operacionMatrizA(self, bks):
        self.A = self.matrizUnidimensional(len(self.matrizA))
        for k in range(len(self.A) - 1):
            suma = 0.0
            for s in range(k + 1, self.grado + 1):
                suma += self.matrizA[s] * bks[s][k]
            self.A[k] = self.matrizA[k] + suma
        self.A[len(self.matrizA) - 1] = self.matrizA[-1]

    def Orto(self, v):
        rOrtogonal = ort(v)
        rOrtogonal.ejecutar()
        u = rOrtogonal.getMatrizOrtogonal()
        proy = rOrtogonal.getProyecta()
        dOrtho = u
        aux = proy[-1]
        bks = self.matrizBidimensional(len(proy), (len(aux) + 1))

        for i in range(len(bks)):
            bks[i][i] = 1.0

        for k in range(1, len(proy)):
            a = proy[k]
            for s in range(k):
                suma = 0.0
                for t in range((k - s - 1) + 1):
                    suma += a[k - (t + 1)] * bks[k - (t + 1)][s]
                bks[k][s] = suma
        self.calculaMatrizB(dOrtho)
        self.h_k(dOrtho)
        self.calculaMatrizA()
        self.operacionMatrizA(bks)
        return u

    def matricesTotales(self, datos, matrizA):
        matrizR = self.matrizBidimensional(len(datos), 2)
        for i in range(len(datos)):
            matrizR[i][0] = datos[i][1]
            suma = 0.0
            for j in range(len(matrizA)):
                print(f'({datos[i][1]} * {matrizA[j]}) + ', end='')
                suma += operaciones.calculo(datos[i][1], self.alpha, self.beta, j) * matrizA[j]
            print()
            matrizR[i][1] = suma

        return matrizR

    def error(self, datos, dMatrizR, m):
        suma = 0.0
        for i in range(len(datos)):
            suma += math.pow(datos[i][2] - dMatrizR[i][1], 2)
        valor = suma / (len(datos) - (m + 1))
        if valor == 0 or valor < 0:
            return 0
        else:
            return math.sqrt(valor)

    def MatrizDatos(self):
        v = self.matrizBidimensional(self.grado + 1, len(self.datos))
        print('Datos de la matriz')
        for i in range(self.grado + 1):
            for j in range(len(self.datos)):
                v[i][j] = operaciones.calculo(self.datos[j][1], self.alpha, self.beta, i)
        print(len(v) * len(v[0]))
        self.Orto(v)

        return v
