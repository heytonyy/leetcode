# https://leetcode.com/problems/divide-array-into-equal-pairs/
from typing import List
from collections import defaultdict

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d=defaultdict(int)
        expected = len(nums) / 2
        for k in nums:
            d[k]+=1

        total_pairs = 0
        for p in d.values():
            if not p % 2 == 0:
                return False
            total_pairs += p / 2

        return total_pairs == expected