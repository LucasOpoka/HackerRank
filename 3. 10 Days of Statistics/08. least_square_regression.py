#https://www.hackerrank.com/challenges/s10-least-square-regression-line

lst = [list(map(int, input().split())) for _ in range(5)]
x = [i[0] for i in lst]
y = [i[1] for i in lst]

mean = lambda x: sum(x)/len(x)
std = lambda x: (sum([(i-mean(x))**2 for i in x])/len(x))**0.5
prsn = lambda x, y: sum((i[0]-mean(x))*(i[1]-mean(y)) for i in list(zip(x,y))) / (len(x)*std(x)*std(y))

slope = lambda prsn_xy,std_x,std_y : prsn_xy*(std_y/std_x)
intercept = lambda slope, mean_x, mean_y : mean_y - slope*mean_x

slpe = slope(prsn(x,y), std(x), std(y))
intr = intercept(slpe, mean(x), mean(y))
print(f'{slpe*80+intr:.3f}')