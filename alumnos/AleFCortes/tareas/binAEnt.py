def binEn(n):
    entero = 0
    contador =-1
    for i in range(1,len(n)):
        if (n[i-1] == "1"):
            entero = entero + 2**(len(n)-i)
    print entero
    