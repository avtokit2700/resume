# sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
# Test.assert_equals(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
# Test.assert_equals(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])


def sort_array1(source_array):

    print(source_array)
    n = len(source_array)
    m = n - 1
    while m > 0:
        for i in range(m):
            if (source_array[i] > source_array[i + 1]):
                x = source_array[i]
                source_array[i] = source_array[i + 1]
                source_array[i + 1] = x
        m = m - 1
    print(source_array)

# sort_array1([5, 3, 2, 8, 1, 4])

def sort_array(source_array):
    print(source_array)
    n = len(source_array)
    m = n - 1
    while m > 0:
        for i in range(m):
            if (source_array[i] % 2 == 0) and (source_array[i] > source_array[i + 1]) and (source_array[i+1] % 2 == 0):
                x = source_array[i]
                source_array[i] = source_array[i + 1]
                source_array[i + 1] = x
        m = m - 1
    print(source_array)

sort_array([5, 3, 2, 8, 1, 4])