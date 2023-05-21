#https://www.hackerrank.com/challenges/itertools-product

import itertools

A = map(int, input().split())
B = map(int, input().split())

prod = list(itertools.product(A, B))

string = ''
for i in prod:
    string += str(i) + ' '
    
print(string)