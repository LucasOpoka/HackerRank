#https://www.hackerrank.com/challenges/itertools-permutations

from itertools import permutations
inpt = input().split()

S = inpt[0]
k = int(inpt[1])

perm = list(permutations(S, k))
perm.sort()

for i in perm:
    print(''.join(i))
