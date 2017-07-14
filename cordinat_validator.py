"""

    -23, 25
    24.53525235, 23.45235
    04, -23.234235
    43.91343345, 143
    4, -3

And some invalid ones:

    23.234, - 23.4234
    2342.43536, 34.324236
    N23.43345, E32.6457
    99.234, 12.324
    6.325624, 43.34345.345
    0, 1,2
    0.342q0832, 1.2324

"""

def is_valid_coordinates(coordinates):
    number = coordinates.split(',', maxsplit=1)
    if len(number) == 2:
        if 'e' in number[0] or 'e' in number[1]:
            return False
        try:
            float(number[0])
            float(number[1])
        except ValueError:
            return False
        else:
            number1 = float(number[0])
            number2 = float(number[1])
            if -90 <= number1 <= 90:
                if -180 <= number2 <= 190:
                    return True
    return False

print(is_valid_coordinates("-16-438016450125517 37-9288-641569761"))
