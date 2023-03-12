# https://leetcode.com/problems/remove-palindromic-subsequences/

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        
        def is_palindrome(word):
            return word == word[::-1]
        
        return 1 if is_palindrome(s) else 2