
n = 22
m = 11

print(n // m, n % m)

a = n ; p = 0
while a >= m:
	a -= m
	p += 1

print(p, a)


