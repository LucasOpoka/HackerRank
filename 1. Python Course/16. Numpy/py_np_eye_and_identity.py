#https://www.hackerrank.com/challenges/np-eye-and-identity

import numpy as np
np.set_printoptions(legacy='1.13')
print(np.eye(*map(int, input().split())))