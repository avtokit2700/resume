"""
Examples:
k = 2 -> 4, 6, 9, 10, 14, 15, 21, 22, …
k = 3 -> 8, 12, 18, 20, 27, 28, 30, …
k = 5 -> 32, 48, 72, 80, 108, 112, …
"""

from math import sqrt
# itertools.takewhile(func, iterable) - элементы до тех пор, пока func возвращает истину.
# itertools.filterfalse(func, iterable) - все элементы, для которых func возвращает ложь.
import itertools
"""
testing(count_Kprimes(2, 0, 100), [4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95])
testing(count_Kprimes(3, 0, 100), [8, 12, 18, 20, 27, 28, 30, 42, 44, 45, 50, 52, 63, 66, 68, 70, 75, 76, 78, 92, 98, 99])
testing(count_Kprimes(5, 1000, 1100), [1020, 1026, 1032, 1044, 1050, 1053, 1064, 1072, 1092, 1100])
testing(count_Kprimes(5, 500, 600), [500, 520, 552, 567, 588, 592, 594])

"""

def prime(num):
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def divisible(num, k):
    start = num
    div = []
    while num != 1:
        for i in range(2, start):
            if prime(i):
                while num % i == 0:
                    num /= i
                    div.append(i)
                    if len(div) >= k:
                        continue
        break
    if len(div) == k:
        return True
    else:
        return False


def count_Kprimes(k, start, nd):
    result = [i for i in range(start, nd+1) if divisible(i, k)]
    return result


print(count_Kprimes(7, 10000, 10100))

def puzzle(s):
    mb_a = [i for i in range(1, int(s/10)) if prime(i)]
    mb_b = [i for i in range(1, int(s/2)) if divisible(i, 3)]
    mb_c = [i for i in range(1, s) if divisible(i, 7)]
    result = []
    for c in mb_c:
        for b in mb_b:
            for a in mb_a:
                if a + b + c == s:
                    result.append([a, b, c])
    return result


print(puzzle(138))


def count_Kprimes(k, start, end):
    return [n for n in range(start, end + 1) if find_k(n) == k]


def puzzle(s):
    a = count_Kprimes(1, 0, s)
    b = count_Kprimes(3, 0, s)
    c = count_Kprimes(7, 0, s)

    return sum(1 for x in a for y in b for z in c if x + y + z == s)


def find_k(n):
    res = 0
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            res += 1
        i += 1
    if n > 1: res += 1
    return res
