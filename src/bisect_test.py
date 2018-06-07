numbers = [1,2,20,3,4,5,10]

print(sorted(numbers))
print(numbers)

print(numbers.sort())
print(numbers)

print(10 in numbers)

import bisect
print(bisect.bisect(numbers, x))

x = 3

found = False
for n in numbers:
	if x == n:
		found = True
		break
print(found)