#https://www.hackerrank.com/challenges/triangle-quest-2

for i in range(1,int(input())+1):
    print(sum(map(lambda x:10**x, range(i)))**2)