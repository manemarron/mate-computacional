from math import sin, cos
def coor_cartesianas(r,theta,phi):
    """
    devuelve las coordenadas a (x,y,z) apartir de las coordenadas esfericas 
    """
    x=r*sin(phi)*cos(theta)
    y=r*sin(phi)*sin(theta)
    z=r*cos(phi)
    return x,y,z    