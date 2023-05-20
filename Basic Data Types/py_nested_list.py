#https://www.hackerrank.com/challenges/nested-list

if __name__ == '__main__':

    lst = []

    for _ in range(int(input())):
        name, score = input(), float(input())
        
        sub_lst = [name, score]
        lst.append(sub_lst)
        
    lst.sort(key = lambda l:l[1])    
    uniq_grde_lst = list(set(i[1] for i in lst))
    uniq_grde_lst.sort()
    scnd_lwst_grde = uniq_grde_lst[1]

    stdnts = [i for i in lst if i[1] == scnd_lwst_grde]
    stdnts.sort()
   
    for stdnt in stdnts:
        print(stdnt[0])