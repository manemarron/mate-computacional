def phi(x,y,z):
    from math import sqrt, pi, atan
    if z>0:
        phi=atan(sqrt(x**2+y**2)/z)
    elif z==0:
        phi=pi/2.0
    else:
        phi=pi+atan(sqrt(x**2+y**2)/z)
    return phi
def theta(x,y,z):
    from math import sqrt, pi, atan
    if x>0 and y>0:
        theta=atan(y/x)
    elif x>0 and y<0:
        theta=2.0*pi+atan(y/x)
    elif x==0 and y>0:
        theta=pi/2.0
    elif x==0 and y<0:
        theta=(-1)*pi/2.0
    else:
        theta=pi+atan(y/x)
    return theta
def coordenadasCartesianas(x,y,z):
    """ cambia de coordenadas cartesianas a esfericas"""
    from math import sqrt, pi, atan
    r=sqrt(x**2+y**2+z**2)
    p=phi(x,y,z)
    t=theta(x,y,z)
    print r, t, p
    return r, t, p