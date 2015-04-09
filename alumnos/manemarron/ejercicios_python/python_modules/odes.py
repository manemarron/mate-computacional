# -*- coding: utf8 -*-


def euler(f, y, t, dt):
    return y + f(y, t)*dt


def rk4(f, y, t, dt):
    """
    Función que obtiene la 'y' en la siguiente iteración
    en el método de Runge Kutta de orden 4.

    Parámetros:
    f - función a la que es igual la derivada de 'y'
    y - valor actual de 'y'
    t - valor actual del tiempo
    h - paso de tiempo
    """
    k1 = f(y, t)
    k2 = f(y + 0.5*k1*dt, t + 0.5*dt)
    k3 = f(y + 0.5*k2*dt, t + 0.5*dt)
    k4 = f(y + k3*dt, t + dt)

    return y + 1/6*dt*(k1 + 2*k2 + 2*k3 + k4)
