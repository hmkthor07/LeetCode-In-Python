"""
Given an array of integers, find if the array contains any duplicates

Return true if any value appears at least twice in the array, otherwise it should return false

Methods: 
1. Sorting (Time : O(NlogN)) and looping(Time : O(N)) to find the consecutive number. : Space complexity : O(1)
2. Add all elements in a set (Time: O(N), Space: O(N)) and compare the size of the set to the array size : if sizes are the same, return true
3. Use a hash map 
"""

from typing import List
from collections import defaultdict

class Solution:
    def FindDuplicates(self, l: List[int]) -> bool:
        m = defaultdict(int)
        for i in l: # T.C : O(N)
            if m[i]: # T.C : O(N)
                return True
            m[i]=1    # S.C : O(N)
        
        return False


s = Solution()
answer = s.FindDuplicates([1,2,3,1])
print(answer)