# https://leetcode.com/problems/sum-of-all-subset-xor-totals/
from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        from itertools import combinations # handy

        total_xor = 0
        for i in range(len(nums) + 1):
            for subset in combinations(nums, i):
                if len(subset) == 0:
                    continue

                if len(subset) == 1:
                    total_xor += subset[0]
                    continue

                temp_xor = subset[0]
                for s in range(1, len(subset)):                    
                    temp_xor = temp_xor ^ subset[s]
                
                total_xor += temp_xor

        return total_xor