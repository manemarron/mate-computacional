# -*- coding: utf8 -*-
import numpy as np

from pendulo import Pendulo


class PenduloReal(Pendulo):
    def __init__(self, masa, longitud, gravedad):
        Pendulo.__init__(self, masa, longitud, gravedad)

    def dynamics(self, state, t):
        g0 = state[1]
        g1 = -self.gravedad/self.longitud*np.sin(state[0])
        return np.array([g0, g1])
