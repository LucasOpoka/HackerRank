#https://www.hackerrank.com/challenges/array-left-rotation

def rotateLeft(d, arr):
    mod = d % len(arr)
    return arr[mod:] + arr[:mod]
        
if __name__ == '__main__':
    n,d = map(int, input().split())
    arr = list(map(int, input().split()))
    print(*rotateLeft(d, arr))