#https://www.hackerrank.com/challenges/diagonal-difference

def diagonalDifference(arr):
    rslt = 0
    for i in range(len(arr)):
        rslt += arr[i][i] - arr[i][-1-i]
    return abs(rslt)
        
arr = [list(map(int, input().split())) for _ in range(int(input()))]
print(diagonalDifference(arr))