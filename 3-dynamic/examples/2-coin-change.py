import math

tipos_monedas = [1, 4, 6]
numero_monedas = len(tipos_monedas)
cantidad = 8
matriz = [[-1 for col in range(cantidad + 1)] for row in range(numero_monedas)]

for row in range(numero_monedas):
    # el numero de monedas para devolver 0 siempre será 0
    matriz[row][0] = 0

for row in range(numero_monedas):
    for col in range(1, cantidad + 1):
        if row == 0 and col < tipos_monedas[row]:
            # si la cantidad a devolver es menor que el valor de la moneda 
            # no se podrá devolver la cantidad (inf)
            matriz[row][col] = math.inf
        elif row == 0:
            # en la primera fila vamos sumando los valores anteriores con el tipo de moneda
            matriz[row][col] = 1 + matriz[0][col - tipos_monedas[0]]
        elif col < tipos_monedas[row]:
            # mientras que la cantidad sea menor que la moneda actual 
            # copiamos los datos obtenidos en la fila anterior
            matriz[row][col] = matriz[row - 1][col]
        else:
            # si la moneda es ya mayor que la cantidad evaluamos si es mejor el uso de la moneda
            matriz[row][col] = min(matriz[row - 1][col], 1 + matriz[row][col - tipos_monedas[row]])

print(matriz[numero_monedas - 1][cantidad])
