def criba(n):
    vectormatriz = np.ones((n,), dtype=bool)
    vectormatriz[0] = 0
    vectormatriz[1] = 0
    N_max = int(np.sqrt(len(vectormatriz)))
    for k in range(2, N_max):
        vectormatriz[2*k::k] = False  
        
    return np.nonzero(vectormatriz)

maximo=[10,100,200]
for i in xrange(0,len(maximo)):
    print criba(maximo[i])