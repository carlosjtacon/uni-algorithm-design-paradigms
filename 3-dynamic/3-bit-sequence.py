'''
A sequence of bits A is defined as a sequence A = {a1, a2, ..., an} where each ai can take the
value 0 or the value 1, and n is the length of the sequence A. From a sequence is defined a
X subsequence of A as X = {x1, x2, ..., xk}, where k ≤ n, so that X can be obtained by eliminating
some element of A but respecting the order in which the bits appear; for example,
if A = {1, 0, 1, 1, 0, 0, 1} we could obtain as subsequences {1, 1, 1, 0, 1}, {1, 0, 1} or {1, 1, 0, 0 }
among others, but you could never get the subsequence {1, 0, 0, 1, 1}.

Given two sequences A and B, X is called a common subsequence of A and B when X is subsequence
of A and it is also a subsequence of B. (although it may have been obtained by removing different elements in A
than B, and even different amount). Assuming the sequences A = {0, 1, 1, 0, 1, 0, 1, 0} and
B = {1, 0, 1, 0, 0, 1, 0, 0, 1}, a common subsequence would be X = {1, 1, 0, 1}, but could not
be X = {0, 1, 1, 1, 0}.

It is desired to determine the common subsequence of two sequences A and B that have the maximum length, for which it is requested:
     - Explain in detail how to solve the problem, and
     - Make a Dynamic Programming algorithm that obtains the maximum possible length and a
       common sequence of said length.
'''

A = [0, 1, 1, 0, 1, 0, 1, 0]
B = [1, 0, 1, 0, 0, 1, 0, 0, 1]
N, M = len(A), len(B)

# A should be greater or equal to B in length, else A / B swapped
if N < M:
    C = A[:]
    A = B[:]
    B = C[:]
    N = len(A)
    M = len(B)

# default 0
matrix = [[0 for col in range(N)] for row in range(M)]

if A[0] == B[0]:
    matrix[0][0] = 1

for row in range(1, M):
    if A[0] == B[row] or matrix[row - 1][0] == 1:
        matrix[row][0] = 1

for col in range(1, N):
    if A[col] == B[0] or matrix[0][col - 1] == 1:
        matrix[0][col] = 1

for row in range(1, M):
    for col in range(1, N):
        if B[row] == A[col]:
            # diagonal inc
            matrix[row][col] = matrix[row - 1][col - 1] + 1
        else:
            # max previous values
            matrix[row][col] = max(matrix[row][col - 1], matrix[row - 1][col])


len_sec = matrix[M - 1][N - 1]
print('bigger sequence', len_sec, 'bits')

# get sequence from A, diagonal loop
sequence = [-1 for i in range(len_sec)]
row, col = 1, 1
pos_sec = 0

if matrix[0][0] == 1:
    # si el primer caracter coincide lo añadiremos a la sequence
    sequence[pos_sec] = A[0]
    pos_sec += 1

while pos_sec < len_sec:
    if matrix[row][col] == matrix[row-1][col-1]+1:
        # si en este paso se incrementó el numero de bits 
        # coincidente cogeremos ese bit de A
        sequence[pos_sec] = A[col]
        pos_sec += 1

    # cuando lleguemos a la última fila nos 
    # moveremos en ella solamente por columnas
    if col < N - 1: col += 1
    if row < M - 1: row += 1

print('example sequence', sequence)
