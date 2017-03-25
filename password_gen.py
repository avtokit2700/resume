from random import randint
import random as r
low = "abcdefghijklmnopqrstuvwxyz"
up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def password_gen():
    len_pass = randint(6, 20)
    print(len_pass)

    def gen(len):
        password = ''
        while len > 1:
            password += r.choice(up)
            len -= 1
            password += str(randint(0, 9))
            len -= 1
            password += r.choice(low)
            len -= 1
        return password
    return gen(len_pass)[:20]

print(password_gen())
print(len(password_gen()))

