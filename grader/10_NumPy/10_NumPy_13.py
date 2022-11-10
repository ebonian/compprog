import numpy as np
import math


def p(x):
    return np.array([1 / (1 + math.e ** -(-3.98 + (0.1 * x[0]) + (0.5 * x[1]))) for x in x])


exec(input().strip())
