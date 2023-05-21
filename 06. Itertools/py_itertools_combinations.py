#https://www.hackerrank.com/challenges/itertools-combinations

from itertools import combinations
inpt = input().split()

S = inpt[0]
k = int(inpt[1])
comb = []

for i in range(1, k+1):
    sublist = [''.join(sorted(i)) for i in combinations(S, i)]
    sublist.sort()
    comb += sublist

for i in comb:
    print(i)