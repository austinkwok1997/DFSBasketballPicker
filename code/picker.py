import numpy as np
from numpy.linalg import solve
from scipy.optimize import approx_fprime
import knapsack

class NBAPicker:
    def __init__(self,pg=1,sg=1,sf=1,pf=1,c=1,g=1,f=1,util=1,salary=50000):
        self.numOfPG = pg
        self.numOfSG = sg
        self.numOfSF = sf
        self.numOfPF = pf
        self.numOfC = c
        self.numOfG = g
        self.numOfF = f
        self.numOfUtil = util
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
        players = knapsack.solve(salary=int(self.salary/100),X=X,)
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
    
    def getPG():
        return self.pg
    def getSG():
        return self.sg
    def getSF():
        return self.sf
    def getPF():
        return self.pf
    def getC():
        return self.c
    def getG():
        return self.g
    def getF():
        return self.f
    def getUtil():
        return self.util
    
    def setPG(x):
        self.pg = x
    def setSG(x):
        self.sg = x
    def setSF(x):
        self.sf = x
