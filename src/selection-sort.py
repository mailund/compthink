
x = [1, 3, 2, 4, 5, 2, 3, 4, 1, 2, 3]



for i in range(len(x)):
	# find index of smallest elm in x[i:]
	min_idx, min_val = i, x[i]
	for j in range(i, len(x)):
		if x[j] < min_val:
			min_idx, min_val = j, x[j]
			
	# swap x[i] and x[j] puts
	# x[j] at the right position
	x[i], x[min_idx] = min_val, x[i]

	print(x[:i+1], x[i+1:])

print(x)

