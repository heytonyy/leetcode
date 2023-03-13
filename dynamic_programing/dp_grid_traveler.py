# practice from: https://youtu.be/oBt53YbR9Kk

from functools import cache

class Solution:
    def grid_traveler(self, l, w):
        
        @cache
        def dp(l, w):
            if l == 1 and w == 1:
                return 1
            if l == 0 or w == 0:
                return 0
            
            return dp(l-1, w) + dp(l, w-1)
        
        return dp(l,w)

# TESTCASES

s = Solution()

print(s.grid_traveler(18,18))