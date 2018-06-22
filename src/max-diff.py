
def min_max_maxdiff(x, i, j):
	# Invariant: j >= i
	if i + 1 == j:
		return x[i], x[i], 0
	else:
		mid = (i + j) // 2
		min_l, max_l, maxdiff_l = min_max_maxdiff(x, i, mid)
		min_r, max_r, maxdiff_r = min_max_maxdiff(x, mid, j)
		min_res = min(min_l, min_r)
		max_res = max(max_l, max_r)
		maxdiff_res = max(maxdiff_l, maxdiff_r,
			              max_r - min_l, max_l - min_r)
		return min_res, max_res, maxdiff_res

def maxdiff(x):
	if len(x) == 0: return None
	_, _, md = min_max_maxdiff(x, 0, len(x))
	return md

print("empty")
print(maxdiff([]))
print("one")
print(maxdiff([1]))
print("two")
print(maxdiff([1,1]))
print(maxdiff([1,2]))
print(maxdiff([2,1]))
print(maxdiff([2,2]))
print("three")
print(maxdiff([1,2,3]))
print(maxdiff([2,1,3]))
print(maxdiff([2,3,1]))
print("four")
print(maxdiff([4,1,2,3]))
print(maxdiff([2,4,1,3]))
print(maxdiff([2,3,4,1]))
