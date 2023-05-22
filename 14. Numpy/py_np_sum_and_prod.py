#https://www.hackerrank.com/challenges/np-sum-and-prod

import numpy as np
N, M = map(int, input().split())
arr = np.array([input().split() for _ in range(N)], int)
print(np.product(np.sum(arr, axis=0)))