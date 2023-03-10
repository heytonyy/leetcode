# https://leetcode.com/problems/minimum-time-visiting-all-points/
from typing import List

# rational behind solution:
'''
moving diagonally is optimal [ sqrt(2) > 1 units ]
move diagonally until x or y matches next point [ aka diff == 0 ]
the diff = abs(x2-x1) and diff = abs(y2-x1) indicate the displacement in that direction
the larger value will be the optimal time between those two points.
p1=[0,1]
p2=[2,2]
max(abs(2-0), abs(2-1)) = 2 seconds (first second diagonal, second second horizontal)
'''

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        seconds = 0

        for i in range(len(points) - 1):
            x2 = points[i+1][0]
            x1 = points[i][0]
            y2 = points[i+1][1]
            y1 = points[i][1]
            time = max( abs(x2 - x1), abs(y2 - y1) )
            seconds += time

        return seconds