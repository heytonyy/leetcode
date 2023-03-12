# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:

        def is_substring(string, pattern):
            p1 = 0
            n = len(pattern)

            while p1 < len(string):
                if string[p1] == pattern[0]:
                    if pattern == string[p1:p1+n]:
                        return True

                p1 += 1
            
            return False

        cnt = 0
        for p in patterns:
            cnt += 1 if is_substring(word, p) else 0

        return cnt