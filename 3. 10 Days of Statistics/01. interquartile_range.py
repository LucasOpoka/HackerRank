#https://www.hackerrank.com/challenges/s10-interquartile-range

def median(arr):
    arr = sorted(arr)
    if len(arr) % 2 == 0:
        m = int(len(arr)/2)
        return [(arr[m-1]+arr[m])/2, arr[:m], arr[m:]]
    else:
        m = int(len(arr)/2 + 0.5)
        return [arr[m-1], arr[:m-1], arr[m:]]

def quartiles(arr):
    x = median(sorted(arr))
    q1 = int(median(x[1])[0])
    q2 = int(x[0])
    q3 = int(median(x[2])[0])
    return [q1, q2, q3]

def interQuartile(values, freqs):
   new_lst = []
   for i in range(len(freqs)):
       for j in range(freqs[i]):
           new_lst.append(values[i])
   
   quart = quartiles(sorted(new_lst))
   print('{:.1f}'.format(quart[2] - quart[0]))
   
if __name__ == '__main__':
    n = int(input().strip())
    val = list(map(int, input().rstrip().split()))
    freq = list(map(int, input().rstrip().split()))
    interQuartile(val, freq)