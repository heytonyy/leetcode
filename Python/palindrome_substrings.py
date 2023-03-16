# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        from functools import cache
        
        @cache
        def is_palindrome(word, left, right):
            #base case: pointers crossed
            if left > right: 
                return True
            #base case: fails rule of palindrome
            if word[left] != word[right]: 
                return False
            #recurse left+1 , right-1 until reaching a base case
            return is_palindrome(word, left+1, right-1)

        substring_count = 0
        for i in range(len(s)):
            # need to start j-loop @ i to include single letters cases ('a' is a palindrome)
            for j in range(i, len(s)):
                if is_palindrome(s, i, j):
                    substring_count += 1

        return substring_count