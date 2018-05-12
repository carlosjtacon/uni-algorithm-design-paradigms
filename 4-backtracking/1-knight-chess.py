'''
There is an M-board of size FxC (F is the number of rows and C the number of columns)
and a chess knight is placed in an initial box (posx, posy). The goal is to find,
If possible, the way in which the knight should move to travel the entire board in a way
that each box is used only once in the course (the 8x8 board always has a solution
regardless of where the knight starts). The knight can end up in any
board position. A knight has eight possible movements (assuming, of course
is, that does not leave the board). 

A movement between the squares Mij and Mpq is valid only if:
    - (|p–i|=1)&&(|q–j|=2),
    - (|p–i|=2)&&(|q–j|=1),
'''

rows = 5
columns = 5
# row, col
init = [0, 0]

board = [[0 for col in range(columns)] for row in range(rows)]
board[init[0]][init[1]] = 1

def knights(board, nrow, ncol, k):
    global rows, columns
    if k >= rows * columns:
        # movements = board boxes
        escribir(board)
        return True

    for row in range(rows):
        for col in range(columns):
            # loop until valid box
            if valid(nrow, ncol, row, col) and board[row][col] == 0:
                # box is free
                board[row][col] = 1
                exito = knights(board, row, col, k+1)
                board[row][col] = 0

                if exito:
                    return True

def valid(nrow1, ncol1, nrow2, ncol2):
    return (abs(nrow2 - nrow1) == 1 and abs(ncol2 - ncol1) == 2) or (abs(nrow2 - nrow1) == 2 and abs(ncol2 - ncol1) == 1)

def escribir(board):
    print('boards')
    for row in board:
        print(row)


knights(board, init[0], init[1], 1)
