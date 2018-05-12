n = 4
solution = [-1 for i in range(n)]

def queens(solution, k):
    if k >= n:
        # tree ending, final solution
        writesol(solution)
    else:
        for row in range(n):
            if valid(solution, row, k):
                solution[k] = row
                queens(solution, k+1)

def valid(solution, row, k):
    for i in range(k):
        if solution[i] == row or abs(solution[i] - row) == abs(i - k):
            # same row or diagonal
            return False
    return True

def writesol(solution):
    board = [[' ' for col in range(n)] for row in range(n)]
    for row in range(n):
        for col in range(n):
            if solution[col] == row:
                board[row][col] = 'x'
    
    print(solution)
    for row in board:
        print(row)


queens(solution, 0)