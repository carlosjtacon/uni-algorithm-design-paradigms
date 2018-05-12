'''
Problema 6
==========
Se tiene la tabla de sustitución que aparece a continuación que se usa de la manera siguiente: 
en una cadena cualquiera, dos caracteres consecutivos se pueden sustituir por el valor 
que aparece en la tabla, utilizando el primer carácter como fila y el segundo carácter como 
columna. Por ejemplo, se puede cambiar la secuencia ca por una b, ya que M[c,a]=b.

| |A|b|c|d|
|a|b|b|a|d|
|b|c|a|d|a|
|C|B|a|c|c|
|d|d|c|d|b|

Implementar un algoritmo Backtracking que, a partir de una cadena no vacía texto y 
utilizando la información almacenada en una tabla de sustitución M, sea capaz de encontrar 
la forma de realizar las sustituciones que permite reducir la cadena texto a un carácter final, 
si es posible.

Ejemplo: Con la cadena texto=acabada y el carácter final=d, una posible forma de sustitución 
es la siguiente (las secuencias que se sustituyen se marcan para mayor claridad): 
acabada -> acacda -> abcda -> abcd -> bcd -> bc -> d.
'''

indice = 'abcd'
tabla = [
    ['b', 'b', 'a', 'd'],
    ['c', 'a', 'd', 'a'],
    ['b', 'a', 'c', 'c'],
    ['d', 'c', 'd', 'b'],
]

cadena_inicial = 'acabada'
cadena_final = 'd'

# numero de sustituciones que tendrá que realizar siempre será la diferencia de longitudes
solucion = [-1 for char in range(len(cadena_inicial) - len(cadena_final))]
cadena = cadena_inicial

def sustitucion(solucion, cadena, k):
    global tabla, cadena_inicial, cadena_final
    if cadena == cadena_final:
        escribir(solucion)
        return True
    
    # desde cero hasta la cantidad de movimientos posibles restantes
    for i in range(len(cadena) - len(cadena_final)):
        # tomamos i como solución[k], sustituimos y recorremos 
        # en profundidad, luego deshacemos la solución[k] = -1
        solucion[k] = i
        cadena_sustituida = sustituir(cadena, i)
        exito = sustitucion(solucion, cadena_sustituida, k+1)
        solucion[k] = -1

        if exito:
            # dispersamos True para parar la recursividad
            return True

def sustituir(cadena, posicion):
    global tabla, indice
    # fusionamos la letra en la posición con la 
    # siguiente mirando el valor en la tabla
    row = cadena[posicion]
    col = cadena[posicion + 1]
    nuevo = tabla[indice.find(row)][indice.find(col)]
    # devolvemos la nueva cadena compuesta
    return cadena[:posicion] + nuevo + cadena[posicion+2:]

def escribir(solucion):
    # se imprime el array de sustituciones con cada posición en cada paso
    print(solucion)
    cadena_imprimir = cadena_inicial
    print(cadena_imprimir)
    for i in solucion:
        # la cadena va mutando y se va imprimiendo cada 
        # estado a partir de nuestro vector de solución
        cadena_imprimir = sustituir(cadena_imprimir, i)
        print(cadena_imprimir)


sustitucion(solucion, cadena, 0)
