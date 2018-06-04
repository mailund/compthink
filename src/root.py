

a = 0 ; b = 1
x = (a + b) / 2
epsilon = 0.01

val = x ** 3 - 3 * x ** 2 + 1
while abs(val) > epsilon:
	if val > 0:
		a = x
	else:
		b = x
	x = (a + b) / 2
	val = x ** 3 - 3 * x ** 2 + 1

	print(a, b, x, val)
print(x, val)