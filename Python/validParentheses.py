## https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = ['(','{','[']
        right = [')','}',']']
        if len(s) == 1 or s[0] in right:
            return False
        for symbol in s:
            if symbol in right and len(stack) > 0:
                ridx = right.index(symbol)
                lidx = left.index(stack[-1])
                if ridx == lidx:
                    stack.pop()
                else:
                    return False
            elif symbol in left:
                stack.append(symbol)
            else:
                return False
        return len(stack) == 0