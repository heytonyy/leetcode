# https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        output = ''
        cnt = p1 = p2 = 0

        while p1 < len(s):
            cnt += 1 if s[p1] == '(' else -1

            if cnt == 0:
                output += s[p2+1:p1]
                p1 += 1
                p2 = p1
                continue

            p1 += 1

        return output