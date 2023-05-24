#https://www.hackerrank.com/challenges/s10-mcq-6

lst, lst2 = list('rrrbbbb'), list('rrbbbb')
S1, S2 = len(lst), len(lst2)
A = len([i for i in lst if i == 'r'])
B = len([i for i in lst2 if i == 'b'])

prob_A = A / S1
prob_B = B / S2

prob_AandB = prob_A * prob_B
prob_BgivenA = prob_AandB / prob_A
print(prob_BgivenA)