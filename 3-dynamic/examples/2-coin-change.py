import math

coin_types = [1, 4, 6]
coin_number = len(coin_types)
quantity = 8
matrix = [[-1 for col in range(quantity + 1)] for row in range(coin_number)]

for row in range(coin_number):
    matrix[row][0] = 0

for row in range(coin_number):
    for col in range(1, quantity + 1):
        if row == 0 and col < coin_types[row]:
            matrix[row][col] = math.inf
        elif row == 0:
            matrix[row][col] = 1 + matrix[0][col - coin_types[0]]
        elif col < coin_types[row]:
            matrix[row][col] = matrix[row - 1][col]
        else:
            matrix[row][col] = min(matrix[row - 1][col], 1 + matrix[row][col - coin_types[row]])

print(matrix[coin_number - 1][quantity])
