
import sys
from math import log

def update_index(y, i):
	left = 2 * i + 1
	right = 2 * i + 2
	if left < len(y) and y[i] > y[left]:
		y[i] = y[left]
	if right < len(y) and y[i] > y[right]:
		y[i] = y[right]

def parent(i):
	return (i - 1) //2

for i in range(10):
	print(i, parent(2 * i + 1), parent(2 * i + 2))
sys.exit(0)

def compute_layer(y, start, end):
	if start >= end: return

	# O(n)
	for j in range(start, end):
		print(j, y[j])
		update_index(y, j)

	# Recurse on half size
	compute_layer(y, l - 1)
		

def construct(x):
	y = [sys.maxsize] * (len(x) - 1) + x
	for j in range(len(y) - 1, -1, -1):
		update_index(y, j)
	#no_layers, n = 0, len(y)
	#while 2**no_layers <= n: 
	#	no_layers += 1
	#compute_layer(y, no_layers)

	return y


print("empty")
construct([])
print("one")
x = [1]
y = construct(x)
print(y)

print("two")
x = [4,2]
y = construct(x)
print(y)

print("three")
x = [4,2,5]
y = construct(x)
print(y)

print("four")
x = [4,2,1,5]
y = construct(x)
print(y)

print("five")
x = [4,2,7,3,6]
y = construct(x)
print(y)
