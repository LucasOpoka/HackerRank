#https://www.hackerrank.com/challenges/30-conditional-statements

N = int(input())
ev = N%2==0
print('Weird') if ev == False or (ev == True and 6<=N<=20) else print('Not Weird')