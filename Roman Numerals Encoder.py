"""
Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000

test.assert_equals(solution(1),'I', "solution(1),'I'")
test.assert_equals(solution(4),'IV', "solution(4),'IV'")
test.assert_equals(solution(6),'VI', "solution(6),'VI'")
"""
numeric = [
    (1000, 'M'),
    (500, 'D'),
    (100, 'C'),
    (50, 'L'),
    (10, 'X'),
    (5, 'V'),
    (1, 'I'),
]


def solution(num):

    result = ''
    for i, (number, roman) in enumerate(numeric):
        print(roman)
        current = num//number
        if current:
            if str(num)[0] == '4':
                result += roman + numeric[i-1][1]
                num -= number + numeric[i-1][0]
            elif str(num)[0] == '9':
                result += numeric[i+1][1] + numeric[i-1][1]
                num -= numeric[i+1][0] + numeric[i-1][0]
            else:
                result += roman*current
                num -= number*current
    return result

print(solution(542))

def solution2(n):
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_string = ''
    for key in sorted(roman_numerals.keys(),reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string

print(solution2(542))