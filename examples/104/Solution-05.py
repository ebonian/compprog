# Prog-05: The 24 Game
# Knight N104

from itertools import permutations, product
import math

def generate_all_combinations(num_list, operators):
    all_combi = []
    for n,o in product(sorted(set(permutations(num_list))),
                       product(operators, repeat=3)): 
        x = [None]*(len(n)+len(o))
        x[::2] = n
        x[1::2] = o
        all_combi.append(x)
    return all_combi
#--------------------------------------------------------- 
import math as m
def cal(num1,op,num2):
        if op=='+':
            r=num1+num2
        elif op=='-':
            r=num1-num2
        elif op=='*':
            r=num1*num2
        elif op=='/':
            if num2 !=0 :
                r=num1/num2
            else:
                r=m.e
        return r


#---------------------------------------------------------
nums = input('Enter 4 integers: ')
nums = [int(m) for m in nums.split()]
check=False
cases = generate_all_combinations( nums,  '+-*/' )
for i in cases:
    if cal(cal(cal(i[0],i[1],i[2]),i[3],i[4]),i[5],i[6])==24:
        check=True
        ans=f'( ( {i[0]} {i[1]} {i[2]} ) {i[3]} {i[4]} ) {i[5]} {i[6]} = 24'
        break
    elif cal(cal(i[0],i[1],cal(i[2],i[3],i[4])),i[5],i[6])==24:
        check=True
        ans=f'( {i[0]} {i[1]} ( {i[2]} {i[3]} {i[4]} )  ) {i[5]} {i[6]} = 24'
        break
    elif cal(cal(i[0],i[1],i[2]),i[3],cal(i[4],i[5],i[6]))==24:
        check=True
        ans=f'( {i[0]} {i[1]} {i[2]} ) {i[3]} ( {i[4]} {i[5]} {i[6]} ) = 24'
        break
    elif cal(i[0],i[1],cal(cal(i[2],i[3],i[4]),i[5],i[6]))==24:
        check=True
        ans=f'{i[0]} {i[1]} ( ( {i[2]} {i[3]} {i[4]} ) {i[5]} {i[6]} ) = 24'
        break
    elif cal(i[0],i[1],cal(i[2],i[3],cal(i[4],i[5],i[6])))==24:
        check=True
        ans=f'{i[0]} {i[1]} ( {i[2]} {i[3]} ( {i[4]} {i[5]} {i[6]} ) ) = 24'
        break
    
if check :
    print(ans)
else :
    print("No Solutions")
