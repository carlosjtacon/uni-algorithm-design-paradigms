
'''
Problema 3
==========
Se tiene un número de Tam cifras almacenado en una cadena de texto; por ejemplo, la cadena dato = 1151451.
Diseñar un algoritmo que mediante técnicas de Backtracking encuentre, de la manera más eficiente posible, 
todos los números distintos de N cifras que puedan formarse con los números de la cadena sin alterar su 
orden relativo dentro de la misma. Por ejemplo, si N = 4, son números válidos 1151, 1511 y 1541, 
pero no 4551 o 5411 que aunque pueden formarse con los dígitos de la cadena dato implican una reordenación.
'''

def buscarCadena(datos, solucion, n, k):
    if k == n:
        print(solucion)
    else:
        for i in range(k, len(datos)):
            solucion[k] = datos[i]
            buscarCadena(datos, solucion, n, k+1)

n = 4
datos = [1,1,5,1,4,5,1]
solucion = ['?'] * n

buscarCadena(datos, solucion, n, 0)
