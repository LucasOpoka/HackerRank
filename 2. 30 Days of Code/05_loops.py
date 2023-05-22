#https://www.hackerrank.com/challenges/30-loops

n = int(input())
print(*map(lambda x:f'{n} x {x} = {x*n}',range(1,11)),sep='\n')