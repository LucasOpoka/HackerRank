#https://www.hackerrank.com/challenges/staircase

def staircase(n):
    for i in range(1, n+1):
        print(('#'*i).rjust(n))

n = int(input().strip())
staircase(n)