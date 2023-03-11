# https://leetcode.com/problems/delete-columns-to-make-sorted/
from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        to_delete = 0

        for i in range(len(strs[0])):
            col = [ s[i] for s in strs ]
            if not col == sorted(col):
                to_delete += 1

        return to_delete