#https://www.hackerrank.com/challenges/collections-counter

from collections import Counter

X = int(input())
shoe_counter = Counter(map(int, input().split()))
N = int(input())
sales = 0
i = 0

while i < N:
    inpt = input().split()
    shoe_size = int(inpt[0])
    shoe_price = int(inpt[1])
    
    if shoe_counter[shoe_size] > 0:
        sales += shoe_price
        shoe_counter[shoe_size] -= 1
    i += 1

print(sales)