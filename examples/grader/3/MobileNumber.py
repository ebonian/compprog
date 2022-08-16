n=input()
m=n[:2]
if len(n)==10 and (m=='06' or m=='08' or m=='09'):
    print("Mobile number")
else:
    print("Not a mobile number")