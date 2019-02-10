def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

for i in range(10):
    print("fib({}) = {}".format(i, fib(i)))

def fib(n):
    if n <= 1:
        return 1
    fibn1, fibn = 1, 1
    for i in range(1,n):
        # when n -> n + 1
        # F((n + 1) - 2) <- F(n - 1)
        # F((n + 1) - 1) <- F(n - 1) + F(n - 2)
        fibn1, fibn = fibn, fibn + fibn1
    return fibn

for i in range(10):
    print("fib({}) = {}".format(i, fib(i)))
