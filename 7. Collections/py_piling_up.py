#https://www.hackerrank.com/challenges/piling-up

T = int(input())
for _ in range(T):
    n = int(input())
    lst = list(map(int, input().split()))
    ind = lst.index(min(lst))
    cond1, cond2 = True, True
    for x in range(len(lst[:ind])):
        if not (lst[x] >= lst[x+1]):
            cond1 = False
            break
    for y in range(len(lst[ind:-1])):
        if not (lst[y+ind] <= lst[y+ind+1]):
            cond2 = False
            break
    print('Yes' if cond1 and cond2 else 'No')