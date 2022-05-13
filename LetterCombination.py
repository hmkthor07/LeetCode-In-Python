class Solution:
    def letterCombination(self, digits:str) -> List[str]:
        ans = []
        if len(digits) == 0:
            return ans

        m = {}
        m[2] = "abc"
        m[3] = "def"
        m[4] = "ghi"
        m[5] = "jkl"
        m[6] = "mno"
        m[7] = "pqrs"
        m[8] = "tuv"
        m[9] = "wxyz"