#funcion para obtener un número x (inicialmente en base 2) en base hexadecimal
#se definen la siguiente tabla de conversion entre valores binarios y el 
#correspondiente hexadecimal:
numBin = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
baseHex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
i=0
def hexadecimal(x):
    numhex=str()
    x = str(x)
#se verifica el tamaño del numero binario sino es un multiplo de 4 (porque
#2^4 es 16), sino completar con ceros a la izquierda del número
    if len(x)%4 != 0:
        faltan = 4 - len(x)%4
        while faltan != 0:
            x = str('0') + x
            faltan -=1
#se particiona el número binario en pedazos de 4 y posterior se compara con
#las equivalencias declaradas inicialmente
    for i in xrange(len(x), 0, -4):
        numbin = x[i-4:i]
        for j in xrange(0, len(numBin), 1):
            if numbin == str(numBin[j]):
                numhex = str(baseHex[j]) + numhex
    print "El número x en base hexadecimal es:", numhex
