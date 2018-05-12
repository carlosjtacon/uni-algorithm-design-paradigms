'''
Se define una secuencia de bits A como una sucesión A = {a1, a2, ..., an} donde cada ai puede tomar el 
valor 0 o el valor 1, y n es la longitud de la secuencia A. A partir de una secuencia se define una 
subsecuencia X de A como X = {x1, x2, ..., xk}, siendo k ≤ n, de forma que X puede obtenerse eliminando 
algún elemento de A pero respetando el orden en que aparecen los bits; por ejemplo, 
si A = {1, 0, 1, 1, 0, 0, 1} podríamos obtener como subsecuencias {1, 1, 1, 0, 1}, {1, 0, 1} o {1, 1, 0, 0} 
entre otras, pero nunca se podría conseguir la subsecuencia {1, 0, 0, 1, 1}.

Dadas dos secuencias A y B, se denomina a X una subsecuencia común de A y B cuando X es subsecuencia 
de A y además es subsecuencia de B. (aunque puede que se hayan obtenido quitando distintos elementos en A 
que B, e incluso distinta cantidad). Suponiendo las secuencias A = {0, 1, 1, 0, 1, 0, 1, 0} y 
B = {1, 0, 1, 0, 0, 1, 0, 0, 1}, una subsecuencia común sería X = {1, 1, 0, 1}, pero no podría 
serlo X = {0, 1, 1, 1, 0}.

Se desea determinar la subsecuencia común de dos secuencias A y B que tenga la longitud máxima, para lo 
que se pide:
    - Explicar con detalle la forma de resolver el problema, y
    - Hacer un algoritmo de Programación Dinámica que obtenga la longitud máxima posible y una 
      secuencia común de dicha longitud.
'''

A = [0, 1, 1, 0, 1, 0, 1, 0]
B = [1, 0, 1, 0, 0, 1, 0, 0, 1]
N, M = len(A), len(B)

# A deberá ser de longitud mayor o igual a B (por el método usado para identificar 
# la secuencia a partir de la matriz), si no es así se deberían intercambiar los valores A y B
if N < M:
    C = A[:]
    A = B[:]
    B = C[:]
    N = len(A)
    M = len(B)

# por defecto los valores de la matriz son 0 esto
# facilitará las primeras inicializaciones
matriz = [[0 for col in range(N)] for row in range(M)]

# primera casilla
if A[0] == B[0]:
    matriz[0][0] = 1

# primera columna
for row in range(1, M):
    if A[0] == B[row] or matriz[row - 1][0] == 1:
        matriz[row][0] = 1

# primera fila
for col in range(1, N):
    if A[col] == B[0] or matriz[0][col - 1] == 1:
        matriz[0][col] = 1

# resto de la matriz
for row in range(1, M):
    for col in range(1, N):
        if B[row] == A[col]:
            # incrementaremos en diagonal cuando los bits actuales a evaluar sean iguales
            matriz[row][col] = matriz[row - 1][col - 1] + 1
        else:
            # si no, cogeremos el máximo de ambos valores anteriores
            matriz[row][col] = max(matriz[row][col - 1], matriz[row - 1][col])


len_secuencia = matriz[M - 1][N - 1]
print('LA SECUENCIA MAS LARGA ES DE', len_secuencia, 'BITS')

# recorremos la diagonal para sacar la secuencia a partir de la cadena más larga (A)
secuencia = [-1 for i in range(len_secuencia)]
row, col = 1, 1
pos_secuencia = 0

if matriz[0][0] == 1:
    # si el primer caracter coincide lo añadiremos a la secuencia
    secuencia[pos_secuencia] = A[0]
    pos_secuencia += 1

while pos_secuencia < len_secuencia:
    if matriz[row][col] == matriz[row-1][col-1]+1:
        # si en este paso se incrementó el numero de bits 
        # coincidente cogeremos ese bit de A
        secuencia[pos_secuencia] = A[col]
        pos_secuencia += 1

    # cuando lleguemos a la última fila nos 
    # moveremos en ella solamente por columnas
    if col < N - 1: col += 1
    if row < M - 1: row += 1

print('UNA SECUENCIA EJEMPLO PODRÍA SER', secuencia)
