# https://leetcode.com/problems/counting-bits/
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        count = 0

        while count <= n:
            binary = bin(count)[2:]
            output.append(binary)
            count+=1
        
        for b in range(len(output)):
            output[b] = output[b].count('1')
            
        return output

# TESTING
s = Solution()
s.countBits(n=5)