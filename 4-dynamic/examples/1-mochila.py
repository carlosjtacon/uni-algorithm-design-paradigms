objetos_pesos = [1, 2,  5,  6,  7]
objetos_valor = [1, 6, 18, 22, 28]
mochila_capacidad = 11

num_objetos = len(objetos_pesos)
matriz = [[-1 for col in range(mochila_capacidad + 1)] for row in range(num_objetos + 1)]
# fila = objetos disponibles | columna = capacidad de la mochila

for col in range(mochila_capacidad + 1):
    # rellenamos la primera fila de la matriz con 0
    # el equivalente a no meter ningún objeto en mochilas de capacidad 0 - mochila_capacidad
    matriz[0][col] = 0

for row in range(1, num_objetos + 1):
    # recorriendo el resto de filas de la matriz
    
    for col in range(objetos_pesos[row - 1]):
        # rellenamos copiando los valores de la fila anterior hasta 
        # llegar al la posición del peso actual
        matriz[row][col] = matriz[row - 1][col]
    
    for col in range(objetos_pesos[row - 1], mochila_capacidad + 1):
        # rellenamos el resto de columnas eligiendo el máximo entre el mismo valor 
        # que la fila anterior y misma columna o el valor del objeto actual más el valor de la matriz 
        # de la fila anterior y la columna que se corresponde a restar el peso del objeto a la capacidad
        matriz[row][col] = max(matriz[row - 1][col], matriz[row - 1][col - objetos_pesos[row - 1]] + objetos_valor[row - 1])

print('EL VALOR DE LA MOCHILA ES', matriz[num_objetos][mochila_capacidad])
for row in matriz:
    print(row)

