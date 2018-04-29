'''
Problema 5
==========
Se tiene un grafo dirigido G = < N, A >, siendo N = {1, ..., n} el conjunto de nodos y A ⊆ NxN el conjunto 
de aristas. Sea M la matriz de adyacencia del grafo G, es decir, M[i, j] = TRUE si existe la arista (i, j), 
y M[i, j] = FALSE en caso contrario.

Se está interesado en saber desde qué vértices se puede acceder a cualquier otro vértice (mediante un camino 
de cualquier longitud), mediante el algoritmo de Warshall, por lo que:
    - Hay que obtener una matriz de caminos C de manera que C[i, j] = TRUE si existe un camino (de cualquier 
      longitud) entre los nodos i y j, y C[i, j] = FALSE si no existe forma de llegar de i a j.
    - Para ello, hay que ir considerando con un enfoque Bottom-Up una cantidad mayor nodos. Se empieza 
      intentando ir directamente de un nodo a otro, después se intenta encontrar los caminos que pueden 
      utilizar el vértice 1, a continuación los que pueden usar los vértices 1 y 2, después lo que se 
      consiguen con los vértices 1, 2 y 3, etc, hasta llegar a obtener los caminos que pueden utilizar 
      todos los vértices de 1 hasta n.

Implementar un método de Programación Dinámica en los términos anteriores, que obtenga la matriz de 
existencia de caminos C de un grafo teniendo como datos la cantidad de nodos n y la matriz de adyacencia M.
'''

# ORIGINAL
# '''
M = [
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 1, 0, 1]
]
# '''

# MODIFICACIÓN
'''
M = [
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 1, 0, 1]
]
'''

N = len(M)
C = [[0] * N] * N

i, j = 0, 0
for i in range(N):
    for j in range(N):
        C[i][j] = M[i][j]

k, i, j = 0, 0, 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if C[i][k] == 1 and C[k][j] == 1:
                C[i][j] = 1

print('MATRIZ M')
for f in M:
    print(f)

print('MATRIZ C')
for f in C:
    print(f)
