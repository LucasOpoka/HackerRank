#https://www.hackerrank.com/challenges/s10-mcq-2

from itertools import product
lst = [1,2,3,4,5,6]
prd = list(product(lst, repeat=2))
prd2 = [i for i in prd if sum(i) == 6 and i[0] != i[1]]
result = len(prd2) / len(prd)
print(result)