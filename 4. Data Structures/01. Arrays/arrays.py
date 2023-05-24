#https://www.hackerrank.com/challenges/arrays-ds

def reverseArray(a):
    return a[::-1]

#My own implementation
#def reverseArray(a):
#    l = len(a)
#    return [a[l-(i+1)] for i in range(l)]

if __name__ == '__main__':
    arr_count = int(input())
    arr = list(map(int, input().split()))
    print(*reverseArray(arr))