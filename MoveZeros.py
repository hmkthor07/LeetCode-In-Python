"""
Given an array of integers, write a function to move all 0's to the end 
while maintaining the relative order of the other elements.
"""

#Time complexity : O(N+M)
#Space complexity: O(1) : input 으로 들어온 배열의 공긴복잡도는 별도로 게산하지 않는다. 

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1
        
        for k in range(i,n):
            nums[k] = 0
        
        return nums


my_solution = Solution()
print(my_solution.moveZeroes([0,1,0,3,12]))
