"""
Given 2 seperated sorted linked lists, merge them together and retain the sorting.

Utilize the fact that the lists are sorted. 
"""

# Definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        curLinkedList = ListNode(0)
        ans = curLinkedList

        while l1 and l2:
            if l1.val > l2.val:
                curLinkedList.next = l2
                l2 = l2.next
            else:
                curLinkedList.next = l1
                l1 = l1.next

            curLinkedList = curLinkedList.next
        
        while l1:
            curLinkedList.next = l1
            l1 = l1.next
            curLinkedList = curLinkedList.next
        while l2:
            curLinkedList.next = l2
            l2 = l2.next
            curLinkedList = curLinkedList.next

        return ans.next

s = Solution()

l1_1 = ListNode(1)
l1_2 = ListNode(2)
l1_4 = ListNode(4)
l1_1.next = l1_2
l1_2.next = l1_4

l2_1 = ListNode(1)
l2_3 = ListNode(3)
l2_4 = ListNode(4)
l2_1.next = l2_3
l2_3.next = l2_4

ans = s.mergeTwoLists(l1_1, l2_1)

print(ans)

while (ans!=None):
    print(ans.val)
    ans = ans.next