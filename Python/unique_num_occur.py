# https://leetcode.com/problems/unique-number-of-occurrences/
from typing import List
from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d=defaultdict(int)
        for n in arr:
            d[n]+=1
        return sorted(list(set(d.values()))) == sorted(list(d.values()))