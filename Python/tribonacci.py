# https://leetcode.com/problems/n-th-tribonacci-number/
from functools import cache

class Solution:
    # def tribonacci(self, n: int) -> int:
    #     if n == 0:
    #         return 0
    #     if n == 1 or n == 2:
    #         return 1
    #     ans = self.tribonacci(n-1) + self.tribonacci(n - 2) + self.tribonacci(n-3)
    #     return ans
    
    def tribonacci(self, n: int) -> int:

        cache = {}
        def dp(n):
            if n in cache:
                return cache[n]
            if n == 0:
                value = 0
            elif n == 1 or n == 2:
                value = 1
            else:
                value = dp(n-1) + dp(n-2) + dp(n-3)
            cache[n] = value
            return value

        return dp(n)

# TESTING
print(Solution().tribonacci(100))