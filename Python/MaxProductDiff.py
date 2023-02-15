# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        first_max = nums[len(nums)-1]
        second_max = nums[len(nums)-2]
        first_min = nums[0]
        second_min = nums[1]
        return first_max * second_max - first_min * second_min

