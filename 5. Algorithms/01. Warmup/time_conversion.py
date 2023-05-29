#https://www.hackerrank.com/challenges/time-conversion

def timeConversion(s):
    hh, mm, ss = s[:-2].split(':')
    m = s[-2:]
    if hh == '12' and m == 'AM':
        hh = '00'
    elif hh != '12' and m == 'PM':
        hh = str(int(hh) + 12)    
    return f'{hh}:{mm}:{ss}'

if __name__ == '__main__':
    s = input()
    print(timeConversion(s))