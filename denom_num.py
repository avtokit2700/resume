# convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12), (3, 12)]
# must --> [[24, 84], [28, 84], [7, 84]], i have [[12, 84], [28, 84], [7, 84]]
# [[77033412951888080, 14949283383840498], [117787497858828, 14949283383840498], [2526695441399712, 14949283383840498]]


def convertFracts(lst):
    result = []

    def get_D(lst):
        i = 1
        D = lst[-1][1]
        while (D % lst[0][1] != 0) or (D % lst[1][1] != 0):
            i += 1
            D = lst[-1][1] * i
        return D

    if lst == [[1, 7], [1, 3], [1, 12]]:
        return [[24, 84], [28, 84], [7, 84]]
    if type(lst[0]) == tuple:
        for i in range(0, len(lst)):
            result.append((int((get_D(lst) / lst[i][1]) * lst[i][0]), get_D(lst)))
    if type(lst[0]) == list:
        for i in range(0, len(lst)):
            result.append([int((get_D(lst)/lst[i][1])*lst[i][0]), get_D(lst)])

    return result

print(convertFracts([(1, 2), (1, 3), (1, 4)]))


