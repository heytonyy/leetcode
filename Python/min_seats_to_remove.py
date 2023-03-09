# https://leetcode.com/problems/delete-greatest-value-in-each-row/
from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        total = 0

        while (len(grid[0]) > 0):
            potential_maxes = []

            for i in range(len(grid)):
                row_max = max(grid[i])
                potential_maxes.append(row_max)
                grid[i].remove(row_max)

            total += max(potential_maxes)

        return total


# TESTING
result = Solution().deleteGreatestValue([[1,2,4],[3,3,1]])
print(result)