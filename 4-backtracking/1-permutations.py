
'''
Problema 1
==========
Se tienen N elementos distintos almacenados en una estructura de acceso directo 
(por ejemplo, un vector con los números 1, 2, 3, 4 y 5, o la cadena abcdefg) y se 
quiere obtener todas las formas distintas de colocar esos elementos, es decir, hay 
que conseguir todas las permutaciones de los N elementos. Diseñar un algoritmo que 
use Backtracking para resolver el problema.
'''

def permutaciones(entrada, salida, validos, k):
    if k > len(entrada) - 1:
        # SI HEMOS LLEGADO AL FINAL DEL ARBOL IMPRIMIMOS LA SALIDA
        print(salida)
    else:
        for i in range(len(entrada)):
            if validos[i]:
                # INVALIDAMOS EL ACTUAL Y LO AÑADIMOS A LA SOLUCIÓN Y CONTINUAMOS RECURSIVAMENTE
                validos[i] = False
                salida[k] = entrada[i]
                permutaciones(entrada, salida, validos, k+1)
                # REVALIDAMOS EL ACTUAL PARA LAS SIGUIENTES LLAMADAS RECURSIVAS
                validos[i] = True


# VECTOR ENTRADA DEL QUE TENEMOS QUE OBTENER LAS PERMUTACIONES
entrada = [1, 2, 3, 4]
# VECTOR DE SALIDA DONDE IREMOS GENERANDO LAS DIFERENTES PERMUTACIONES POSIBLES
salida = ['?'] * len(entrada)
# VECTOR AUXILIAR DEL MISMO TAMAÑO QUE ALMACENA SI YA SE HA UTILIZADO EL VALOR DE ENTRADA
validos = [True] * len(entrada)

# PRIMERA LLAMADA A LA FUNCIÓN BACKTRAKING CON LOS VALORES DE ENTRADA ASIGNADOS
permutaciones(entrada, salida, validos, 0)
