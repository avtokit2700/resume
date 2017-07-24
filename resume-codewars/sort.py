s = [6, 5, 9, 12, 3, 1, 2, 4, 7, 10, 11]
s2 = [6, 5, 9, 12, 3, 1, 2, 4, 7, 10, 11, 14, 67, 99]


def sort_method_1(s):
    """Сортировка методом перестановки"""
    print(s)
    k = 0
    while k < len(s) - 1:  # -1, т.к. последний элемент обменивать уже не надо
        m = k  # в m хранится минимальное значение
        i = k + 1  # откуда начинать поиск минимума (элемент следующий за k)
        while i < len(s):
            if s[i] < s[m]:
                m = i
            i += 1
        t = s[k]
        s[k] = s[m]
        s[m] = t
        k += 1  # переходим к следующему значению для обмена

    print(s)


def sort_method_2(s):
    """Сортировка пузырьковым методом"""
    print(s)
    n = len(s)
    m = n - 1
    while m > 0:
        for i in range(m):
            if s[i] > s[i + 1]:
                s[i], s[i+1] = s[i+1], s[i]
        m = m - 1

    print(s)

# sort_method_2(s)


def insertion_sort(items):
    """ Implementation of insertion sort """
    print(items)
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j - 1] = items[j - 1], items[j]
            j -= 1
    return items

# print(insertion_sort(s))


def quick_sort(items):
    """ Implementation of quick sort """
    if len(items) > 1:
        pivot_index = int(len(items) / 2)
        smaller_items = []
        larger_items = []

        for i, val in enumerate(items):
            if i != pivot_index:
                if val < items[pivot_index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)

        quick_sort(smaller_items)
        quick_sort(larger_items)
        items[:] = smaller_items + [items[pivot_index]] + larger_items
        return items

print(quick_sort(s2))
