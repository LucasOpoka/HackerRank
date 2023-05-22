#https://www.hackerrank.com/challenges/30-dictionaries-and-maps

n = int(input())
dct = dict([tuple(input().split()) for _ in range(n)])
try:
    for _ in range(n): print(f'{inp}={dct[inp]}') if (inp:=input()) in dct else print('Not found')
except:
    EOFError