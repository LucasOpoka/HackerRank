#https://www.hackerrank.com/challenges/py-set-difference-operation

n_uk = int(input())
set_uk = set(input().split())
n_fr = int(input())
set_fr = set(input().split())

set_both = set_uk.difference(set_fr)

print(len(set_both))