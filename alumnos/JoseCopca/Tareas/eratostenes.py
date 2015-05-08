%matplotlib inline
import numpy as np
import matplotlib as plt
def criba_eratostenes(maximo):
    bool_arr=np.ones((maximo,), dtype=bool)
    bool_arr[0:2]=0
    N_max = int(np.sqrt(len(bool_arr)))
    for j in xrange(2, N_max+1):
        bool_arr[2*j::j] = False
    return np.nonzero(bool_arr)