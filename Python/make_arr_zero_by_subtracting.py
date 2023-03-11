# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        ops = 0
        
        while len(nums) > 0:
            if nums[0] == 0:
                nums = nums[1:]
            else:
                to_subtract = nums[0]
                nums = [ x-to_subtract for x in nums[1:] ]
                ops += 1

        return ops