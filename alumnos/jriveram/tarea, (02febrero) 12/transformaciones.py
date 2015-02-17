from math import sqrt, sin, cos, acos, atan2
def convierte_esfericas_a_cartesianas(r, theta, phi):
    """
    función que devuelve las coordenadas (x, y, z), a partir de coordenadas esféricas (r, theta, phi)
    """
    x = r*sin(theta)*cos(phi)
    y = r*sin(theta)*sin(phi)
    z = r*cos(theta)
    return x, y, z

def convierte_cartesianas_a_esfericas(x, y, z):
    """
    función que devuelve las coordenadas esférias (r, theta, phi), a partir de coordenadas rectangulares (x, y, z)
    """
    r = sqrt(x**2 + y**2 + z**2)
    theta = acos(z / r)
    phi = atan2(y,  x)
    return (r, theta, phi)
