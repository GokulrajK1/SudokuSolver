# Sudoku Solver

## A tool used to solve Sudoku boards easily in Python 

This Python script can easily solve a Sudoku board by filling in the appropriate
values to make sure that each row, column, and 3x3 box uses the values from 1-9
only once.  


## How to use it 
1) Clone this project. This will give you the __main.py__ and __sudoku.py__ files 
2) Open __main.py__ file and edit the board list to solve the board that you want
3) Run the __main.py__ file and the solved board will be printed out 
3) Alternatively, the __sudoku.py__ file can be used in other projects and 
folders

## Importing the solveBoard function 
``` python
from sudoku import solveBoard 
board = [ 
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
answer = solveBoard(board)
    for row in answer:
        print(row)
"""
Result:
[6, 9, 1, 3, 2, 4, 8, 5, 7]
[3, 4, 8, 6, 7, 5, 9, 1, 2]
[7, 2, 5, 1, 8, 9, 6, 4, 3]
[2, 1, 7, 5, 9, 3, 4, 6, 8]
[5, 6, 9, 7, 4, 8, 3, 2, 1]
[8, 3, 4, 2, 1, 6, 5, 7, 9]
[9, 5, 2, 4, 3, 7, 1, 8, 6]
[4, 7, 3, 8, 6, 1, 2, 9, 5]
[1, 8, 6, 9, 5, 2, 7, 3, 4]
"""
```
