def DecimalABinario(decimal):
    assert -128<=decimal<=127
    b=[0 for x in range(8)]   
    i=0
    while decimal!=0 and i<=7:
        b[7-i]=decimal%2
        i+=1
        decimal=decimal/2
    binario=''
    for i in xrange(0,len(b),1):
        binario=binario+str(b[i])
    print binario
    return binario