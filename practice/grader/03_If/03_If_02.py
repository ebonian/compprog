# take the input of score
score = float(input())

# check score for each condition and print the result
if (score >= 80):
  print("A")
elif (score >= 70):
  print("B")
elif (score >= 60):
  print("C")
elif (score >= 50):
  print("D")
else:
  print("F")