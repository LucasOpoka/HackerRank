#https://www.hackerrank.com/challenges/py-set-union

n_uk = int(input())
set_uk = set(input().split())
n_fr = int(input())
set_fr = set(input().split())

set_total = set_uk.union(set_fr)

print(len(set_total))