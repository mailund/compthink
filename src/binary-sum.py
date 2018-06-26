
def binary_sum(x):
	if len(x) == 0: return 0
	if len(x) == 1: return x[0]

	# O(n) work
	y = []
	for i in range(1, len(x), 2):
		y.append(x[i - 1] + x[i])
	if i + 1 < len(x): # handle odd lengths
		y[0] += x[i + 1]
	
	return binary_sum(y) # recurse on n//2 size


print("0:", end = " ") ; val = binary_sum([]) ; print(val)
print("1:", end = " ") ; val = binary_sum([2]) ; print(val)
print("2:", end = " ") ; val = binary_sum([2,3]) ; print(val)
print("3:", end = " ") ; val = binary_sum([2,3,1]) ; print(val)
print("4:", end = " ") ; val = binary_sum([1,2,3,4]) ; print(val)
print("5:", end = " ") ; val = binary_sum([1,2,3,4,5]) ; print(val)
