def coordenadasEsfericas(r,theta,phi):
    """ cambia de coordenadas esfericas a coordenadas x,y,z """
    from math import sin, cos
    x=r*sin(phi)*cos(theta)
    y=r*sin(phi)*sin(theta)
    z=r*cos(phi)
    print x,y,z
    return x,y,z