#https://www.hackerrank.com/challenges/compare-the-triplets

def compare(a, b):
    alice, bob = 0, 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    print(f'{alice} {bob}')

if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = compare(a, b)