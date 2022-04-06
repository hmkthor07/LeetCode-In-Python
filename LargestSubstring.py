"""
Largest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters. 

Sliding window 방식
Time complexity : O(N)
Space complexity : O(N)
"""

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, my_string: str) -> int:
        
        str_len = len(my_string)
        
        left = 0
        right = 0
        my_map = {} # 'char':'index'
        longest = 0

        while(left < str_len and right < str_len):
            if my_string[right] in my_map:   #map 에 해당 문자가 존재한다면,
                left = max(left, my_map[my_string[right]] + 1)  # 기존 left 보다 클때만 갱신이 필요하다. 
                    
            my_map[my_string[right]] = right    # 그리고 기존 것은 새 index 로 바꿔준다. 
            longest = max(longest, right-left+1)
            
            right += 1 # 작업를 마쳤으면 오른쪽으로 한칸씩 이동한다. 

        return longest

s = Solution()
answer = s.lengthOfLongestSubstring('fivestarreview')
print(answer)
                  