def no_lowercase(t):
    for i in t:
        if  'a' <= i <='z':
            return False
    return True

def no_uppercase(t):
    for i in t:
        if  'A' <= i <='Z':
            return False
    return True

def no_numbers(t):
    for i in t:
        if  '0' <= i <='9':
            return False
    return True

def no_symbols(t):
    for i in t:
        if i in "'" or i in '"' or i in "!@#$%^&*()_+-=:;[}]{\.<>,":
            return False
    return True

def repete(t):
    for i in range (len(t)-3):
        if t[i]==t[i+1]==t[i+2]==t[i+3]:
            return True
    return False

def num_sequence(t):
    num='01234567890987654321'
    for i in range (len(t)-3):
        ch1=t[i:i+4]
        if ch1 in num:
            return True
    return False

def alp_sequence(t):
    alp='abcdefghijklmnopqrstuvwxyz'
    alp+=alp[-2::-1]
    s=t.lower()
    for i in range(len(t)-3):
        if s[i:i+4] in alp:
            return True
    return False

def key_pattern(t):
    key1='!@#$%^&*()_+_)(*&^%$#@!'
    key2='qwertyuiopoiuytrewq'
    key3='asdfghjklkjhgfdsa'
    key4='zxcvbnmnbvcxz'
    s=t.lower()
    for i in range (len(t)-3):
        chk=s[i:i+4]
        if chk in key1 or chk in key2 or chk in key3 or chk in key4:
            return True
    return False

t=input()
ans=[]
if len(t)<8:
    ans.append("Less than 8 characters")
if no_lowercase(t):
    ans.append("No lowercase letters")
if no_uppercase(t):
    ans.append("No uppercase letters")
if no_numbers(t):
    ans.append("No numbers")
if no_symbols(t):
    ans.append("No symbols")
if repete(t):
    ans.append("Character repetition")
if num_sequence(t):
    ans.append("Number sequence")
if alp_sequence(t):
    ans.append("Letter sequence")
if key_pattern(t):
    ans.append("Keyboard pattern")
if ans==[]:
    print("OK")
else:
    for i in ans:
        print(i)
        