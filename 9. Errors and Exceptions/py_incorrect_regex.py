#https://www.hackerrank.com/challenges/incorrect-regex

import re
T = int(input())

for _ in range(T):
    try:
        re.compile(input())
        print('True')
    except re.error:
        print('False')