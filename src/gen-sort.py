
lst = [[x,y] for x in range(4,0,-1) for y in range(1,3)]
print(lst)
print(sorted(lst))

names = [
    ("Jane", "Doe"),
    ("John", "Deer"),
    ("John", "Doe"),
    ("Joe", "Smith")
]

for x in sorted(names):
    print(x)

print("foo")
for x in sorted(names, key = lambda x: (x[1],x[0])):
    print(x)

fruit = ["apple", "orange", "bananba", "kiwi"]
sorted(fruit)
print(sorted(fruit, key = len))


fruits = ["apple", "orange", "bananba", "kiwi"]
key_fun = len

# Selection sort
x = list(fruits)
print(x)

infinity = float("inf")
for i in range(len(x)):
    min_idx, min_val, min_key = 0, None, infinity
    for j in range(i, len(x)):
        if key_fun(x[j]) < min_key:
            min_idx, min_val, min_key = j, x[j], key_fun(x[j])      
    x[i], x[min_idx] = min_val, x[i]
print(x)
print(fruits)

# Insertion sort
x = list(fruits)
for i in range(1,len(x)):
    j = i
    while j > 0 and key_fun(x[j-1]) > key_fun(x[j]):
        x[j-1], x[j] = x[j], x[j-1]
        j -= 1  
print(x)

# Bucket sort
n = len(x)
m = max(key_fun(e) for e in x) + 1
buckets = [[] for bucket in range(m)]

y = []
for e in x:
    buckets[key_fun(e)].append(e)
for b in buckets:
    for e in b:
        y.append(e)
x = y
print(x)

from operator import itemgetter
print(sorted(names))
print(sorted(names, key = itemgetter(1)))

