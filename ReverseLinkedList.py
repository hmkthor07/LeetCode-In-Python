"""
Revers a singly linked list.

1 -> 2 -> 3 -> 4 -> 5

5 -> 4 -> 3 -> 2 -> 1

"""

class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverseLinkedList(self, l:LinkedNode) -> LinkedNode:

        firstNode = l
        firstNode.next = None

        if firstNode.next is None:
            return firstNode

        while l.next:
            prevNode = l
            nextNode = l.next
            nextNode.next = prevNode
            l = l.next
            
        return nextNode