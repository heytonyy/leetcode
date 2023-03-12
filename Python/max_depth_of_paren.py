# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        maximum = 0
        for i in range(len(s)):
            leftParentheses = s[:i+1].count("(")
            rightParentheses = s[:i+1].count(")")
            maximum = max(maximum, (leftParentheses - rightParentheses))
        return maximum