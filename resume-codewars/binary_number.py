import sys
import re

n = int(input().strip())
num = str(bin(n))[2:]
lst = re.sub(r'0', ' ', num).split()
max_len = []
for l in lst:
    max_len.append(len(l))
print(max(max_len))