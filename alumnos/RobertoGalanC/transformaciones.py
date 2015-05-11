from math import acos, sin, pi, sqrt, degrees
def esfericas(x,y,z):
    r =sqrt(x*x+y*y+z*z)
    theta = degrees(acos(z/r))
    phi = degrees(acos(x/r*sin(theta)))
    return r, theta, phi
    