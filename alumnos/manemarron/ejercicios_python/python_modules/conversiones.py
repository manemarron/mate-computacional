def decimalToBinTwosComplement(n,k):
    """
    Funcion que transforma de decimal n a binario de k bits en complemento a 2
    """
    try:
        assert -2**(k-1)<=n<2**(k-1)
        if n<0:
            n+=2**k
        binary=""
        while len(binary)<8:
            binary="%s%s"%(n%2,binary)
            n/=2
        return binary
    except(AssertionError):
        return "Overflow"

def binTwosComplementToDecimal(binary):
    """
    Funcion que transforma un numero binario en complemento a 2 a decimal
    """
    try:
        dec=0
        for i in range(0,len(binary)):
            c = int(binary[i])
            if c!=0 and c!=1: raise Exception("No es binario")
            if i==0:
                c=-c
            dec+=c*2**(len(binary)-i-1)
        return dec
    except Exception as e:
        print e

###### HEXADECIMAL A BINARIO Y VICEVERSA ##############
HEX_BIN = [
    ("0000","0"),
    ("0001","1"),
    ("0010","2"),
    ("0011","3"),
    ("0100","4"),
    ("0101","5"),
    ("0110","6"),
    ("0111","7"),
    ("1000","8"),
    ("1001","9"),
    ("1010","A"),
    ("1011","B"),
    ("1100","C"),
    ("1101","D"),
    ("1110","E"),
    ("1111","F"),
]
def binaryToHex(binary):
    """
    Funcion que convierte de binario a hexadecimal
    """
    digits=len(binary)/4
    if len(binary)%4 != 0: digits += 1
    binary = "0"*(digits*4-len(binary))+binary
    hexa=""
    for i in range(0,digits):
        aux = binary[4*i:4*(i+1)]
        j=0
        for t in HEX_BIN:
            if t[0] == aux:
                hexa += t[1]
                break
    return hexa

def hexToBinary(hexa):
    """
    Funcion que convierte de hexadecimal a binario
    """
    binary=""
    for d in hexa:
        for t in HEX_BIN:
            if t[1] == d:
                binary += t[0]
                break
    return binary