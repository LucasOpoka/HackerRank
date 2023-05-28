#https://www.hackerrank.com/challenges/a-very-big-sum

def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':
    ar_count = int(input().strip())
    ar = list(map(int, input().split()))

    print(aVeryBigSum(ar))