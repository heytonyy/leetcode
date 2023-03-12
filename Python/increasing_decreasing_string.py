# https://leetcode.com/problems/increasing-decreasing-string/
import collections, string

# had to look up this answer... seems like it was a irrelevent/specific solution

class Solution:
    def sortString(self, s: str) -> str:
        cnt, ans, asc  = collections.Counter(s), [], True
        while len(ans) < len(s):
            for i in range(26):
                c = string.ascii_lowercase[i if asc else ~i] # this swaps asc/dsc bc bitwise..?
                if cnt[c] > 0:
                    print(f'c: {c} -- cnt: {cnt}')
                    ans.append(c)
                    cnt[c] -= 1
            asc = not asc
        return ''.join(ans)