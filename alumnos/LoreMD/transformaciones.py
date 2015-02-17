def esfericasCartesianas (r, phi, theta):
    x=r*sin(phi)*cos(theta)
    y=r*sin(phi)*sin(theta)
    z=r*cos(phi)
    return x,y,z

def cartesianasEsfericas (x,y,z):
    r=sqrt(x*x+y*y+z*z)
    if z>0:
        theta=atan((sqrt(x*x+y*y))/z)
    elif z<0:
        theta=atan((sqrt(x*x+y*y))/z)+pi
    else:
        theta=pi/2
    if x>0:
        if y>=0:
            phi=atan(x/y)
        else:
            phi=atan(x/y)+2*pi
    elif x<0:
         phi=atan(x/y)+pi
    else:
        phi=2*pi*copysign(y)
    return r, theta, phi
    