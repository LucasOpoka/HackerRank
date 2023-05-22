#https://www.hackerrank.com/challenges/s10-mcq-5

from itertools import combinations
lst = list(13*'c' + 13*'d' + 13*'h' + 13*'s')
comb = list(combinations(lst,2))
x = [i for i in comb if i[0]==i[1]]
print(len(x) / len(comb))