# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        return len( [ neg for i in grid for neg in i if neg < 0 ] )