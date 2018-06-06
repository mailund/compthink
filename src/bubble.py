
numbers = [1, 3, 2, 4, 5, 2, 3, 4, 1, 2, 3]


for i in range(1,len(numbers)):
	x = numbers[i]
	j = i - 1
	while x < numbers[j]:
		numbers[i], numbers[j] = numbers[j], x
		i -= 1 ; j -= 1		

print(numbers)