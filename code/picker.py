import numpy as np
from numpy.linalg import solve
from scipy.optimize import approx_fprime

class NBAPicker:
    def __init__(self,pg=1,sg=1,sf=1,pf=1,c=1,g=1,f=1,util=1,salary=50000):
        self.pg = pg
        self.sg = sg
        self.sf = sf
        self.pf = pf
        self.c = c
        self.g = g
        self.f = f
        self.util = util
        self.salary = salary

    def pick(self,X):
        raise NotImplementedError
