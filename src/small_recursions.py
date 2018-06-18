
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
