## https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = str(x)[::-1]
        if reverse[-1] == '-' or x != int(reverse):
            return False
        return True

