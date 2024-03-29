# https://leetcode.com/problems/pascals-triangle-ii/submissions/911607086/
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        for i in range(1, rowIndex):
            row[i] = row[i-1] * (rowIndex-i+1) // i
        return row