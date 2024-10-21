# Checks to see if the number can be placed into the grid position 
def satisfyBoard (board, row, column, num):
    if num in board[row]: return False

    for r in board: 
        if r[column] == num:
            return False
    
    boxRow = (row // 3) * 3
    boxCol = (column // 3) * 3
    
    for i in range(boxRow, boxRow + 3):
        for j in range(boxCol, boxCol + 3):
            if board[i][j] == num:
                return False
                
    return True

# Checks to see if the board is full
def isboardFull (board):
    for row in board:
        if 0 in row:
            return False
    return True

# Function used to solve the Sudoku board recursively 
def solveBoard (board):
    newBoard = board
    for rNum in range(0, 9):
        for cNum in range(0, 9):
            if newBoard[rNum][cNum] == 0:
                for num in range(1, 10):
                    if satisfyBoard(newBoard, rNum, cNum, num):
                        newBoard[rNum][cNum] = num
                        newBoard = solveBoard(newBoard)
                        if isboardFull(newBoard):
                            break
                        newBoard[rNum][cNum] = 0
                    
                return newBoard
    return newBoard
