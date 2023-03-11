# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/
from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = [ p for p in nums if p > 0 ]
        neg = [ n for n in nums if n < 0 ]

        return max(len(pos), len(neg))