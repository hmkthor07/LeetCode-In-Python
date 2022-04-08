"""
You have N versions of a software, we want to find the first "bad" version of the software.

how to determine a bad version? 

We will be given a method called "isBadVersion" by default, 

it returns a boolean, true if the version you pass to it is bad, false otherwise.

Important note : 
if a version is bad, all versions after it are bad. 

Brute Force : Linear Search : O(N)
Optimal Solution : Binary Search : O(log N)

"""

from typing import List

class Soultion:
    def isBadVersion(self, target: int) -> bool:
        return target >= 3

    def findFirstBadVersion(self, versions: List[int]) -> int:
        if len(versions) < 1:
            return -1
        
        left = 0
        right = len(versions)-1

        while (left <= right):
            mid = (left + right)//2
            if self.isBadVersion(versions[mid]): # bad 버전이면 
                if ( mid == 0 or ( mid-1>=0 and self.isBadVersion(versions[mid-1]) == False) ):
                    return mid
                else:
                    right = mid - 1
            else:
                left = mid + 1
        return -1


