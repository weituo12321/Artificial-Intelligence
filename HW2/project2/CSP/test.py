def find_next_block(board, cube):
    minnum = 9
    minX = -1
    minY = -1
    for i,j in range(9):
        #print('checking...')
        #print(i, j)
        if board[i][j]==0:
            remainValues = cube[i][j][0]
            if remainValues:
                if remainValues <minnum:
                    minX=i
                    minY=j
                    minnum=remainValues
            else:
                return[-1,-1]
    return [minX, minY]

def solve_puzzle_fancy(board, row, col, cube):            
    for c in range(1,10):
        if cube[row][col][c] == 1:
            board[row][col] = c
            mark_unavailable(board, row, col, cube)
            nextCoord = find_next_block(board, cube)
            nextRow = nextCoord[0]
            nextCol = nextCoord[1]
            if nextRow == -1 or nextCol == -1:
                mark_available(board, row, col, cube)
                board[row][col] = 0                
            else:
                if solve_puzzle_fancy(board,nextRow,nextCol,cube):
                    return True
    return False



#-------------------------------

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
                #print remainValues
                if remainValues:
                    if remainValues == 1:
                        return [i, j]
                    elif remainValues>1:
                        minnum=min(remainValues,minnum)
                        minX=i
                        minY=j
                
                #elif remainValues > 1 and remainValues <= minnum:
  #                  minnum = remainValues
#                    minX = i
#                    minY = j
                
                #else:
                    #return [-1, -1]
    return [minX, minY]


def solve_puzzle_fancy(board, row, col, cube):            
    for c in range(1,10):
        if cube[row][col][c] == 1:
            board[row][col] = c
            mark_unavailable(board, row, col, cube)
            nextCoord = find_next_block(board, cube)
            nextRow = nextCoord[0]
            nextCol = nextCoord[1]
            if nextRow == -1 and nextCol == -1:
                return False
            else:
                if solve_puzzle_fancy(board,nextRow,nextCol,cube):
                    return True
                mark_available(board, row, col, cube)
                board[row][col] = 0
    return False
