#https://www.hackerrank.com/challenges/dynamic-array

idx_func = lambda x, la, n : (x^la) % n

def dynamic_arr(n, queries):
    la = [0]
    arr = [[] for _ in range(n)]
    for q in queries:
        idx = idx_func(q[1],la[-1],n)
        if q[0]==1:
            arr[idx].append(q[2])
        else:
            la.append(arr[idx][q[2]%len(arr[idx])])
    return la[1:]
    
if __name__ == '__main__':
    n, q = map(int, input().split())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))

    print(*dynamic_arr(n,queries), sep='\n')