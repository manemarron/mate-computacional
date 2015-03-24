import numpy as np
from euler import *

class Pendulo:
    def __init__(self,l,m,g):
        self._m = m
        self._l = l
        self.G = g
        self.frequency = np.sqrt(self.G/self._l)
        self.T = 2*np.pi/self.frequency
        self.dy = lambda y: np.array([y[1],-self.G/self._l*y[0]])
        
    def analytic_position(self,t,theta,omega):
        return (theta*np.cos(t*self.frequency)) + (omega/self.frequency*np.sin(t*self.frequency))
    
    def euler_position(self,y,tau,N):
        return euler(y,self.dy,tau,N)
    