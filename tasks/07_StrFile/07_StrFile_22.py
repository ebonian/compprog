string1 = input().lower().replace(" ", "")
string2 = input().lower().replace(" ", "")

if (sorted(string1) == sorted(string2)): print("YES")
else: print("NO")