class game:
    def __init__(self, path):
        self.nodesExpanded = 0
        self.trace = []
        self.n = 0
        self.gameState = self.readGame(path)
        self.parent = 0

    def readGame(self,path):
        #Reading file
        fileHandle = open(path, 'r')
        n = fileHandle.readline()
        self.n = int(n)
        puzzle = [[0 for x in range(int(n))] for x in range(int(n))]
        for i in range(self.n):
            rawState = fileHandle.readline().strip().split(',')
            if len(rawState) != self.n:
                print "1: Wrong gameState given, check txt file"
                exit(0)
            for j in range(self.n):
                puzzle[i][j] = rawState[j]
        return puzzle

    def is_empty(self,pos):
        if int(self.gameState[pos[0]][pos[1]]) == 0:
            return True
        return False

    def is_valid(self,pos,dir):
        newPos = self.getNextPosition(pos,dir)
        if (newPos[0] < 0 or newPos[0] > self.n-1) or (newPos[1] < 0 or newPos[1] > self.n-1) :
            return False
        return self.is_empty(newPos)

    def is_goal(self):
        ind  = 0
        for i in range(self.n):
            for j in range(self.n):
                if not int(self.gameState[i][j]) == ind:
                    return False
                ind  = ind + 1
        return True

    def getNextPosition(self,oldPos, dir):
        newPos = []
        newPos.append(oldPos[0]+(dir[0]))
        newPos.append(oldPos[1]+(dir[1]))
        return newPos

    def getNextState(self,oldPos,dir):
        self.nodesExpanded += 1
        if not self.is_valid(oldPos, dir):
            print "Error, You are not checking for valid move"
            return None
        newPos = self.getNextPosition(oldPos,dir)
        self.gameState[newPos[0]][newPos[1]] = self.gameState[oldPos[0]][oldPos[1]]
        self.gameState[oldPos[0]][oldPos[1]] = 0
        self.trace.append(oldPos)
        self.trace.append(newPos)
        return self.gameState