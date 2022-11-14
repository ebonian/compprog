import numpy as np


def sum_2_rows(M):
    result = []
    for i in range(M.shape[0] // 2):
        result.append(M[i*2:i*2+2].sum(axis=0))
    return np.array(result)


def sum_left_right(M):
    left, right = np.split(M, 2, axis=1)
    return np.add(left, right)


def sum_upper_lower(M):
    left, right = np.split(M, 2, axis=0)
    return np.add(left, right)


def sum_4_quadrants(M):
    n = M.shape[1]//2
    return M[0:n, 0:n] + M[0:n, n:] + M[n:, 0:n] + M[n:, n:]


def sum_4_cells(M):
    result = []
    for i in range(M.shape[0] // 2):
        row = []
        for j in range(M[i*2:i*2+2].shape[1] // 2):
            row.append(M[i*2:i*2+2][:, j*2:j*2+2].sum())
        result.append(row)
    return np.array(result)


def count_leap_years(years):
    return len([year for year in [year - 543 for year in years] if year % 4 == 0 and year % 100 != 0 or year % 400 == 0])


print(count_leap_years(
    np.array([2143, 2543, 2544, 2643, 2562, 2559, 2560, 2561, 2547, 2562, 2563])))
