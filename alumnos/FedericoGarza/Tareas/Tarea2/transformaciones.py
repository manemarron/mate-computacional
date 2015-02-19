from math import sin,cos
def cartesianas(r,theta,phi):
    """
    convierte coordenadas esfericas en cartesianas
    """
    x=r*sin(phi)*cos(theta)
    y=r*sin(phi)*sin(theta)
    z=r*cos(phi)
    print x,y,z    
    
from math import sqrt,atan2
def esfericas(x,y,z):
    """
    convierte coordenadas cartesianas en esfericas
    """
    r=sqrt(x**2+y**2+z**2)
    theta=atan2(sqrt(x**2+y**2)/z)
    phi=atan2(y/x)
    print r,theta,phi      
