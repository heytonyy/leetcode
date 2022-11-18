## https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d=dict()
        for s in sentence:
          if s in d:
            d[s]+=1
          else:
            d[s]=1
        return len(d.keys()) == 26