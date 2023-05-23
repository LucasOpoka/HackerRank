#https://www.hackerrank.com/challenges/np-transpose-and-flatten

import numpy as np
N, M = map(int, input().split())
lst = np.array([input().split() for _ in range(N)], int)
print(lst.transpose(), lst.flatten(), sep='\n')