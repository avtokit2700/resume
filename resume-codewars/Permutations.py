"""
permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

"""
inp = 'aabb'
inp2 = 'ab'
inp3 = 'abcd'
"""
['abcd', 'abdc', 'acdb', 'adbc', 'bacd', 'cabd', 'cdab', 'cdba', 'dabc', 'dacb', 'dcab']
should equal
['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd',
'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']
"""

def shuffle(string):
    result = []
    new_str = []
    final = []

    for i in string:
        new_str.append(i)
    #if len(string) == 3:
        #final.append(new_str[1] + new_str[2] + new_str[0])

    for i in range(len(new_str)):
        for j in range(len(new_str)):
            new_str[i], new_str[j] = new_str[j], new_str[i]
            a = ''.join(new_str)
            result.append(a)

    for res in result:
        if res not in final:
            final.append(res)

    return final


def permutations(string):
    final = []
    full = []
    result = shuffle(string)
    for one in result:
        full.append(shuffle(one))
    for res in full:
        for r in res:
            if r not in final:
                final.append(r)
    return sorted(final)


print(permutations('mcywa'))




"""
IMBA VERSION
"""

def permutations2(string):
    result = {string}
    if len(string) == 2:
        result.add(string[1] + string[0])

    elif len(string) > 2:
        for i, c in enumerate(string):
            print(i,c)
            for s in permutations2(string[:i] + string[i + 1:]):
                result.add(c + s)

    return list(result)

print(permutations2('abcd'))