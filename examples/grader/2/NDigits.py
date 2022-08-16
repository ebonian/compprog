num=input()
count=int(input())
for c in range(len(num),count):
    num="0"+num
    c+=1
print(num)