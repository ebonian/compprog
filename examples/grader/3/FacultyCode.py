n=input()
if n=='01' or n=='02' or (n>='20' and n<='40' and len(n)==2) or n=='51' or n=='53' or n=='55' or n=='58':
    print("OK")
else:
    print("Error")