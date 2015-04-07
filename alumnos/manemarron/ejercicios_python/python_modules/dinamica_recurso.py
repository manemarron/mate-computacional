# -*- coding: utf8 -*-
import numpy as np
from scipy.integrate import odeint
# import matplotlib.pyplot as plt


class DinamicaRecurso(object):
    """
    Clase para representar la dinámica de la extracción de un
    recurso de acuerdo a la demanda del mismo.
    """
    def __init__(self, **kwargs):
        super(DinamicaRecurso, self).__init__()
        for key, value in kwargs.iteritems():
            if key == "alpha":
                self.alpha = value
            if key == "eta":
                self.eta = value

    def integrate(self, initial_state, step_number, dt, method):
        """
        Realiza la integración mediante el método dado.
        """
        self._reset()
        y = initial_state
        self.states.append(y)
        for i in xrange(step_number):
            t = i * dt
            self.derivatives.append(self._dynamic(y, t))
            y = method(self._dynamic, y, t, dt)
            self.states.append(y)
            self.costs.append(self._cost(i+1))

    def integrate_odeint(self, initial_state, step_number):
        self._reset()
        y = initial_state
        self.states.append(y)
        for i in xrange(step_number):
            t = i
            self.derivatives.append(self._dynamic(y, t))
            y = odeint(self._dynamic, y, t)
            self.states.append(y)
            self.costs.append(self._cost(i+1))

    def _dynamic(self, y, t):
        """
        Define la dinámica del sistema.
        _E - tasa de extracción del recurso
        _D - tasa de cambio de la demanda del recurso
        """
        _D = self.alpha * y[1]
        _E = y[0] * (1 - y[1])
        return np.array([_D, _E])

    def _cost(self, t):
        return self.states[t][0]/self.derivatives[t][1]*self.eta

    def _reset(self):
        self.derivatives = [np.array([0, 0])]
        self.states = []
        self.costs = [0]
