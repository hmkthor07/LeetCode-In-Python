"""
You are given two non-empty linked lists representing non-negative integers.

The digits are stored in reverse order and each node contains a single digit.

Add the two numbers and return it as a linked list.

1->2->3
3->4->5

answer 
4->6->8
"""

class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def addTwoSum(self, l1:LinkedNode, l2:LinkedNode)-> LinkedNode:
        
        head = NOne
        ans = None
        sum = 0
        carry = 0
        remain = 0

        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + carry
            if sum >= 10:
                carry = 1
                remain = sum - 10
            else:
                carry = 0
                remain = sum
            
            if ans is not None:
                ans.next = LinkedNode(remain)
            else:
                head = LinkedNode(remain)
                ans = head
            
            l1 = l1.next
            l2 = l2.next

        while l1:
            sum = l1.val + carry
            if sum >= 10:
                carry = 1
                remain = sum - 10
            else:
                carry = 0
                remain = sum
            
            ans.next = LinkedNode(remain)
        
        while l2:
            sum = l2.val + carry
            if sum >= 10:
                carry = 1
                remain = sum - 10
            else:
                carry = 0
                remain = sum
            
            ans.next = LinkedNode(remain)


        return head
