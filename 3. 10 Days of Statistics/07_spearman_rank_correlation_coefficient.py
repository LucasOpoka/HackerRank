#https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient

n = int(input())
a = list(map(float, input().split()))
b = list(map(float, input().split()))
ranks = lambda x : [sorted(x).index(i)+1 for i in x]
spear = lambda n,a,b : 1-6*sum([(i[0]-i[1])**2 for i in list(zip(ranks(a),ranks(b)))]) / (n*(n**2-1))
print(round(spear(n,a,b),3))