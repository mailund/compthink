
def get_sub_key(k):
	subkeys = (k         & 0xff
	          ,(k >> 8)  & 0xff
	          ,(k >> 16) & 0xff
	          ,(k >> 24) & 0xff)
	return subkeys

print(get_sub_key(4))
print(get_sub_key(256))

n = 5 ; m = 256 ; d = 4
values = [v * 1024 + 1 for v in range(n)]
keys = [get_sub_key(v) for v in values]
print(values) ; print(keys)

for j in range(d):
	key_buckets = [[] for bucket in range(m)]
	value_buckets = [[] for bucket in range(m)]
	for i in range(n):
		key = keys[i]
		subkey = key[j]
		val = values[i]
		key_buckets[subkey].append(key)
		value_buckets[subkey].append(val)

	key_result, value_result = [], []
	for subkey in range(m):
		for key in key_buckets[subkey]:
			key_result.append(key)
		for val in value_buckets[subkey]:
			value_result.append(val)

	keys = key_result
	values = value_result

print(keys)
print(values)

n = 5 ; d = 2
values = list(range(5))
keys = [(1,0), (2,1), (1,1), (0,1), (1,1)]

#for j in range(d-1,-1,-1):
for j in range(d):
	key_buckets = [[] for bucket in range(m)]
	value_buckets = [[] for bucket in range(m)]
	for i in range(n):
		key = keys[i]
		subkey = key[j]
		val = values[i]
		key_buckets[subkey].append(key)
		value_buckets[subkey].append(val)

	key_result, value_result = [], []
	for subkey in range(m):
		for key in key_buckets[subkey]:
			key_result.append(key)
		for val in value_buckets[subkey]:
			value_result.append(val)

	keys = key_result
	values = value_result
	print(keys)
