## https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
      count = 0
      for r in stones:
        if r in jewels:
          count+=1
      return count