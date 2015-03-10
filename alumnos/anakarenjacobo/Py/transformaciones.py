from math import sin,acos 
def coor_esfericas(x,y,z):
    """
    devuelve las coordenadas apartir de las coordenas cartesianas
    """
    r=sqrt(x^2+y^2+z^2)
    theta =acos(z/r)
    phi= acos(x/(rsen(theta)))
    return r, theta,phi