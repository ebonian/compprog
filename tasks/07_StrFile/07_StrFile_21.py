rot13 = str.maketrans('ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz', 'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')

while (True):
  sentences = input()
  if (sentences != "end"):
    print(sentences.translate(rot13))
  else: break