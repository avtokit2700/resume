from math import sqrt

def is_square(n):
    if sqrt(n) % 1 == 0:
        return True
    else:
        return False

print(is_square(-1))