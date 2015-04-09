# -*- coding: utf8 -*-
import numpy as np

from pendulo import Pendulo


class PenduloActuado(Pendulo):
    def __init__(self, masa, longitud, gravedad, beta, A, frequency):
        Pendulo.__init__(self, masa, longitud, gravedad)
        self.beta = beta
        self.A = A
        self.frequency = frequency

    def dynamics(self, state, t):
        g0 = state[1]
        g1 = (-self.gravedad/self.longitud*np.sin(state[0]) -
              self.beta*state[1] + self.A * np.cos(self.frequency * t))
        return np.array([g0, g1])
