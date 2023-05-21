#https://www.hackerrank.com/challenges/py-set-discard-remove-pop

n = int(input())
s = set(map(int, input().split()))
N = int(input())
i = 0
    
while i < N:
    cmnd_val = input().split()
    cmnd = cmnd_val[0]
    
    if len(cmnd_val) == 1:
        exec('s.' + cmnd + '()')
    else:
        val = int(cmnd_val[1])
        exec('s.' + cmnd + '(' + str(val) + ')')
    
    i += 1
    
print(sum(s))