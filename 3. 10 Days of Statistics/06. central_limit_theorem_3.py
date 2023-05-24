#https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3

import math as m
mn, std, z = 500*100, 80*m.sqrt(100), 1.96
A, B = (mn-z*std)/100, (mn+z*std)/100
print(f'{A:.2f}\n{B:.2f}')