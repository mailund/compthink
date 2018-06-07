
numbers = [1, 3, 2, 4, 5, 2, 3, 4, 1, 2, 3]


for i in range(1,len(numbers)):
	x = numbers[i]
	j = i
	while j > 0 and numbers[j-1] > numbers[j]:
		numbers[j-1], numbers[j] = numbers[j], numbers[j-1]
		j -= 1		

print(numbers)

