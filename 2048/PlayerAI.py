#!/usr/bin/env python
#coding:utf-8

from random import randint
from BaseAI import BaseAI
import math as mathterms

directionVectors = (UP_VEC, DOWN_VEC, LEFT_VEC, RIGHT_VEC) = ((-1, 0), (1, 0), (0, -1), (0, 1))

def max(a, b):
	if a>b:
		return a
	else:
		return b

def min(a,b):
	if a<b:
		return a
	else:
		return b
def maxofarray(array):
	maxim = 0
	for i in array:
		if i > maxim:
			maxim + i

	return maxim

def FarthestPosition(grid, cell, vector):
	while (grid.crossBound(cell)) and (not grid.getCellValue(cell)==0):
		previous = cell
		cell = (previous[0]+directionVectors[vector][0] , previous[1]+directionVectors[vector][1])

	return cell

def evalFunc(grid):
	smoothWeight = 0.1
	monoWeight = 1.0
	emptyWeight = 2.7
	maxWeight = 1.0
	empty = len(grid.getAvailableCells())
	if not empty==0:
		return (mono(grid)*monoWeight + mathterms.log(empty)*emptyWeight + grid.getMaxTile()*maxWeight + smoothness(grid)*smoothWeight )
	else:
		return (mono(grid)*monoWeight + empty*emptyWeight + grid.getMaxTile()*maxWeight + smoothness(grid)*smoothWeight )
	#print "length",len(grid.getAvailableCells())
	#+ mathterms.log( len(grid.getAvailableCells()) )*emptyWeight


def smoothness(grid):
	smoothness = 0
	for x in range(4):
		for y in range(4):
			if not (grid.getCellValue((x,y))==0):
				value = mathterms.log(grid.getCellValue((x,y)))/mathterms.log(2)
				for direction in range(1,3):
					vector = directionVectors[direction]
					targetCell = FarthestPosition(grid, (x,y), vector)
					if not (grid.getCellValue(targetCell)==0):
						target = grid.getCellValue(targetCell)
						targetValue = mathterms.log(target)/mathterms.log(2)
						smoothness = smoothness - abs(value - targetValue)
	return smoothness

def mono(grid):
	score_directions = [0,0,0,0];
	for x in range(4):
		current_row = 0
		next_row = current_row + 1
		while next_row<4 :
			# find number of rows occupied in current column
			while (next_row<4) and (not grid.getCellValue((x,next_row))==0):
				next_row = next_row+1
			if next_row>=4:
				next_row = next_row-1

			if not grid.getCellValue([x,current_row]) == 0:
				current_value = mathterms.log(grid.getCellValue((x,current_row)))/mathterms.log(2)
			else:
				current_value = 0

			if not grid.getCellValue((x,next_row)) == 0:
				next_value = mathterms.log(grid.getCellValue((x,next_row)))/mathterms.log(2)
			else:
				next_value = 0

			if current_value > next_value :
				score_directions[0] = score_directions[0] + (current_value - next_value)
			elif next_value > current_value:
				score_directions[1] = score_directions[1] + (next_value - current_value)

			current_row = next_row
			next_row = next_row+1

	for y in range(4):
		current_col = 0
		next_col = current_col + 1
		while next_col<4 :
			#find number of cols occupied:
			while (next_col<4) and (not grid.getCellValue((next_col,y))==0) :
				next_col = next_col+1
			if next_col>=4 :
				next_col = next_col - 1

			if not grid.getCellValue((current_col,y)) == 0:
				current_value = mathterms.log(grid.getCellValue((current_col,y))) / mathterms.log(2)
			else:
				current_value = 0

			if not grid.getCellValue((next_col,y)) == 0:
				next_value = mathterms.log(grid.getCellValue((next_col,y)))/ mathterms.log(2)
			else:
				next_value = 0

			if current_value > next_value:
				score_directions[2] = score_directions[2] + (current_value - next_value)
			elif next_value > current_value:
				score_directions[3] = score_directions[3] + (next_value - current_value)

			current_col = next_col
			next_col = next_col + 1

	max_tot = 0
	max_1 = 0
	if score_directions[0] > score_directions[1] :
		max_1 = score_directions[0]
	else :
		max_1 = score_directions[1]

	if score_directions[2] > score_directions[3] :
		max_tot = max_1 + score_directions[2]
	else:
		max_tot = max_1 + score_directions[3]

	return max_tot

class PlayerAI(BaseAI):


	# def AlphaBeta(self, grid, depth, alpha, beta, positions, cuts, player):
	# 	global bestScore, result
	# 	bestMove = -1

	# 	if player:
	# 		bestScore = alpha
	# 		for direction in grid.getAvailableMoves():
	# 			GridCopy = grid.clone()
	# 			if GridCopy.move(direction) :
	# 				positions = positions + 1

	# 				if depth==0:
	# 					result = {'move':direction, 'score':self.evalFunc(GridCopy), 'positions':positions, 'cuts':cuts}
	# 					# result = (direction, self.evalFunc(GridCopy), positions, cuts)
	# 				else :
	# 					result = self.AlphaBeta(GridCopy, depth-1, bestScore, beta, positions, cuts, False)
	# 				positions = result['positions']
	# 				cuts = result['cuts']

	# 			if result['score'] > bestScore:
	# 				bestScore = result['score']
	# 				bestMove = direction

	# 			if bestScore > beta:
	# 				cuts = cuts + 1
	# 				return {'move':bestMove, 'score':beta, 'positions':positions, 'cuts':cuts}

	# 	else:
	# 		bestScore = beta
	# 		candidates = []
	# 		cells = grid.getAvailableCells()
	# 		scores = [[],[]]
	# 		val =[2,4]
	# 		for value in range(2):
	# 			for i in range(len(cells)):
	# 				scores[value].extend(0)
	# 				grid.insertTile(i, val[value])
	# 				scores[value][i]=scores[value][i] - self.smoothness(grid)
	# 				grid.setCellValue(i, 0)

	# 		maxScore = max( max( None, maxofarray(scores[2]) ), max(None, scores[4] ) )




	# 	return {'move':bestMove, 'score':bestScore, 'positions':positions, 'cuts':cuts}

	# def AlphaBeta(self, grid, depth, alpha, beta):
	# 	global bestScore, result
	# 	bestMove = -1
	# 	localGrid = grid.clone()
	# 	bestScore = alpha
	# 	for dir in localGrid.getAvailableMoves():
	# 		#print "iter"
	# 		gridCopy = grid.clone()
	# 		if gridCopy.move(dir) is True:
	# 			newCopy = gridCopy.clone()
	# 			if depth == 0 :
	# 				direction, score_val = (dir, self.evalFunc(newCopy))
	# 				print "depth 0"
	# 				return (direction, score_val)
	# 				#print "touple",direction, score_val
	# 			else:
	# 				direction, score_val = self.AlphaBeta(newCopy, depth-1, bestScore, beta)
	# 		#print "score", score_val
	# 		if score_val > bestScore:
	# 			print "score  gt best"
	# 			bestScore = score_val
	# 			bestMove = direction
	# 			print "touple",direction, score_val, bestMove

	# 		if bestScore > beta :
	# 			print "beta score", bestMove, beta
	# 			return (bestMove, beta)


	# 	print "final dec", bestMove
	# 	return (bestMove, bestScore)

	def MiniMax(self, grid, depth, MaxPlayer, eval_func=evalFunc):
		return_val = tuple()
		if depth == 0:
			return (eval_func(grid),None)

		if MaxPlayer:
			bestValue = float("-inf")

			for move in grid.getAvailableMoves():
				gridCopy = grid.clone()
				gridCopy.move(move)
				result = self.MiniMax(gridCopy, depth-1, not MaxPlayer, eval_func)
				if(bestValue < max(bestValue, result[0])):
					bestValue = max(bestValue, result[0])
					return_val = (bestValue, move)

			return return_val
		else:
			candidates = []
			bestValue = float("inf")
			next_values = [2,4]
			localGrid = grid.clone()
			for cell_values in next_values:
				for cell in grid.getAvailableCells():
					localGrid.setCellValue(cell, cell_values)
					result_min = self.MiniMax(localGrid, depth-1, not MaxPlayer, eval_func)
					localGrid.setCellValue(cell, 0)
					#print result_min
					if bestValue > min(bestValue, result_min[0]):
						bestValue = min(bestValue, result_min[0])
						return_val = (bestValue, result_min[1])

			return return_val

	def getMove(self, grid):
		# I'm too naive, please change me!
		moves = grid.getAvailableMoves()
		# self.AlphaBeta(grid, 4, -1000, 1000, 0, 0, True)
		print "eval",evalFunc(grid)

		#print moves
		#print "test",moves[randint(0, len(moves) - 1)]
		move = self.MiniMax(grid, 2, True, evalFunc)[1]
		return move
		#return moves[randint(0, len(moves) - 1)] if moves else None
