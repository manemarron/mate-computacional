def decimalBinario(num,bits):
    assert(num>=1*(-2**(bits-1)) and num<=1*(2**(bits-1))-1)
    bin=""
    i=0
    for i in xrange(bits,0,-1):
        bin+=str(num%2)
        num/=2
    return bin[::-1]

def binarioDecimal(num,bits):
    i=0
    dec=0
    for i in xrange(bits,0,-1):
        aux=int(num[i-1])*(2**(bits-i))
        dec+=aux
    return dec

diccionarioBH={"0000":"0","0001":"1","0010":"2","0011":"3","0100":"4","0101":"5","0110":"6","0111":"7","1000":"8","1001":"9","1010":"A","1011":"B","1100":"C","1101":"D","1110":"E","1111":"F"}
diccionarioHB={"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}

def binarioHexadecimal(num):
    hex=""
    cacho=num
    for i in xrange(0,len(num)/4,1):
        cacho=cacho[len(cacho)-4:len(cacho)]
        hex+=diccionarioBH[cacho]
        cacho=num[0:len(num)-4*(i+1)]
    return hex[::-1]

def hexadecimalBinario(num):
    bin=""
    char=""
    for i in xrange(0,len(num),1):
        char=num[i]
        bin+=diccionarioHB[char]
    return bin