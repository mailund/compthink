roads = [
	(0, 1), (0, 2), (0, 3),
	(1, 4), (1, 5),
	(2, 5), (2, 6),
	(3, 6), (3, 7),
	(4, 8),
	(5, 9),
	(6, 9),
	(7, 10),
	(8, 11),
	(8, 12),
	(9, 13),
	(10, 13)
]

N = 14 # number of cities
S = list(range(N))
print("# Initial state")
print("S =", S)
print("# Entering loop...")
for p, q in roads:
	rep_p = S[p]
	rep_q = S[q]
	new_rep = max(rep_p, rep_q)
	for i in range(N):
		if S[i] == rep_p or S[i] == rep_q:
			S[i] = new_rep

	print("S =", S)

print("# After loop")
print("S =", S)
