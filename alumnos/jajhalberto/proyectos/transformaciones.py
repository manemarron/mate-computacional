from math import sqrt, atan,pi,sin,cos
def cart(r,th,ph):
    """
    """
    
    x=r*sin(th)*cos(ph)
    y=r*sin(th)*sin(th)
    z=r*cos(th)
    return x,y,z