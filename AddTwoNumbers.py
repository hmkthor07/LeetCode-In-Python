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
        ans = LinkedNode(None)
        carry = 0
        sum = 0
        pointer:LinkedNode = ans

        while (l1!=None or l2!=None):
            sum = carry
            if l1!=None:
                sum += l1.val
                l1=l1.next
            if l2!=None:
                sum += l2.val
                l2=l2.next
            
            carry = int(sum/10)
            pointer.next = LinkedNode(sum%10)
            pointer = pointer.next
        
        if carry > 0:
            pointer.next = LinkedNode(carry)
        
        return ans.next

s = Solution()

l1_node_2 = LinkedNode(2)
l1_node_4 = LinkedNode(4)
l1_node_3 = LinkedNode(3)

l1_node_2.next = l1_node_4
l1_node_4.next = l1_node_3

l2_node_5 = LinkedNode(5)
l2_node_6 = LinkedNode(6)
l2_node_4 = LinkedNode(4)

l2_node_5.next = l2_node_6
l2_node_6.next = l2_node_4

ans = s.addTwoSum(l1_node_2, l2_node_5)

while ans:
    print(ans.val)
    ans = ans.next