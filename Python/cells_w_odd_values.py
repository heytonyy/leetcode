# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
from typing import List

'''
notes:
instead of matrix = m x n:
- rows[i] is the value with respect to the row
- cols[i] is the value with respect to the col
data structures: m x n -> m + n

bitwise used here bc wanted odd. 
even/odd is a binary so dont care the # just if 1 or 0
'''

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n

        for r, c in indices:
            rows[r] ^= 1
            cols[c] ^= 1

        return sum([ (r+c)%2 for c in cols for r in rows ]) 