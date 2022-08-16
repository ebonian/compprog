def gcd(a,b):
    while b!=0:
        a , b = b , a%b
    return a

def is_coprime(a, b, c):
    return gcd(gcd(a,b),c)==1

def primitive_Pythagorean_triples(max_len):
    triple=[]
    for i in range (5,max_len+1):
        temp=[]
        for j in range(1,i+1):
            for k in range(1,j+1):
                if is_coprime(k,j,i) and (k**2+j**2)==i**2:
                    temp.append([k,j,i])
        temp.sort()
        triple+=temp
    return triple

exec(input().strip())
