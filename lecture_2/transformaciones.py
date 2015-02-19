
from math import sqrt, sin, cos
def coord(r,phi, theta):
    x=r*sin(phi)*cos(theta) 
    y =r* sin(phi)*sin(theta)
    z=r*cos(phi)
    return x,y,z
    print x,y,z