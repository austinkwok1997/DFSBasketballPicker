import numpy as np
from numpy.linalg import solve
from scipy.optimize import approx_fprime
import knapsack

class NBAPicker:
    def __init__(self,pg=1,sg=1,sf=1,pf=1,c=1,g=1,f=1,util=1,salary=50000):
        self.limits = PlayerLimits(pg=pg,sg=sg,sf=sf,pf=pf,c=c,g=g,f=f,util=util)
        self.salary = salary

    def pick(self,X):
        pgIndex = []
        sgIndex = []
        sfIndex = []
        pfIndex = []
        cIndex = []
        gIndex = []
        fIndex = []
        for player in range(X["position"].size):
            if "PG" in X["position"][player]:
                pgIndex.append(player)
                gIndex.append(player)
            if "SG" in X["position"][player]:
                sgIndex.append(player)
                gIndex.append(player)
            if "SF" in X["position"][player]:
                sfIndex.append(player)
                fIndex.append(player)
            if "PF" in X["position"][player]:
                pfIndex.append(player)
                fIndex.append(player)
            if "C" in X["position"][player]:
                cIndex.append(player)
        players = knapsack.solve(salary=int(self.salary/100),X=X,limits=self.limits)
        print(X["player"][players])
        
class PlayerLimits:
    def __init__(self,pg,sg,sf,pf,c,g,f,util):
        self.pg = pg
        self.sg = sg
        self.sf = sf
        self.pf = pf
        self.c = c
        self.g = g
        self.f = f
        self.util = util
    
    def getPG(self):
        return self.pg
    def getSG(self):
        return self.sg
    def getSF(self):
        return self.sf
    def getPF(self):
        return self.pf
    def getC(self):
        return self.c
    def getG(self):
        return self.g
    def getF(self):
        return self.f
    def getUtil(self):
        return self.util
    
    def setPG(self,x):
        self.pg = x
    def setSG(self,x):
        self.sg = x
    def setSF(self,x):
        self.sf = x
    def setPF(self,x):
        self.pf = x
    def setC(self,x):
        self.c = x
    def setG(self,x):
        self.g = x
    def setF(self,x):
        self.f = x
    def setUtil(self,x):
        self.util = x