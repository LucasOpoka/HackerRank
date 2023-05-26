#https://www.hackerrank.com/challenges/30-linked-list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        nd = Node(data)
        nth = head
        if head is None:
            head = nd
        else:
            while nth.next is not None:
                nth = nth.next
            nth.next = nd
        return head
            
mylist= Solution()