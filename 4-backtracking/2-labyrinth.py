'''
There is a labyrinth table [1..n, 1..m] with logical values representing a labyrinth.
The TRUE value indicates the existence of a wall (you can not traverse), while FALSE
represents a recordable box. To move through the labyrinth, from a box
You can go horizontally or vertically, but only to an empty square (FALSE). The edges
of the table are completely TRUE except one box, which is the output of the maze.
'''

import math

def printlab(maze):
    print('labyrinth')
    for row in maze:
        print(row)

def calcValue(maze):
    value = 0
    for row in maze:
        for box in row:
            if box == '•':
                value += 1
    
    return value

def traverse(maze, labyrinthBest, labyrinthBestValue, i, j):
    if maze[i][j] == 'S':
        printlab(maze)

        labyrinthValue = calcValue(maze)
        if labyrinthValue < labyrinthBestValue:
            labyrinthBestValue = labyrinthValue
            labyrinthBest = maze

        return

    maze[i][j] = '•'

    if maze[i - 1][j] == ' ' or maze[i - 1][j] == 'S':
        traverse(maze, labyrinthBest, labyrinthBestValue, i - 1, j)

    if maze[i][j + 1] == ' ' or maze[i][j + 1] == 'S':
        traverse(maze, labyrinthBest, labyrinthBestValue, i, j + 1)
    
    if maze[i + 1][j] == ' ' or maze[i + 1][j] == 'S':
        traverse(maze, labyrinthBest, labyrinthBestValue, i + 1, j)
    
    if maze[i][j - 1] == ' ' or maze[i][j - 1] == 'S':
        traverse(maze, labyrinthBest, labyrinthBestValue, i, j - 1)

    maze[i][j] = ' '


labyrinthBest = []
labyrinthBestValue = math.inf
maze = [
    ['#','#','#','#','#','#','#'],
    ['#',' ',' ',' ',' ',' ','S'],
    ['#',' ','#',' ','#',' ','#'],
    ['#','O','#',' ','#',' ','#'],
    ['#',' ','#',' ','#',' ','#'],
    ['#',' ',' ',' ','#',' ','#'],
    ['#','#','#',' ',' ',' ','#'],
    ['#','#','#','#','#','#','#']
]

traverse(maze, labyrinthBest, labyrinthBestValue, 3, 1)

print('best path:')
printlab(labyrinthBest)
