#https://www.hackerrank.com/challenges/python-quest-1

for i in range(1,int(input())):
    print(i * sum(map(lambda x:10**x,range(i))))