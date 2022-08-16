import numpy as np
def mult_table(nrows, ncols):
    a=np.arange(1,ncols+1)
    b=np.arange(1,nrows+1).reshape((nrows,1))
    return a*b
exec(input().strip())