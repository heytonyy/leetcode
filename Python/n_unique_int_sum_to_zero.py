# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        output = [0] * n

        for i in range(len(output)):
            output[i]= i * 2 - n + 1

        return output