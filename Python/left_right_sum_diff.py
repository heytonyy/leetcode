# https://leetcode.com/problems/left-and-right-sum-differences/
from typing import List

class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            left = sum(nums[0:i])
            right = sum(nums[i+1:])
            output.append(abs(left-right))

        return output