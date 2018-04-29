
n = 4
solucion = [-1 for i in range(n)]

def reinas(solucion, k):
    if k >= n:
        # cuando llega al final del árbol es 
        # porque la solución es válida y definitiva
        escribir(solucion)
    else:
        for row in range(n):
            if valido(solucion, row, k):
                # si puede colocarse en la fila[row] para la columna[k] la 
                # colocamos y seguimos recorriendo el árbol en profundidad
                solucion[k] = row
                reinas(solucion, k+1)

def valido(solucion, row, k):
    for i in range(k):
        if solucion[i] == row or abs(solucion[i] - row) == abs(i - k):
            # misma fila or misma diagonal
            return False
    
    return True

def escribir(solucion):
    tablero = [[' ' for col in range(n)] for row in range(n)]
    for row in range(n):
        for col in range(n):
            if solucion[col] == row:
                tablero[row][col] = 'x'
    
    print(solucion)
    for row in tablero:
        print(row)


reinas(solucion, 0)