import numpy as np 
import scipy as sc 
from scipy.stats import beta

class Class1:
    
    v1 = None

    # constructor
    def __init__(self, p):
        self.v1 = p
    
    # private method
    def __m1(self):
        return 2
            
    # public method
    def m2(self, arg1):
        self.v1 = self.__m1()
        return arg1


