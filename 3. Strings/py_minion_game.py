#https://www.hackerrank.com/challenges/the-minion-game

def minion_game(string):
    vowels = list('AEIOU')
    consonants = list('BCDFGHJKLMNPQRSTVWXYZ')
    kevin = 0 #vowels
    stuart = 0 #consonants
 
    for i, c in enumerate(string):
        if c in vowels:
            kevin += len(range(i, len(string)))
        if c in consonants:
            stuart += len(range(i, len(string)))

    if kevin > stuart:
        print(f'Kevin {kevin}')
    elif stuart > kevin:
        print(f'Stuart {stuart}')
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)