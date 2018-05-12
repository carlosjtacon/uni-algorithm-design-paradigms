'''
Se dispone de un tablero M de tamaño FxC (F es la cantidad de filas y C la cantidad de columnas) 
y se pone en una casilla inicial (posx, posy) un caballo de ajedrez. El objetivo es encontrar, 
si es posible, la forma en la que el caballo debe moverse para recorrer todo el tablero de manera 
que cada casilla se utilice una única vez en el recorrido (el tablero 8x8 siempre tiene solución 
independientemente de dónde comience el caballo). El caballo puede terminar en cualquier 
posición del tablero. Un caballo tiene ocho posibles movimientos (suponiendo, claro 
está, que no se sale del tablero). 

Un movimiento entre las casillas Mij y Mpq es válido solamente si:
    - (|p–i|=1)&&(|q–j|=2), o bien si 
    - (|p–i|=2)&&(|q–j|=1),

Es decir, una coordenada cambia dos unidades y la otra una única unidad.
'''

filas = 5
columnas = 5
# fila, columna
posicion_inicial = [0, 0]

tablero = [[0 for col in range(columnas)] for row in range(filas)]
tablero[posicion_inicial[0]][posicion_inicial[1]] = 1

def caballos(tablero, nrow, ncol, k):
    global filas, columnas
    if k >= filas * columnas:
        # el numero de movimientos realizados será el numero de casillas
        escribir(tablero)
        return True

    for row in range(filas):
        for col in range(columnas):
            # recorremos el tablero hasta encontrar una casilla válida
            if valido(nrow, ncol, row, col) and tablero[row][col] == 0:
                # si la casilla está libre la ocupamos y recorremos el árbol de 
                # posibilidades en profundidad, hasta encontrar el tablero completo
                tablero[row][col] = 1
                exito = caballos(tablero, row, col, k+1)
                tablero[row][col] = 0

                if exito:
                    return True

def valido(nrow1, ncol1, nrow2, ncol2):
    # la casilla es válida si la diferencia de [filas, columnas] es [1, 2] o [2, 1]
    return (abs(nrow2 - nrow1) == 1 and abs(ncol2 - ncol1) == 2) or (abs(nrow2 - nrow1) == 2 and abs(ncol2 - ncol1) == 1)

def escribir(tablero):
    print('TABLERO')
    for row in tablero:
        print(row)


caballos(tablero, posicion_inicial[0], posicion_inicial[1], 1)
