# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/
from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        output = []

        for i in range(len(nums)-1):
            output.append(nums[i])
            if sum(output) > sum(nums[i+1:]):
                return output
        
        return nums