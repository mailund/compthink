
x = ['Peter', 'Paul', 'James']
y = ['Paul', 'James', 'Mark']

# Selection sort x
for i in range(len(x)):
	min_idx, min_val = i, x[i]
	for j in range(i, len(x)):
		if x[j] < min_val:
			min_idx, min_val = j, x[j]
	x[i], x[min_idx] = min_val, x[i]

# Selection sort y
for i in range(len(y)):
	min_idx, min_val = i, y[i]
	for j in range(i, len(y)):
		if y[j] < min_val:
			min_idx, min_val = j, y[j]
	y[i], y[min_idx] = min_val, y[i]

intersection = []

while x and y:
    largest_x = x[-1]
    largest_y = y[-1]
    if largest_x == largest_y:
        intersection.append(largest_x)
        x.pop()
        y.pop()

    elif largest_x < largest_y:
        y.pop()
    else:
        x.pop()

print(intersection)



x = ['Peter', 'Paul', 'James']
y = ['Paul', 'James', 'Mark']

def compute_intersection(x, y):
    x = sorted(x)
    y = sorted(y)
    intersection = []
    while x and y:
        largest_x = x[-1]
        largest_y = y[-1]
        if largest_x == largest_y:
            intersection.append(largest_x)
            x.pop()
            y.pop()

        elif largest_x < largest_y:
            y.pop()
        else:
            x.pop()
    
    return intersection


x = ['Peter', 'Paul', 'James']
y = ['Paul', 'James', 'Mark']

intersection = compute_intersection(x, y)
print(intersection)

x = ['Peter', 'Paul', 'James']
y = ['Paul', 'James', 'Mark']

intersection = []
for elm in y:
    if elm in x:
        intersection.append(elm)

print(intersection)
