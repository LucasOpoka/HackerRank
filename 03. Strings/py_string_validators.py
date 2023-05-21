#https://www.hackerrank.com/challenges/string-validators

if __name__ == '__main__':
    
    def string_contains(string, tests):
        for t in tests:
            condition = False
            for i in string:
                if not condition:
                    condition = eval(f"'{i}'.is{t}()")         
            print(condition)
    
    s = input()
    tsts = ['alnum','alpha','digit','lower','upper']

    string_contains(s,tsts)