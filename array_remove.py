# array_diff([1,2,2,2,3],[2]) == [1,3]


def array_diff(a, b):
    for num in b:
        while num in a:
            a.remove(num)
    return a


print(array_diff([], [2]))

