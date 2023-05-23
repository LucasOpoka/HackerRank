#https://www.hackerrank.com/challenges/matrix-script

import re
n,m = map(int, input().split())
matrix = []

[matrix.append(list(input())) for _ in range(n)]
matrix = list(zip(*matrix))

result = ''.join([c for s in matrix for c in s])
print(re.sub(r'(?<=[^\W_])([\W]+?)(?=[^\W_])',' ', result))
