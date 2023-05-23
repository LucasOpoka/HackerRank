#https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth

#At first I came up with a function similar to the most common approach on HackerRank's forum:
"""def depth(elem, level):
    global maxdepth
    if level+1 > maxdepth: maxdepth = level+1
    [depth(child, level+1) for child in elem]   
    return  maxdepth """
#Unfortunately I'm stubborn and I felt the urge to find an original solution. :V
# As a result of my struggle you can now admire this lambda abomination:

import xml.etree.ElementTree as etree

maxdepth = 0
depth = lambda n, l, md=0 : (exec('global maxdepth'+'\n'+'maxdepth=max(md,l+1)'), [depth(c,l+1,maxdepth) for c in n])

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)