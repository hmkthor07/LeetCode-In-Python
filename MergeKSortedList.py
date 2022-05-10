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