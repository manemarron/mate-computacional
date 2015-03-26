def criba_eratostenes(x):
    bool_arr = np.ones((x,),dtype=bool)
    bool_arr[:2] = 0
    N_max = int(np.sqrt(len(bool_arr)))
    for j in range(2, N_max):
        bool_arr[2*j::j] = False
    return np.nonzero(bool_arr)    