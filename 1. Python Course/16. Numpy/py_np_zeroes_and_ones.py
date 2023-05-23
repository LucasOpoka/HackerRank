#https://www.hackerrank.com/challenges/np-zeros-and-ones

import numpy as np
x = tuple(map(int, input().split()))
print(np.zeros(x, int), np.ones(x, int), sep='\n')