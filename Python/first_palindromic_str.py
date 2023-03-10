# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        def isPalindrome(word):
            return word == word[::-1]

        for word in words:
            if isPalindrome(word):
                return word
        
        return ''