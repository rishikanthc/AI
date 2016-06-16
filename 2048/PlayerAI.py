#!/usr/bin/env python
#coding:utf-8

from random import randint
from BaseAI import BaseAI
import math as mathterms

class PlayerAI(BaseAI):
	def evalFunc(self, grid):
		smoothWeight = 0.1
		monoWeight = 1.0
		emptyWeight = 2.7
		maxWeight = 1.0
		empty = len(grid.getAvailableCells())
		#print "length",len(grid.getAvailableCells())
		#+ mathterms.log( len(grid.getAvailableCells()) )*emptyWeight
		return (self.mono(grid)*monoWeight + empty*emptyWeight + grid.getMaxTile()*maxWeight)

	# def smoothness(self, grid):
	# 	for x in range(4):
	# 		for y in range(4):
	# 			if grid.getCellValue([x,y]) not 0:
	# 				value = mathterms.log(grid.getCellValue([x,y]))/mathterms.log(2)

	def mono(self, grid):
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
					current_value = mathterms.log(2,grid.getCellValue((x,current_row)))
				else:
					current_value = 0

				if not grid.getCellValue((x,next_row)) == 0:
					next_value = mathterms.log(2, grid.getCellValue((x,next_row)))
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
					current_value = mathterms.log(2, grid.getCellValue((current_col,y)))
				else:
					current_value = 0

				if not grid.getCellValue((next_col,y)) == 0:
					next_value = mathterms.log(2, grid.getCellValue((next_col,y)))
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



	def AlphaBeta(self, grid, depth, alpha, beta):
		global bestScore, result
		bestMove = -1
		localGrid = grid.clone()
		bestScore = alpha
		for dir in localGrid.getAvailableMoves():
			#print "iter"
			gridCopy = grid.clone()
			if gridCopy.move(dir) is True:
				newCopy = gridCopy.clone()
				if depth == 0 :
					direction, score_val = (dir, self.evalFunc(newCopy))
					print "depth 0"
					return (direction, score_val)
					#print "touple",direction, score_val
				else:
					direction, score_val = self.AlphaBeta(newCopy, depth-1, bestScore, beta)
			#print "score", score_val
			if score_val > bestScore:
				print "score  gt best"
				bestScore = score_val
				bestMove = direction
				print "touple",direction, score_val, bestMove

			if bestScore > beta :
				print "beta score", bestMove, beta
				return (bestMove, beta)
		print "final dec", bestMove
		return (bestMove, bestScore)


	def getMove(self, grid):
		# I'm too naive, please change me!
		moves = grid.getAvailableMoves()
		#print self.evalFunc(grid)
		#print moves
		final_move, score = self.AlphaBeta(grid, 4, -1000, 1000)
		print "move", final_move
		return final_move
		#print "test",moves[randint(0, len(moves) - 1)]
		#return moves[randint(0, len(moves) - 1)] if moves else None
