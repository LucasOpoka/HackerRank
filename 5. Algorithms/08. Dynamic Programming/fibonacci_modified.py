#https://www.hackerrank.com/challenges/fibonacci-modified

import sys
sys.set_int_max_str_digits(0)

def fibonacciModified(t1, t2, n):
    for _ in range(n - 2):
        x = t2**2 + t1
        t1, t2 = t2, x
    return t2
    
t1, t2, n = map(int, input().split())
print(fibonacciModified(t1, t2, n))