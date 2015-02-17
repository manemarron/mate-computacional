from math import *
def cartesianas_a_esfericas(x, y, z):
    r= sqrt(x^2 + y^2 + z^2)
    theta= atan(y/x)
    phi  = atan((sqrt(x^2 + y^2))/z)
    return  r, theta, phi
def esfericas_a_cartesianas(r, theta, phi):
    x=r*sin(phi)*cos(theta)
    y=r*sin(phi)*sin(theta)
    z=r*cos(theta)
    return x, y, z