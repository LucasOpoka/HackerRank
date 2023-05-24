#https://www.hackerrank.com/challenges/s10-standard-deviation

def stdDev(arr):
    std_sum = sum(map(lambda x:(x-sum(arr)/len(arr))**2, arr))
    print('{:.1f}'.format((std_sum/len(arr))**(1/2)))

if __name__ == '__main__':
    n = int(input().strip())
    vals = list(map(int, input().rstrip().split()))
    stdDev(vals)