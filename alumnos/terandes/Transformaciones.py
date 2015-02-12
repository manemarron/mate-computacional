from math import sin, cos
def cartesiana(r,theta,phi):
    """
    r, theta, phi son las coordenadas esfericas
    """
    x = r*sin(phi)*cos(theta)
    y = r*sin(phi)*sin(theta)
    z = r*cos(theta)
    print "La coordenada x es: ", x
    print "La coordenada y es: ", y
    print "La coordenada z es: ", z
