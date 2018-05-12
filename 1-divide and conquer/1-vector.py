'''
Se tiene un vector V[1..N] formado por números enteros, de manera que todos 
ellos distintos, y que están ordenados de manera creciente. Se dice que un vector 
de estas características es coincidente si tiene al menos una posición tal que es 
igual al valor que contiene el vector en esa posición. Por ejemplo, en el vector
[-14,-6,3,6,16,28,37,43] puede verse que V[3] = 3; por lo tanto, este vector es coincidente.

Diseñar un algoritmo Divide y Vencerás que determine en un orden de eficiencia no 
superior a O(log N) si un vector es coincidente, recibiendo como datos el vector 
y su tamaño.
'''

### FUNCTIONS ###

# UN VECTOR[v] ES COINCIDENTE SI EL VALOR COINCIDE CON SU POSICIÓN,
# USAMOS LA POSICION DE INICIO[xi] Y DE FIN[xf] DEL SECTOR DEL VECTOR
# IMPORTANTE QUE EL VECTOR ESTÉ ORDENADO PARA DESCARTAR UNA DE LAS PARTES
def esCoincidente(xi, xf, v):
    coincidente = False
    if xi == xf:
        if v[xi] == xi:
            coincidente = True
    else:
        mitad = (xi + xf) // 2
        if v[mitad] == mitad:
            coincidente = True
        else:
            # COMO ESTÁ ORDENADO PODEMOS ASEGURAR QUE SI NO ES COINCIDENTE,
            # DEPENDIENDO DEL VALOR Y LA POSICIÓN SOLO HABRÁ POSIBLES
            # COINCIDENTES A IZQUIERDA O DERECHA
            if v[mitad] < mitad:
                xi = mitad + 1
            else:
                xf = mitad - 1
            coincidente = esCoincidente(xi, xf, v)
    
    return coincidente



### MAIN ###

# vector = [-14, -6, 3, 6, 16, 18, 27, 43]      # NO COINCIDENTE
vector = [-20, -14, -6, 3, 6, 16, 18, 27, 43]   # SI COINCIDENTE

es_coincidente = esCoincidente(0, len(vector) - 1, vector)
print('SI ES COINCIDENTE' if es_coincidente else 'NO ES COINCIDENTE', vector)