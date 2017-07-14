# ip_to_int32("128.32.10.1") => 2149583361
import re


def ip_to_int32(ip):
    result = ''
    container = re.split(r"\.", ip)
    for c in container:
        if len(bin(int(c))[2:]) < 8:
            result += "0" * (8-len(bin(int(c))[2:])) + bin(int(c))[2:]
        else:
            result += bin(int(c))[2:]
    print(result)
    return int(result, base=2)

print(ip_to_int32("128.32.10.1"))

# a = '001'
# b = '011'

# c = bin(int(a,2) + int(b,2))