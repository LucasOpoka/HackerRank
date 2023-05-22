#https://www.hackerrank.com/challenges/np-min-and-max

import numpy as np
N, M = map(int, input().split())
arr = np.array([input().split() for _ in range(N)], int)
print(np.max(np.min(arr, axis=1)))