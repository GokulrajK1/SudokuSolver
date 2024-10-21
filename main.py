from sudoku import solveBoard

def main():
    board = [ # Edit this list
        [0, 0, 0, 3, 0, 0, 8, 0, 7],
        [0, 0, 8, 0, 0, 0, 9, 0, 0],
        [0, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 1, 0, 5, 0, 0, 0, 0, 0],
        [5, 0, 9, 7, 0, 8, 3, 0, 1],
        [0, 0, 0, 0, 0, 6, 0, 7, 0],
        [0, 5, 0, 0, 0, 7, 0, 8, 0],
        [0, 0, 3, 0, 0, 0, 2, 0, 0],
        [1, 0, 6, 0, 0, 2, 0, 0, 0],
    ]
    # Prints out the board 
    answer = solveBoard(board)
    for row in answer:
        print(row)
        
if __name__ == "__main__": main()