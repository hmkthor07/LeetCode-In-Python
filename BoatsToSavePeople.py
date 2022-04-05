"""
Given an array people and an integer limit

People array is an array of people's weights, i-th person has a weight people[i] and each boat can carry at most limit. 

Each boat carries at most 2 people at the same time, Given that their weight sum is at most limit. 

Return the minimum number of boats to carry every giben person

# Time complexity : O(Nlog(N))
This is due to the fact that we sort the input array

# Space Complexity: O(N)
people.sort() internally uses an algorithm that has O(N) space complexity.

"""   

from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() # O(NlogN)

        boats = 0
        heavyP = len(people)-1
        lightP = 0

        while(lightP <= heavyP):
            if lightP == heavyP:
                boats +=1
                break

            if(people[lightP] + people[heavyP] <= limit):
                lightP += 1
                
            boats += 1
            heavyP -= 1
        
        return boats

s = Solution()
print(s.numRescueBoats([2,1,3,4],4))

