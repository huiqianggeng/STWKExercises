
class CaculateResult():

    def __init__(self,s1,s2):
        self.s1 = s1
        self.s2 = s2

    def getFz(self):
        # fz1 = self.s1.split('/')[0]
        # fz2 = self.s2.split('/')[0]
        # return fz1, fz2

        fz1 = self.s1[0]
        fz2 = self.s2[0]
        return fz1,fz2

    def getFm(self):
        # fm1 = self.s1.split('/')[1]
        # fm2 = self.s2.split('/')[1]
        # return fm1, fm2

        fm1 = self.s1[-1]
        fm2 = self.s2[-1]
        return fm1,fm2

    def caculate(self):
        fz1,fz2 = self.getFz()
        fm1,fm2 = self.getFm()
        fz = int(fz1)*int(fz2)
        fm = int(fm1)*int(fm2)
        return str(fz)+"/"+str(fm)


if __name__=='__main__':
    # cr =  CaculateResult("2/5","3/5")
    cr = CaculateResult([2,5],[3,5])
    print(cr.caculate())



