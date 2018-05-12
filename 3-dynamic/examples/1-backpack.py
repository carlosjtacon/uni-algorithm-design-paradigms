obj_weight = [1, 2,  5,  6,  7]
obj_val = [1, 6, 18, 22, 28]
backpack_capacity = 11

num_obj = len(obj_weight)
matrix = [[-1 for col in range(backpack_capacity + 1)] for row in range(num_obj + 1)]
# row = available obj | column = backpack capacity

for col in range(backpack_capacity + 1):
    # first matrix row is 0 no object with a 0 backpack_capacity
    matrix[0][col] = 0

for row in range(1, num_obj + 1):
    
    for col in range(obj_weight[row - 1]):
        # copy previous row until 
        # current weight position
        matrix[row][col] = matrix[row - 1][col]
    
    for col in range(obj_weight[row - 1], backpack_capacity + 1):
        # for the remaining we pick the max
        matrix[row][col] = max(matrix[row - 1][col], matrix[row - 1][col - obj_weight[row - 1]] + obj_val[row - 1])

print('BACKPACK TOTAL VALUE ', matrix[num_obj][backpack_capacity])
for row in matrix:
    print(row)

