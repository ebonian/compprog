height = int(input())

space = height

for i in range(1,height+1):
    # space before triangle border
    for j in range(1, space):
        print(" ", end="")

    for k in range(1, i*2):
        # triangle border
        if k==1 or k == 2 * i - 1 or i == height :
            print("*", end="")
        # space inside
        else:
            print(" ", end="")

    space-=1
    
    print()