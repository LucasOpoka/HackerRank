#https://www.hackerrank.com/challenges/mini-max-sum

def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[:-1]), sum(arr[1:]))

arr = list(map(int, input().rstrip().split()))
miniMaxSum(arr)