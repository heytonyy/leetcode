# https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0

        for m in moves:
            if m == "L" or m == "R":
                x += 1 if m == "R" else -1
            else:
                y += 1 if m == "U" else -1

        return x == 0 and y == 0