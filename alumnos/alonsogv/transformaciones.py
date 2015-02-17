from math import sqrt, acos, atan
def esferica(x,y,z):
    r = sqrt(x**2 + y**2 + z**2)
    theta = acos(z/r)
    phi = atan(sqrt(x**2 + y**2)/z)
    return r, theta, phi