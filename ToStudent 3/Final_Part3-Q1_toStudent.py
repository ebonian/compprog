import numpy as np

# Part 2 Q1 (DO NOT DELETE this line or add line before this) 
def f1(a):
    # !!! YOUR CODE HERE !!!  







    
def test(expected, actual):
    print('Expected:\n', expected)
    print('Your result:\n', actual)

#you can write your own tests too.
  
#test a1 3x3
a1 = np.array([1,2,3,4,5,6,7,8,9])
a1 = a1.reshape(3,3)
a1[1,0] = 77
a1[1,2] = 13
test([[64]],f1(a1))

#test a2 6x6
a2 = np.arange(1,37,1)
a2 = a2.reshape(6,6)
a2[2,0] = 32
a2[2,1] = 22
a2[3,0] = 56
a2[3,1] = 11
a2[3,4] = 66
a2Expected = np.array([[15,4],[-10,-13]])
test(a2Expected,f1(a2))

#test a3 3x9
a3 = np.arange(1,28)
a3 = a3.reshape(3,9)
a3[1,0] = 10
a3[1,1] = 21
a3[1,2] = 43
a3[1,6] = 16
a3[1,7] = 17
a3[1,8] = 33
a3Expected  = np.array([[-6,4,10]])
test(a3Expected,f1(a3))

#test a4 6x3
a4 = np.arange(1,19)
a4 = a4.reshape(6,3)
a4[2,0] = 1
a4[2,2] = 10
a4[3,0] = 66
a4[3,2] = 22
a4Expected = np.array([[-9],[44]])
test(a4Expected,f1(a4))

#test a5 6x12
a5 = np.arange(1,73)
a5 = a5.reshape(6,12)

a5[2,0] = 23
a5[2,1] = 80
a5[2,2] = 3
a5[2,3] = 22
a5[3,0] = 91
a5[3,1] = 37
a5[3,2] = 66
a5[3,3] = 88
a5Expected = np.array([[-10,46,-32,-14],[46,-9,19,40]])
test(a5Expected,f1(a5))

#test a6 9x6
a6 = np.arange(1,55)
a6 = a6.reshape(9,6)

a6[3,0] = 11
a6[3,1] = 22
a6[4,0] = 33
a6[4,1] = 38
a6[5,0] = 21
a6[5,1] = 45
a6Expected = np.array([[-12,-2],[4,8],[-14,9]])
test(a6Expected,f1(a6))
