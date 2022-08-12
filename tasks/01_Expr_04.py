import math

# define func
def mostellerFormula(w: float, h: float) -> float:
  result = (math.sqrt(w * h)) / (60)
  return result

def haycockFormula(w: float, h: float) -> float:
  result = 0.024265 * w**0.5378 * h**0.3964
  return result

def boydFormula(w: float, h: float) -> float:
  result = 0.0333 * (w**(0.6157 - (0.0188 * math.log10(w)))) * h**0.3
  return result


# take input of w: widht & h: height
w = float(input())
h = float(input())


# print the result
print(mostellerFormula(w, h))
print(haycockFormula(w, h))
print(boydFormula(w, h))