'''
Problema 3
==========
Se tiene un sistema de billetes de distintos valores y ordenados de menor a mayor (por 
ejemplo 1, 2, 5, 10, 20, 50 y 100 euros), que se representan mediante los valores vi, con i ∈ {1, ..., N} 
(en el caso anterior, N = 7) de manera que de cada billete se tiene una cantidad finita, mayor o igual 
a cero, que se guarda en ci (siguiendo con el ejemplo, c3 = 6 representaría que hay 6 billetes de 5 euros).
                                                                                                                                                                                                                                                                                                                      6 representaría que hay 6 billetes de 5 euros).
Se quiere pagar exactamente una cierta cantidad de dinero D, utilizando para ello la menor cantidad de 
billetes posible. Se sabe que D <= ∑ ci vi, pero puede que la cantidad exacta D no sea obtenible mediante 
los billetes disponibles.

Diseñar un algoritmo con la metodología de Programación Dinámica que determine, teniendo como 
datos los valores ci, vi y D:
    - Si la cantidad D puede devolverse exactamente o no.
    - En caso afirmativo, cuantos billetes de cada tipo forman la descomposición óptima.
'''

import math

pagar = 13
billetes = [1, 2, 5, 10]
cantidad = [9, 6, 4,  3]
# billetes = [1, 2, 5, 10, 20, 50, 100]
# cantidad = [9, 6, 4,  3,  2,  1,   1]
num_billetes = len(billetes)

# array tridimensional donde las filas representasn los billetes disponibles, 
# las columnas el valor a pagar y la profundidad el numero de billetes a usar de cada tipo
matriz = [[[0 for depth in range(num_billetes)] for col in range(pagar + 1)] for row in range(num_billetes)]

for col in range(1, pagar + 1):
    if col < billetes[0]:
        # si la cantidad a devolver es menor que el valor de la moneda
        # no se podrá devolver con esa moneda (inf)
        matriz[0][col][0] = math.inf
    elif cantidad[0] > matriz[0][col - billetes[0]][0]:
        # en la primera fila vamos añadiendo billetes necesarios si tenemos unidades disponibles
        matriz[0][col][0] = 1 + matriz[0][col - billetes[0]][0]
    else:
        # no hay monedas suficientes
        matriz[0][col][0] = math.inf

for row in range(1, num_billetes):
    for col in range(1, pagar + 1):
        for depth in range(row):
            if col < billetes[depth]:
                # mientras que la pagar sea menor que la moneda actual 
                # copiamos los datos obtenidos en la fila anterior
                matriz[row][col][depth] = matriz[row - 1][col][depth]
            else:
                # si la moneda es ya mayor que la pagar evaluamos si es mejor el uso de la moneda
                matriz[row][col][depth] = min(matriz[row - 1][col][depth], 1 + matriz[row][col - billetes[depth]][depth])


print(matriz[num_billetes - 1][pagar])
