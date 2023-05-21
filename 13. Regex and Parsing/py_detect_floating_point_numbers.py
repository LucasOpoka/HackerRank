#https://www.hackerrank.com/challenges/introduction-to-regex

import re
for _ in range(int(input())):
    print(bool(re.fullmatch('[+-]?\d*\.\d+', input())))