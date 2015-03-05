#funcion para determinar si una matriz es un cuadrado magico
def esmagico (x):
    if (a,) == x.shape:
        print 'El arreglo tiene solo una dimension '
    else:
        (m,n) = x.shape
        if m != n :
    #assert m != n , 'x no es una matriz cuadrada'
            print 'la matriz no es cuadrada'
        magico = np.unique(x)
        (n1,) = magico.shape
        if n1 != m*n:
    #assert m1 == m*n, 'x no puede ser un cuadrado mágico'
            print 'x no puede ser un cuadrado mágico, hay elementos repetidos'
        diagonal=np.diag(x)
        sumdiag = diagonal.sum()
        sumaFila = x.sum(1)
        sumaColumna = x.sum(0)
    
        fila = np.unique(sumaFila)
        columna = np.unique(sumaColumna)
        comparacion=np.all(fila==sumdiag)
        comparacion1=np.all(columna==sumdiag)
        if comparacion == True and comparacion1 == True :
            print 'la matriz es un cuadrado mágico'
        else:
            print 'la matriz no es un cuadrado mágico'
        