def Decimal_a_Binario(n):
    lista=[0, 0, 0, 0, 0, 0, 0, 0]
    i=7
    l=0
    while(i>=0):
        if n>=(2**(i)):
            n=n-(2**(i))
            i=i-1
            lista[l]=1
            l=l+1
        else:
            lista[l]=0
            l=l+1
            i=i-1
    print lista