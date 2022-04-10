"""

Imagine a robot standing at position(0,0) in a 2D grid, 

given a string consisting of its moves, 

find the final location of the robot. 

"""

class Solution:
    def findLocation(self, moves: str) -> bool:

        X = Y = 0

        for move in moves:
            if move == "U":
                Y += 1
            elif move == "D":
                Y -= 1
            elif move == "L":
                X -= 1
            elif move == "R":
                X += 1
        
        return X==0 and Y==0

s = Solution()
answer = s.findLocation("URRDLL")
print(answer)