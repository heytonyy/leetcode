# https://leetcode.com/problems/percentage-of-letter-in-string/
import collections

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:

        letter_freq = collections.Counter(s)

        return int( letter_freq[letter]/len(s) * 100 )