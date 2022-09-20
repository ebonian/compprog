VOWEL = ["a", "e", "i", "o", "u"]

user_word = input()

if (user_word[-1] == "s" or user_word[-1] == "x" or user_word[-2:] == "ch"):
  print(user_word + "es")
elif (user_word[-2:] in VOWEL):
  print("?")
elif (user_word[-1] == "y" and  user_word[-2] not in VOWEL):
  print(user_word[:-1] + "ies")
else:
  print(user_word + "s")