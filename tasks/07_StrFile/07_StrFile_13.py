import re

string = input()

string = [word.lower() for word in re.sub(r"[^a-zA-Z0-9]"," ",string).split(" ") if word]

for i in range(1, len(string)):
  string[i] = string[i][0].upper() + string[i][1:]

string = ''.join(string)


print(string)