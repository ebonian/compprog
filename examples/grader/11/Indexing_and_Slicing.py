import numpy as np
def get_column_from_bottom_to_top( A, c ):
    return A[:,c][::-1]
def get_odd_rows( A ):
    return A[1::2]
def get_even_column_last_row( A ):
    return A[-1,::2]
def get_diagonal1( A ): # A is a square matrix
    n=A.shape[0]
    r=np.arange(n)
    return A[r,r]
def get_diagonal2( A ): # A is a square matrix
    n=A.shape[0]
    r=np.arange(n)
    return A[r,r[::-1]]
exec(input().strip())