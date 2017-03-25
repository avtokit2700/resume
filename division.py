# Input: 42/9, expected result: 4 2/3.
# Input: 6/3, expedted result: 2.
# Input: 4/6, expected result: 2/3.
# Input: 0/18891, expected result: 0.
# Input: -10/7, expected result: -1 3/7.
# Test.assert_equals(mixed_fraction('-22/-7'), '3 1/7')

import re


def mixed_fraction(s):
    result = re.split(r'/', s)
    res = int(result[0]) / int(result[1])
    res2 = int(result[0]) % int(result[1])
    dif = int(result[1])-res2
    print(result[0])
    if int(result[0]) != 0:
        if int(res) == 0:
            if res2 % dif == 0 and int(result[1]) % dif == 0:
                return str(int(res2/dif)) + '/' + str(int(int(result[1])/dif))
        elif int(res2) == 0:
            return str(int(res))
        else:
            if int(result[0]) > 0 ^ int(result[1]) > 0:
                if res2 % dif == 0 and int(result[1]) % dif == 0:
                    return str(int(res)) + ' ' + str(int(res2 / dif)) + '/' + str(int(int(result[1]) / dif))
                else:
                    return str(int(res)) + ' ' + str(dif) + '/' + str(result[1])
            else:
                return str(int(res)) + ' ' + str((int(result[0]) - int(res)*int(result[1]))*-1) + '/' + str(int(result[1])*-1)
    else:
        return str(0)



#print(mixed_fraction('-10/7'))
#print('-10/7'.mixed_fraction())

# str(int(res)) + ' ' +

# Two SUM
# Test.assert_equals(sorted(two_sum([1,2,3], 4)), [0,2])
# Test.assert_equals(sorted(two_sum([1234,5678,9012], 14690)), [1,2])
# Test.assert_equals(sorted(two_sum([2,2,3], 4)), [0,1])


def two_sum(numbers, target):
    result = []
    for i in range(1, len(numbers)):
        print(numbers[i])
        if numbers[0] + numbers[i] == target:
            result.append(0)
            result.append(i)
            return result
        elif numbers[i] + numbers[i+1] == target:
            result.append(i)
            result.append(i+1)
            return result

print(two_sum([1234,5678,9012], 14690))
# (str(0) + ' ' + str(i)).split()