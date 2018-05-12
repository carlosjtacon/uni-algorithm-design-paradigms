'''
Warshall Algorithm
https://en.wikipedia.org/wiki/Floyd–Warshall_algorithm
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

# MODIFICATION
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

print('MATRIX M')
for f in M:
    print(f)

print('MATRIX C')
for f in C:
    print(f)
