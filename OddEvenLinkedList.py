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
        tempNode = ListNode(0)
        tempNode.next = head

        newNode = head
        ans = newNode

        while head.next and head.next.next is not None:
            head = head.next.next
            newNode.next = head
        
        while tempNode.next and tempNode.next.next is not None:
            tempNode = tempNode.next.next
            newNode.next = tempNode

        return ans

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

s = Solution()
ans = s.setOddEvenLinkedList(node1)

while ans:
    print(ans.val)
    ans = ans.next