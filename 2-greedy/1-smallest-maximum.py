# Se tienen n números naturales, siendo n una cantidad par, que tienen que juntarse formando 
# parejas de dos números cada una. A continuación, de cada pareja se obtiene la suma de sus 
# dos componentes, y de todos estos resultados se toma el máximo.

# Diseñar un algoritmo voraz que cree las parejas de manera que el valor máximo de las sumas de los números de cada pareja sea lo más pequeño posible, demostrando que la función de selección de candidatos usada proporciona una solución óptima.
# Ejemplo: suponiendo que los datos se encuentran en el vector siguiente [5,8,1,4,7,9]
# vamos a ver un par de formas de resolver el problema (no necesariamente la óptima): 
# Seleccionamos como pareja los elementos consecutivos
# De esta forma conseguimos las parejas (5, 8), (1, 4) y (7, 9); entonces, 
# al sumar las componentes tenemos los valores 15, 5 y 16, por lo que el resultado 
# final es 16. Seleccionamos como pareja los elementos opuestos en el vector
# Ahora tenemos las parejas (5, 9), (8, 7) y (1, 4); sumando conseguimos 14, 15 y 5, por 
# lo que el resultado final es 15 (mejor que antes).
# ¿Habrá un resultado mejor para este problema? ¿Puede generalizarse un método que nos 
# proporcione un algoritmo voraz correcto para cualquier cantidad de datos, y que además 
# sea independiente del valor de los mismos?

### FUNCTIONS ###
def quicksort(vector):
    if len(vector) == 1 or len(vector) == 0:
        return vector
    else:
        pivot = vector[0]
        i = 0
        for j in range(len(vector) - 1):
            if vector[j + 1] < pivot:
                vector[j + 1], vector[i + 1] = vector[i + 1], vector[j + 1]
                i += 1
        vector[0], vector[i] = vector[i], vector[0]
        first_part = quicksort(vector[:i])
        second_part = quicksort(vector[i + 1:])
        first_part.append(vector[i])
        return first_part + second_part

# FUNCION QUE DEVUELVE LA COMBINACIÓN MÁXIMA MÁS PEQUEÑA DE PAREJAS DE ARRAY
# HABRÁ QUE COMBINAR vector[0] CON vector[n], [1] CON [n-1]... ETC CON EL VECTOR ORDENADO
def agruparParejas(vector):

    print('VECTOR', vector)
    vector = quicksort(vector)
    print('SORTED', vector)

    maximo = -1
    for i in range(0, len(vector) // 2):
        pareja = vector[i] + vector[len(vector) - 1 - i]
        print('PAREJA', vector[i], vector[len(vector) - 1 - i], '=', pareja)
        if pareja > maximo:
            #FUNCION OBJETIVO
            maximo = pareja
        
    return maximo

### MAIN ###
vector = [5, 8, 1, 4, 7, 9]
maximo_mas_pequeño = agruparParejas(vector)

print('MÁXIMO MAS PEQUEÑO', maximo_mas_pequeño)
