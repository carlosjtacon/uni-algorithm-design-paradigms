'''
Se dispone de un vector V formado por n datos, del que se quiere encontrar el 
elemento mínimo del vector y el elemento máximo del vector. El tipo de los datos 
que hay en el vector no es relevante para el problema, pero la comparación entre 
dos datos para ver cuál es menor es muy costosa, por lo que el algoritmo para la 
búsqueda del mínimo y del máximo debe hacer la menor cantidad de comparaciones entre 
elementos posible.

Un método trivial consiste en un recorrido lineal del vector para buscar el máximo y 
después otro recorrido para buscar el mínimo, lo que requiere un total de aproximadamente 
2n comparaciones entre datos. Este método no es lo suficientemente rápido, por lo que se 
pide implementar un método con metodología Voraz que realice un máximo de 3/2n comparaciones.
'''

### FUNCTIONS ###
def getMayor(a, b):
    return a if a > b else b

def maximoMinimo(vector):
    print('VECTOR', vector)
    i = 0
    vectorMinimo = []
    vectorMaximo = []
    while i < len(vector):
        # CONSTRUIMOS DOS VECTORES, UNO DE LOS ELEMENTOS QUE HAN SIDO 
        # MAYORES Y OTRO DE LOS QUE HAN SIDO MENORES, ASÍ PODEMOS ASEGURAR 
        # QUE AHÍ SE ENCONTRARÁ EL MÁXIMO Y MÍNIMO RESPECTIVAMENTE
        
        if i == len(vector) -1:
            # ULTIMA POSICION IMPAR COMPARAMOS CON ANTERIOR
            if vector[i] > vector[i - 1]:
                vectorMaximo.append(vector[i])
            else:
                vectorMinimo.append(vector[i])
        elif vector[i] > vector[i + 1]:
            vectorMaximo.append(vector[i])
            vectorMinimo.append(vector[i + 1])
        else:
            vectorMaximo.append(vector[i + 1])
            vectorMinimo.append(vector[i])
        
        # AUMENTAMOS 2 ASÍ RECORREMOS N/2
        i += 2
    
    print('VECTOR MINIMO', vectorMinimo)
    print('VECTOR MAXIMO', vectorMaximo)

    minimo = vectorMinimo[0]
    for k in range(1, len(vectorMinimo)):
        # ENCONTRAR EL MINIMO N/2
        if vectorMinimo[k] < minimo:
            minimo = vectorMinimo[k]

    maximo = vectorMaximo[0]
    for j in range(1, len(vectorMaximo)):
        # ENCONTRAR EL MAXIMO N/2
        if vectorMaximo[j] > maximo:
            maximo = vectorMaximo[j]

    return [minimo, maximo]


### MAIN ###
v = [10, 4, 5, 11, 1, -1, 23]
resultado = maximoMinimo(v)
print('EL MINIMO ES', resultado[0], 'Y EL MAXIMO ES', resultado[1])
