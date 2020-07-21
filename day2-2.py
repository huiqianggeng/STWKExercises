

class Direction():
    North = 'N'
    East = 'E'
    South = 'S'
    West = 'W'
    directionList = [West,South,East,North]
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

    dirCorMap = {Direction.North:1,Direction.South:1,Direction.East:0,Direction.West:0}
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

class Command():
    Move = 'M'
    Right = 'R'
    Left = 'L'
    Back = 'B'

class MarsRover():

    def __init__(self,coordinateX,coordinateY,direction):
        self.marsRoverPosition = MarsRoverPosition(coordinateX,coordinateY,direction)
        self.flag = True
    def receiveCommand(self,command):
        cmdList = list(command)
        for i  in range(len(cmdList)):
            cmd = cmdList[i]
            if cmd == Command.Move:
                self.marsRoverPosition.forward()
            elif cmd == Command.Right:
                self.marsRoverPosition.turnRight()
            elif cmd == Command.Left:
                self.marsRoverPosition.turnLeft()
            elif cmd == Command.Back:
                if len(cmdList)>1 and cmdList[i-1]==Command.Back and self.flag:
                    self.flag = False
                    continue
                else:
                    self.marsRoverPosition.back()
        print (self.marsRoverPosition.getInfo())


if __name__=='__main__':

    marsRover = MarsRover(0,0,'N')
    marsRover.receiveCommand("MMMRMBBB")





