from math import sin, cos, asin, acos, sqrt

def esfericas_a_cartesianas(r, theta, phi):
    x=r*sin(phi)*cos(theta)
    y=r*sin(phi)*sin(theta)
    z=r*cos(phi)
    return x,y,z

def cartesianas_a_esfericas(x,y,z):
    r=sqrt(x**2+y**2+z**2)
    phi=acos(z/r)
    theta=asin(y/(r*sin(phi)))
    return r,theta,phi