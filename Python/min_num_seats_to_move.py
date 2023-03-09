# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/
from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        moves = 0

        for i in range(len(students)):
            moves += abs(students[i] - seats[i])

        return moves