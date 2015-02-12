def coordenadasCartesianas(x,y,z):
    """ cambia de coordenadas cartesianas a esfericas """
    from math import arcsin, arccos, sin
    r=sqrt(x**2 + y**2 + z**2)
    t=arccos(z/r)
    f=(y/(r*sin(t)))
    
    print r,t,f
    return r,t,f