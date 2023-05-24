#https://www.hackerrank.com/challenges/s10-binomial-distribution-2

from math import comb as c
n, p, q = 10, 0.12, 0.88
print(f'{sum(map(lambda x:c(n,x)*p**x*q**(n-x),range(0,3))):.3f}')
print(f'{sum(map(lambda x:c(n,x)*p**x*q**(n-x),range(2,11))):.3f}')