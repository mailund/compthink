
def merge(x, y, i = 0, j = 0, acc = None):
	acc = acc or []
	while True:
		if i == len(x):
			acc.extend(y[j:])
			return acc
		if j == len(y):
			acc.extend(x[i:])
			return acc
		if x[i] < y[j]:
			acc.append(x[i])
			i += 1
		else:
			acc.append(y[j])
			j += 1

def merge_sort(x):
	if len(x) <= 1: return x
	mid = len(x) // 2
	return merge(merge_sort(x[:mid]), merge_sort(x[mid:]))

def inplace_merge(x, i, j, k, l):
	# invariant: i <= j <= k <= l
	if i == j or k == l: return # nothing left to be done
	if x[i] < x[k]:
		inplace_merge(x, i + 1, j, k, l)
	else:
		x[i], x[k] = x[k], x[i]
		inplace_merge(x, i + 1, j, k, l)


def inplace_merge(x, i, j, k, l):
	while True:
		# invariant: i <= j < k <= l
		if i == j or k == l: return # nothing left to be done
		if x[i] < x[k]:
			i += 1
		else:
			x[i], x[k] = x[k], x[i]
			i += 1

y = []
inplace_merge(y, 0, 1, 1, 1)
print(y)
y = [1]
inplace_merge(y, 0, 1, 1, 1)
print(y)
y = [1,2, 0]
inplace_merge(y, 0, 2, 2, 3)
print(y)
y = [1,2, 0,3,4]
inplace_merge(y, 0, 2, 2, 5)
print(y)

def merge_sort_rec(x, low, high):
	if high - low <= 1: return
	mid = (low + high) // 2
	merge_sort_rec(x, low, mid)
	merge_sort_rec(x, mid, high)
	inplace_merge(x, low, mid, mid, high)
	
def merge_sort(x):
	merge_sort_rec(x, 0, len(x))
	return x

x = []
print(merge_sort(x))

x = [2]
print(merge_sort(x))

x = [3,1]
print(merge_sort(x))

x = [1,3]
print(merge_sort(x))

x = [1,2,3]
print(merge_sort(x))

x = [3,2,1]
print(merge_sort(x))
