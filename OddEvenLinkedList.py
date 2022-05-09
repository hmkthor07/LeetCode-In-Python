"""
Given a singly linkedlist, group all odd nodes together followed by even nodes.

We are talking about the node number, not the value in the nodes.

For instance, 

1 -> 2 -> 3 -> 4 -> 5 -> Null

1 -> 3 -> 5 -> 2 -> 4 -> Null

"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def setOddEvenLinkedList(self, head:ListNode) -> ListNode:
        
        if not head:
            return head

        odd = head
        even = odd.next
        evenList = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenList

        return head