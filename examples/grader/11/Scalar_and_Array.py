import numpy as np
def toCelsius( f ):
    return (f-32)*(5/9)
def BMI( wh ):
    return wh[:,0]/(wh[:,1]/100)**2
def distanceTo( p, Points ):
    temp=Points-p
    return (temp[:,0]**2+temp[:,1]**2)**0.5
exec(input().strip())