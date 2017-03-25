import re

class Mod:
    mod4 = re.compile(".*\[[+-]?([048]|\d*([02468][048]|[13579][26]))\]") #Your regular expression here

# "[+05620]" // 5620 is divisible by 4 (valid)
# "[+05621]" // 5621 is not divisible by 4 (invalid)
# "[-55622]" // -55622 is not divisible by 4 (invalid)
# "[005623]" // 5623 invalid
# "[005624]" // 5624 valid

t = (1, 2)
t = t +(3,)
print(t)

s = '123'
print(2**4)

n = set()
print(type(n))

d = {1:2, 2:4}
print(d.items())