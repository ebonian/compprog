word = input()
sentence = input()

sentence = sentence.replace('"', "").replace('(', "").replace(')', "").replace(',', "").replace('.', "").replace("'", "")

sentence = sentence.split(" ")

count = 0

for w in sentence:
  if (word == w):
    count += 1

print(count)