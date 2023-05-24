#https://www.hackerrank.com/challenges/s10-weighted-mean

def weightedMean(X, W):
    print(round(sum(map(lambda i, j: i * j, X, W)) / sum(W), 1))

if __name__ == '__main__':
    n = int(input().strip())
    vals = list(map(int, input().rstrip().split()))
    weights = list(map(int, input().rstrip().split()))
    weightedMean(vals, weights)