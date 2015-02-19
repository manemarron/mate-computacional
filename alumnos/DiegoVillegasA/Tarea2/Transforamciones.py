
# Función que transforma de cartesianas a esféricas

import math
def esferica(x,y,z):
    
    # Llamemos el vector E=(x,y,z)
    
    ro = math.sqrt(x**2+y**2+z**2) #Magnitud de E
    
    """"Theta es el ángulo formado por la proyección de E al plano x,y. Es decir, es el ángulo formado del eje x al vector 
    (x,y,0). Llamemos "r" a este vector. Se calcula a través de arctang(y/x)"""
    
    magr = math.sqrt(x**2+y**2) #Magnitud de r
    
    theta = math.atan(y/x)
    
    """Notemos que:
        x = rcos(theta)
        y = rsen(theta)
    
    
     Phi es el ángulo del eje z al vector E. Para encontrar phi se considera el vector r. Trasladando r a la altura de 
    la coordenada cartesiana (valor de z del vector E) se puede formar un triángulo rectángulo entre el eje z, r trasladada y E
    (de todas formas lo único que nos interesa son las magnitudes de dichos catetos) Aplicamos arctan(magr/z) para calcular 
    phi"""
    
    phi = math.atan(ro/z)
    
    """
    Notemos que:
        r = sin(phi)
    
    Por lo tanto tenemos que:
    """
    
    x1= ro*math.sin(phi)*math.cos(theta)
    y1= ro*math.sin(phi)*math.sin(theta)
    z1= ro*math.cos(theta)
    
    return (x1,y1,z1)
    