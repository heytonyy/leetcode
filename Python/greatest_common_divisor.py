# https://leetcode.com/problems/find-greatest-common-divisor-of-array/
from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        def computeGCD(x, y):
            while(y):
                x, y = y, x % y
            return abs(x)

        return computeGCD(max(nums), min(nums))