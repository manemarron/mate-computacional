from math import sin , cos, sqrt, atan, pi
def sgn(r):
    """
    r cualquier real
    """
    if r>0:
       resp=1
    else:
        if r<0:
            resp=-1
        else: 
            resp=0
    print resp
def esfCart(r,th,ph):
    """
    r radio, th la asimutal(angulo con el eje z, en grados),
    ph la colatitud (angulo de la proyeccion en el plano xy y el eje x
    en grados)
    """
    x=r*sin((th*2*pi)/360)*cos((ph*2*pi)/360)
    y=r*sin((th*2*pi)/360)*sin((ph*2*pi)/360)
    z=r*cos((th*2*pi)/360)
    print x,y,z

def cartEsf(x,y,z):
    """
    x, y, z son una terna ordenada
    """
    r=sqrt(x**2+y**2+z**2)
    if z>0:
        th=atan(sqrt(x**2+y**2)/z)
    else:
        if z<0:
            th=atan(sqrt(x**2+y**2)/z)+pi
        else:
                th=pi/2
    if x>0 and y>0:
        ph=atan((y*1.0)/(x*1.0))
    else:
        if x>0 and y<0:
            ph=atan((y*1.0)/(x*1.0))+2*pi
        else:
            if x<0:
                ph=atan((y*1.0)/(x*1.0))+pi
            else:
                ph=sgn(y)*pi/2
    phg=(ph*360)/(2*pi)
    thg=(th*360)/(2*pi)
    print r,thg,phg