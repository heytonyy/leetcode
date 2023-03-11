# https://leetcode.com/problems/baseball-game/
from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []

        for op in operations:
            if op == "C":
                records.pop()
            elif op == "D":
                new_record = records[-1] * 2
                records.append(int(new_record))
            elif op == "+":
                new_record = records[-2] + records[-1]
                records.append(int(new_record))
            else:
                records.append(int(op))

        return sum(records)