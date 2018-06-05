
# input
numbers = [1, 2, 3, 4, 5]


accumulator = 0
for n in numbers:
	accumulator += n

print(accumulator)

accumulator = 0
length = len(numbers)
i = 0
while i < length:
	n = numbers[i]
	accumulator += n
	i += 1
print(accumulator)


accumulator = 0
for n in numbers:
	accumulator += n
mean = accumulator / len(numbers)

print(mean)

accumulator = 0
length = 0
for n in numbers:
	accumulator += n
	length += 1
mean = accumulator / length

print(mean)

x = 3

in_list = False
for n in numbers:
	if n == x:
		in_list = True
		break

print(in_list)

x = 14

in_list = False
for n in numbers:
	if n == x:
		in_list = True
		break

print(in_list)
