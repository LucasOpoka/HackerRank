#https://www.hackerrank.com/challenges/s10-geometric-distribution-2

p, q, n = 1/3, 2/3, 5
print(f'{sum(map(lambda x:q**(x-1)*p, range(1,n+1))):.3f}')