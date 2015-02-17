from math import sqrt,acos,asin
def coordenadasCaEsfericas(x,y,z):
    r=sqrt(x**2+y**2+z**2)
    theta=acos(x/(x**2+y**2))
    phi=asin(z/(x**2+y**2+z**2))
    print r,theta,phi
    return r,theta,phi