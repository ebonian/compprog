import numpy as np
def sum_2_rows( M ):
    return M[::2]+M[1::2]
def sum_left_right( M ):
    n=M.shape[1]
    return M[:,:n//2]+M[:,n//2:]
def sum_upper_lower( M ):
    n=M.shape[0]
    return M[:n//2]+M[n//2:]
def sum_4_quadrants( M ):
    r=M.shape[0]
    c=M.shape[1]
    q1=M[:r//2,:c//2]
    q2=M[:r//2,c//2:]
    q3=M[r//2:,:c//2]
    q4=M[r//2:,c//2:]
    return q1+q2+q3+q4
def sum_4_cells( M ):
    return M[0::2,0::2]+M[1::2,0::2]+M[0::2,1::2]+M[1::2,1::2]
def count_leap_years( years ):
    return len(years[((years-543)%400==0 )| (((years-543)%4==0 )&( (years-543)%100!=0))])
exec(input().strip())