# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.


def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False

year_inp = input("Enter year ")

print(is_year_leap(int(year_inp)))
