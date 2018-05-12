n, k = 3, 2
matriz = [[-1 for col in range(k + 1)] for row in range(n + 1)]

for row in range(n + 1):
    matriz[row][0] = 1

for row in range(1, n + 1):
    matriz[row][1] = row

for row in range(2, k + 1):
    matriz[row][row] = 1

for row in range(3, n + 1):
    for col in range(2, row):
        if col <= k:
            matriz[row][col] = matriz[row-1][col-1] + matriz[row-1][col]

print(matriz[n][k])