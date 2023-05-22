#https://www.hackerrank.com/challenges/defaultdict-tutorial

from collections import defaultdict
N, M = map(int, input().split())
d = defaultdict(list)

for i in range(N):
    d[input()].append(i+1)

for j in range(M):
    inpt = input()
    if len(d[inpt]) == 0:
        print(-1)
    else:
        print(*d[inpt])