# take the input of mobile number
n = input()

# check mobile number for each condition if first 2 number are in the considered list
if (n[0:2] in ["06", "08", "09"]):
  print("Mobile number")
else:
  print("Not a mobile number")