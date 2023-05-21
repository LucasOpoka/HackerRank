#https://www.hackerrank.com/challenges/find-angle

import math

AB = int(input())
BC = int(input())
tan_x = AB / BC

print(f'{round(math.atan(tan_x) * 180 / math.pi)}{chr(0xB0)}')
