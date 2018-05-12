'''
Alí Babá ha conseguido entrar en la cueva de los ciento un mil ladrones, y ha llevado consigo su camello 
junto con dos grandes alforjas; el problema es que se encuentra con tanto tesoro que no sabe ni qué llevarse. 
Los tesoros son joyas talladas, obras de arte, cerámica... es decir, son objetos únicos que no pueden 
partirse ya que entonces su valor se reduciría a cero.
 
Afortunadamente los ladrones tienen todo muy bien organizado y se encuentra con una lista de todos los 
tesoros que hay en la cueva, donde se refleja el peso de cada pieza y su valor en el mercado de Damasco. 
Por su parte, Alí sabe la capacidad de peso que tiene cada una de las alforjas.

Diseñar un algoritmo que, teniendo como datos los pesos y valor de las piezas, y la capacidad de las 
dos alforjas, permita obtener el máximo beneficio que podrá sacar Alí Babá de la cueva de las maravillas.
'''

import math

def mochila(matriz, objetos, capacidad):

    num_objetos = len(objetos[0])

    for col in range(capacidad + 1):
        # rellenamos la primera fila de la matriz con 0
        # el equivalente a no meter ningún objeto en mochilas de capacidad [0 - capacidad]
        matriz[0][col] = 0

    for row in range(1, num_objetos + 1):
        # recorriendo el resto de filas de la matriz

        for col in range(objetos[0][row - 1]):
            # rellenamos copiando los valores de la fila anterior hasta
            # llegar al la posición del peso actual
            matriz[row][col] = matriz[row - 1][col]

        for col in range(objetos[0][row - 1], capacidad + 1):
            # rellenamos el resto de columnas eligiendo el máximo entre el mismo valor
            # que la fila anterior o el valor del objeto actual más el valor de la matriz
            # de la fila anterior y la columna que se corresponde a restar el peso del objeto a la capacidad
            matriz[row][col] = max(matriz[row - 1][col], objetos[1][row - 1] + matriz[row-1][col - objetos[0][row - 1]])

    return matriz[num_objetos][capacidad]

# APLICAR EL ALGORITMO DE LA MOCHILA DINAMICO PRIMERO A LA MOCHILA PEQUENA,
# PORQUE SI APLICAMOS PRIMERO A LA GRANDE OBTENEMOS EL RESULTADO INCORRECTO

alforjas_capacidad = [6, 14]
tesoros = [
    [1, 2,  5,  6,  7], # [0] peso
    [1, 6, 15, 22, 28]  # [1] valor
]

alforja_pequeña = [[-1 for col in range(min(alforjas_capacidad) + 1)] for row in range(len(tesoros[0]) + 1)]
valor_pequeña = mochila(alforja_pequeña, tesoros, min(alforjas_capacidad))

# ELIMINAR LOS TESOROS QUE YA HAYAMOS METIDO EN LA ALFORJA PEQUENA
col = min(alforjas_capacidad)
row = len(tesoros[0])
delete =[]
while col != 0:
    if alforja_pequeña[row][col] == alforja_pequeña[row - 1][col]:
        row -= 1
    else:
        delete.append(row-1)
        col -= tesoros[0][row-1]
        row -= 1

for i in delete:
    del tesoros[0][i]
    del tesoros[1][i]
# FIN ELIMINAR TESOROS

alforja_grande = [[-1 for col in range(max(alforjas_capacidad) + 1)] for row in range(len(tesoros[0]) + 1)]
valor_grande = mochila(alforja_grande, tesoros, max(alforjas_capacidad))

print('EL VALOR TOTAL DE AMBAS ALFORJAS ES', valor_grande + valor_pequeña)
print('ALFORJA PEQUEÑA', min(alforjas_capacidad))
for linea in alforja_pequeña:
    print(linea)
print('ALFORJA GRANDE', max(alforjas_capacidad))
for linea in alforja_grande:
    print(linea)
