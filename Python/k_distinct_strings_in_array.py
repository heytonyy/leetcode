# https://leetcode.com/problems/kth-distinct-string-in-an-array/
from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d={}
        for idx, a in enumerate(arr):
            if a not in d:
                d[a]=[1, [idx]]
            else:
                d[a][0]+=1
                d[a][1].append(idx)
        
        ans = [ item for item in d.items() if item[1][0] == 1 ]

        if len(ans) < k:
            return ''
        else:
            return ans[k-1][0]