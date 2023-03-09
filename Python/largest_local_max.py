# https://leetcode.com/problems/largest-local-values-in-a-matrix/submissions/912300581/
from typing import List

def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        def local_max(row, col):
            max_val = grid[row][col]
            for i in range(3):
                print(grid[row+i][col+0:3])
                lg = max(grid[row+i][col+0:col+3])
                if lg > max_val:
                    max_val = lg
            return max_val

        kernel = len(grid[0]) - 3 + 1
        output = [ kernel * [0] for i in range(kernel) ]

        for i in range(kernel):
            for j in range(kernel):
                output[i][j] = local_max(i, j)

        return output