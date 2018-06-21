
def linear_search(x, e, i = 0):
	if i == len(x):
		return False
	if e == x[i]:
		return True
	else:
		return linear_search(x, e, i + 1)

x = [1,4,2]
print(linear_search(x, 3))
print(linear_search(x, 4))

def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n - 1)

print(factorial(3))

def factorial(n, acc = 1):
	if n == 1:
		return acc
	else:
		return factorial(n - 1, n * acc)

def factorial(n):
	acc = 1
	while True:
		if n == 1:
			return acc
		n, acc = n - 1, n * acc

print("tail recursive")
print(factorial(3))

def factorial(n):
	acc = 1
	while True:
		if n == 1:
			return acc
		acc = n * acc
		n = n - 1
		

print("tail recursive right")
print(factorial(3))

def factorial(n):
	acc = 1
	while True:
		if n == 1:
			return acc
		n = n - 1
		acc = n * acc

print("tail recursive wrong")
print(factorial(3))

def bsearch(x, e, low = 0, high = len(x)):
	if low >= high:
		return False
	mid = (low + high) // 2
	if x[mid] == e:
		return True
	elif x[mid] < e:
		return bsearch(x, e, mid + 1, high)
	else:
		return bsearch(x, e, low, mid)

print(bsearch(x, 3))
print(bsearch(x, 4))


def Fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return Fib(n - 1) + Fib(n - 2)

print(Fib(5))


def merge(x, y):
	result = []
	i, j = 0, 0
	while True:
		if i == len(x):
			# no more elements in x
			while j < len(y):
				result.append(y[j])
				j += 1
			return result
		if j == len(y):
			# no more elements in y
			while i < len(x):
				result.append(x[i])
				i += 1
			return result
		if x[i] < y[j]:
			result.append(x[i])
			i += 1
		else:
			result.append(y[j])
			j += 1

x = [1,2,3,6,7,8,9]
y = [2,3,3,3,4,5]
print("dresden")
print(merge(x,y))
print(merge([1],[3]))
print("bar")
print(merge([3],[1]))

def merge(x, y):
	if len(x) == 0:	return y
	if len(y) == 0:	return x
	if x[0] < y[0]:
		return [x[0]] + merge(x[1:], y)
	else:
		return [y[0]] + merge(x, y[1:])

print("leipzig")
print(merge(x,y))
print(merge([1],[3]))
print("bar")
print(merge([3],[1]))

def merge(x, y, i = 0, j = 0):
	if i == len(x): return y[j:]
	if j == len(y):	return x[i:]
	if x[i] < y[j]:
		return [x[i]] + merge(x, y, i + 1, j)
	else:
		return [y[j]] + merge(x, y, i, j + 1)

print("horse")
print(merge(x,y))
print(merge([1],[3]))
print("bar")
print(merge([3],[1]))

def merge(x, y, i = 0, j = 0, result = None):
	if result is None:
		result = []

	if i == len(x):
		# no more elements in x
		while j < len(y):
			result.append(y[j])
			j += 1
		return result
	if j == len(y):
		# no more elements in y
		while i < len(x):
			result.append(x[i])
			i += 1
		return result
	if x[i] < y[j]:
		result.append(x[i])
		return merge(x, y, i + 1, j, result)
	else:
		result.append(y[j])
		return merge(x, y, i, j + 1, result)

print("bar")
print(merge(x,y))
print("---")
print(merge([1],[3]))
print("bar")
print(merge([3],[1]))


def merge_rec(x, y, i = 0, j = 0):
	if i == len(x):	return y[j:]
	if j == len(y):	return x[i:]
	if x[i] < y[j]:
		res = merge_rec(x, y, i + 1, j)
		res.append(x[i])
		return res
	else:
		res = merge_rec(x, y, i, j + 1)
		res.append(y[j])
		return res

def merge(x, y):
	return list(reversed(merge_rec(x, y)))
print("foo")
print(merge(x,y))
print(merge([1],[3]))
print("bar")
print(merge([3],[1]))

def app(lst, x):
	lst.append(x)
	return lst

def merge_rec(x, y, i = 0, j = 0):
	if i == len(x):	return y[j:]
	if j == len(y):	return x[i:]
	if x[i] < y[j]:
		return app(merge_rec(x, y, i + 1, j), x[i])
	else:
		return app(merge_rec(x, y, i, j + 1), y[j])

def merge(x, y):
	return list(reversed(merge_rec(x, y)))

print("pony")
print(merge(x,y))
print(merge([1],[3]))
print("bar")
print(merge([3],[1]))


def merge(x, y, i = 0, j = 0, acc = None):
	if acc is None:
		acc = []
	if i == len(x):	
		return acc + y[j:]
	if j == len(y):	
		return acc + x[i:]
	if x[i] < y[j]:
		return merge(x, y, i + 1, j, app(acc, x[i]))
	else:
		return merge(x, y, i, j + 1, app(acc, y[j]))

print("qax")
print(merge(x,y))
print(merge([1],[3]))
print("bar")
print(merge([3],[1]))


def merge(x, y, i = 0, j = 0, acc = None):
	if acc is None:
		acc = []
	while True:
		if i == len(x):	return acc + y[j:]
		if j == len(y):	return acc + x[i:]
		if x[i] < y[j]:
			acc.append(x[i])
			i += 1
		else:
			acc.append(y[j])
			j += 1

print("qux")
print(merge(x,y))
print(merge([1],[3]))
print("bar")
print(merge([3],[1]))

def merge(x, y, i = 0, j = 0, acc = None):
	if acc is None:
		acc = []
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

print(merge(x,y))
print("foo")
print(merge([1],[3]))
print("bar")
print(merge([3],[1]))


x = [2, 5, 3, 5]

def my_min(x, y):
	return y if x is None else min(x, y)

smallest = None
for e in x:
	smallest = my_min(smallest, e)

print(smallest)



