#https://www.hackerrank.com/challenges/30-scope

class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        elem = set(self.__elements)
        d.maximumDifference = max(elem) - min(elem)
        return

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)