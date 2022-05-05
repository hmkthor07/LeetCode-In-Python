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
    def removeNode(self, n_th:int, l:LinkedNode) -> LinkedNode:  

        temp = l
        head = l

        cnt = 0
        while l:
            cnt += 1
            if l.next:
                l = l.next
            else:
                break

        num = 0
        while head:
            num += 1
            nextNode = head.next

            if num == cnt-n_th:
                head.next = nextNode.next
                return temp
            
            head = head.next

        if num == 1:
            return None

        if num == cnt:
            return temp.next
                

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

        

