#https://www.hackerrank.com/challenges/maximize-it

from itertools import product
K, M = list(map(int, input().split()))
lst, opt = [], []

for i in range(K):
    lst.append(list(map(int, input().split()[1:])))
for i in product(*lst):
    opt.append(sum([x**2 for x in i]) % M)
    
print(max(opt))