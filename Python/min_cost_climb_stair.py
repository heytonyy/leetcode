# https://leetcode.com/problems/min-cost-climbing-stairs/
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def dp(step, cost, cache={}):
            if step in cache:
                return cache[step]
            if step >= len(cost):
                return 0

            cache[step+1]=dp(step+1, cost)
            cache[step+2]=dp(step+2, cost)
            
            return cost[step] + min( cache[step+1], cache[step+2] )

        start_at_0 = dp(0, cost)
        start_at_1 = dp(1, cost)

        return min(start_at_0, start_at_1)
