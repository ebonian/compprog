n=int(input())
if n<=100:
    print("18")
elif n>100 and n<=250:
    print("22")
elif n>250 and n<=500:
    print("28")
elif n>500 and n<=1000:
    print("38")
elif n>1000 and n<=2000:
    print("58")
else:
    print("Reject")