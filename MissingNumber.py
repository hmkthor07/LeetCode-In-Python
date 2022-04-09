"""
Given an array containing n distinct numbres taken from 0,1,2,3,..., n.

Find the number that is missing from the array.

The input array has distinction integer numbers and only one missing number

And an empty array is not allowed. 

* Constant time으로 무엇인가를 찾으려고 할때 -->> Hash map 사용한다. 
"""

from typing import List

class Solution:
    def findMissing(self, arr: List[int]) -> int:

        presentNumbers = {}
        for i in arr:
            presentNumbers[arr[i]] = True

        for i in range(0,len(arr)+1):
            if presentNumbers[i] != True:
                return i
    
    def findMissingBetter(self, arr: List[int])-> int:
        n = len(arr)
        
        return int(n*(n+1)/2 - sum(arr)) # ; Sum's time complexity : O(n)


s = Solution()
answer = s.findMissingBetter([2,1,3,0])
print(answer)