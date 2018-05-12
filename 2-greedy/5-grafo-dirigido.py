# Algoritmo de dijkstra

import math
### FUNCTIONS ###
def dijkstra(nodos, aristas):
    candidatos = nodos[:]       # VECTOR CANDIDATOS (TODOS LOS NODOS)
    visitados = [candidatos[0]]  # VECTOR SOLUCION (PRIMER NODO)
    del candidatos[0]           # ELIMINAMOS PRIMER NODO DE CANDIDATOS
    
    distancias = []  # VECTOR CON DISTANCIAS TEMPORALES (DESDE PRIMER NODO A RESTO)
    for i in range(1, len(aristas[0])):
        distancias.append(aristas[0][i])

    # VORAZ
    while candidatos:         
        min_coste = math.inf
        min_coste_nodo = None
        for coste in distancias:
            nodo = distancias.index(coste) + 1
            if coste < min_coste and nodo in candidatos:
                min_coste_nodo = nodo
                min_coste = coste

        candidatos.remove(min_coste_nodo)
        visitados.append(min_coste_nodo)
        
        d_aux = []  # VECTOR CON DISTANCIAS TEMPORALES (DESDE NODO ACTUAL A RESTO)
        for i in range(1, len(aristas[min_coste_nodo])):
            d_aux.append(aristas[min_coste_nodo][i])

        for i in range(len(distancias)):
            distancias[i] = min(distancias[i], min_coste + d_aux[i])
        
    return distancias, visitados

### MAIN ###

#     20
# |1|--->|2|
#  |     ^|
# 3|  1/  |2
#  v /    v
# |3|--->|4|
#     4

nodos = [0, 1, 2, 3]
adyacencia = [
    [0, 20, 3, math.inf],
    [math.inf, 0, math.inf, 2],
    [math.inf, 1, 0, 4],
    [math.inf, math.inf, math.inf, 0]
]

camino_minimo = dijkstra(nodos, adyacencia)
print(camino_minimo)
