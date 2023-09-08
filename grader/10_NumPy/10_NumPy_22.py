import numpy as np


def mult_table(nrows, ncols):
    a = np.arange(nrows).reshape(nrows, 1) + 1
    b = np.arange(ncols).reshape(1, ncols) + 1
    return a*b


exec(input().strip())
