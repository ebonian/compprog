import numpy as np


def peak_indexes(x):
    n = np.arange(x.shape[0])
    x1 = np.diff(x)
    x1 = np.concatenate([x1, [0]])
    x2 = np.diff(x) * (-1)
    x2 = np.concatenate([[0], x2])
    ans = n[(x1 < 0) & (x2 < 0)]
    return ans


def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")


exec(input().strip())
