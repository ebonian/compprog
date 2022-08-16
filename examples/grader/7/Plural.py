vowels=['a','e','i','o','u']
text=input()
ch1=text[-1]
ch2=text[-2:]
if ch1 == 's' or ch1 == 'x' or ch2 == 'ch':
    text+='es'
elif ch1=='y' and text[-2] not in vowels:
    text=text[:-1]+'ies'
else:
    text+='s'
print(text)