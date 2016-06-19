#!/usr/bin/env python
#coding:utf-8
import sys
import time
from random import randint
from BaseAI import BaseAI
import math as mathterms
import Grid as GridClass
from sets import Set
from copy import deepcopy
# import Board as Board
directionVectors = (UP_VEC, DOWN_VEC, LEFT_VEC, RIGHT_VEC) = ((-1, 0), (1, 0), (0, -1), (0, 1))
def heuristics(actualScore, EmptyCells, Cluster):
	if actualScore==0:
		score = actualScore + (0*EmptyCells) - Cluster
	else:
		score = actualScore + (mathterms.log(actualScore)*EmptyCells) - Cluster
	return max(score, min(actualScore,1))

def max(a,b):
	if a>=b:
		return a
	else:
		return b

def min(a,b):
	if a>=b:
		return b
	else:
		return a

def ClusterScore(board):
	cluster = 0


	for x in range(4):
		for y in range(4):
			if not (board.getCellValue((x,y))>0 ):
				continue
			Neighbours = 0
			sumVal = 0
			for k in [-1,0,1]:
				x_n = x + k
				if (x_n<0) or (x_n>=4):
					continue
				for j in [-1,0,1]:
					y_n = y+j
					if (y_n<0) or (y_n>=4):
						continue

					if board.getCellValue((x_n,y_n))>0:
						Neighbours = Neighbours +  1
						sumVal = sumVal + abs(board.getCellValue((x,y)) - board.getCellValue((x_n,y_n)) )

			cluster = cluster + (sumVal/Neighbours)
	return cluster


def arrayeq(board1, board2):
	for x in range(4):
		for y in range(4):
			if not(board1[x][y]==board2[x][y]):
				return False
	return True

def alphaBeta(board, depth, alpha, beta, player):
	bestMove = -1
	bestScore = 0
	result = (bestScore, bestMove)
	if depth == 0 :
		bestScore = heuristics(board.score, len(board.getAvailableCells()), ClusterScore(board))
		return (bestScore, None)
	else:
		if player:
			bestScore = float("-inf")
			for direction in [0,1,2,3]:
				newBoard = board.clone()
				newBoard.move(direction)
				points = newBoard.score

				if points==0 and arrayeq(newBoard.map, board.map) :
					continue
				# print "reach?"
				result = alphaBeta(newBoard, depth-1, alpha, beta, False)
				# print "result", result
				currentScore = result[0]
				if currentScore > alpha:
					alpha = currentScore
					bestMove = direction

				if beta<=alpha:
					break
			bestScore = alpha

		else:
			bestScore = beta
			moves = board.getAvailableCells()
			possibleValues = [2,4]
			breakFlag = False
			for cell in moves:
				for value in possibleValues:
					newBoard = board.clone()
					newBoard.setCellValue(cell, value)
					result = alphaBeta(newBoard, depth-1, alpha, beta, True)
					# print "res",result, "depth", depth
					currentScore = result[0]
					if currentScore<beta:
							beta=currentScore

					if beta<=alpha:
						breakFlag=True
						break
				if breakFlag:
					break

			bestScore = beta
			if( len(board.getAvailableCells())==0 ):
				bestScore = 0
		# print "return",(bestScore,bestMove)
		return (bestScore, bestMove)



class PlayerAI(BaseAI):



	def iterativeDeep(self, board):
		start = round(time.time() * 1000)
		depth = 1
		while ((round(time.time() * 1000))-start < 100):

			move = alphaBeta(board,depth,(float("-inf")),float("inf"),True)
			if move == ():
				break
			else:
				best = move
				print "depth",depth, "move:", best[1]
			depth = depth+1
		return best[1]

	def getMove(self, grid):
		# I'm too naive, please change me!
		moves = grid.getAvailableMoves()
		# self.AlphaBeta(grid, 4, -1000, 1000, 0, 0, True)
		board = Board()
		board.map = grid.map

		#print moves
		#print "test",moves[randint(0, len(moves) - 1)]
		# move = self.alphabeta(grid, 4, True,  float("-inf"), float("inf"), evalFunc)[1]
		# move = self.intelli(grid, 2, True, float("-inf"), float("inf"), evalFunc)[1]
		move = self.iterativeDeep(board)
		return move
		# return alphaBeta(board,1,(float("-inf")),float("inf"),True)[1]
		#return moves[randint(0, len(moves) - 1)] if moves else None



vecIndex = [UP, DOWN, LEFT, RIGHT] = range(4)
class Board:
    def __init__(self, size=4):
        self.size = size
        self.map = [[0] * self.size for i in xrange(self.size)]
        # MH3478 EDIT
        self.score = 0

    # make a deepcopy of this current object
    def clone(self):
        gridCopy = Board()
        gridCopy.map = deepcopy(self.map)
        gridCopy.size = self.size
        gridCopy.score = self.score
        return gridCopy

    # insert a tile in an empty cell
    def insertTile(self, pos, value):
        self.setCellValue(pos, value)

    def setCellValue(self, (x, y), value):
        self.map[x][y] = value

    # return all the empty cells
    def getAvailableCells(self):
        cells = []
        for x in xrange(self.size):
            for y in xrange(self.size):
                if self.map[x][y] == 0:
                    cells.append((x, y))
        return cells

    # return the tile with maximum number
    def getMaxTile(self):
        maxTile = 0
        for x in xrange(self.size):
            for y in xrange(self.size):
                maxTile = max(maxTile, self.map[x][y])
        return maxTile

    # check whether we can insert a tile in pos
    def canInsert(self, pos):
        return self.getCellValue(pos) == 0

    # move the grid
    def move(self, dir):
        dir = int(dir)
        if dir == UP:
            return self.moveUD(False)
        if dir == DOWN:
            return self.moveUD(True)
        if dir == LEFT:
            return self.moveLR(False)
        if dir == RIGHT:
            return self.moveLR(True)

    # move up or down
    def moveUD(self, down):
        r = range(self.size - 1, -1, -1) if down else range(self.size)
        moved = False
        for j in range(self.size):
            cells = []
            for i in r:
                cell = self.map[i][j]
                if cell != 0:
                    cells.append(cell)
            self.merge(cells)
            for i in r:
                value = cells.pop(0) if cells else 0
                if self.map[i][j] != value:
                    moved = True
                self.map[i][j] = value
        return moved

    # move left or right
    def moveLR(self, right):
        r = range(self.size - 1, -1, -1) if right else range(self.size)
        moved = False
        for i in range(self.size):
            cells = []
            for j in r:
                cell = self.map[i][j]
                if cell != 0:
                    cells.append(cell)
            self.merge(cells)
            for j in r:
                value = cells.pop(0) if cells else 0
                if self.map[i][j] != value:
                    moved = True
                self.map[i][j] = value
        return moved

    # merge tiles
    # EDITED BY MH3478
    def merge(self, cells):
        if len(cells) <= 1:
            return cells
        i = 0
        while i < len(cells) - 1:
            if cells[i] == cells[i + 1]:
                cells[i] *= 2

                # MH3478 EDIT START

                self.score += cells[i]

                # MH3478 EDIT END

                del cells[i + 1]
            i += 1


    def canMove(self, dirs=vecIndex):
        # init moves to be checked
        checkingMoves = Set(dirs)

        for x in xrange(self.size):
            for y in xrange(self.size):
                # if current cell is filled
                if self.map[x][y]:
                    # look ajacent cell value
                    for i in checkingMoves:
                        move = directionVectors[i]
                        adjCellValue = self.getCellValue((x + move[0], y + move[1]))
                        # if value is the same or ajacent cell is empty
                        if adjCellValue == self.map[x][y] or adjCellValue == 0:
                            return True
                # else if current cell is emtpy
                elif self.map[x][y] == 0:
                    return True
        return False

    # return all vailable moves, can be optimized
    def getAvailableMoves(self, dirs=vecIndex):
        availableMoves = []
        for x in dirs:
            gridCopy = self.clone()
            if gridCopy.move(x):
                availableMoves.append(x)
        return availableMoves

    def crossBound(self, (x, y)):
        return x < 0 or x >= self.size or y < 0 or y >= self.size

    def getCellValue(self, pos):
        if not self.crossBound(pos):
            return self.map[pos[0]][pos[1]]
        else:
            return None

    # MH3478 EDIT
    def getHighestValue(self):
        highest = 0
        for x in self.map:
            for y in x:
                if y > highest:
                    highest = y
        return highest


    def getAverageValue(self):
        sum = 0
        count = 0
        for x in self.map:
            for y in x:
                sum += y
                if y != 0:
                    count += 1
        return sum / count


    def gridInsertOk(self, cell):
        return cell[0] >= 0 and cell[0] < len(self.map) and cell[1] >= 0 and cell[1] < len(self.map[0])

    def findFarthestAway(self, cell, vector):

        previous = cell
        cell = [previous[0] + vector[0], previous[1] + vector[1]]

        while self.gridInsertOk(cell) and self.map[cell[0]][cell[1]] == 0:
            previous = cell
            cell = [previous[0] + vector[0], previous[1] + vector[1]]

        if self.gridInsertOk(cell) == False:
            cell = previous

        return cell

    #MH3478 END