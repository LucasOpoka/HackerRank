#https://www.hackerrank.com/challenges/s10-poisson-distribution-1

from math import factorial as fc
e, l, k = 2.71828, 2.5, 5
print(f'{(l**k * e**-l) / fc(k):.3f}')