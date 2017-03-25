"""
Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764.
The sum of the squared divisors is 2500 which is 50 * 50, a square!

list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
"""

from math import sqrt


def count_divisors(num):
    suma = [i**2 for i in range(1, num + 1) if num % i == 0]
    koren = sqrt(sum(suma))
    if koren.is_integer():
        return [num, sum(suma)]


def list_squared(m, n):
    result = []
    # result = [count_divisors(num) for num in range(m, n) if count_divisors(num) is not None]
    for num in range(m, n):
        if count_divisors(num) is not None:
            result.append(count_divisors(num))
    return result

#print(list_squared(1, 250))


"""
Second Variant
"""


def list_squared2(m, n):
    result = []
    for num in range(m, n):
        divisors = [i ** 2 for i in range(1, num + 1) if num % i == 0]
        suma_d = sum(divisors)
        koren = sqrt(suma_d)
        if koren.is_integer():
            result.append([num, suma_d])
    return result

#print(list_squared2(42, 1000))


"""
Third variant
"""

from math import sqrt
from itertools import chain


def list_squared3(m, n):
    result = []

    for num in range(m, n):
        divisors = set(chain.from_iterable(([i, num/i] for i in range(1, int(sqrt(num)) + 1) if num % i == 0)))
        divisor_squares = [i**2 for i in divisors]
        divisor_squares_sum = sum(divisor_squares)
        if sqrt(divisor_squares_sum).is_integer():
            result.append([num, int(divisor_squares_sum)])

    return result

print(list_squared3(1, 43))