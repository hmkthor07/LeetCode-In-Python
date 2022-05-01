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
    

    def reverseLinkedList2(self, head:LinkedNode) -> LinkedNode:
        node = None

        while head is not None:
            next = head.next
            head.next = node
            node = head
            head = next

        return node

s = Solution()

node_1 = LinkedNode(1)
node_2 = LinkedNode(2)
node_3 = LinkedNode(3)
node_4 = LinkedNode(4)
node_5 = LinkedNode(5)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
node_5.next = None



answer = s.reverseLinkedList2(node_1)

while answer:
    print(answer.val)
    answer=answer.next



