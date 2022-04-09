"""
Count the amount of prime numbers less than a given number N

What is a prime number? 
1. Greater than 1
2. Non-divisible my anything except one and itself

* in other words: 
for any numbrer, n, wee need to check if it is not divisible by any number less than n and bigger than 1

for instance, 
if input : 10 , the output : 4

1< ? < N
"""
from typing import List
import math

class Solution:
    def countPrimes(self, n:int) -> int:
        if(n<2):
           return 0

        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False

        for i in range(2, int(math.ceil(math.sqrt(n)))): # 정수면 놔두고, 정수가 안되면 올린다. 
            for j in range(i*i, n, i):  
                isPrime[j] = False

        return sum(isPrime) # 배열에서 값이 True인것만 더한다. 

s = Solution()
answer = s.countPrimes(34)
print(answer)