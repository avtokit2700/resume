"""
"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
"""

txt = "This is a test!"
encrypt_txt = "hsi  etTi sats!"


def decrypt(encrypted_text, n):
    for time in range(n):
        half = int(len(encrypted_text) / 2)
        begin = 0
        first = ''
        for one in range(int(len(encrypted_text)/2)):
            first += encrypted_text[half] + encrypted_text[begin]
            half += 1
            begin += 1
        if len(encrypted_text) % 2 == 0:
            encrypted_text = first
        elif len(encrypted_text) % 2 != 0:
            encrypted_text = first + encrypted_text[-1]
    return encrypted_text


def encrypt(text, n):
    for time in range(n):
        first = ''
        second = ''
        for i in range(1, len(text), 2):
            first += text[i]
        for i in range(0, len(text), 2):
            second += text[i]
        text = first + second
    return text

print(encrypt(txt, 1))
print(decrypt(encrypt_txt, 1))
print(decrypt("hskt svr neetn!Ti aai eyitrsig", 1))
print(len("hskt svr neetn!Ti aai eyitrsig"))
print(len(txt))