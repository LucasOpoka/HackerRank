#https://www.hackerrank.com/challenges/zipped

N, X = map(int, input().split())
lst = []
for _ in range(X):
    lst.append(list(map(float, input().split())))
print(*map(lambda i:sum(i)/X, zip(*lst)), sep='\n')