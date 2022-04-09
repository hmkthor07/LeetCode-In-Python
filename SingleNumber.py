"""
Given a non-empty array of integers, 
every element appears twice except for one, find it. 

Input : [2,2,1,1,4]
"""

from typing import List

class Solution:

    # Time complexity : O(N) , Space complexity : O(N)
    def findOnlyElement(self, l: List[int]) -> int:
        # Hashmap 을 쓴 이유는 constant 타임으로 true or false 를 찾기 위해서. 
        hash_map = {}  
        for i in l:
            if i in hash_map:
                if hash_map[i] == True:
                    hash_map[i] = False
            else:
                hash_map[i] = True
        
        for k,v in hash_map.items():
            if v == True:
                return k

    # Time complexity : O(N) , Space complexity : O(N)
    def findOnlyElementBetter(self, l: List[int])-> int:
        return 2*sum(set(l))-sum(l)

    # Time complexity : O(N), Space complexity : O(1)
    def findOnlyElementAwesome(self, l: List[int]) -> int:
        
        final = 0
        for i in l:
            final ^= i

        return final

s = Solution()
answer = s.findOnlyElementAwesome([2,2,1,1,4])
print(answer)