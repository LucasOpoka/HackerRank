#https://www.hackerrank.com/challenges/s10-basic-statistics

import numpy as np
from scipy import stats

N = int(input())
arr = np.array(list(map(int, input().split())))

print(np.mean(arr))
print(np.median(arr))
print(min(stats.mode(arr)[0]))