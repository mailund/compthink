
def factorial(n, acc = 1):
	if n == 1:
		return acc
	else: 
		return factorial(n - 1, n * acc)

print(factorial(4))

def factorial_cps(n, cont = lambda x: x):
	if n == 1:
		return cont(1)
	else:
		new_cont = lambda x: cont(n * x)
		return factorial_cps(n - 1, new_cont)

print(factorial_cps(4))

def trampoline(f):
	while callable(f):
		f = f()
	return f

def make_thunk(f, *args):
	return lambda: f(*args)

def factorial_rec(n, acc = 1):
	if n == 1:
		return acc
	else: 
		return make_thunk(factorial_rec, n - 1, acc * n)

def factorial(n):
	return trampoline(factorial_rec(n))

print(factorial(1))
print(factorial(2))
print(factorial(3))

def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib(n - 1) + fib(n - 2)

def fib_cps(n, cont = lambda x: x):
	if n == 0:
		return cont(0)
	if n == 1:
		return cont(1)
	else:
		new_cont = lambda x: fib_cps(n - 2, lambda y: cont(x + y))
		return fib_cps(n - 1, new_cont)



print(fib(3))
print(fib_cps(3))
print(fib(4))
print(fib_cps(4))
print(fib(5))
print(fib_cps(5))

def fib_cps(n, cont = lambda x: x):
	if n == 0:
		return cont(0)
	if n == 1:
		return cont(1)
	else:
		new_cont = lambda x: fib_cps(n - 2, lambda y: cont(x + y))
		return make_thunk(fib_cps, n - 1, new_cont)


def fib(n):
	return trampoline(fib_cps(n, lambda x: x))

print(fib(3))
print(fib(4))
print(fib(5))
