# Test.assert_equals(iq_test("2 4 7 8 10"),3)
# Test.assert_equals(iq_test("1 2 2"), 1)


def iq_test(numbers):
    even = 0
    even_list = []
    odd = 0
    odd_list = []
    for n in numbers.split():
        if int(n) % 2 == 0:
            even += 1
            even_list.append(n)
        elif int(n) % 2 != 0:
            odd += 1
            odd_list.append((n))
    if odd > even:
        return numbers.split().index(''.join([n for n in numbers.split() if int(n) % 2 == 0])) + 1
    else:
        return numbers.split().index(''.join([n for n in numbers.split() if int(n) % 2 != 0])) + 1


print(iq_test("1 2 2"))
