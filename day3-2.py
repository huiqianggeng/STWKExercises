
import time,datetime
import unittest

class ConsumeType():
    #pos机消费
    posConsume = r'pos机消费'
    #微信支付消费
    wxConsume = r'微信支付消费'
    #信用卡快捷支付消费
    creditQuickConsume = r'快捷支付消费'
    #信用卡分期购物消费
    creditTimesConsume = r'信用卡分期购物消费'

class ScoreShowFormat():

    formalFormat = "formal"
    htmlFormat = "html"

"""
pos机消费的积分计算实现
"""
class PosConsume():

    money = 10
    score = 1
    goldenRatio = 0.5
    def __init__(self):
        pass

    def getConsumeScores(self,consumeType,sumOfConsume,goldenCardFlag):
        consumeScores = 0
        if consumeType == ConsumeType.posConsume:
            consumeScores += (sumOfConsume // PosConsume.money)*PosConsume.score
            if goldenCardFlag:
                goldenScore = str(consumeScores*PosConsume.goldenRatio).split('.')[0]
                consumeScores += int(goldenScore)

        return consumeScores

"""
微信支付消费的积分计算实现
"""
class WxConsume():
    money = 20
    score = 1
    goldenRatio = 0.5
    def __init__(self):
        pass
    def getConsumeScores(self,consumeType,sumOfConsume,goldenCardFlag):
        consumeScores = 0
        if consumeType == ConsumeType.wxConsume:
            consumeScores += (sumOfConsume // WxConsume.money)*WxConsume.score
            if goldenCardFlag:
                goldenScore = str(consumeScores*WxConsume.goldenRatio).split('.')[0]
                consumeScores += int(goldenScore)
        return consumeScores

"""
信用卡快捷支付消费的积分计算实现
"""
class CreditQuickConsume():
    basicMoney = 10
    basicScore = 1
    otherMoney = 100
    otherScore = 5
    maxScore = 100
    goldenRatio = 0.5
    def __init__(self):
        pass

    def getConsumeScores(self,consumeType, sumOfConsume,goldenCardFlag):
        consumeScores = 0
        if consumeType == ConsumeType.creditQuickConsume:
            basicScore = (sumOfConsume // CreditQuickConsume.basicMoney)*CreditQuickConsume.basicScore
            consumeScores += basicScore
            otherScore1 = (sumOfConsume // CreditQuickConsume.otherMoney)*CreditQuickConsume.otherScore
            consumeScores += (CreditQuickConsume.maxScore if otherScore1 > CreditQuickConsume.maxScore else otherScore1)
            if goldenCardFlag:
                otherScore2 = int(str(basicScore*CreditQuickConsume.goldenRatio).split('.')[0])
                consumeScores += otherScore2

        return consumeScores

"""
信用卡分期消费积分计算实现
"""
class CreditTimesConsume():
    basicMoney = 10
    basicScore = 1
    otherMoney = 5000
    otherScore = 100
    goldenRatio = 0.5
    def __init__(self):
        pass

    def getConsumeScores(self,consumeType, sumOfConsume,goldenCardFlag):
        consumeScores = 0
        if consumeType == ConsumeType.creditTimesConsume:
            basicScore = (sumOfConsume // CreditTimesConsume.basicMoney) * CreditTimesConsume.basicScore
            consumeScores += basicScore
            if sumOfConsume >= CreditTimesConsume.otherMoney:
                consumeScores += CreditTimesConsume.otherScore
            if goldenCardFlag:
                otherScore2 = int(str(basicScore*CreditTimesConsume.goldenRatio).split('.')[0])
                consumeScores += otherScore2
        return consumeScores
"""
最后的积分展示实现
"""
class ShowScores():

    def __init__(self):
        pass

    def getFormalScores(self,scoreInfoList):
        infolist = []
        totalScore = 0
        for item in scoreInfoList:
            consumeTime = item[0]
            consumeType = item[1]
            sumOfConsume = item[2]
            score = item[3]
            scoreInfo = "{} {} {}元, 积分 +{}".format(consumeTime, consumeType, sumOfConsume, score)
            infolist.append(scoreInfo)
            totalScore += score
        infolist.append("总积分：{}".format(totalScore))
        infolist = list(reversed(infolist))
        for info in infolist:
            print(info)

    def getHtmlScores(self,scoreInfoList):
        infolist = []
        totalScore = 0
        for item in scoreInfoList:
            consumeTime = item[0]
            consumeType = item[1]
            sumOfConsume = item[2]
            score = item[3]
            scoreInfo = "<p>{} {} {}元, 积分 <b>+{}</b></p>".format(consumeTime, consumeType, sumOfConsume, score)
            infolist.append(scoreInfo)
            totalScore += score
        infolist.append("<h2>总积分：<b>{}</b></h2>".format(totalScore))
        infolist = list(reversed(infolist))
        for info in infolist:
            print(info)

"""
积分计算实现
"""
class CalculateScores():

    def __init__(self):
        self.consumeMap = {}
        self.consumeMap[ConsumeType.posConsume] = (PosConsume())
        self.consumeMap[ConsumeType.wxConsume] = (WxConsume())
        self.consumeMap[ConsumeType.creditQuickConsume] = (CreditQuickConsume())
        self.consumeMap[ConsumeType.creditTimesConsume] = (CreditTimesConsume())
        self.showScores = ShowScores()
        self.scoreInfolist = []
    def getScores(self,consumeList):
        totalScore = 0
        for item in consumeList:
            consumeType = item[0]
            sumOfConsume = item[1]
            goldenCardFlag = item[2]
            consumeTime = item[3]
            consumeTypeObject = self.consumeMap[consumeType]
            score =  consumeTypeObject.getConsumeScores(consumeType,sumOfConsume,goldenCardFlag)
            totalScore += score
            self.scoreInfolist.append((consumeTime,consumeType,sumOfConsume,score))
        return totalScore

    def printScores(self,formatFlag):
        if formatFlag == ScoreShowFormat.formalFormat:
            self.showScores.getFormalScores(self.scoreInfolist)
        elif formatFlag == ScoreShowFormat.htmlFormat:
            self.showScores.getHtmlScores(self.scoreInfolist)
        self.scoreInfolist = []



class TestCalculateScores(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_posConsume(self):
        consumeList = [[r'pos机消费', 8, False, '2020-07-23 11:31:41'],[r'pos机消费', 108, False, '2020-07-23 11:34:40'],
                       [r'pos机消费', 208, False, '2020-07-23 12:10:11']]
        scoreShowFormat = "formal"
        calculateScores = CalculateScores()
        totalScore = calculateScores.getScores(consumeList)
        calculateScores.printScores(scoreShowFormat)
        self.assertEqual(30,totalScore)

    def test_pos_wxConsume(self):
        consumeList = [[r'微信支付消费', 25, False, '2020-07-23 11:31:41'],[r'微信支付消费', 18, False, '2020-07-23 11:34:40'],
                       [r'pos机消费', 108, False, '2020-07-23 12:10:11'],[r'微信支付消费', 10, False, '2020-07-23 14:34:22'],
                       [r'微信支付消费', 22, False, '2020-07-23 14:54:20'],[r'pos机消费', 208, False, '2020-07-23 12:10:11']]
        scoreShowFormat = "formal"
        calculateScores = CalculateScores()
        totalScore = calculateScores.getScores(consumeList)
        calculateScores.printScores(scoreShowFormat)
        self.assertEqual(32,totalScore)

    def test_pos_wx_creditConsume(self):
        consumeList = [[r'微信支付消费', 25, False, '2020-07-23 11:31:41'],[r'微信支付消费', 18, False, '2020-07-23 11:34:40'],
                       [r'pos机消费', 108, False, '2020-07-23 12:10:11'],[r'微信支付消费', 10, False, '2020-07-23 14:34:22'],
                       [r'微信支付消费', 22, False, '2020-07-23 14:54:20'],[r'pos机消费', 208, False, '2020-07-23 15:10:11'],
                       [r'快捷支付消费', 208, False, '2020-07-23 15:59:21'], [r'快捷支付消费', 2208, False, '2020-07-23 16:09:19']]
        scoreShowFormat = "formal"
        calculateScores = CalculateScores()
        totalScore = calculateScores.getScores(consumeList)
        calculateScores.printScores(scoreShowFormat)
        self.assertEqual(382,totalScore)

    def test_pos_wx_creditsConsume(self):
        consumeList = [[r'微信支付消费', 25, False, '2020-07-23 11:31:41'],[r'微信支付消费', 18, False, '2020-07-23 11:34:40'],
                       [r'pos机消费', 108, False, '2020-07-23 12:10:11'],[r'微信支付消费', 10, False, '2020-07-23 14:34:22'],
                       [r'微信支付消费', 22, False, '2020-07-23 14:54:20'],[r'pos机消费', 208, False, '2020-07-23 15:10:11'],
                       [r'快捷支付消费', 208, False, '2020-07-23 15:59:21'], [r'快捷支付消费', 2208, False, '2020-07-23 16:09:19'],
                       [r'信用卡分期购物消费', 6400, False, '2020-07-23 16:28:28']]
        scoreShowFormat = "formal"
        calculateScores = CalculateScores()
        totalScore = calculateScores.getScores(consumeList)
        calculateScores.printScores(scoreShowFormat)
        self.assertEqual(1122,totalScore)

    def test_pos_wx_credit_goldenConsume(self):
        consumeList = [[r'微信支付消费', 25, True, '2020-07-23 11:31:41'],[r'微信支付消费', 18, True, '2020-07-23 11:34:40'],
                       [r'pos机消费', 108, True, '2020-07-23 12:10:11'],[r'微信支付消费', 10, True, '2020-07-23 14:34:22'],
                       [r'微信支付消费', 22, True, '2020-07-23 14:54:20'],[r'pos机消费', 208, True, '2020-07-23 15:10:11'],
                       [r'快捷支付消费', 208, True, '2020-07-23 15:59:21'], [r'快捷支付消费', 2208, True, '2020-07-23 16:09:19'],
                       [r'信用卡分期购物消费', 6400, True, '2020-07-23 16:28:28']]
        scoreShowFormat = "html"
        calculateScores = CalculateScores()
        totalScore = calculateScores.getScores(consumeList)
        calculateScores.printScores(scoreShowFormat)
        self.assertEqual(1577,totalScore)


if __name__ =='__main__':

    tests = [TestCalculateScores("test_posConsume"),TestCalculateScores("test_pos_wxConsume"),
             TestCalculateScores("test_pos_wx_creditConsume"),TestCalculateScores("test_pos_wx_creditsConsume"),
             TestCalculateScores("test_pos_wx_credit_goldenConsume")]
    suite = unittest.TestSuite()
    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)


        
