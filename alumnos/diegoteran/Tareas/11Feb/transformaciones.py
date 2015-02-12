from math import *
def coordenadasEsfericas(r, theta, phi):
    x = r*sin(phi)*cos(theta)
    y = r*sin(phi)*sin(theta)
    x = r*cos(phi)
    print x,y,z
    
def coordenadasCartesianas(x, y, z):
    r = x**2 + y**2 + z**2
    r = sqrt(r)
    theta = atan2(sqrt(x**2 + y**2), z)
    phi = atan2(y, x)
    print r, theta, phi