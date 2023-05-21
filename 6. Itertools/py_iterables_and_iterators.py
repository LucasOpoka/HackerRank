#https://www.hackerrank.com/challenges/iterables-and-iterators

from itertools import combinations
N = int(input())
lst = list(input().split())
K = int(input())

tuples = list(combinations(range(N), K))
occurences = 0

for i in tuples:
    if 'a' in [lst[i[k]] for k in range(K)]: 
        occurences += 1

print(occurences / len(tuples))