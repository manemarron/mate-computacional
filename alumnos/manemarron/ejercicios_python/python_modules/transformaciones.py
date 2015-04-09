from math import sin,cos
def coordFromSphericCoordinates(r,theta,phi):
    x = r*sin(theta)*cos(phi)
    y = r*sin(theta)*sin(phi)
    z = r*cos(phi)
    return x,y,z