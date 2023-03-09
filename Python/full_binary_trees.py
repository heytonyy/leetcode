# https://leetcode.com/problems/all-possible-full-binary-trees/
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        if n == 1:
            return TreeNode()
        
        opts = []


# TESTING
test_cases = [
    (7, 5),
    (3, 1),
]

for n, expected in test_cases:
    print(f"n={n}, expected={expected}")
    result = Solution().allPossibleFBT(n)
    print(f"result={result}")
    assert len(result) == expected

