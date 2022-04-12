"""
Given an array of integers of size N, find the majority element of the array

A majority element appears more than n/2 times

Map 사용 = T.C. = O(N) / S.C. = O(N)
"""

from typing import List

class Solution:
    def findMajorityElement(self, nums:List[int]) -> int:
        m = {}

        for num in nums:
            m[num] = m.get(num,0) + 1 # if exists put the 'num' otherwise, put 0 in it.
        for num in m:
            if m[num] > len(m)//2:
                return num


s = Solution()
answer = s.findMajorityElement([1,2,3,1,1])

print(answer)