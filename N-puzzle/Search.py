import Gamestate
import Queue
import copy
import argparse
import time
from sys import getsizeof


DIRECTION = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1) }
def printArray(args):
    print "\t".join(args)


def BreadthFirstSearch(nPuzzleObject):
    global maxqueueSize
    n = nPuzzleObject.n
    queue = Queue.Queue()
    queue.put(nPuzzleObject)
    moves = 0
    maxqueueSize=0
    visited = set()
    while not queue.empty():
        puzzleTemp = queue.get()
        maxqueueSize = maxqueueSize+1
        if puzzleTemp.is_goal():
            nPuzzleObject.trace = puzzleTemp.trace
            nPuzzleObject.nodesExpanded = moves
            return nPuzzleObject

        if puzzleTemp not in visited:
            visited.add(puzzleTemp)
            for i in range(n):
                for j in range(n):
                    if not puzzleTemp.gameState[i][j] == 0:
                        for direction in DIRECTION:
                            puzzleCopy = copy.deepcopy(puzzleTemp)
                            flag = puzzleCopy.is_valid([i, j], DIRECTION[direction])
                            if flag:
                                puzzleCopy.getNextState([i, j], DIRECTION[direction])
                                moves = moves+1

                                if puzzleCopy.is_goal():
                                    nPuzzleObject.trace = puzzleCopy.trace
                                    nPuzzleObject.nodesExpanded = moves
                                    return nPuzzleObject
                                queue.put(puzzleCopy)
    nPuzzleObject.trace = ['NO GOAL STATE FOUND']
    return nPuzzleObject
'''
def BreadthFirstSearch(nPuzzleObject):
    n = nPuzzleObject.n
    nPuzzleObject.depth = 0
    queue = list()
    queue.append(nPuzzleObject)
    moves = 0
    visited = set()
    while not len(queue) == 0:
        puzzleTemp = queue.pop()
        if puzzleTemp.is_goal():
            nPuzzleObject.trace = puzzleTemp.trace
            nPuzzleObject.nodesExpanded = moves
            return nPuzzleObject

        if puzzleTemp not in visited:
            visited.add(puzzleTemp)
            expanded_nodes,moves = expand_node(puzzleTemp,moves)
            queue.extend(expanded_nodes)
    nPuzzleObject.trace = ['NO GOAL STATE FOUND']
    return nPuzzleObject
'''

def expand_node(node,moves):
    expanded_nodes = []
    for i in range(node.n):
        for j in range(node.n):
            if not node.gameState[i][j] == 0:
                for direction in DIRECTION:
                    puzzleCopy = copy.deepcopy(node)
                    puzzleCopy.depth = node.depth + 1
                    flag = puzzleCopy.is_valid([i, j], DIRECTION[direction])
                    if flag:
                        puzzleCopy.getNextState([i, j], DIRECTION[direction])
                        moves = moves + 1
                        expanded_nodes.append(puzzleCopy)
    return expanded_nodes,moves



def DepthFirstSearch(nPuzzleObject,depth):
    global maxstackSize
    maxstackSize=0
    n = nPuzzleObject.n
    stack = list()
    nPuzzleObject.depth = 0
    stack.append(nPuzzleObject)
    moves = 0
    while True:
        if len(stack)>maxstackSize:
            maxstackSize=len(stack)
        if len(stack) == 0: return None
        puzzleTemp = stack.pop()
        if puzzleTemp.is_goal():
            nPuzzleObject.trace = puzzleTemp.trace
            nPuzzleObject.nodesExpanded = moves
            return nPuzzleObject
        if(puzzleTemp.depth < depth):
            expanded_nodes,moves = expand_node(puzzleTemp,moves)
            expanded_nodes.extend(stack)
            stack = expanded_nodes
        else:
            break

    nPuzzleObject.trace = ['NO GOAL STATE FOUND']
    return nPuzzleObject

def heuristic(node):
    score = 0
    ind  = 0
    for i in range(node.n):
        for j in range(node.n):
            if not int(node.gameState[i][j]) == ind:
                score = score + 1
            ind  = ind + 1
	return score


def astar(node):
    global pqSize
    pqSize=0
    pq = Queue.PriorityQueue()
    pq.put((0, node))
    n = node.n
    moves=0
    while not pq.empty():
        pqSize = pqSize+1
        array_pq = pq.get()
        puzzleTemp = array_pq[1]
        if puzzleTemp.is_goal():
            node.trace = puzzleTemp.trace
            node.nodesExpanded = moves
            return node
        for i in range(n):
            for j in range(n):
                if not node.gameState[i][j] == 0:
                    for direction in DIRECTION:
                        puzzleCopy = copy.deepcopy(puzzleTemp)
                        flag = puzzleCopy.is_valid([i, j], DIRECTION[direction])
                        if flag:
                            puzzleCopy.getNextState([i, j], DIRECTION[direction])
                            moves = moves+1
                            if puzzleCopy.is_goal():
                                node.trace = puzzleCopy.trace
                                node.nodesExpanded = moves
                                return node
                            hn = heuristic(puzzleCopy)
                            gn = puzzleCopy.nodesExpanded
                            pq.put(((hn+gn), puzzleCopy))

    node.trace = ['NO GOAL STATE FOUND']
    return node

def main(args):
    file = args.input

    print "--BFS--"
    tic = time.clock()
    gameBFS = Gamestate.game(file)
    tracing_state=gameBFS
    res = BreadthFirstSearch(gameBFS)
    toc = time.clock()
    timeBFS = toc - tic
    print "Nodes Expanded: ",res.nodesExpanded
    print "Number of Moves:", len(res.trace)/2
    print "Max Depth of Queue", maxqueueSize
    print "Memory:", maxqueueSize*getsizeof(Gamestate), "Bytes"
    print "Solution Path:"
    for i in range(0,len(res.trace),2):
        tracing_state.gameState[res.trace[i+1][0]][res.trace[i+1][1]]=tracing_state.gameState[res.trace[i][0]][res.trace[i][1]]
        tracing_state.gameState[res.trace[i][0]][res.trace[i][1]]=0
        for row in tracing_state.gameState:
            printArray([str(x) for x in row])
        print
    print "Running Time: ", timeBFS
    print

    tic = time.clock()
    gameDFS = Gamestate.game(file)
    tracing_state=gameDFS
    res = DepthFirstSearch(gameDFS,10)
    toc = time.clock()
    timeDFS = toc - tic
    print "--DFS--"
    print "Nodes Expanded: ",res.nodesExpanded
    print "Number of Moves:", len(res.trace)/2
    print "Max Depth of Stack:", maxstackSize
    print "Memory:", maxstackSize*getsizeof(Gamestate), "Bytes"
    print "Solution Path:"
    for i in range(0,len(res.trace),2):
        tracing_state.gameState[res.trace[i+1][0]][res.trace[i+1][1]]=tracing_state.gameState[res.trace[i][0]][res.trace[i][1]]
        tracing_state.gameState[res.trace[i][0]][res.trace[i][1]]=0
        for row in tracing_state.gameState:
            printArray([str(x) for x in row])
        print
    print "Running Time: ", timeDFS
    print

    print "--Astar--"
    tic = time.clock()
    gameAstar = Gamestate.game(file)
    tracing_state=gameAstar
    res = astar(gameAstar)
    toc = time.clock()
    timeAstar = toc - tic
    print "Nodes Expanded: ",res.nodesExpanded
    print "Number of Moves:", len(res.trace)/2
    print "Max Depth of Queue", pqSize
    print "Memory:", pqSize*getsizeof(Gamestate), "Bytes"
    print "Solution Path:"
    for i in range(0,len(res.trace),2):
        tracing_state.gameState[res.trace[i+1][0]][res.trace[i+1][1]]=tracing_state.gameState[res.trace[i][0]][res.trace[i][1]]
        tracing_state.gameState[res.trace[i][0]][res.trace[i][1]]=0
        for row in tracing_state.gameState:
            printArray([str(x) for x in row])
        print
    print "Running Time: ", timeAstar


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="N-Puzzle")
    parser.add_argument("--input", type=str)
    #parser.add_argument("--flag", type = int)
    args = parser.parse_args()
    main(args)