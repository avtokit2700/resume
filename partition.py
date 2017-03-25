# Partition                 Product
# [8]                          8
# [7, 1]                       7
# [6, 2]                      12
# [6, 1, 1]                    6
# [5, 3]                      15
# [5, 2, 1]                   10
# [5, 1, 1, 1]                 5
# [4, 4]                      16
# [4, 3, 1]                   12
# [4, 2, 2]                   16
# [4, 2, 1, 1]                 8
# [4, 1, 1, 1, 1]              4
# [3, 3, 2]                   18   <---- partition with maximum product value
# [3, 3, 1, 1]                 9
# [3, 2, 2, 1]                12
# [3, 2, 1, 1, 1]              6
# [3, 1, 1, 1, 1, 1]           3
# [2, 2, 2, 2]                16
# [2, 2, 2, 1, 1]              8
# [2, 2, 1, 1, 1, 1]           4
# [2, 1, 1, 1, 1, 1, 1]        2
# [1, 1, 1, 1, 1, 1, 1, 1]     1

arr = [0, 0]


def mult(arr):
    rez = 1
    for elem in arr:
        rez *= elem
    return rez


def find_part_max_prod(n):
    arr = [n-1, 1]
    result = {n: [n],
              n-1: [n-1, 1]}
    k = n - 2
    arr[0] = k
    arr[1] = n - k
    if arr[1] == 1:
        result[mult(arr)] = arr
        find_part_max_prod(k-1)
    print(result)
    return arr

print(find_part_max_prod(8))