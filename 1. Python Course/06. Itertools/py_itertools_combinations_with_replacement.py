#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement

from itertools import combinations_with_replacement
inpt = input().split()

S = list(inpt[0])
k = int(inpt[1])

comb_w_r =  list(combinations_with_replacement(sorted(S), k))
   
for i in comb_w_r:
    print(''.join(i))