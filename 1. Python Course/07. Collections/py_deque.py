#https://www.hackerrank.com/challenges/py-collections-deque

from collections import deque
d = deque()

for _ in range(int(input())):
    inpt = input().split()
    if len(inpt) == 2: 
        exec('d.'+ inpt[0] + '(' + inpt[1] +')')
    else:
        exec('d.'+ inpt[0] + '()')
  
print(*d)