#https://www.hackerrank.com/challenges/python-sort-sort

N, M = map(int, input().split())
lst=[list(map(int, input().split())) for _ in range(N)]
k = int(input())
for i in sorted(lst,key = lambda x:x[k]):
    print(*i)  