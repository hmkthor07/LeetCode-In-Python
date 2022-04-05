"""
Given an array of integers, return true if the following conditions are fulfilled
1. Length of the array is bigger than or equal to 3
2. There exists some index i such that: a[0] < a[1] < ... a[i] > a[i+1] > ... > a[a.size -1]

In a nutshell : Find if there is an increasing subarray followed by a decreasing subarray  
"""

from typing import List

class Solution:
    def validMountainArray(self, A:List[int]) -> bool:
        
        arr_len = len(A)
        if(arr_len<3):
            return False
        i=1
        while(i<arr_len and A[i] > A[i-1]):
            i+=1
        if(i==1 or i==arr_len):
            return False

        while(i<arr_len and A[i] < A[i-1]):
            i+=1

        return i == arr_len

s = Solution()
answer = s.validMountainArray([1,2,3,4,1])
print(answer)