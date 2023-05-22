#https://www.hackerrank.com/challenges/word-order

from collections import OrderedDict
n = int(input())
words = OrderedDict()

for i in range(n):
    wrd = input()
    words[wrd] = words.get(wrd, 0) + 1

print(len(words)) 
for j in words.values():
    print(j, end=' ')