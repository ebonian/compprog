k = input()
xxx = [ '(', ')', '-', '_', '[', ']' ,'"' ,"'" ,';', ':', '>', '<','.' ]
for i in range(len(k)):
    if k[i] in xxx :
        k = k[:i]+" "+k[i+1:]
h = k.split()
ans = ''
for i in range(len(h)):
    h[i] = h[i].lower()
    if len(ans) == 0 :
        ans += h[i][0]
    else :
        ans += h[i][0].upper()
    for j in range(1,len(h[i])) :
        ans += h[i][j]
print(ans)