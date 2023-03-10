# https://leetcode.com/problems/find-the-highest-altitude/
from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]

        for net in gain:
            new_alt = altitudes[-1] + net
            altitudes.append(new_alt)
        
        return max(altitudes)