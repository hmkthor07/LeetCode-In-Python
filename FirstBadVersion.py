"""
You have N versions of a software, we want to find the first "bad" version of the software.

how to determine a bad version? 

We will be given a method called "isBadVersion" by default, 

it returns a boolean, true if the version you pass to it is bad, false otherwise.

Important note : 
if a version is bad, all versions after it are bad. 

Brute Force : Linear Search : O(N)
Optimal Solution : Binary Search : O(log N)

버전은 1~N 까지 이다. 

"""

from typing import List

class Soultion:
    def isBadVersion(self, target: int) -> bool:
        return target >= 3

    def findFirstBadVersion(self, n: int) -> int:
        left = 1
        right = n 

        while (left < right):
            mid = (left + right) // 2
            if (self.isBadVersion(mid)):
                right = mid
            else:
                left = mid + 1
        return left

s = Soultion()
answer = s.findFirstBadVersion(10)
print(answer)


