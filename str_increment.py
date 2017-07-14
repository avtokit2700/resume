# ("foo"), "foo1")
# ("foobar001"), "foobar002")
# ("foobar1"), "foobar2")
# ("foobar00"), "foobar01")
# ("foobar99"), "foobar100")
# ("foobar099"), "foobar100")
# (""), "1")

import re
def increment_string(strng):
    letter = []
    num = []
    zero_slt = ''
    if not strng:
        return '1'
    if strng.isalpha():
        return strng + '1'
    for s in strng:
        if s.isalpha():
            letter.append(s)
        elif s.isdigit():
            num.append(s)
    increment = ''
    print(num)
    if (int(''.join(num)) + 1) % 10 == 0:
        res = ''.join(letter) + zero_slt + str(int(''.join(num)) + 1)
        if num.count('0') == 1:
            return res
        if num[0] == '0':
            return ''.join(letter) + '0' + str(int(''.join(num)) + 1)
        return res
    print(num)
    for i in num:
        increment += i

    return ''.join(letter) + increment[:-1] + str(int(num[-1])+1)

print(increment_string("!378632345%75408000000929"))

print(1 % 10)