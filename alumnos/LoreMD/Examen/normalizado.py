from math import log,floor
def normalizado(num):
    exponente=0
    f=""
    mantisa=0
    
    if num>=0:
        signo="0"
    else:
        signo="1"
    
    num=abs(num)
    exponente=int(log(num)/log(2))
    mantisa=num/(2**exponente)
    
    x=mantisa
    for i in xrange(1,manBits,1):
        if x>=1:
            x=str(x)
            x=x[1:len(x)]
            print x
            x=float(x)
        x*=2
        f+=str(x)[0]
        
    exponente=exponente-bias
    return signo+str(decimalBinario(exponente,expBits))+ f