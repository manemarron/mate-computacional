def decimalBin(x):
    assert -128<=x<=127
    listaBin=[0 for x in range(8)]
    i=0
    while x!=0 and i<=7:
        listaBin[7-i]=x%2
        i+=1
        x=x/2
    binario=''
    for i in xrange(0,len(b),1):
        binario=binario+str(listaBin[i])
    print binario
    return binario