code = int(input())

# convert to list of int
code = [int(x) for x in str(code)]

def intToList(n: int) -> list[int]:
  result  = [int(x) for x in str(n)]
  return result

def listToInt(list: list[int]) -> str:
  s = [str(i) for i in list]

  result = ""

  for value in s:
    result += value

  if result:
    result = int(result)

  return result

def pickNumber(startIdx: int, skipIdx: int) -> int:
  result = []

  start = startIdx

  for val in code:
    if len(code) - start <= 0:
      break
    if val == code[start]:
      result.append(val)
      start += skipIdx

  result = listToInt(result)

  return result

def pickThousandsHundredsTens(num: int) -> int:
  thousands = (num % 10000) // 1000
  hundreds = (num % 1000) // 100
  tens = (num % 100) // 10

  result = int(str(thousands) + str(hundreds) + str(tens))

  return result

def combineDigits(n: int) -> int:
  result = intToList(n)

  digitSum = 0

  for val in result:
    digitSum += val

  return digitSum

def convertNumToAlphabets(idx: int) -> str:
  alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
  return alphabets[idx - 1]

a = pickNumber(3, 7)
b = pickNumber(7, 5)
if (a and b):
  # combine numbers from a and b then add it with 10000
  c = a + b + 10000
  # pick the thousands, hundreds and tens digit from the result of c
  d = pickThousandsHundredsTens(c)
  # combine the digits from d
  e = combineDigits(d)
  # pick the units digit and add it with 1
  e = (e % 10) + 1
  f = convertNumToAlphabets(e)
  g = str(d) + f
  
  print(hex(12341234))
else:
  print("000A")
