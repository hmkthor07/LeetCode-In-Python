"""

Find First and Last Position of Element in Sorted Array 

Find the starting and ending postion of a given target value. 

For optimal solution to this problem,

"""

from typing import List

class Solution:
    def findFirstPosition(self, l: List[int], target: int) -> List[int]:

        left = 0
        right = len(l)-1

        while(left <= right):
            mid = left + right // 2

            if(l[mid]== target):
                if(mid==0 or l[mid-1]!=target):
                    return mid
                right = mid -1 
            elif(l[mid]>target):
                right = mid -1
            else: 
                left = mid + 1

    def findLastPosition(self, l: List[int], target: int) -> List[int]:

        left = 0
        right = len(l)-1

        while(left <= right):
            mid = left + right // 2

            if(l[mid]== target):
                if(mid==(len(l)-1) or l[mid+1]!=target):
                    return mid
                left = mid + 1 
            elif(l[mid]>target):
                right = mid -1
            else: 
                left = mid + 1