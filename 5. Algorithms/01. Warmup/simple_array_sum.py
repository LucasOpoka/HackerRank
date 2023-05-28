#https://www.hackerrank.com/challenges/simple-array-sum

def simpleArraySum(arr):
    return sum(arr)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = simpleArraySum(arr)
    print(result)