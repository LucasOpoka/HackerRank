#https://www.hackerrank.com/challenges/alphabet-rangoli

def print_rangoli(size):
    rows = size * 2 - 1
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    list_of_rows = []

    for i in range(0, rows // 2 + 1):
        row = alph[i + 1:size][::-1] + list(alph[i]) + alph[i + 1:size]
        if i == 0:
            width = len('-'.join(row))
        row = ('-'.join(row)).center(width,'-')    
        list_of_rows.append(row)

    list_of_rows  = list_of_rows[1:][::-1] + list_of_rows
    print('\n'.join(list_of_rows))
   
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)