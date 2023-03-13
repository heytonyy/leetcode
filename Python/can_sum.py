# not on leetcode... for practicing dp
from typing import List
from functools import cache

class Solution:
    def canSum(targetSum: int, numbers: List[int]) -> bool:
        
        def dp(targetSum, nums, cache={}):
            if targetSum in cache:
                return cache[targetSum]
            if targetSum == 0:
                return True
            if targetSum < 0:
                return False

            for n in nums:
                if dp(targetSum - n, nums, cache):
                    cache[targetSum - n] = True
                    return True
                
            cache[targetSum] = False
            return False

        return dp(targetSum, numbers)


# TESTING
print(Solution.canSum(7, [2, 3]))
print(Solution.canSum(7, [5, 3, 4, 7]))
print(Solution.canSum(7, [2, 4]))
print(Solution.canSum(8, [5, 3, 2]))
print(Solution.canSum(300, [7, 14]))

