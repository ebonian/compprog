import re

word = input()

sentence = input()

ans=0

sentence = re.split(r'\W',sentence)

for words in sentence:
  if word == words:
    ans+=1
    
print(ans)