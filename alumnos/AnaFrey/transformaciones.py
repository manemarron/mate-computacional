def esfericaCoordenada(x, y, z):
    from math import atan, sqrt, pi
    r=sqrt(x**2+y**2+z**2)
    if z>0:
        phi=atan(sqrt(x**2+y**2)/z)
    elif z=0:
        phi= pi/2
    else:
        phi= pi+ atan(sqrt(x**2+y**2)/z)
    
    if x>0 and y>0:
        theta= atan(y/x)
    elif x>0 and y<0:
        theta= 2*pi + atan(y/x)
    elif x=0 and y>0:
        theta= (pi/2)*y
    elif x=0 and y<0:
        theta= (pi/2)*-y   
    else:
        theta= pi+atan(y/x)
    print r, phi, theta
    return r, phi, theta