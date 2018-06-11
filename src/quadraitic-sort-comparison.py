
def selection_sort(x):
	x = x[:]
	comparisons, swaps = 0, 0
	infinity = float("inf")
	for i in range(len(x)):
		# find index of smallest elm in x[i:]
		min_idx, min_val = 0, infinity
		for j in range(i, len(x)):
			comparisons += 1
			if x[j] < min_val:
				min_idx, min_val = j, x[j]
			
		# swap x[i] and x[j] puts
		# x[j] at the right position
		if x[i] > min_val:
			swaps += 1
			x[i], x[min_idx] = min_val, x[i]

		

	print("selection", comparisons, swaps)
	return x

def insertion_sort(x):
	x = x[:]
	comparisons, swaps = 0, 0
	for i in range(1,len(x)):
		j = i
		comparisons += 1
		while j > 0 and x[j-1] > x[j]:
			x[j-1], x[j] = x[j], x[j-1]
			j -= 1		
			swaps += 1
			comparisons += 1
	print("insertion", comparisons, swaps)
	return x


def bubble_sort(x):
	x = x[:]
	comparisons, swaps = 0, 0
	while True:
		swapped = False
		for i in range(1,len(x)):
			comparisons += 1
			if x[i-1] > x[i]:
				x[i-1], x[i] = x[i], x[i-1]
				swaps += 1
				swapped = True

		if not swapped:
			break

	print("bubble", comparisons, swaps)
	return x

def cocktail_sort(x):
	x = x[:]
	comparisons, swaps = 0, 0
	while True:
		swapped = False
		for i in range(1, len(x)):
			comparisons += 1
			if x[i-1] > x[i]:
				x[i-1], x[i] = x[i], x[i-1]
				swaps += 1
				swapped = True
				
		if not swapped:
			break

		for i in range(len(x)-1, 1, -1):
			comparisons += 1
			if x[i-1] > x[i]:
				x[i-1], x[i] = x[i], x[i-1]
				swaps += 1
				swapped = True

		if not swapped:
			break

	print("cocktail", comparisons, swaps)
	return x

def run_sorted(n):
	x = list(range(n))
	print("sorted", n, end=" ") ; selection_sort(x)
	print("sorted", n, end=" ") ; insertion_sort(x)
	print("sorted", n, end=" ") ; bubble_sort(x)
	print("sorted", n, end=" ") ; cocktail_sort(x)

from numpy.random import permutation
from random import sample
def run_permuted(n):
	x = list(permutation(n))
	print("permuted", n, end=" ") ; selection_sort(x)
	print("permuted", n, end=" ") ; insertion_sort(x)
	print("permuted", n, end=" ") ; bubble_sort(x)
	print("permuted", n, end=" ") ; cocktail_sort(x)

def run_almost_sorted(n):
	m = n // 10 # 10%
	x = list(range(n))
	idx1, idx2 = sample(range(n), m), sample(range(n), m)
	for i,j in zip(idx1, idx2):
		x[i], x[j] = x[j], x[i]

	print("almost_sorted", n, end=" ") ; selection_sort(x)
	print("almost_sorted", n, end=" ") ; insertion_sort(x)
	print("almost_sorted", n, end=" ") ; bubble_sort(x)
	print("almost_sorted", n, end=" ") ; cocktail_sort(x)

def run_reversed(n):
	x = list(range(n,0,-1))
	print("reversed", n, end=" ") ; selection_sort(x)
	print("reversed", n, end=" ") ; insertion_sort(x)
	print("reversed", n, end=" ") ; bubble_sort(x)
	print("reversed", n, end=" ") ; cocktail_sort(x)

for n in range(10, 100, 10):
	run_sorted(n)
	run_reversed(n)
	for k in range(10):
		run_permuted(n)
		run_almost_sorted(n)

