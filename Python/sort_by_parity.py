# https://leetcode.com/problems/sort-array-by-parity/
from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odds = [ o for o in nums if o % 2 == 1 ]
        evens = [ e for e in nums if e % 2 == 0 ]

        return evens + odds