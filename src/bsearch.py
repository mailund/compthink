
numbers = [1, 2, 2, 3, 4, 5]

x = 0

low, high = 0, len(numbers)
found = False
while low < high:
	mid = (low + high) // 2
	if numbers[mid] == x:
		found = True
		break
	elif numbers[mid] < x:
		low = mid + 1
	else:
		high = mid

print(found)