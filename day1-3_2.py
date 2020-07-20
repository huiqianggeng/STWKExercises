
class Frame():

    """
     self.rolls,用于记录每次扔球的得分列表
    """
    def __init__(self):

        self.rolls = []

    def roll(self,hits):
        #将每次扔球击中的球的个数(得分)加入到得分列表
        self.rolls.append(hits)

    def getScore(self):
        score = sum(self.rolls)
        return score

    def getRolls(self):
        return self.rolls

    def isEnd(self):

        return True if len(self.rolls)== 2 else False

class BowlingGame():

    endFrame = 10

    def __init__(self):
        self.frames = [Frame() for i in range(BowlingGame.endFrame)]
        self.frameScore = []
        self.currentFrame = None
        #标识当前所处的格子数
        self.currentFlag = 0

    def roll(self,hits):
        #根据标识，取出对应的格子
        self.currentFrame = self.frames[self.currentFlag]
        self.currentFrame.roll(hits)
        #当当前的格子的两次扔球完毕时，更新格子标识
        if self.currentFlag >= 1:
            lastFrameScore = self.frameScore[self.currentFlag - 1]
            if lastFrameScore == BowlingGame.endFrame:
                curFirstScore = self.currentFrame.getRolls()[0]
                lastFrameScore += curFirstScore
                self.frameScore[self.currentFlag - 1] = lastFrameScore
        if self.currentFrame.isEnd():
            self.currentFlag += 1
            self.frameScore.append(self.currentFrame.getScore())


    def isEnd(self):

        return True if self.currentFlag+1 == BowlingGame.endFrame else False


    def showEveryFrameScore(self):
        for i in range(len(self.frameScore)):
            print ("Current Frame is {}, score is {}".format(i,self.frameScore[i]))

if __name__=="__main__":

    bg = BowlingGame()
    bg.roll(4)
    bg.roll(6)
    bg.roll(2)
    bg.roll(1)
    bg.roll(1)
    bg.roll(1)
    bg.showEveryFrameScore()





