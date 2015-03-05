def binarizar(decimal,bits):
    binario=''
    assert decimal<2**(bits-1),"Overflow"
    while decimal//2!=0:
        binario=str(decimal%2)+binario
        decimal=decimal//2
    return str(decimal)+binario