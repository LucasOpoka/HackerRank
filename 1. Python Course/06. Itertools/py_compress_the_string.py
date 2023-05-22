#https://www.hackerrank.com/challenges/compress-the-string

from itertools import groupby
s = input()
output = ''
for k, g in groupby(s):
    output += f'({sum(1 for d in g)}, {k}) '

print(output)