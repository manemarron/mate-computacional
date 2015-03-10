#Ej 9 examen, SERIE DE MACLAURIN, falla al intentar aproximar el valor de la exp(x=1), da como resultado 1.
#lo que cambie al codigo es volvi al valor de x flotante, porque al encontrar en la serie correspondiente a x=1, racionales
#creo que por default redondea hacia el cero y por eso estaba fallando, en los otros dos casos porque se introducen ya de entrada
#numeros que no son enteros entonces no sucede lo que pasa con x=1
def exp_maclaurin(x,n):
    x=float(x)
    aprox = 1
    print "%12s\t%12s\t%12s\t%12s\t%20s\t%20s" % ("i", "x", "x^i", "factorial(i)", "x^i/factorial(i)", "suma")
    for i in range (1,n+1,1):
        #x^i=x**i
        factor=factorial(i)
        aprox = aprox + x**i/factorial(i)
        print "%12s\t%12s\t%12s\t%12s\t%20s\t%20s" %  (i, x, x**i, factorial(i), x**i/factorial(i), aprox)
