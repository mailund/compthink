
x = [1, 3, 2, 4, 5, 2, 3, 4, 1, 2, 3]


for i in range(1,len(x)):
	x = x[i]
	j = i
	while j > 0 and x[j-1] > x[j]:
		x[j-1], x[j] = x[j], x[j-1]
		j -= 1		

print(x)

