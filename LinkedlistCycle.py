"""
Given a linked list, return a boolean indicating if there is a cycle.
"""

class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:

    def __init__(self):
        self.head = None

    def findLinkedListCycle(self, l:LinkedNode) -> bool:
        hare = self.head
        turtle = self.head

        while turtle and hare and hare.next:
            hare = hare.next.next
            turtle = turtle.next

            if(hare.val == turtle.val):
                return True
        
        return False