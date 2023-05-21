#https://www.hackerrank.com/challenges/py-check-strict-superset

A = set(map(int, input().split()))
n = int(input())
spr_set = 'True'
i = 0

while i < n and spr_set == 'True':
    
    B = set(map(int, input().split()))
    
    if not(len(A - B) > 0 and len(B - A) == 0) :
        spr_set = 'False'
    
    i += 1

print(spr_set)