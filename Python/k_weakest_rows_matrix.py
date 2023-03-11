# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
from typing import List
from collections import defaultdict

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d=defaultdict(list)
        for i, row in enumerate(mat):
            d[i]=row

        weak_to_strong = sorted( d.items(), key=lambda x: sum(x[1]) )
        row_index = [ key[0] for key in weak_to_strong ]

        return row_index[:k]