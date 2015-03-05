from math import cos, sin
def cartesianas(r,theta,phi):
    x=r*cos(theta)*sin(phi)
    y=r*sin(theta)*sin(phi)
    z=r*cos(phi)
    print (x,y,z)