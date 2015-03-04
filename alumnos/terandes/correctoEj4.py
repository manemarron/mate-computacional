#funcion para detectar si el vector de entrada tiene los 
#datos correctos 
def correcto(x):
    (a,) = x.shape
    elementos=np.unique(x)
    (b,) = np.shape(elementos)
    if a == b:
        print 'los elementos son los necesarios'
    else:
        print 'hay elementos repetidos y mayores a 9'
