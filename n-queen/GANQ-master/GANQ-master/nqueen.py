from Borad import Chess,GeneticChess
from tkinter import *
'''Single BackTracking -------------------------------'''
dimension = int(input("Enter board dimension: "))
from time import time
chess = Chess(dimension)
start = time()
chess.solveBackTracking(0)
end =time()

for solution in chess.solutions:
     for row in solution:
         print(row)
     print("")
print(end - start)

chess.showBoardGui(solution)

'''Single BackTracking report --------------------------------'''
with open("Single_BackTrackingResults.txt","r+") as file:
     file.truncate(0)
     file.close()
for i in range(4,10):
     chess = Chess(i)
     chess.reportBackTrackingTime()
     print("dimension "+str(i)+" completed")


'''Single GA solution ---------------------------------'''
dimension = int(input("Enter board dimension: "))
chess = GeneticChess(dimension)
from time import time
start = time()
solution = chess.solveGA()
end =time()
board = chess.createBoard(chess.size)
chess.setBoard(board,solution)
print("Solution:")
print(solution)
print("\nBoard:")
for row in board:
     print(row)
print(end - start)
chess.showBoardGui(board)

'''GA report------------------------------------------------'''
with open("GA_report.txt","r+") as file:
     file.truncate(0)
     file.close()
for i in range(4,10):
     chess = GeneticChess(i)
     chess.reportGASolverTime()
     print("dimension "+str(i)+" completed")






