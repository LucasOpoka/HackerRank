#https://www.hackerrank.com/challenges/np-array-mathematics

import numpy as np
N, M = map(int, input().split())
lst = ['+','-','*','//','%','**']
A = np.array([input().split() for _ in range(N)], int)
B = np.array([input().split() for _ in range(N)], int)
for i in lst: exec(f'print(A{i}B)')