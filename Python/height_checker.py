# https://leetcode.com/problems/height-checker/
from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        diffs = 0
        
        for i in range(len(heights)):
            if not heights[i] == expected[i]:
                diffs += 1

        return diffs