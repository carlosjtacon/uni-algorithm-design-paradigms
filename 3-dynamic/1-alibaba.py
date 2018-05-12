'''
Ali Baba has managed to enter the cave of one hundred and one thousand thieves, and has brought his camel with him
along with two large panniers; The problem is that he finds so much treasure that he does not know what to take.
The treasures are carved jewels, works of art, ceramics ... that is, they are unique objects that can not be
split as its value would then be reduced to zero.
 
Fortunately the thieves have everything very well organized and you find a list of all the
treasures in the cave, which reflects the weight of each piece and its value in the market of Damascus.
For his part, Ali knows the weight capacity of each of the saddlebags.

Design an algorithm that, taking as data the weights and value of the pieces, and the capacity of the
two saddlebags, to obtain the maximum benefit that Ali Baba can get from the cave of wonders.
'''

import math

def backpack(matrix, objs, capacity):
    num_objs = len(objs[0])

    for col in range(capacity + 1):
        matrix[0][col] = 0

    for row in range(1, num_objs + 1):

        for col in range(objs[0][row - 1]):
            matrix[row][col] = matrix[row - 1][col]

        for col in range(objs[0][row - 1], capacity + 1):
              matrix[row][col] = max(matrix[row - 1][col], objs[1][row - 1] + matrix[row-1][col - objs[0][row - 1]])

    return matrix[num_objs][capacity]


# first we need to fill the small backpack

bk_capacity = [6, 14]
treasures = [
    [1, 2,  5,  6,  7], # [0] weight
    [1, 6, 15, 22, 28]  # [1] value
]

bk_small = [[-1 for col in range(min(bk_capacity) + 1)] for row in range(len(treasures[0]) + 1)]
val_small = backpack(bk_small, treasures, min(bk_capacity))

# delete treasures we already used
col = min(bk_capacity)
row = len(treasures[0])
delete =[]
while col != 0:
    if bk_small[row][col] == bk_small[row - 1][col]:
        row -= 1
    else:
        delete.append(row-1)
        col -= treasures[0][row-1]
        row -= 1

for i in delete:
    del treasures[0][i]
    del treasures[1][i]



bk_big = [[-1 for col in range(max(bk_capacity) + 1)] for row in range(len(treasures[0]) + 1)]
val_big = backpack(bk_big, treasures, max(bk_capacity))

print('Total value', val_big + val_small)
print('Small', min(bk_capacity))
for linea in bk_small:
    print(linea)
print('Big', max(bk_capacity))
for linea in bk_big:
    print(linea)
