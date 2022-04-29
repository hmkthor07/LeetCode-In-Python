"""
Given a linked list, return a boolean indicating if there is a cycle.
"""

class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    
    def hasCycle(self, head: LinkedNode) -> bool:
        hare = head
        turtle = head

        # TC : O(N) 
        # SC : O(1)
        while turtle and hare and hare.next:
            hare = hare.next.next
            turtle = turtle.next

            if(turtle == hare):
                return True
        
        return False


s = Solution()

node_1 = LinkedNode(1)
node_5 = LinkedNode(5)
node_11 = LinkedNode(11)
node_8 = LinkedNode(8)
node_9 = LinkedNode(9)

node_1.next = node_5
node_5.next = node_11
node_11.next = node_8
node_8.next = node_9
#node_9.next = node_5

print(s. hasCycle(node_1))