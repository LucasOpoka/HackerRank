#https://www.hackerrank.com/challenges/symmetric-difference

if __name__ == '__main__':
    M = int(input())
    M_elem = set(map(int, input().split()))
    N = int(input())
    N_elem = set(map(int, input().split()))

    lst = list(M_elem.symmetric_difference(N_elem))
    lst.sort()

    for i in lst:
        print(i)