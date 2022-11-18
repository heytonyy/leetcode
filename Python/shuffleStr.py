# https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
      d=dict()
      for i in range(len(s)):
        d[i]=''
      for j in range(len(s)):
        d[indices[j]]=s[j]
      return ''.join(d.values())
        