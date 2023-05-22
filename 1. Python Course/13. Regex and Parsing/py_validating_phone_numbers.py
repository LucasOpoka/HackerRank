#https://www.hackerrank.com/challenges/validating-the-phone-number

import re
for _ in range(int(input())):
    print('YES' if re.fullmatch('[789]\d{9}',input()) else 'NO')