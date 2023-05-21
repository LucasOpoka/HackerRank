#https://www.hackerrank.com/challenges/python-string-formatting

def print_formatted(number):
    wdth = len(format(number, 'b')) + 1

    for i in range(1, number + 1):
        deci = format(i).rjust(wdth - 1)
        octa = format(i, 'o').rjust(wdth)
        hexa = format(i, 'x').rjust(wdth).upper()
        bina = format(i, 'b').rjust(wdth)
    
        print(deci + octa + hexa + bina)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)