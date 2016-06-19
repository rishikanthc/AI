#!/usr/bin/env python
#coding:utf-8
import time
from random import randint
from BaseAI import BaseAI
import math as mathterms

directionVectors = (UP_VEC, DOWN_VEC, LEFT_VEC, RIGHT_VEC) = ((-1, 0), (1, 0), (0, -1), (0, 1))

def s_pattern(grid,commonRatio=0.25):
	linearWeightedVal = 0
	invert = False
	weight = 1.
	malus = 0
	criticalTile = (-1,-1)
	for y in range(0,4):
		for x in range(0,4):
			b_x = x
			b_y = y
			if invert:
				b_x = 4 - 1 - x
                #linearW
			currVal=grid.getCellValue((b_x,b_y))
			if(currVal == 0 and criticalTile == (-1,-1)):
				criticalTile = (b_x,b_y)
			linearWeightedVal += currVal*weight
			weight *= commonRatio
		invert = not invert

	linearWeightedVal2 = 0
	invert = False
	weight = 1.
	malus = 0
	criticalTile2 = (-1,-1)
	for x in range(0,4):
		for y in range(0,4):
			b_x = x
			b_y = y
			if invert:
				b_y = 4 - 1 - y
                #linearW
			currVal=grid.getCellValue((b_x,b_y))
			if(currVal == 0 and criticalTile2 == (-1,-1)):
				criticalTile2 = (b_x,b_y)
			linearWeightedVal2 += currVal*weight
			weight *= commonRatio
		invert = not invert


	linearWeightedVal3 = 0
	invert = False
	weight = 1.
	malus = 0
	criticalTile3 = (-1,-1)
	for y in range(0,4):
		for x in range(0,4):
			b_x = x
			b_y = 4 - 1 - y
			if invert:
				b_x = 4 - 1 - x
                #linearW
			currVal=grid.getCellValue((b_x,b_y))
			if(currVal == 0 and criticalTile3 == (-1,-1)):
				criticalTile3 = (b_x,b_y)
			linearWeightedVal3 += currVal*weight
			weight *= commonRatio
		invert = not invert

	linearWeightedVal4 = 0
	invert = False
	weight = 1.
	malus = 0
	criticalTile4 = (-1,-1)
	for x in range(0,4):
		for y in range(0,4):
			b_x = 4 - 1 - x
			b_y = y
			if invert:
				b_y = 4 - 1 - y
                #linearW
			currVal=grid.getCellValue((b_x,b_y))
			if(currVal == 0 and criticalTile4 == (-1,-1)):
				criticalTile4 = (b_x,b_y)
			linearWeightedVal4 += currVal*weight
			weight *= commonRatio
		invert = not invert


	linearWeightedVal5 = 0
	invert = True
	weight = 1.
	malus = 0
	criticalTile5 = (-1,-1)
	for y in range(0,4):
		for x in range(0,4):
			b_x = x
			b_y = y
			if invert:
				b_x = 4 - 1 - x
                #linearW
			currVal=grid.getCellValue((b_x,b_y))
			if(currVal == 0 and criticalTile5 == (-1,-1)):
				criticalTile5 = (b_x,b_y)
			linearWeightedVal5 += currVal*weight
			weight *= commonRatio
		invert = not invert

	linearWeightedVal6 = 0
	invert = True
	weight = 1.
	malus = 0
	criticalTile6 = (-1,-1)
	for x in range(0,4):
		for y in range(0,4):
			b_x = x
			b_y = y
			if invert:
				b_y = 4 - 1 - y
                #linearW
			currVal=grid.getCellValue((b_x,b_y))
			if(currVal == 0 and criticalTile6 == (-1,-1)):
				criticalTile6 = (b_x,b_y)
			linearWeightedVal6 += currVal*weight
			weight *= commonRatio
		invert = not invert


	linearWeightedVal7 = 0
	invert = True
	weight = 1.
	malus = 0
	criticalTile7 = (-1,-1)
	for y in range(0,4):
		for x in range(0,4):
			b_x = x
			b_y = 4 - 1 - y
			if invert:
				b_x = 4 - 1 - x
                #linearW
			currVal=grid.getCellValue((b_x,b_y))
			if(currVal == 0 and criticalTile7 == (-1,-1)):
				criticalTile7 = (b_x,b_y)
			linearWeightedVal7 += currVal*weight
			weight *= commonRatio
		invert = not invert

	linearWeightedVal8 = 0
	invert = True
	weight = 1.
	malus = 0
	criticalTile8 = (-1,-1)
	for x in range(0,4):
		for y in range(0,4):
			b_x = 4 - 1 - x
			b_y = y
			if invert:
				b_y = 4 - 1 - y
                #linearW
			currVal=grid.getCellValue((b_x,b_y))
			if(currVal == 0 and criticalTile8 == (-1,-1)):
				criticalTile8 = (b_x,b_y)
			linearWeightedVal8 += currVal*weight
			weight *= commonRatio
		invert = not invert

	maxVal = maxofarray([linearWeightedVal,linearWeightedVal2,linearWeightedVal3,linearWeightedVal4,linearWeightedVal5,linearWeightedVal6,linearWeightedVal7,linearWeightedVal8])
	if(linearWeightedVal2 > linearWeightedVal):
		linearWeightedVal = linearWeightedVal2
		criticalTile = criticalTile2
	if(linearWeightedVal3 > linearWeightedVal):
		linearWeightedVal = linearWeightedVal3
		criticalTile = criticalTile3
	if(linearWeightedVal4 > linearWeightedVal):
		linearWeightedVal = linearWeightedVal4
		criticalTile = criticalTile4
	if(linearWeightedVal5 > linearWeightedVal):
		linearWeightedVal = linearWeightedVal5
		criticalTile = criticalTile5
	if(linearWeightedVal6 > linearWeightedVal):
		linearWeightedVal = linearWeightedVal6
		criticalTile = criticalTile6
	if(linearWeightedVal7 > linearWeightedVal):
		linearWeightedVal = linearWeightedVal7
		criticalTile = criticalTile7
	if(linearWeightedVal8 > linearWeightedVal):
		linearWeightedVal = linearWeightedVal8
		criticalTile = criticalTile8

	return maxVal

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

def islands(grid):
	pass
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

def FarthestPosition(grid, cell, vector):
	while (grid.crossBound(cell)) and (not grid.getCellValue(cell)==0):
		previous = cell
		cell = (previous[0]+directionVectors[vector][0] , previous[1]+directionVectors[vector][1])

	return cell
def corners(grid):
	a=1
	maxtile = grid.getMaxTile()
	if maxtile >512:
		a=1.5
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

def toprow(grid):
	sum = 0
	for x in range(4):
		if not grid.getCellValue((0,x)) == 0:
			sum = sum + grid.getCellValue((0,x))

	return sum

def evalFunc(grid):
	smoothWeight = 10
	monoWeight = 1.0
	emptyWeight = 2.7
	maxWeight = 1.0
	cornerWeight = 1.5
	islandWeight = 1.5
	topweight = 0
	empty = len(grid.getAvailableCells())
	if not empty==0:
		return (mono(grid)*monoWeight + mathterms.log(empty)*emptyWeight + grid.getMaxTile()*maxWeight + smoothness(grid)*smoothWeight - islands(grid)*islandWeight + corners(grid) + toprow(grid)*topweight )#+ s_pattern(grid,5))
	else:
		return (mono(grid)*monoWeight + empty*emptyWeight + grid.getMaxTile()*maxWeight + smoothness(grid)*smoothWeight - islands(grid)*islandWeight +corners(grid) + toprow(grid)*topweight)# + s_pattern(grid,5))
	#print "length",len(grid.getAvailableCells())
	#+ mathterms.log( len(grid.getAvailableCells()) )*emptyWeight

def evalformin(grid):
	smoothWeight = 4
	monoWeight = 10
	emptyWeight = 2.7
	maxWeight = 5.0
	cornerWeight = 0
	islandWeight = 1.5
	empty = len(grid.getAvailableCells())
	if not empty==0:
		return (islands(grid)*islandWeight - mono(grid)*monoWeight - grid.getMaxTile()*maxWeight + smoothness(grid)*smoothWeight - corners(grid) - toprow(grid) )#+ s_pattern(grid,5))
	else:
		return (islands(grid)*islandWeight - mono(grid)*monoWeight - grid.getMaxTile()*maxWeight + smoothness(grid)*smoothWeight - corners(grid) - toprow(grid))#+ s_pattern(grid,5))
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
	def intelli(self, grid, depth, MaxPlayer, alpha, beta, eval_func=evalFunc):
		bestScore = None
		temp = grid.getAvailableMoves()

		bestMove = temp[randint(0, len(temp) - 1)] if temp else None
		result = tuple()
		if depth == 0:
			return (eval_func(grid), None)

		if MaxPlayer:
			bestScore = alpha
			for move in grid.getAvailableMoves():
				gridCopy = grid.clone()
				if gridCopy.move(move):
					result = self.intelli(gridCopy, depth-1, not MaxPlayer, alpha, beta, eval_func)

					if result[0] > bestScore:
						bestScore = result[0]
						bestMove = move

					if bestScore>=beta:
						return (beta, bestMove)



		else:
			bestScore = beta
			next_values = [2,4]
			localGrid = grid.clone()
			candidates = []
			scoreList = []
			maxScore = float("-inf")
			for cell_values in next_values:
				for cell in grid.getAvailableCells():

					localGrid.setCellValue(cell, cell_values)
					# scoreVal = smoothness(localGrid)*(-1)
					# scoreVal = islands(grid) - smoothness(grid)
					# scoreVal = eval_func(grid)*(-1)
					scoreVal = evalformin(grid)
					localGrid.setCellValue(cell, 0)
					scoreList_tuple = (tuple([scoreVal,cell,cell_values]))
					scoreList.extend([scoreList_tuple])

			for i in scoreList:
				if i[0] > maxScore:
					maxScore = i[0]

			for i in scoreList:
				if i[0] == maxScore:
					candidates.extend([i])

					# if scoreVal < maxScore:
					# 	maxScore = scoreVal

					# 	# candidates_tuple = []
					# 	candidates_tuple=(tuple([scoreVal,cell, cell_values]))
					# 	# print candidates_tuple
					# 	# print candidates
					# 	candidates.extend([candidates_tuple])

			for i in candidates:
				cell = i[1]
				cell_value = i[2]
				localGrid.setCellValue(cell, cell_value)
				result = self.intelli(localGrid, depth-1, not MaxPlayer, alpha, bestScore, eval_func)
				if result[0] < bestScore :
						bestScore = result[0]

				if bestScore <= alpha:
					return (alpha, None)



		return (bestScore, bestMove)

	def iterativeDeep(self, grid):
		start = round(time.time() * 1000)
		depth = 1
		while ((round(time.time() * 1000))-start < 100):

			move = self.intelli(grid, depth, True, float("-inf"), float("inf"), evalFunc)
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
		print "eval",evalFunc(grid)

		#print moves
		#print "test",moves[randint(0, len(moves) - 1)]
		# move = self.alphabeta(grid, 4, True,  float("-inf"), float("inf"), evalFunc)[1]
		# move = self.intelli(grid, 2, True, float("-inf"), float("inf"), evalFunc)[1]
		move = self.iterativeDeep(grid)
		return move
		#return moves[randint(0, len(moves) - 1)] if moves else None
