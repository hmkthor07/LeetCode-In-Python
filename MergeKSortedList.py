"""

Merge K sorted linked lists and return it as one sorted list.

1 -> 4 - > 5
1 -< 3 -> 4
2 -> 6

answer
1 -> 1 -> 2 -> 3-> 4 -> 4 -> 5 -> 6

"""


class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def mergeKLists(self, lists:List[LinkedNode]) -> LinkedNode:
        if len(lists) == 0:
            return None

        i = 0
        last = len(lists)
        j = last

        while last != 0:
            i = 0
            j = last

            while j>i:
                lists[i] = mergeTwoLists(lists[i], lists[j])
                i += 1
                j -= 1
                last = j
        
        return lists[0]

    def mergeTwoLists(self, l1:List, l2:List) -> List:
        
        head = LinkedNode(0)
        newList = head

        while l1 and l2:
            if l1.val > l2.val:
                newList.next = l2
                l2 = l2.next
            else:
                newList.next = l1
                l1 = l1.next
            newList = newList.next
        
        while l1:
            newList.next = l1
            l1 = l1.next
            newList = newList.next    
        
        while l2:
            newList.next = l2
            l2 = l2.next
            newList = newList.next

        return head.next