'''
Resolver el problema anterior considerando la posibilidad de que los elementos se repitan 
entre sí (por ejemplo, el vector 1, 2, 3, 1 o la cadena acabada).
'''

def intercambiar(entrada, i, j):
    aux = entrada[i]
    entrada[i] = entrada[j]
    entrada[j] = aux

def permutacionesRepeticion(entrada, salida, k):
    if k > len(entrada) - 1:
        # SI HEMOS LLEGADO AL FINAL DEL ARBOL IMPRIMIMOS LA SALIDA
        print(salida)
    else:
        for i in range(k, len(entrada)):
            saltar_iteracion = 0
            for j in range(k, i):
                if entrada[i] == entrada[j]:
                    # SALTAMOS LA ITERACION SI YA HEMOS REALIZADO ANTES ESA PERMUTACIÓN
                    saltar_iteracion = 1
                    break
            
            if saltar_iteracion == 0:
                # AÑADIMOS EL ACTUAL A LA SOLUCIÓN E INTERCAMBIAMOS LOS VALORES PARA LA SIGUIENTE LLAMADA
                salida[k] = entrada[i]
                intercambiar(entrada, i, k)
                permutacionesRepeticion(entrada, salida, k + 1)
                # REINTERCAMBIAMOS PARA LAS SIGUIENTES LLAMADAS
                intercambiar(entrada, k, i)


# VECTOR ENTRADA DEL QUE TENEMOS QUE OBTENER LAS PERMUTACIONES
entrada = [1, 2, 3, 1]
# VECTOR DE SALIDA DONDE IREMOS GENERANDO LAS DIFERENTES PERMUTACIONES POSIBLES
salida = ['?'] * len(entrada)

# PRIMERA LLAMADA A LA FUNCIÓN BACKTRAKING CON LOS VALORES DE ENTRADA ASIGNADOS
permutacionesRepeticion(entrada, salida, 0)
