import numpy as np


def toCelsius(f):
    return np.array([((x - 32) * 5) / 9 for x in f])


def BMI(wh):
    return np.array([x[0] / (x[1] * 10 ** -2) ** 2 for x in wh])


def distanceTo(p, Points):
    return np.array([((x[0] - p[0]) ** 2 + (x[1] - p[1]) ** 2) ** (1 / 2) for x in Points])


exec(input().strip())
