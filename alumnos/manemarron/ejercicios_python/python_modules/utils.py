import numpy as np

def read_data(path,m=2,dtype=float,header=True):
    """
    Method to read a set of data from a file
    
    Parameters:
    path: path to the file from which data will be read
    columns: number of columns in the file (defaults to 2)
    dtype: data type of resulting array (defaults to float)
    header: boolean value that specifies if the file contains a header (defaults to true)
    
    Return:
    Array of n rows and m columns with the data read from file
    """
    result = []
    n=0
    for row in open(path):
        if header:
            header = not header
            continue
        row=row.split()
        result.append(row)
        n+=1
    return np.array(result,dtype=dtype).reshape([n,m])
    
def sort_string(s):
    s = sorted(s)
    print ''.join(s)