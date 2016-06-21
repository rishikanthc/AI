#!/usr/bin/env python
#coding:utf-8
import time
from random import randint
from BaseAI import BaseAI
import math
directionVectors = (UP_VEC, DOWN_VEC, LEFT_VEC, RIGHT_VEC) = ((-1, 0), (1, 0), (0, -1), (0, 1))
def log2(val):
	return math.log(val)/math.log(2)

def islands(grid):
	grid_dist = [[0 for x in range(4)] for x in range(4)]
	def mark(x,y, value):
		if (x>=0 and x<=3 and y>=0 and y<=3) and (grid.getCellValue((x,y))==value) and (grid_dist[x][y]==0):
			grid_dist[x][y]=1

			for direction in [0,1,2,3]:
				vector = directionVectors[direction]
				mark( x+vector[0], y+vector[1], value)

	islands =0
	for x in range(4):
		for y in range(4):
			if (not grid.getCellValue((x,y))==0):
				grid_dist[x][y] = 0

	for x in range(4):
		for y in range(4):
			if (not grid.getCellValue((x,y))==0) and grid_dist[x][y]==0:
				islands = islands + 1
				mark(x,y, grid.getCellValue((x,y)))

	return islands
def corners(grid):
	a=1
	maxtile = grid.getMaxTile()
	# if maxtile >512:
	# 	a=1.5
	if grid.getCellValue((0,0)) == maxtile:
		return maxtile*a
	elif grid.getCellValue((0,3)) == maxtile:
		return maxtile*a
	elif grid.getCellValue((3,0)) == maxtile:
		return maxtile*a
	elif grid.getCellValue((3,3)) ==maxtile:
		return maxtile*a
	else:
		return maxtile*(-1)*a


def Utility(grid):
	emptFact = 25
	highestFact =10
	scoregrade = 14
	gradientFac =1
	directionFac =15

	score, emptyCells = getScore(grid)
	maxTile = grid.getMaxTile()
	smoothScore = smooth(grid)
	patternScore = pattern(grid)

	gridScore = score*scoregrade + emptyCells*emptFact + maxTile*highestFact + smoothScore*gradientFac + patternScore*directionFac - islands(grid)*30 + corners(grid)

	return gridScore/10
	# return S_Pattern(grid)

def smooth(grid):
	simpleGrid = [[0 for i in range(4)] for j in range(4)]
	for row in range(4):
		for col in range(4):
			simpleGrid[row][col] = grid.getCellValue((row, col))

	bonus = 0
	for row in range(4):
		for col in range(4):
			if simpleGrid[row][col] is not 0:
				if simpleGrid[row][3] is not 0:
					bonus += abs(log2(simpleGrid[row][col])-log2(simpleGrid[row][3]))
				if simpleGrid[3][col] is not 0:
					bonus += abs(log2(simpleGrid[row][col])-log2(simpleGrid[3][col]))

	return bonus

def pattern(grid):
    simpleGrid = [[0 for i in range(4)] for j in range(4)]
    for row in range(4):
		for col in range(4):
			if grid.getCellValue((row, col))>0:
				simpleGrid[row][col] = log2(grid.getCellValue((row, col)))
			else:
				simpleGrid[row][col] = 0

    asndud = 0
    dsndud = 0
    asndlr = 0
    dsndlr = 0
    for row in range(4):
        for col in range(4):
            if col+1<4:
                if simpleGrid[row][col]>simpleGrid[row][col+1]:
                    dsndlr-=simpleGrid[row][col]-simpleGrid[row][col+1]
                else:
                    asndlr+=simpleGrid[row][col]-simpleGrid[row][col+1]
            if row+1<4:
                if simpleGrid[row][col]>simpleGrid[row+1][col]:
                    dsndud-=simpleGrid[row][col]-simpleGrid[row+1][col]
                else:
                    asndud+=simpleGrid[row][col]-simpleGrid[row+1][col]
    return max(dsndlr,asndlr)+max(dsndud,asndud)



def getScore(grid):
	emptyCells = 0
	score = 0
	for x in range(4):
		for y in range(4):
			cellValue = grid.getCellValue((x,y))
			if cellValue>0 :
				score = score + math.log(cellValue)/math.log(2)
			else:
				emptyCells = emptyCells + 1
	if emptyCells > 0:
		emptyCells = math.log(emptyCells)

	return (score*(-1), emptyCells)

class PlayerAI(BaseAI):
	def __init__(self):
		self.direction = 0

	def AlphaBeta(self, grid, alpha, beta, Player, depth):
		AvailableMoves = grid.getAvailableMoves()
		bestMove = AvailableMoves[randint(0, len(AvailableMoves) - 1)] if AvailableMoves else None
		bestScore = 0
		if depth == 0:
			return (Utility(grid),None)
		if Player:

			bestScore = alpha
			if len(AvailableMoves)>0:
				for move in AvailableMoves:
					gridCopy = grid.clone()
					gridCopy.move(move)
					result = self.AlphaBeta(gridCopy, alpha, beta, False, depth-1)
					if result[0] > bestScore:
						bestScore = result[0]
						bestMove = move
					if bestScore >= beta:
						return (beta,bestMove)
				return (bestScore, bestMove)

		else:
			bestScore = beta
			for cell in grid.getAvailableCells():
				for cell_values in [2,4]:
					gridCopy = grid.clone()
					gridCopy.setCellValue(cell, cell_values)
					result = self.AlphaBeta(gridCopy, alpha, beta, True, depth-1)
					gridCopy.setCellValue(cell, 0)
					if result[0] < bestScore :
						bestScore = result[0]

					if bestScore <= alpha:
						return (alpha, None)
			return (bestScore, None)
		return(bestScore,bestMove)

	def iterativeDeep(self, grid):
		start = round(time.time() * 1000)
		depth = 1
		while ((round(time.time() * 1000))-start < 80):

			move = self.AlphaBeta(grid, float("-inf"), float("inf"), True, depth)
			if move == ():
				break
			else:
				best = move
			if depth<20:
				depth = depth+1
			else:
				return best[1]
		return best[1]

	def DepthSelect(self,grid):
		length = len(grid.getAvailableCells())
		if length > 3:
			depth = 3
		else:
			depth = 4
		return self.AlphaBeta(grid, float("-inf"), float("inf"), True, depth)[1]

	def getMove(self, grid):
		# I'm too naive, please change me!
		# moves = grid.getAvailableMoves()
		# return moves[randint(0, len(moves) - 1)] if moves else None
		# return self.AlphaBeta(grid, float("-inf"), float("inf"), True, 3)[1]
		# return self.iterativeDeep(grid)
		return self.DepthSelect(grid)

