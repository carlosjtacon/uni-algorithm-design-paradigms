matriz = [[3, 2, 5], [1, 2, 6]]
NF = len(matriz) - 1  # NUMERO FILAS - 1
NC = len(matriz[0]) - 1  # NUMERO COLUMNAS - 1

### FUNCTIONS ###
# FUNCIÓN QUE DEVUELVE EL CAMINO DE COSTE MINIMO AL RECORRER
# UNA MATRIZ. LOS UNICOS MOVIMIENTOS POSIBLES SON DERECHA Y ABAJO
# LA FUNCIÓN RECIBE LA MATRIZ[m] Y LA POSICIÓN EN FILAS[fi] Y COLUMNAS[ci]
def costeMinimo(fi, ci, m):
    coste = 0
    if fi == NF and ci == NC:
        coste = m[fi][ci]
    else:
        if fi == NF:
            # EL ALGORITMO HA LLEGADO A LA ÚLTIMA FILA
            # Y SOLO TIENE QUE RECORRER COLUMNAS
            coste = m[fi][ci] + costeMinimo(fi, ci + 1, m)
        elif ci == NC:
            # EL ALGORITMO HA LLEGADO A LA ÚLTIMA COLUMNA
            # Y SOLO TIENE QUE RECORRER FILAS
            coste = m[fi][ci] + costeMinimo(fi + 1, ci, m)
        else:
            # SUMAMOS EL COSTE HASTA AHORA CON EL MINIMO 
            # DE LOS DOS COSTES POSIBLES (DERECHA Y ABAJO)
            coste = m[fi][ci] + min(costeMinimo(fi + 1, ci, m), costeMinimo(fi, ci + 1, m))    
    return coste

### MAIN ###
minimo = costeMinimo(0, 0, matriz)
print('EL COSTE MINIMO ES', minimo, 'PARA LA MATRIZ', matriz)
