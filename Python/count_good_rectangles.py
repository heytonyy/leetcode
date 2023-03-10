# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/
from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        largest_squares = [ min(rect) for rect in rectangles ]

        return largest_squares.count(max(largest_squares))