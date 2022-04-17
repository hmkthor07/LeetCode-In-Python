"""
Given a string S and a string T, 
find the minimum window in S which will contain all the characters in T

꼭 T 의 순서를 따라갈 필요가 없으며, 중간에 T 문자들 이외 문자들어가도됨. 
어쨋든 최소길이 WINDOW를 구할 것. Shortest substring!!

S = "ADOBECODEBANCC" T = "ABC

ABSSSSCDBBCABBCCAB

ANSWER = BANC (4자)

1. KEY:INDEX DICT() 흐름에 따른 인덱스
2. 최소인것을 저장하는 STR

"""

class Solution:
    def findMWS(self, s:str, t:str) -> str:
        m = dict()

        n = len(s)
        min_len = n
        min_str = ""
        left = 0
        right = 0

        for i in range(n):
            if s[i] in t:
                m[s[i]] = i
                # m 안에 모두 있으면, 
                if len(m) == len(t):
                    left = min(m.values())
                    right = max(m.values())
                    if (right - left + 1) < min_len:
                        min_len = right-left+1
                        min_str = s[left:(right+1)]

        return min_str

s = Solution()
answer = s.findMWS("ADOBECODEBANCC","ABC")
print(answer)                

       
            


