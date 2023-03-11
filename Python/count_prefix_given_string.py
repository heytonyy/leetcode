# https://leetcode.com/problems/count-prefixes-of-a-given-string/
from typing import List

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        prefixes = 0

        for w in words:
            if s[:len(w)] == w:
                prefixes += 1

        return prefixes
