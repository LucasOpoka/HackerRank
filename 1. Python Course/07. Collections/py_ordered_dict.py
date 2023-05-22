#https://www.hackerrank.com/challenges/py-collections-ordereddict

from collections import OrderedDict
N = int(input())

ordr_dict = OrderedDict()

for i in range(N):
    inpt = input().split()
    prod = ' '.join(inpt[:-1])
    pric = int(inpt[-1])
    
    if prod in ordr_dict.keys():
        ordr_dict[prod] += pric
    else:
        ordr_dict[prod] = pric

for j in ordr_dict:
    print(f'{j} {ordr_dict[j]}')