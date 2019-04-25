
x = [1, 3, 2, 4, 5, 2, 3, 4, 1, 2, 3]


while True:
	swapped = False
	for i in range(1,len(x)):
		if x[i-1] > x[i]:
			x[i-1], x[i] = x[i], x[i-1]
			swapped = True

	if not swapped:
		break

print(x)

