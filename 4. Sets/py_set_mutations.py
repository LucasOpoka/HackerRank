#https://www.hackerrank.com/challenges/py-set-mutations

N_setA =int(input())
setA = set(int(i) for i in input().split())
N = int(input())
i = 0

while i < N:
    cmnd_N_setN = input().split()
    cmnd = cmnd_N_setN[0]
    N_setN = int(cmnd_N_setN[1])
    setN = set(int(i) for i in input().split())
    
    exec('setA.' + cmnd + '(setN)')
    
    i += 1
    
print(sum(setA))