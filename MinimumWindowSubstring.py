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
        n = len(s)
        left, right = 0, 0
        t_dict, s_dict = dict(), dict()
        count = n
        window = ""

        for char in t:
            if char not in t_dict:
                t_dict[char] = 0
            t_dict[char] += 1
        
        print(t_dict)

        while left <= n-1 and right <= n-1 and left <= right:
            if s[right] not in s_dict:
                s_dict[s[right]] = 0
            if s[right] not in t_dict:
                s_dict[s[right]] += 1
                right +=1
                continue
            else:
               # 있으면 
                s_dict[s[right]] += 1
                # s_dict >= t_dict 이면, 
                if all(item in s_dict.items() for item in t_dict.items()):
                    if right - left +1 < count:
                        count = right - left + 1
                        window = s[left:right+1]
                        print(window)
                # 아니면, 
                else:
                    if s_dict[s[right]] > t_dict[s[right]]:
                        s_dict[s[left]] -= 1
                        left +=1
            right += 1
                
            
      
        return window


s = Solution()
answer = s.findMWS("ADOBECODEBANCC","ABC")
answer = s.findMWS2("ADOBECODDEBANCC","DDE")
print(answer)                

       
            


