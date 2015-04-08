# -*- coding: utf8 -*-
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


class DinamicaRecurso(object):
    """
    Clase para representar la dinámica de la extracción de un
    recurso de acuerdo a la demanda del mismo.
    """
    def set_parameters(self, **kwargs):
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
        self.states = np.array([y])
        for i in xrange(step_number):
            t = i * dt
            self.derivatives = np.append(
                self.derivatives,
                [self._dynamic(y, t)],
                axis=0
            )
            y = method(self._dynamic, y, t, dt)
            self.states = np.append(self.states, [y], axis=0)
        self._calculate_costs()

    def integrate_odeint(self, initial_state, step_number, dt):
        self._reset()
        y = initial_state
        t = np.linspace(0, dt*step_number, step_number + 1)
        self.states = odeint(self._dynamic, y, t)
        for i in xrange(step_number):
            t = i * dt
            self.derivatives = np.append(
                self.derivatives,
                [self._dynamic(self.states[i], t)],
                axis=0
            )
        self._calculate_costs()

    def plot(self, time, *args):
        """
        Grafica los arreglos especificados respecto al tiempo

        args: lista de arreglos que se graficarán, donde cada arreglo
              es una tupla conteniendo el arreglo y la etiqueta
        """
        plt.figure(1, figsize=(8, 6))
        for a in args:
            plt.plot(time, a[0], label=a[1])
        plt.xlabel(r"t (s)")
        plt.legend(loc="best")

    def _calculate_costs(self):
        self.costs = np.append(
            self.costs,
            self.states[1:, 0]/self.derivatives[1:, 1]*self.eta,
            axis=0
        )

    def _dynamic(self, y, t):
        """
        Define la dinámica del sistema.
        _E - tasa de extracción del recurso
        _D - tasa de cambio de la demanda del recurso
        """
        _D = self.alpha * y[1]
        _E = y[0] * (1 - y[1])
        return np.array([_D, _E])

    def _reset(self):
        self.derivatives = np.array([np.array([0, 0])])
        self.costs = np.array([0])
