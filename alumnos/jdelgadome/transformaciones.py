import math
def c_esfericas(x,y,z):
    """
    cambio de coordenadas cartesianas a esfericas
    """
    p = math.sqrt(x*x+y*y+z*z)
    theta = math.acos(z/p)
    phi = math.asin(y/(p*math.sin(theta)))
    
    return p, theta, phi