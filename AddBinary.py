"""
Given 2 binary strings, return their sum


"""

class Solution:
    def addBinary(self, a: str, b: str)-> str:
        n = max(len(a), len(b))
        a_chk = [0]*(n+1)
        b_chk = [0]*(n+1)
        sum_chk = [0]*(n+1)

        carry_v = 0
        sum_v = 0

        for i in range(-1, -len(a)-1, -1):
            a_chk[i] = int(a[i])

        for i in range(-1, -len(b)-1, -1):
            b_chk[i] = int(b[i])

        for i in range(-1, -n-2, -1):
            print(int(a_chk[i]), int(b_chk[i]), carry_v, sum_v)
            sum_v = (int(a_chk[i]) + int(b_chk[i])+ carry_v)%2
            carry_v = (int(a_chk[i]) + int(b_chk[i])+ carry_v)//2
            sum_chk[i] = sum_v
            if i == -n-1 and carry_v == 1:
                sum_chk[i] = carry_v

        show_sum = ''
        for i in sum_chk:
            show_sum += str(i)

        return (show_sum)
        
    def AddBinaryCleaner(self, a: str, b: str) -> str:
        i, j = len(a)-1, len(b)-1
        carry = 0
        result=[]

        while(i>=0 or j>=0 or carry==1):
            
            sum_v = carry
            if i >= 0:
                sum_v += int(a[i])
                i -= 1
                
            if j >= 0: 
                sum_v += int(b[j])
                j -= 1
           
            carry = sum_v // 2
            sum_v = sum_v % 2

            result.append(str(sum_v))

        return ''.join(reversed(result))

s = Solution()
answer = s.AddBinaryCleaner('111111', '1101')
print(answer)