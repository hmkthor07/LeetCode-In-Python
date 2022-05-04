"""
Remove Nth node from end of list

Given a linked list, remove the n-th node from the end of list and return its head.

for instance, 

n = 2
1 -> 2 -> 3 -> 4 -> 5

answer : 
1 -> 2 -> 3 -> 5
"""

class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def removeNode(self, n_th:int, l:LinkedNode) -> LinkedNode:  

        temp = l
        head = l

        cnt = 0
        while l:
            cnt += 1
            if l.next:
                l = l.next
            else:
                break

        num = 0
        while head:
            num += 1
            head = head.next
            nextNode = head.next

            if num == cnt-n_th:
                head.next = nextNode.next
                return temp

        if num == 1:
            return None
                
        

