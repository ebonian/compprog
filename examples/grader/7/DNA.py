m='ATCGatcg'
n='TAGC'

def reverse(dna):
    new=''
    for i in dna:
        if i in m:
            new+=n[m.index(i)%4]
        else:
            print("Invalid DNA")
            return
    new=new[::-1]
    print(new)

def freq(dna):
    c=[0]*4
    for i in dna:
        if i in m:
            c[m.index(i)%4]+=1
        else:
            print("Invalid DNA")
            return
    print("A="+str(c[0])+", "+"T="+str(c[1])+", "+"G="+str(c[3])+", "+"C="+str(c[2]))

def duo(dna):
    st=''
    for i in dna:
        if i in 'atcg':
            st+=m[m.index(i)-4]
        elif i in 'ATCG':
            st+=i
        else:
            print("Invalid DNA")
            return
    chk=input().strip()
    c=0
    for i in range (len(dna)-1):
        if chk==st[i:i+2]:
            c+=1
    print(c)

def main(x,dna):
    if x=='R':
        reverse(dna)
    elif x=='F':
        freq(dna)
    elif x=='D':
        duo(dna)
    else:
        print("Invalid Syntax")

dna=input().strip()
key=input().strip()
main(key,dna)