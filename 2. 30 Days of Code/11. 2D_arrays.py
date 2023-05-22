#https://www.hackerrank.com/challenges/30-2d-arrays

a, b = [list(map(int, input().split())) for _ in range(6)], []
hrgls_sum = lambda a,r,c : sum(a[r][c:c+3]) + a[r+1][c+1] + sum(a[r+2][c:c+3])

for r in range(len(a)-2):
    for c in range(len(a[0])-2):
       b.append(hrgls_sum(a,r,c))

print(max(b))