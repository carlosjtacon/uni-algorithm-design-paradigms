'''
Se dispone de una tabla laberinto[1..n,1..m] con valores lógicos que representa un laberinto.
El valor TRUE indica la existencia de una pared (no se puede atravesar), mientras que FALSE 
representa una casilla recorrible. Para moverse por el laberinto, a partir de una casilla se 
puede desplazar horizontal o verticalmente, pero solo a una casilla vacía (FALSE). Los bordes 
de la tabla están completamente a TRUE excepto una casilla, que es la salida del laberinto. 

- Diseñar un algoritmo Backtracking que encuentre todos los caminos posibles que llevan a la 
salida desde una casilla inicial determinada, si es posible salir del laberinto.

- Diseñar un algoritmo Backtracking que encuentre el mejor camino posible que lleve a la salida desde una 
casilla inicial determinada, si es posible salir del laberinto.
'''

import math

def imprimir(laberinto):
    print('LABERINTO')
    for fila in laberinto:
        print(fila)

def calcularValor(laberinto):
    valor = 0
    for fila in laberinto:
        for casilla in fila:
            if casilla == '•':
                valor += 1
    
    return valor

def recorrer(laberinto, laberintoMejor, laberintoMejorValor, i, j):
    if laberinto[i][j] == 'S':
        imprimir(laberinto)

        laberintoValor = calcularValor(laberinto)
        if laberintoValor < laberintoMejorValor:
            laberintoMejorValor = laberintoValor
            laberintoMejor = laberinto

        return

    laberinto[i][j] = '•'

    # IZQUIERDA
    if laberinto[i - 1][j] == ' ' or laberinto[i - 1][j] == 'S':
        recorrer(laberinto, laberintoMejor, laberintoMejorValor, i - 1, j)

    # ARRIBA
    if laberinto[i][j + 1] == ' ' or laberinto[i][j + 1] == 'S':
        recorrer(laberinto, laberintoMejor, laberintoMejorValor, i, j + 1)
    
    # DERECHA
    if laberinto[i + 1][j] == ' ' or laberinto[i + 1][j] == 'S':
        recorrer(laberinto, laberintoMejor, laberintoMejorValor, i + 1, j)
    
    # ABAJO
    if laberinto[i][j - 1] == ' ' or laberinto[i][j - 1] == 'S':
        recorrer(laberinto, laberintoMejor, laberintoMejorValor, i, j - 1)

    laberinto[i][j] = ' '


laberintoMejor = []
laberintoMejorValor = math.inf
laberinto = [
    ['#','#','#','#','#','#','#'],
    ['#',' ',' ',' ',' ',' ','S'],
    ['#',' ','#',' ','#',' ','#'],
    ['#','O','#',' ','#',' ','#'],
    ['#',' ','#',' ','#',' ','#'],
    ['#',' ',' ',' ','#',' ','#'],
    ['#','#','#',' ',' ',' ','#'],
    ['#','#','#','#','#','#','#']
]

recorrer(laberinto, laberintoMejor, laberintoMejorValor, 3, 1)

print('EL MEJOR LABERINTO ES:')
imprimir(laberintoMejor)
