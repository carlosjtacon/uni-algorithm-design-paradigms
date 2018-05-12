'''
Se dispone de una matriz M de tamaño FxC (F es la cantidad de filas y C la cantidad de columnas), cuyas 
celdas tienen un valor numérico entero positivo. Por ejemplo, la matriz con 4 filas y 5 columnas siguiente:

|3|2|3|2|5|
|1|2|4|5|6|
|4|3|6|2|4|
|2|5|3|4|3|

Un movimiento entre las casillas Mij y Mpq es válido solamente si (p=i && q=j+1) o bien si (p=i+1 && q=j). 
De denomina camino de la matriz como la sucesión de movimientos que llevan de la casilla M11 a la casilla 
MFC y el coste de un camino es igual a la suma de los valores de las casillas que recorre.

Diseñar un algoritmo de Programación Dinámica que obtenga el menor de los costes de todos 
los caminos de una matriz dada como parámetro.
'''

import math

def crearMatriz(nf, nc):
    return [[math.inf for x in range(nc + 1)] for y in range(nf + 1)]

matriz = [
    [3, 2, 5],
    [1, 2, 6]
]
NF = len(matriz)        # NUMERO FILAS
NC = len(matriz[0])     # NUMERO COLUMNAS

matriz_aux = crearMatriz(NF, NC)
matriz_mov = crearMatriz(NF + NC - 1, 2)

matriz_aux[0][0] = matriz[0][0]
for i in range(1, NF):
    matriz_aux[i][0] = matriz[i][0] + matriz_aux[i-1][0]
for j in range(1, NC):
    matriz_aux[0][j] = matriz[0][j] + matriz_aux[0][j-1]
for i in range(1, NF):
    for j in range(1, NC):
        matriz_aux[i][j] = matriz[i][j] + min(matriz_aux[i-1][j], matriz_aux[i][j-1])

matriz_mov[NF + NC - 2][0] = NF - 1
matriz_mov[NF + NC - 2][1] = NC - 1
i, j = NF-1, NC-1

for nmov in range(NF + NC - 3, -1, -1):
    if matriz_aux[i-1][j] <= matriz_aux[i][j-1] and i > 0:
        i -= 1
    elif i == 1 or j > 0:
        j -= 1
    
    matriz_mov[nmov][0] = i
    matriz_mov[nmov][1] = j

print('EL COSTE MINIMO ES', matriz_aux[NF-1][NC-1])
print('POR EL CAMINO:')
for row in matriz_mov:
    print(row)
print('PARA LA MATRIZ:')
for row in matriz:
    print(row)

print('MATRIZ DE COSTES:')
for row in matriz_aux:
    print(row)
