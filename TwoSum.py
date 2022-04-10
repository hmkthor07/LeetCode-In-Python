"""
Given an array of integers and a target value, return the indices of 2 numbers 
that add up to the input target value

Constraints : 
1. Input can't have multiple solutions. 
2. Guaranteed at lieast 2 integers in the array. 
3. Guaranteed to always have a soultion.      

for instance, numbers = [2,11,7,15], target = 26

Brute force : Time complexity O(N^2), Space Complexity : O(1)
Using Hashmap : Time complexity O(N), Space Complexity : O(N)

We can utilize some extra space to make the time complexity better. 
Space is normally cheaper than time. 
"""

from typing import List

class Solution:
    def findTwoNumbers(self, numbers: List[int], target: int) -> list:
        target_map = {}                         # Space complexity : O(N)
        for index in range(len(numbers)):       # Time complexity : O(N)
            if numbers[index] in target_map:    #==> Hash map 찾는데 시간복잡도는 O(1)
                return [target_map[numbers[index]], index]  #==> 타겟 찾아서 value 엑세스 하는데도 O(1)
            target_map[target-numbers[index]] = index


s = Solution()
answer = s.findTwoNumbers([2,11,7,15], 26)

print(answer)


