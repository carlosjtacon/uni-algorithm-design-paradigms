n = 4 # se jugarán máximo 7 partidos ganará el campeonato el equipo que gane 4
p = 0.6 # probabilidad de que gane el equipo A
q = 1 - p # probabilidad de que gane el equipo B
matriz = [[-1 for col in range(n + 1)] for row in range(n + 1)]

# def prob(i, j):
#     if i == 0:
#         return 1
#     elif j == 0:
#         return 0
#     else:
#         return p * prob(i-1, j) + q * prob(i, j-1)

for s in range(1, n + 1):
    matriz[0][s] = 1
    matriz[s][0] = 0
    for k in range(1, s):
        matriz[k][s-k] = p * matriz[k-1][s-k] + q * matriz[k][s-k-1]

for s in range(1, n + 1):
    for k in range(n-s + 1):
        matriz[s+k][n-k] = p * matriz[s+k-1][n-k] + q * matriz[s+k][n-k-1]

print(matriz[n][n])