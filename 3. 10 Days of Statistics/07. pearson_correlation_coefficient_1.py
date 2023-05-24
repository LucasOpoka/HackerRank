#https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient

n = int(input())
a = list(map(float, input().split()))
b = list(map(float, input().split()))
mean = lambda x: sum(x)/len(x)
std = lambda x: (sum([(i-mean(x))**2 for i in x])/len(x))**0.5
prsn = lambda n, a, b: sum((i[0]-mean(a))*(i[1]-mean(b)) for i in list(zip(a,b))) / (n*std(a)*std(b))
print(f'{prsn(n,a,b):.3f}')