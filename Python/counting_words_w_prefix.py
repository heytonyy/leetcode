# https://leetcode.com/problems/counting-words-with-a-given-prefix/
from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        return len( [ x for x in words if x[:len(pref)] == pref ] )