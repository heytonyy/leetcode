# https://leetcode.com/problems/where-will-the-ball-fall/
from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        def dp(row, col):
            # reached the end, return col position
            if row == m:
                return col

            # check rightside if at 1 (will move down-right)
            if grid[row][col] == 1:
                # check if right wall and col+1 also is 1 to traverse to next row
                if col + 1 < n and grid[row][col] == grid[row][col+1]:
                    return dp(row+1, col+1)
                else:
                    return -1 # ball got trapped

            # check leftside if at -1 (will move down-left)
            else:
                # check if left wall and col-1 also is -1 to traverse  to next row
                if col - 1 >= 0 and grid[row][col] == grid[row][col-1]:
                    return dp(row+1, col-1)
                else:
                    return -1 # ball got trapped
        
        answers = []
        for ball in range(n):
            answers.append( dp(0,ball) )

        return answers