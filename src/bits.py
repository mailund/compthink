
n = 4
reverse_bits = []
while n > 0:
	reverse_bits.append(n % 2)
	n //= 2
print(reverse_bits[::-1])

n = 4

reverse_bits = []
while n > 0:
	reverse_bits.append(n & 1)
	n >>= 1
print(reverse_bits[::-1])
