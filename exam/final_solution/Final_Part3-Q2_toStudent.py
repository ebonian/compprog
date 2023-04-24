# Part 3 Q2 (DO NOT DELETE this line or add line before this)
import numpy as np


def f2(a):
    # !!! YOUR CODE HERE !!!
    a = a[::2, 1::2]
    a = np.reshape(a, (1, a.size))
    return a


def test(expected, actual):
    print('Expected:\n', expected)
    print('Your result:\n', actual)

# you can write your own tests too.


# test a1 5x3
a1 = np.array([["e", "f", "g"], ["a", "b", "c"], [
    "h", "i", "j"], ["q", "r", "s"], ["w", "x", "y"]])
a1Expected = np.array([['f', 'i', 'x']])
test(a1Expected, f2(a1))

# test a2 7x5
a2 = np.array([["m", "l", "n", "o", "t"], ["e", "r", "h", "u", "n"], ["t", "i", "r", "d", "o"], [
    "m", "e", "a", "l", "o"], ["n", "a", "w", "s", "y"], ["f", "r", "o", "m", "b"], ["e", "p", "n", "y", "s"]])
a2Expected = np.array([['l', 'o', 'i', 'd', 'a', 's', 'p', 'y']])
test(a2Expected, f2(a2))

# test a3 6x8
a3 = np.array([["1", "l", "d", "u", "6", "m", "s", "i"], ["8", "h", "n", "u", "n", "u", "n", "b"], ["t", "s", "2", "1", "o", "s", "4", "t"], [
    "m", "e", "a", "k", "o", "f", "o", "v"], ["n", "w", "w", "i", "3", "f", "y", "u"], ["f", "r", "5", "m", "b", "m", "b", "m"]])
a3Expected = np.array(
    [['l', 'u', 'm', 'i', 's', '1', 's', 't', 'w', 'i', 'f', 'u']])
test(a3Expected, f2(a3))
