# n = "110070234512"
n = input()


def calculateRightmostDigit(n: str)->str:
  nList = [int(x) for x in str(n)]
  result = (11-(13*nList[0] + 12*nList[1] + 11*nList[2] + 10*nList[3] + 9*nList[4] + 8*nList[5] + 7*nList[6] + 6*nList[7]+ 5*nList[8] + 4*nList[9] + 3*nList[10] + 2*nList[11]) % 11) % 10
  return result

print(n[0], n[1:5], n[5:10], n[10:12], calculateRightmostDigit(n))

