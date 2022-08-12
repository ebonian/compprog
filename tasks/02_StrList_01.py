# n = 123456789012
n = int(input())

def calculateRightmostDigit(n: str)->int:
  nList = [int(x) for x in str(n)]
  result = (11-(13*nList[0] + 12*nList[1] + 11*nList[2] + 10*nList[3] + 9*nList[4] + 8*nList[5] + 7*nList[6] + 6*nList[7]+ 5*nList[8] + 4*nList[9] + 3*nList[10] + 2*nList[11]) % 11) % 10
  return result

def listToString(list: list)->str:
  return ''.join([str(x) for x in str(list)])

print(n//10**11, n//10**7 % 10000, n//10**2 % 100000, n%100, calculateRightmostDigit(n))
