#funcion para cambiar enteros de base binaria a decimales para lo cual es 
#importante saber la posicion de los 1's o ceros para saber por cual 2^k 
#multiplicar
def base10(x):
    i = 0
    ndec = 0
    dec= str(x)
    for k in range(len(dec), 0, -1):
        idec = int(dec[k-1])
        ndec = ndec + idec*(2**i)
        i += 1
    print "El número binario x en decimal es:", ndec
