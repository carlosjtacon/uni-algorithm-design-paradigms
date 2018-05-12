'''
Dijkstra's Algoritm
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
'''

import math
### FUNCTIONS ###
def dijkstra(vertex, edges):
    candidates = vertex[:]       # VECTOR CANDIDATOS (TODOS LOS NODOS)
    visited = [candidates[0]]  # VECTOR SOLUCION (PRIMER NODO)
    del candidates[0]           # ELIMINAMOS PRIMER NODO DE CANDIDATOS
    
    distances = []  # VECTOR CON DISTANCIAS TEMPORALES (DESDE PRIMER NODO A RESTO)
    for i in range(1, len(edges[0])):
        distances.append(edges[0][i])

    while candidates:         
        min_cost = math.inf
        min_cost_vertex = None
        for cost in distances:
            vert = distances.index(cost) + 1
            if cost < min_cost and vert in candidates:
                min_cost_vertex = vert
                min_cost = cost

        candidates.remove(min_cost_vertex)
        visited.append(min_cost_vertex)
        
        d_aux = []  # tmp distances
        for i in range(1, len(edges[min_cost_vertex])):
            d_aux.append(edges[min_cost_vertex][i])

        for i in range(len(distances)):
            distances[i] = min(distances[i], min_cost + d_aux[i])
        
    return distances, visited

### MAIN ###

#     20
# |1|--->|2|
#  |     ^|
# 3|  1/  |2
#  v /    v
# |3|--->|4|
#     4

vertex = [0, 1, 2, 3]
ady = [
    [0, 20, 3, math.inf],
    [math.inf, 0, math.inf, 2],
    [math.inf, 1, 0, 4],
    [math.inf, math.inf, math.inf, 0]
]

min_path = dijkstra(vertex, ady)
print(min_path)
