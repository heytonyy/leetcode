# https://leetcode.com/problems/reverse-string/
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p1, p2 = 0, len(s)-1
        mid = len(s) // 2

        for i in range(mid):
            s[p1+i], s[p2-i] = s[p2-i], s[p1+i]