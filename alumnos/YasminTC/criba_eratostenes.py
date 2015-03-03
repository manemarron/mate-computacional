def criba_eratostenes(maximo):
    bool_arr = np.ones((maximo,), dtype=bool)
    bool_arr[0]=False
    bool_arr[1]=False
    N_max = int(np.sqrt(len(bool_arr)))
    for j in range(2, N_max):
        bool_arr[2*j::j] = False
    return np.nonzero(bool_arr)