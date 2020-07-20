

class Service():

    def __init__(self,userFactory):
        self.userFactory = userFactory

    def ShowStocks(self,userid):
        user = self.userFactory.BuildUserById(userid)
        result = user.showStocks()
        return result



class Repository():
    def __init__(self):
        super.__init__()

    def FindHoldingsByUserId(self,userid):

        holdings =[]


        return holdings

class UserFactory():

    def __init__(self,repository):
        self.repository = repository

    def BuildUserById(self,userid):
        holdings = self.repository.FindHoldingsByUserId(userid)
        user = User(userid,holdings)

        return user


class User():


    def __init__(self,userid,holdings):
        self.userid = userid
        self.holdings = holdings


    def showStocks(self):


        return ""


class Holding():

    def __init__(self,unitPrice,amount,stockSymbol):
        self.unitPrice = unitPrice
        self.amount = amount
        self.stockSymbol = stockSymbol

    def describe(self):

        return ""
    def caculateTotal(self):

        return ""







if __name__=='__main__':
    repository = Repository()
    userFactory = UserFactory(repository)
    service = Service(userFactory)
