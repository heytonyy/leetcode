# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:

        def dp(num, cache={}):
            if num in cache:
                return cache[num]
            if num == 1:
                value = 1
            elif num == 2:
                value = 2
            else:
                value = dp(num - 1, cache) + dp(num - 2, cache)
            cache[num] = value
            return value

        return dp(n)