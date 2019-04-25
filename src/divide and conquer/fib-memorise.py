tbl = {}

count = 0
def fib(n):
    global count, tbl
    count += 1
    if n <= 1:
        return 1
    else:
        if n not in tbl:
            tbl[n] = fib(n - 1) + fib(n - 2)
        return tbl[n]
            

print("n fib count")
for i in range(1,11):
    count = 0
    tbl = {}
    print("{} {} {}".format(i, fib(i), count))
    
# def fib(n):
#     if n <= 1:
#         return 1
#     fibn1, fibn = 1, 1
#     for i in range(1,n):
#         # when n -> n + 1
#         # F((n + 1) - 2) <- F(n - 1)
#         # F((n + 1) - 1) <- F(n - 1) + F(n - 2)
#         fibn1, fibn = fibn, fibn + fibn1
#     return fibn

# for i in range(10):
#     print("fib({}) = {}".format(i, fib(i)))

tbl = {}

def fib(n):
    if n <= 1:
        return 1
    fi1, fi2 = 1, 1
    for i in range(n - 1):
        fi1, fi2 = fi1 + fi2, fi1
    return fi1

print("n fib count")
for i in range(1,11):
    count = 0
    tbl = {}
    print("{} {} {}".format(i, fib(i), count))
