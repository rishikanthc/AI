#!/usr/bin/env python
#coding:utf-8
import time
from random import randint
from BaseAI import BaseAI
from sysconfig import sys
import math as mathterms

sys.setrecursionlimit(4000)
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

	#variable that keeps track of the most optimal direction the PlayerAI can make
	def _init_(self):
		self.direction = -1

	def MaxTilesDist(self, grid, maxTiles):
		pos = []
		for x in range(4):
			for y in range(4):
				cellVal = grid.getCellValue((x,y))
				if cellVal == maxTiles[3]:
					pos.append((x,y))
				elif cellVal == maxTiles[2]:
					pos.append((x,y))
				elif cellVal == maxTiles[1]:
					pos.append((x,y))
				elif cellVal == maxTiles[0]:
					pos.append((x,y))
		dist = 0
		dist = dist + (pos[1][0]-pos[1][1])*maxTiles[2]*(pos[0][0]+(0.1*pos[0][1])) + (pos[2][0]-pos[2][1])*maxTiles[1]*(pos[1][0]+(0.1*pos[1][1])) + (pos[3][0]-pos[3][1])*maxTiles[0]*(pos[2][0]+(0.1*pos[2][1]))
		return dist

	#Input for heuristic: Gets the top four tiles and returns to eval function.
	def getMaxTiles(self, grid):
		maxTile = 0
		dist = 0
		maxTiles = [0, 0, 0, 0]
		for x in xrange(grid.size):
			for y in xrange(grid.size):
				dist = dist+(x-y)*grid.map[x][y]*3.0
				maxTile = grid.map[x][y]
				if maxTile > maxTiles[0]:
					maxTiles[0]=maxTile
					maxTiles.sort(cmp=None, key=None, reverse=False)
		maxTiles.append(dist)
		return maxTiles

	#Heuristic: Calculates the utility at leaf node based on - number of empty cells available, top 4 maxTiles values
	#and weighted distance of tiles from bottom left corner.
	def evalfn(self,grid):
		monoWeight = 5.0
		cell = grid.getAvailableCells()
		maxTiles = self.getMaxTiles(grid)
		maxSum = sum(maxTiles)-maxTiles[4]

		evalScore = len(cell)*5000+maxSum*0.8+maxTiles[4]*2 + mono(grid)*monoWeight + self.MaxTilesDist(grid,maxTiles)
		return(evalScore)


	#Allocates new tile as either number 2 (probability 0.9) or 4 (probability 0.1)
	def getNewTileValue(self):
		if randint(0,99) < 100 * 0.9:
			return 2
		else:
			return 4

	#Minimax algorithm implementation with alpha-beta pruning
	def alphabeta(self, grid, depth, alpha, beta, maximizingPlayer):
		if depth == 0:
			e = self.evalfn(grid)
			return [e,-1]
		if maximizingPlayer:
			moves = grid.getAvailableMoves()
			if moves == []:
				return [alpha, self.direction]
			for i in moves:
				newgrid = grid.clone()
				newgrid.move(i)
				r = self.alphabeta(newgrid, depth-1, alpha, beta, False)
				if alpha < r[0]:
					self.direction = i
				if r[0] == -float('inf'):
					self.direction = i
				alpha = max(alpha, r[0])
				if beta <= alpha:
					print "I'm in break stmt"
					break
			result = [alpha, self.direction]
			return result
		else:
			cells = grid.getAvailableCells()
			if cells == []:
				return result
			i = cells[randint(0, len(cells) - 1)]
			grid.map[i[0]][i[1]] = self.getNewTileValue()
			r = self.alphabeta(grid, depth-1, alpha, beta, True)
			beta = min(beta, r[0])
			result = [beta, r[1]]
			return result

	def iterativeDeep(self, grid):
		start = round(time.time() * 1000)
		depth = 1
		while ((round(time.time() * 1000))-start < 100):

			move = self.alphabeta(grid, depth, -float('inf'), float('inf'), True)
			if move == ():
				break
			else:
				best = move
				print "depth",depth, "move:", best[1]
			depth = depth+1
		return best
	#Returns the optimal move per the algorithm to the GameManager function.
	def getMove(self, grid):
		moves = grid.getAvailableMoves()
		print moves

		# result = self.alphabeta(grid, 12, -float('inf'), float('inf'), True)
		result = self.iterativeDeep(grid)
		print "Expected score:",result[0]
		print "Direction",result[1]
		return result[1]

		#return moves[randint(0, len(moves) - 1)] if moves else None




