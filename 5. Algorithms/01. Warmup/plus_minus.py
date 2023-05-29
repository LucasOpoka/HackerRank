#https://www.hackerrank.com/challenges/plus-minus

def plusMinus(arr):
    lst = ['>', '<', '==']
    for x in lst:
        exec(f'print(sum(i{x}0 for i in arr) / len(arr))')
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    plusMinus(arr)