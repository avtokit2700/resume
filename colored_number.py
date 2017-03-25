# ['red', 'yellow', 'blue'].
# f(1) = 1
# f(n) = f(n - 1) + n
# term   value   colour
# 1        1     'red'
# 2        3     'blue'
# 3        6     'blue'
# 4       10      'red'
# 5       15     'blue'
# 6       21     'blue'
# 7       28     'red'
# (3, 3, 'blue') == [6, 15, 21]
# (100, 4, 'red') == [136, 190, 253, 325]
# 100 < val < 1000000
# 3 < k < 20

D, R = {}, [[], [], []]
for i in range(10000):
    D[i] = D.get(i - 1, 0) + i
    R[D[i] % 3].append(D[i])


def same_col_seq(val, k, col):
    r = ['blue', 'red', 'yellow'].index(col)
    return [e for e in R[r] if e > val][:k]

print(same_col_seq(100, 4, 'red'))