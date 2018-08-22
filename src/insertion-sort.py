
x = [1, 3, 2, 4, 5, 2, 3, 4, 1, 2, 3]
print(x)


for i in range(1,len(x)):
	j = i
	while j > 0 and x[j-1] > x[j]:
		x[j-1], x[j] = x[j], x[j-1]
		j -= 1		

print(x)


fruits = ["apple", "orange", "bananba", "kiwi"]
key_fun = len

# Selection sort
x = list(fruits)
print(x)

infinity = float("inf")
for i in range(len(x)):
	min_idx, min_val, min_key = 0, None, infinity
	for j in range(i, len(x)):
		if key_fun(x[j]) < min_key:
			min_idx, min_val, min_key = j, x[j], key_fun(x[j])		
	x[i], x[min_idx] = min_val, x[i]
print(x)
print(fruits)

# Insertion sort
x = list(fruits)
for i in range(1,len(x)):
	j = i
	while j > 0 and key_fun(x[j-1]) > key_fun(x[j]):
		x[j-1], x[j] = x[j], x[j-1]
		j -= 1	
print(x)

# Bucket sort
n = len(x)
m = max(key_fun(e) for e in x) + 1
buckets = [[] for bucket in range(m)]

y = []
for e in x:
	buckets[key_fun(e)].append(e)
for b in buckets:
	for e in b:
		y.append(e)
x = y
print(x)

