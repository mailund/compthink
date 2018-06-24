def check_heap(x):
	for i in range(len(x)):
		check_heap_property(x, i)
		
def check_heap_property(x, j):
	if j > len(x): return

	left_idx = 2 * j + 1
	right_idx = 2 * j + 2
	print("checking", j, left_idx, right_idx, x)
	if left_idx < len(x): print("left", x[j], x[left_idx])
	if right_idx < len(x): print("right", x[j], x[right_idx])
	assert left_idx >= len(x) or x[j] <= x[left_idx]
	assert right_idx >= len(x) or x[j] <= x[right_idx]

	#check_heap_property(x, left_idx)
	#check_heap_property(x, right_idx)


def heapify(x, start, end):
	print("heapify", start, end)
	if start > len(x): return

	# O(n) work
	for j in range(start, end + 1):
		print("j is", j, "start is", start, "end is", end)
		left_idx = 2 * j + 1
		right_idx = 2 * j + 2
		print("updating", j, left_idx, right_idx)#, x[j], x[left_idx], x[right_idx])
		if left_idx < len(x) and x[j] > x[left_idx]:
			print("flip left", j, left_idx, x[j], x[left_idx])
			x[j], x[left_idx] = x[left_idx], x[j]
		if right_idx < len(x) and x[j] > x[right_idx]:
			x[j], x[right_idx] = x[right_idx], x[j]
			print("flip right", j, right_idx, x[j], x[right_idx])
		print(j, left_idx, right_idx)#, x[j], x[left_idx], x[right_idx])
		check_heap_property(x, j)
		
	# recurse on half the size
	heapify(x, end + 1, 2 * (end + 1))



x = [5,4,6,3,1,2, 10, 0, -3]
heapify(x, 0, 0)
print("checking heap")
check_heap(x)
print(x)

from numpy.random import permutation
for i in range(100):
	x = permutation(50)
	heapify(x, 0, 0)
	check_heap(x)
	
