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
    code = data[:, 0].reshape(data.shape[0])
    score = data[:, 1:]
    all_score = np.dot(score, weight)
    avg = np.sum(all_score) // len(all_score)
    ans = code[all_score < avg]
    x = [str(i) for i in ans]
    if x != []:
        return print(", ".join(x))
    else:
        return print('None')


exec(input().strip())
