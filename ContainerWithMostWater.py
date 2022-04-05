"""
Given n non-negative integers where each integer represent the height of a vertical line on a chart.

Find two lines, which together with x-axis forms a container, that holds the biggest amount of water. 

Return the area of that water. 

Brute Force 로 하면, Time Complexity : O(N^2) 및 Space Complexity : O(1) 나온다. 

How can we improve the time complexity?

포인터를 양쪽 끝에 두고, 작은 것을 반대쪽으로 옮겨오는 방식으로 최대값을 구해나가면 , 

Time Complexity : O(N^2) 및 Space Complexity : O(1) 이 될 수 있다. 

"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        arr_len = len(height)
        if(arr_len<2):
            return False
        
        left = 0
        right = arr_len -1
        max_area = 0

        while(left < right):
            x_axis = right - left
            y_axis = min(height[left], height[right])
            max_area = max(x_axis * y_axis, max_area)

            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1

        return max_area

s = Solution()
answer = s.maxArea([5,9,2,1,4])
print(answer)