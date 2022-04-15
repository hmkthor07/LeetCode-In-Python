"""

튜플 4개 각 4개 합쳐서 0이 되는 것 갯수 찾기

"""

class Solution:
    def fourSumCount(self, a,b,c,d)->int:
        
        first_map = {}
        second_map = {}
        total_cnt = 0

        for a_item in a:
            for b_item in b:
                if a_item+b_item not in first_map:
                    first_map[a_item+b_item] = 1
                else:
                    first_map[a_item+b_item] += 1
        
        for c_item in c:
            for d_item in d:
                if c_item+d_item not in second_map:
                    second_map[c_item+d_item] = 1
                else:
                    second_map[c_item+d_item] += 1
        

        for first_key in first_map.keys():
            for second_key in second_map.keys():
                if first_key + second_key == 0:
                    total_cnt += ((first_map[first_key])*(second_map[second_key]))

        return total_cnt

    def fourSumCountBetter(self, a:tuple, b:tuple, c:tuple, d:tuple)->int:

        m = {}
        answer = 0
        for itemA in a:
            for itemB in b:
                sum = itemA+itemB
                if sum not in m:
                    m[sum] = 0
                m[sum] += 1

        for itemC in c:
            for itemD in d:
                sum = -(itemC+itemD)
                if sum in m:
                    answer += m[sum]
        
        return answer


s = Solution()
answer = s.fourSumCountBetter((1,2),(-2,-1),(-1,2),(0,2))
print(answer)