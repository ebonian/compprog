def reverse(d):
    new={}
    for i in d:
        new[d[i]]=i
    return new

def keys(d,v):
    ans=[]
    for i in d:
        if d[i]==v:
            ans.append(i)
    return ans

exec(input().strip())