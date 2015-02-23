
from math import sin, cos
def TransfPolarCart(r,t,f):
    x= r* sin(f)* cos(t)
    y= r* sin(f)*sin(t)
    z= r* cos (f)
    
    return x,y,z
    