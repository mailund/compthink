count = 0
def fib(n):
    global count
    count += 1
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

#print("n fib count")
#for i in range(1,31):
#    count = 0
#    print("{} {} {}".format(i, fib(i), count))

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

def fib_dp(n):
    if n <= 1:
        return 1
    tbl = [1] * n
    for i in range(2,n):
        tbl[i] = tbl[i - 1] + tbl[i - 2]
    return tbl[n - 1] + tbl[n - 2]

print("n fib count")
for i in range(1,10):
    print("{} {} {}".format(i, fib(i), fib_dp(i)))
