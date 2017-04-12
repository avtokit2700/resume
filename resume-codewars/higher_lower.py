numbers1 = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"

def high_and_low(numbers):
    intolist = numbers.split(' ')
    integer = []
    for i in intolist:
        integer.append(int(i))

    maximum = max(integer)
    minimum = min(integer)
    numbers = str(maximum) + ' ' + str(minimum)
    return numbers

print(high_and_low(numbers1))
