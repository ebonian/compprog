# take the integer input of height
height = int(input())

space = height

for i in range(height):
	# start the index by 1 not 0
	i += 1

	# space before triangle border
	for j in range(space):
		print(" ", end="")

	# star and space inside triangle
	for k in range(1, i*2):
		# triangle border
		if (k==1 or k == 2 * i - 1 or i == height):
			print("*", end="")
		# space inside
		else:
			print(" ", end="")

	# decrease space before trangle by 1
	space -= 1
	
	# print next line
	print("")