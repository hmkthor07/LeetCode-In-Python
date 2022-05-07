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
    def removeNode(self, n_th:int, head:LinkedNode) -> LinkedNode:  
        ans = LinkedNode(0)
        ans.next = head

        front = ans
        back = ans

        for i in range(1, n_th+2):
            front = front.next

        while front is not None:
            front = front.next
            back = back.next

        back.next = back.next.next

        return ans.next

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

ans = s.removeNode(5, node_1)

while ans:
    print(ans.val)
    ans = ans.next

        

