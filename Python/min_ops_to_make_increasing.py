# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        prv = -float('inf')
        
        for val in nums:
            if val>prv:
                prv = val
            else:
                ans += prv+1-val
                prv += 1
                
        return ans