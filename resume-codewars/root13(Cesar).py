import string
from codecs import encode as _dont_use_this_

L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))
I2L = dict(zip(range(26), "abcdefghijklmnopqrstuvwxyz"))

key = 13

# encipher

def rot13(message):
    ciphertext = ""
    for c in message:
        if c.isalpha() and c.isupper():
            ciphertext += I2L[(L2I[c] + key) % 26].upper()
        elif c.isalpha() and c.islower():
            ciphertext += I2L[(L2I[c.upper()] + key) % 26]
        else:
            ciphertext += c
    return ciphertext

print(rot13('test'))
# test.assert_equals(rot13("test", "grfg"))
# test.assert_equals(rot13("Test", "Grfg"))