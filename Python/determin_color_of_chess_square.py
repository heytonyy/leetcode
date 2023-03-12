# https://leetcode.com/problems/determine-color-of-a-chessboard-square/

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        x = coordinates[0]
        y = coordinates[1]

        x_idx = letters.index(x)
        y_idx = int(y) - 1

        if x_idx % 2 == 0 and not y_idx % 2 == 0:
            return True
        elif not x_idx % 2 == 0 and y_idx % 2 == 0:
            return True
        else:
            return False