#https://www.hackerrank.com/challenges/py-check-subset

n_tsts = int(input())
i = 0

while i < n_tsts:
    n_a = int(input())
    set_a = set(map(int, input().split()))
    n_b = int(input())
    set_b = set(map(int, input().split()))
    
    if len(set_a.difference(set_b)) == 0:
        print('True')
    else:
        print('False')
    
    i += 1