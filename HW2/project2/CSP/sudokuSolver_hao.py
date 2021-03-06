# SUDOKU SOLVER

import sys
import copy
from time import time
from sudokuUtil import *

# Please implement function solve_puzzle
# input puzzle: 2D list, for example:
# [ [0,9,5,0,3,2,0,6,4]
#   [0,0,0,0,6,0,1,0,0]
#   [6,0,0,0,0,0,0,0,0]
#   [2,0,0,9,0,3,0,0,6]
#   [0,7,6,0,0,0,0,0,3]
#   [3,0,0,0,0,0,0,0,0]
#   [9,0,0,5,0,4,7,0,1]
#   [0,5,0,0,2,1,0,9,0]
#   [0,0,8,0,0,6,3,0,5] ]
# Return a 2D list with all 0s replaced by 1 to 9.
# You can utilize argv to distinguish between algorithms
# (basic backtracking or with MRV and forward checking).
# For example: python sudokuSolver.py backtracking
def solve_puzzle(puzzle, argv):
    """Solve the sudoku puzzle."""
    #return load_sudoku('given_solution.txt')
    board = list(puzzle)
    if argv[1]=='backtracking':
        solve_puzzle_backtracking(board, 0, 0)
        return board
    else:
        cube = init_forward_checking(board)
        #print(cube)
        nextCoord = find_next_block(board, cube)
        print(nextCoord)
        nextRow = nextCoord[0]
        nextCol = nextCoord[1]
        if nextRow == -1 and nextCol == -1:
            return board
        else:
            solve_puzzle_fancy(board, nextRow, nextCol, cube)
        return board

def init_forward_checking(board):
    n=9
    cube = [[[0 for k in xrange(n+1)] for j in xrange(n)] for i in xrange(n)]
    for row in range(9):
        for col in range(9):
            cube[row][col][0]=9
    #print(cube)
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                mark_unavailable(board, row, col, cube)
    #print(cube)            
    return cube

def mark_unavailable(board, row, col, cube):
    value = board[row][col]
    #mark column
    for x in range(9):
        cube[x][col][value] = cube[x][col][value] + 1
        if cube[x][col][value] == 1:
            cube[x][col][0] = cube[x][col][0] - 1
        
    #mark row
    for y in range(9):
        cube[row][y][value] = cube[row][y][value] + 1
        if cube[row][y][value] == 1:
            cube[row][y][0] = cube[row][y][0] - 1
            
    #mark region
    rowGroup = (row//3) * 3
    colGroup = (col//3) * 3
    for i in range(rowGroup, rowGroup+3):
        for j in range(colGroup, colGroup+3):
            cube[i][j][value] = cube[i][j][value] + 1
            if cube[i][j][value] == 1:
                cube[i][j][0] = cube[i][j][0] - 1
                


def mark_available(board, row, col, cube):
    value = board[row][col]
    #mark column
    for x in range(9):
        cube[x][col][value] = cube[x][col][value] - 1
        if cube[x][col][value] == 0:
            cube[x][col][0] = cube[x][col][0] + 1
    #mark row
    for y in range(9):
        cube[row][y][value] = cube[row][y][value] - 1
        if cube[row][y][value] == 0:
            cube[row][y][0] = cube[row][y][0] + 1
    #mark square
    rowGroup = (row//3) * 3
    colGroup = (col//3) * 3
    for i in range(rowGroup, rowGroup+3):
        for j in range(colGroup, colGroup+3):
            cube[i][j][value] = cube[i][j][value] - 1
            if cube[i][j][value] == 0:
                cube[i][j][0] = cube[i][j][0] + 1 


def solve_puzzle_backtracking(board,row,col):
    if row == 9:
        return True
    if col == 8:
        nextRow = row +1
        nextCol = 0
    else:
        nextRow = row
        nextCol = col+1
    if board[row][col]!=0:
        return solve_puzzle_backtracking(board,nextRow,nextCol)
    for c in range(1,10):
        if canPut(board,c,row,col):
            board[row][col] = c
            if solve_puzzle_backtracking(board,nextRow,nextCol):
                return True
            board[row][col] = 0
    return False

def solve_puzzle_fancy(board, row, col, cube):            
    for c in range(1,10):
        if cube[row][col][c] == 0:
            board[row][col] = c
            #temp = copy.deepcopy(cube)
            mark_unavailable(board, row, col, cube)
            #print(cube)
            nextCoord = find_next_block(board, cube)
            nextRow = nextCoord[0]
            nextCol = nextCoord[1]
            if nextRow == -1 and nextCol == -1:
                return True
            else:
                if solve_puzzle_fancy(board,nextRow,nextCol,cube):
                    return True
                mark_available(board, row, col, cube)
                #cube = copy.deepcopy(temp)
                board[row][col] = 0
    return False

def find_next_block(board, cube):
    minnum = 9
    minX = -1
    minY = -1
    for i in range(9):
        for j in range(9):
            #print('checking...')
            #print(i, j)
            if board[i][j] == 0:
                remainValues = cube[i][j][0]
                if remainValues == 1:
                    minX = i
                    minY = j
                    return [minX, minY]
                if remainValues == minnum and minX == -1 and minY == -1:
                    minX = i
                    minY = j
                elif remainValues < minnum:
                    minX = i
                    minY = j
                    minnum = remainValues
    return [minX, minY]
                
def canPut(board, c, row, col):
    for i in range(0,9):
        if board[row][i] == c:
            return False
        if board[i][col] == c:
            return False
    rowGroup = (row//3) * 3
    colGroup = (col//3) * 3 
    for i in range(rowGroup, rowGroup+3):
        for j in range(colGroup, colGroup+3):
            if board[i][j] == c:
                return False
    return True
#===================================================#
puzzle = load_sudoku('puzzle.txt')

print "solving ..."
t0 = time()
solution = solve_puzzle(puzzle, sys.argv)
t1 = time()
print "completed. time usage: %f" %(t1 - t0), "secs."

save_sudoku('solution.txt', solution)

