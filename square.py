# Написать функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
from math import sqrt


def square(side):
    perimetr = 4 * side
    plosha = 2 * side
    diagonal = sqrt(2) * side
    result = str(perimetr) + str(diagonal) + str(plosha)
    return tuple(result)

print(square(2))
