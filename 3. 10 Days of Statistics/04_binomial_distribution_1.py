#https://www.hackerrank.com/challenges/s10-binomial-distribution-1

from math import comb as c
x, n, b, g = 3, 6, 1.09, 1
p, q = b/(b+g), g/(b+g)
print(f'{sum(map(lambda x:c(n,x)*p**x*q**(n-x),range(3,7))):.3f}')