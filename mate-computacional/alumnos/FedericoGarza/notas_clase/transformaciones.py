from math import sin,cos
def cartesianas(r,theta,phi):
    """
    convierte coordenadas esfericas en cartesianas
    """
    x=r*sin(phi)*cos(theta)
    y=r*sin(phi)*sin(theta)
    z=r*cos(phi)
    print x,y,z    