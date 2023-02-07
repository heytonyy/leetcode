# https://leetcode.com/problems/matrix-diagonal-sum/description/
from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        size = len(mat[0])
        isOdd = size % 2 == 1
        sum = 0

        for i in range(0, size):
            sum += mat[i][i] + mat[i][size-1-i]

        if isOdd:
            mid = int(size/2)
            sum -= mat[mid][mid]

        return sum