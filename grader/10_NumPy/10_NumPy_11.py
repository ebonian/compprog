import numpy as np

# A is a 2-d array


def get_column_from_bottom_to_top(A, c):
    return np.flipud(A)[:, c]


def get_odd_rows(A):
    return A[1::2]


def get_even_column_last_row(A):
    return A[-1, ::2]


def get_diagonal1(A):
    return A.diagonal()
    # A is a square matrix
    # from top-left corner down to bottom-right corner


def get_diagonal2(A):
    # A is a square matrix
    # from top-right corner down to bottom-left corner
    return np.fliplr(A).diagonal()


exec(input().strip())  # must have this line when submitting to grader
