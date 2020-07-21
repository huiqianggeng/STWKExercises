
class Frame():
    maxScore = 10
    """
     self.rolls,用于记录每次扔球的得分列表
    """
    def __init__(self):

        self.rolls = [0,0]
        self.flag = 0

    def roll(self,hits):
        #将每次扔球击中的球的个数(得分)加入到得分列表
        #self.rolls.append(hits)
        self.rolls[self.flag] = hits
        self.flag += 1

    def getScore(self):
        score = sum(self.rolls)
        return score

    def getRolls(self):
        return self.rolls

    def isEnd(self):
        flag = False
        if self.flag ==2 or (self.flag ==1 and self.getScore()==Frame.maxScore):
            flag = True
        return flag
    def isStrike(self):
        flag = False
        if self.isEnd():
            if self.flag ==1 :
                flag = True
        return flag
    def isSpare(self):
        flag = False
        if self.flag==2 and self.getScore()==Frame.maxScore:
            flag = True
        return flag


class BowlingGame():
    #最多会有12次
    initFrame = 12
    maxScore = 10
    endFrame = 10

    def __init__(self):
        self.frames = [Frame() for i in range(BowlingGame.initFrame)]
        self.frameScore = []
        self.currentFrame = None
        #标识当前所处的格子数
        self.currentFlag = 0
        self.updateFlag = False

    def roll(self,hits):
        #根据标识，取出对应的格子
        self.currentFrame = self.frames[self.currentFlag]
        self.currentFrame.roll(hits)
        # #当当前的格子的两次扔球完毕时，更新格子标识
        # if self.currentFlag >= 1:
        #     lastFrameScore = self.frameScore[self.currentFlag - 1]
        #     if lastFrameScore == BowlingGame.maxScore:
        #         curFirstScore = self.currentFrame.getRolls()[0]
        #         lastFrameScore += curFirstScore
        #         self.frameScore[self.currentFlag - 1] = lastFrameScore
        if self.currentFrame.isEnd():
            self.currentFlag += 1
            self.frameScore.append(self.currentFrame.getScore())

    def updateScores(self):
        for i in range(BowlingGame.endFrame):
            curFrame = self.frames[i]
            if curFrame.isStrike():
                count = 0
                nextFrame = self.frames[i+1]
                nnextFrame = self.frames[i+2]
                if not nextFrame.isStrike():
                    count = nextFrame.getScore()
                elif nextFrame.isStrike() and (not nnextFrame.isStrike()):
                    count = nextFrame.getScore() + nnextFrame.getRolls()[0]
                elif nextFrame.isStrike() and nnextFrame.isStrike():
                    count = nextFrame.getScore() + nnextFrame.getScore()
                self.frameScore[i] += count
            elif curFrame.isSpare():
                nextFrame = self.frames[i+1]
                count = nextFrame.getRolls()[0]
                self.frameScore[i] += count
            else:
                continue



    def isEnd(self):

        return True if self.currentFlag+1 == BowlingGame.endFrame else False


    def showEveryFrameScore(self):

        if not self.updateFlag :
            self.updateScores()
            self.updateFlag = True
        numScores = len(self.frameScore)
        numFrames = BowlingGame.endFrame if numScores >= BowlingGame.endFrame else numScores
        return '|'.join([str(self.frameScore[i]) for i in range(numFrames)])

if __name__=="__main__":

    bg = BowlingGame()
    # for i in range(20):
    #     bg.roll(4)
    bg.roll(10)
    bg.roll(7)
    bg.roll(3)
    bg.roll(9)
    bg.roll(0)
    bg.roll(10)
    bg.roll(0)
    bg.roll(8)
    bg.roll(8)
    bg.roll(2)
    bg.roll(0)
    bg.roll(6)
    bg.roll(10)
    bg.roll(10)
    bg.roll(10)
    bg.roll(8)
    bg.roll(1)
    print(bg.showEveryFrameScore())





