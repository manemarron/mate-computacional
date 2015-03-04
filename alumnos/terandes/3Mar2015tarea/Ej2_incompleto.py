#LE PONGO MAXIMO COMO ARGUMENTO Y ME MANDA ERROR DE QUE bool_arr1 NO ESTA DEFINIDO
def criba(maximo):
   # import numpy as np
    bool_arr1 = np.ones((maximo,), dtype=bool)
    bool_arr1[0:2]=False
    N_max = int(np.sqrt(len(bool_arr1)))    #aqui se obtiene la cota superior de los números
#dentro de los cuales se va a buscar los números que tiene algun multiplo, tomando como
#la raiz cuadrada del tamaño del arreglo.
    for j in range(2, N_max):
        bool_arr1[2*j::j] = False
#como ya sabemos que 2 y 3 son primos, entonces se parte desde 4, y los multiplos de 2, 
#con 2*j::j, para el siguiente valor j=3, se buscan los multiplos de 3 y así 
#sucesivamente hasta 9. Va buscando cada j entradas los indices correspondientes que
#son múltiplos de j, va recorriendo el indice inicial de busqueda conforme 
#al primer valor de 2*j
np.nonzero(bool_arr1)
