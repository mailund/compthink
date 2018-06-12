
x = [1,3,2,4,6,5]


m = 7

buckets = [0] * m
for key in x:
	buckets[key] += 1
result = []
for key in range(len(buckets)):
	for i in range(buckets[key]):
		result.append(key)

print(result)

buckets = [0] * m
for key in x:
	buckets[key] += 1
i = 0
for key in range(len(buckets)):
	for j in range(buckets[key]):
		x[i] = key
		i += 1

print(x)
