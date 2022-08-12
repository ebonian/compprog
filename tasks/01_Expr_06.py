# take the input of beginning time
h1 = int(input())
m1 = int(input())
s1 = int(input())

# take the input of ending time
h2 = int(input())
m2 = int(input())
s2 = int(input())

# calculate beginning time and ending time in seconds
t1 = h1*60*60 + m1*60 + s1
t2 = h2*60*60 + m2*60 + s2

# calculate time different
dt = t2-t1
dh = dt // (60*60)
dt -= dh * 60*60
dm = dt//60
dt -= dm*60
ds = dt

# check if second time is more than first time, if not minus hour different with 24 hrs
if t2 > t1:
  print(str(dh)+":"+str(dm)+":"+str(ds))
else:
  dh = 24 - abs(dh)
  print(str(dh)+":"+str(dm)+":"+str(ds))

# print(dh)
# print(dm)
# print(ds)