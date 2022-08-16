import numpy as np
def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight, data):
    n=data.shape[0]
    name=data[:,0]
    data_score=np.sum(data[:,1:],axis=0)/n
    mean=np.dot(data_score,weight)/3
    mean_person=np.sum(np.dot(data[:,1:],weight).reshape((n,1)),axis=1)/3
    if len(name[mean_person<mean])== 0:
        print('None')
    else: print(', '.join([str(e) for e in name[mean_person<mean]]))
exec(input().strip())