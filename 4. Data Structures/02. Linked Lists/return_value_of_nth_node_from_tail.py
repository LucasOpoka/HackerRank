#https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#My function starts here
rslt, counter = 0, -1
def getNode(llist, positionFromTail, x = 0):
    global rslt, counter
    
#Recursion to start at the end of the list (var x equals n at the nth node):
    x += 1
    if llist.next != None:
        getNode(llist.next, positionFromTail, x)

#This part is executed once we reach the final node and then for each previous one (var equals 0 at end and +=1 at each previous node):        
    counter += 1 
    if positionFromTail == counter:
        rslt = llist.data
#Here we reset the global counter once we reach the head of the list:
    if x == 1:
        counter = -1
    return rslt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        position = int(input())

        result = getNode(llist.head, position)

        fptr.write(str(result) + '\n')

    fptr.close()
