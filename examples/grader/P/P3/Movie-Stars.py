n=int(input())
star={}
for i in range (n):
    movie,name1,name2=input().split(', ')
    movie=movie.strip()
    name1=name1.strip()
    name2=name2.strip()
    if name1 not in star:
        star[name1]=[movie]
    else:
        star[name1].append(movie)
    if name2 not in star:
        star[name2]=[movie]
    else:
        star[name2].append(movie)
find=input().split(',')
for e in find:
    e=e.strip()
    if e in star:
        print(e,'->',', '.join(star[e]))
    else:
        print(e,'-> Not found')