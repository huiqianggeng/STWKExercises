
class Direction():
    directionList = ['W','S','E','N']
    def __init__(self,direction):
        self.direction = direction

    def getLeftDirection(self,curdirection):
        curIndex = Direction.directionList.index(curdirection)
        index = (curIndex+1)%len(Direction.directionList)
        return Direction.directionList[index]
    def getRightDirection(self,curdirection):
        curIndex = Direction.directionList.index(curdirection)
        index = curIndex -1
        return Direction.directionList[index]



class MarsRoverPosition():

    dirCorMap = {'N':1,'S':1,'E':0,'W':0}
    def __init__(self,x,y,direction):
        self.coordinateX = x
        self.coordinateY = y
        self.direction = Direction(direction)
        self.curdirection = direction


    def getInfo(self):

        return "({},{}) {}".format(self.coordinateX,self.coordinateY,self.curdirection)

    def forward(self):
        if MarsRoverPosition.dirCorMap[self.curdirection] == 0:
            self.coordinateX += 1
        else:
            self.coordinateY += 1

    def turnLeft(self):
        self.curdirection = self.direction.getLeftDirection(self.curdirection)


    def turnRight(self):
        self.curdirection = self.direction.getRightDirection(self.curdirection)

    def back(self):
        if MarsRoverPosition.dirCorMap[self.curdirection] == 0:
            self.coordinateX -= 1
        else:
            self.coordinateY -= 1

class MarsRover():

    def __init__(self,coordinateX,coordinateY,direction):
        self.marsRoverPosition = MarsRoverPosition(coordinateX,coordinateY,direction)

    def receiveCommand(self,command):
        cmdList = list(command)
        for i  in range(len(cmdList)):
            cmd = cmdList[i]
            if cmd == 'M':
                self.marsRoverPosition.forward()
            elif cmd == 'R':
                self.marsRoverPosition.turnRight()
            elif cmd == 'L':
                self.marsRoverPosition.turnLeft()
            elif cmd =='B':
                if len(cmdList)>1 and cmdList[i-1]=='B':
                    continue
                else:
                    self.marsRoverPosition.back()
        print (self.marsRoverPosition.getInfo())


if __name__=='__main__':

    marsRover = MarsRover(0,0,'N')
    marsRover.receiveCommand("MMMRMBB")





