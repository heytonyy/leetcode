# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/
from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:

        return sorted(target) == sorted(arr)