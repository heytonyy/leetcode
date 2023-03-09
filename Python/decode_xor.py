# https://leetcode.com/problems/decode-xored-array/submissions/912281275/
from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for i in range(len(encoded)):
            # ^ is the XOR operator i guess
            arr.append(encoded[i] ^ arr[-1])
        return arr