# https://leetcode.com/problems/count-asterisks/submissions/913474786/

class Solution:
    def countAsterisks(self, s: str) -> int:
        p1 = p2 = 0
        roi = ''
        is_pair = False

        while p1 < len(s):
            if not s[p1] == '|':
                p1 += 1
                continue

            if not is_pair:
                roi += s[p2:p1]
                is_pair = True  
            else:
                is_pair = False
                
            p1 += 1
            p2 = p1

        return roi.count('*') + s[p2:p1].count("*")