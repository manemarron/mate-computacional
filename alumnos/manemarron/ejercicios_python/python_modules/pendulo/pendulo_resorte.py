# -*- coding: utf8 -*-
import numpy as np
from scipy.integrate import odeint

from pendulo import Pendulo


class PenduloResorte(Pendulo):
    def __init__(self, masa, L0, gravedad, k):
        Pendulo.__init__(self, masa, L0, gravedad)
        self.k = k

    def dynamics(self, state, t):
        g0 = state[1]
        g2 = state[3]
        g1 = ((self.L0 + state[0]) * g2**2 - self.k / self.m * state[0] +
              self.gravedad * np.cos(state[2]))
        g3 = (-(self.L0 + state[0])**-1 *
              (self.gravedad * np.sin(state[2]) + 2 * g0 * np.cos(g2)))
        return np.array([g0, g1, g2, g3])

    def integrate(self, y, time):
        print odeint(func=self.dynamics, y0=y, t=time)
