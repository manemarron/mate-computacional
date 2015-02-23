from math import cos, sin
def esfericasCartesianas(r,theta,phi):
    
    """
    Recibe las coordenadas esféricas de un punto en R^3 y devuelve las cartesianas.
    """
    
    x = r*cos(theta)*sin(phi)
    y = r*sin(theta)*sin(phi)
    z = r*cos(phi)
    
    print x, y, z
    return x, y, z