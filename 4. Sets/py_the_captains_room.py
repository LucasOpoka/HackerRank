#https://www.hackerrank.com/challenges/py-the-captains-room
#I found an elegant solution that doesn't use the Collections module.

K = int(input())
RmNumLst = [int(i) for i in input().split()]
RmSet = set(RmNumLst)

sum_lst = sum(RmNumLst)
sum_set = sum(RmSet)

CptRmNum = int(sum_set - ((sum_lst - sum_set) / (K - 1)))

print(CptRmNum)