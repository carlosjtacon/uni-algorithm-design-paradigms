'''
Shrek, Asno y Dragona llegan a los pies del altísimo castillo de Lord Farquaad para 
liberar a Fiona de su encierro. Como sospechaban que el puente levadizo estaría vigilado 
por numerosos soldados se han traído muchas escaleras, de distintas alturas, con la esperanza 
de que alguna de ellas les permita superar la muralla; pero ninguna escalera les sirve 
porque la muralla es muy alta. Shrek se da cuenta de que, si pudiese combinar todas las 
escaleras en una sola, conseguiría llegar exactamente a la parte de arriba y poder entrar 
al castillo.
Afortunadamente las escaleras son de hierro, así que con la ayuda de Dragona van a 
“soldarlas”. Dragona puede soldar dos escaleras cualesquiera con su aliento de fuego, 
pero tarda en calentar los extremos tantos minutos como metros suman las escaleras a soldar. 
Por ejemplo, en soldar dos escaleras de 6 y 8 metros tardaría 6 + 8 = 14 minutos. Si a esta 
escalera se le soldase después una de 7 metros, el nuevo tiempo sería 14 + 7 = 21 minutos, 
por lo que habrían tardado en hacer la escalera completa un total de 14 + 21 = 35 minutos.
Diseñar un algoritmo eficiente que encuentre el mejor coste y manera de soldar las escaleras 
para que Shrek tarde lo menos posible es escalar la muralla, indicando las estructuras de 
datos elegidas y su forma de uso. Se puede suponer que se dispone exactamente de las 
escaleras necesarias para subir a la muralla (ni sobran ni faltan), es decir, que el dato 
del problema es la colección de medidas de las “miniescaleras” (en la estructura de datos 
que se elija), y que solo se busca la forma óptima de fundir las escaleras.
'''

### FUNCTIONS ###

# FUNCION QUE ORDENA LAS ESCALERAS DE MENOR A MAYOR PARA MINIMIZAR EL TIEMPO DE SOLDADO
def soldarEscaleras(escaleras):
    total = 0
    escaleras_ordenadas = []
    while len(escaleras) != 0:
        mejor = 0
        for i in range(1, len(escaleras)):
            if escaleras[i] < escaleras[mejor]:
                mejor = i

        total += total + escaleras[mejor]
        escaleras_ordenadas.append(escaleras[mejor])
        del escaleras[mejor]

    print('SELECCION', escaleras_ordenadas)
    return total


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

# CON QUICKSORT O MERGESORT MEJORAMOS LA COMPLEJIDAD DEL ALGORITMO
def soldarEscalerasQuicksort(escaleras):
    total = 0
    escaleras_ordenadas = quicksort(escaleras)
    for i in range(0, len(escaleras_ordenadas)):
        total += total + escaleras_ordenadas[i]

    print('QUICKSORT', escaleras_ordenadas)
    return total


### MAIN ###
escaleras = [10, 4, 2, 5, 9]
total = soldarEscaleras(escaleras)
# total = soldarEscalerasQuicksort(escaleras)

print('EL TIEMPO TOTAL DE SOLDAR LAS ESCALERAS ES', total)
