from sudokuSolver import solve_puzzle
from sudokuUtil import *
from time import time
import os
import sys

# argv[1]: method to be used to solve the puzzle ('backtracking' or 'fancy')
# argv[2]: number of given digits in the puzzle (30 by default)
average = 0.0
variance = 0.0
givenDigits = 30
timeList = []
method = sys.argv[1]
if len(sys.argv) >= 3:
	givenDigits = int(sys.argv[2])

for n in range(10):
	print n+1
	os.system('python sudokuGenerator.py %s'%(givenDigits)) # generate puzzle
	puzzle = load_sudoku('puzzle.txt')

	t0 = time()
	solution = solve_puzzle(puzzle, method) # compute time used to solve the puzzle
	t1 = time()

	save_sudoku('solution.txt', solution)
	os.system('python sudokuChecker.py') # check solution
	print "completed. time usage: %f" %(t1 - t0), "secs."
	timeList.append(t1-t0)

print "\n", method, "method,", "10 random sudokus with", givenDigits, "given digits:"
average = sum(timeList)/10
print "Average time: %5.20f" %average, "secs."

for i in timeList:
	variance += (i - average) ** 2
variance = variance/10
print "Variance: %5.20f" %variance



