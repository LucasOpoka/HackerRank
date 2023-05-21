#https://www.hackerrank.com/challenges/designer-door-mat

dim = [int(i) for i in input().split()]
N = dim[0]
M = dim[1]
ptrn = '.|.'
n_ptrn = 1
wlc = 'WELCOME'

for i in range(N // 2):
    dash = int((M - (n_ptrn * 3)) / 2)
    print('-' * dash + ptrn * n_ptrn + '-' * dash)
    n_ptrn += 2
print(wlc.center(M, '-'))
n_ptrn -= 2
for i in range(N // 2):
    dash = int((M - (n_ptrn * 3)) / 2)
    print('-' * dash + ptrn * n_ptrn + '-' * dash)
    n_ptrn -= 2