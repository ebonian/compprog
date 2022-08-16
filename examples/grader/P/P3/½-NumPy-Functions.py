import numpy as np
def eq(A, B, p):
    size=1
    for e in A.shape:   size*=e
    return np.sum(A==B)/size*100>=p

def closest_point_indexes(points, p):
    rows=points.shape[0]
    idx=np.arange(rows).reshape((rows,1))
    diff=np.sum(points**2+p**2,axis=1)
    min_values=np.min(diff)
    return idx[diff==min_values].flatten()

def number_of_inversions(A):
    diff=A-A.reshape((len(A),1))
    for i in range(len(A)):
        diff[i,i:]=0
    return np.sum(diff>0)

exec(input().strip())