"""
4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
"""


# Простой алгоритм с сетами
def partition(number):
    answer = set()
    answer.add((number,))
    for x in range(1, number):
        for y in partition(number - x):
            answer.add(tuple(sorted((x,) + y)))
    return answer


# Динамическое программирование
def exp_sum(n):
    memo = [[0 for x in range(n + 1)] for x in range(n + 1)]
    return e_sum(n, 1, memo)


# index is where the loop should start and increase it by 1 so it does not repeated
def e_sum(n, index, memo):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if memo[n][index] != 0:
        return memo[n][index]

    count = 0
    for i in range(index, n + 1):
        count += e_sum(n - i, i, memo)

    memo[n][index] = count
    return count


# Best variant

def exp_sum_best(n):
    if n < 0:
        return 0
    dp = [1] + [0] * n
    for num in range(1, n + 1):
        for i in range(num, n + 1):
            dp[i] += dp[i - num]
    return dp[-1]
