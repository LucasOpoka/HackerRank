#https://www.hackerrank.com/challenges/hex-color-code

import re

for _ in range(int(input())):
    rslt = re.findall(r'(?<=.)(#[\da-fA-F]{6}|#[\da-fA-F]{3})', input())
    if rslt: print(*rslt, sep='\n')