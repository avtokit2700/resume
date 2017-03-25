"""
productFib(714) # should return [21, 34, true],
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return [34, 55, false],
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
"""
M = {0: 0, 1: 1}

def fib(n):
    if n in M:
        return M[n]
    M[n] = fib(n - 1) + fib(n - 2)
    return M[n]

def productFib(prod):
    i = 1
    while True:
        proizved = fib(i) * fib(i+1)
        if proizved == prod:
            return [fib(i), fib(i+1), True]
        else:
            i += 1
        if proizved > prod:
            return [fib(i-1), fib(i), False]


print(productFib(800))