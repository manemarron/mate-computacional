from math import sin,cos,sqrt,atan,pi
def coordFromSphericCoordinates(r,theta,phi):
    """
    Función que convierte un punto de coordenadas esféricas a coordenadas cartesianas
    """
    x = r*sin(theta)*cos(phi)
    y = r*sin(theta)*sin(phi)
    z = r*cos(phi)
    return x,y,z

def cartesianToSphericCoordinates(x,y,z):
    """
    Función que convierte un punto de coordenadas cartesianas a coordenadas esféricas (los ángulos se obtienen en radianes)
    """
    r = sqrt(x**2+y**2+z**2)
    if x==0 : 
        if y>0:
            theta=pi
        elif y<0:
            theta=-pi
        elif y==0:
            theta=0.0
    else: 
        theta = float(atan(y/x))
    if(z==0):
        if sqrt(x**2+y**2) > 0:
            phi=pi
        else:
            phi=0.0
    else:
        phi = float(atan(sqrt(x**2+y**2)/z))
    return r,theta,phi