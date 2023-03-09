# https://leetcode.com/problems/number-of-arithmetic-triplets/
from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        triplets = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if not nums[j] - nums[i] == diff:
                    continue
                
                for k in range(j, len(nums)):
                    if nums[k] - nums[j] == diff:
                        triplets += 1
                
        return triplets