# dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
# dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
# dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
# dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51


def dig_pow(n, p):
    result = 0
    for num in str(n):
        result += int(num) ** p
        p += 1
    if result % n == 0:
        return int(result / n)
    else:
        return -1

# print(dig_pow(46288, 3))

"""
The number 81 has a special property, a certain power of the sum of its digits is equal to 81 (nine squared). Eighty one (81), is the first number in having this property (not considering numbers of one digit). The next one, is 512. Let's see both cases with the details

8 + 1 = 9 and 9^2 = 81

512 = 5 + 1 + 2 = 8 and 8^3 = 512

We need to make a function, power_sumDigTerm(), that receives a number n and may output the n-th term of this sequence of numbers. The cases we presented above means that

power_sumDigTerm(1) == 81

power_sumDigTerm(2) == 512
"""

def power_sumDigTerm(n):
    dig_term = []
    suma = 0
    for i in range(80, 5834):
        for num in str(i):
            suma += int(num)
            for digit in range(2, 6):
                if suma**digit == i:
                    dig_term.append(i)
        suma = 0
    return dig_term


print(power_sumDigTerm(5))
