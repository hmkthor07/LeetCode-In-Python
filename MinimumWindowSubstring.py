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
    # T 문자열이 서로 다를 때, 
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

    # 문자열이 서로 같을 때, 
    def findMWS2(self, s:str, t:str) -> str:
        len1 = len(s)
        len2 = len(t)

        if(len1<len2):
            return ""
        
        hashPat = {}
        hashStr = {}

        for i in range(len2):
            if(hashPat.get(t[i]) is None):
                hashPat[t[i]] = 0
            hashPat[t[i]] += 1

        count = 0
        left = 0
        startIndex = -1
        minLen = float("inf")

        for right in range(len1):
            if hashStr.get(s[right]) is None:
                hashStr[s[right]] = 0
            hashStr[s[right]] += 1

            if hashPat.get(s[right]) is None:
                hashPat[s[right]] = 0

            if hashStr.get(s[right]) <= hashPat.get(s[right]):
                count += 1

            if count == len2:
                while hashStr.get(s[left]) > hashPat.get(s[left]):
                    hashStr[s[left]] -= 1
                    left += 1

                minLen = min(minLen, (right-left+1))
                startIndex = left

        if startIndex == -1:
            return ""
        return s[startIndex:startIndex+minLen]




s = Solution()
answer = s.findMWS2("ADOBECODDEBANCC","DDE")
print(answer)                

       
            


