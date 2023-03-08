# https://leetcode.com/problems/divisor-game/

class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0

# not a really engaging one.....

# TESTING
test_cases = [
    (2, True),
    (3, False),
    (4, True),
    (5, False),
    (6, True),
    (7, False),
    (8, True),
    (9, False),
    (10, True)
]

for test_case in test_cases:
    n = test_case[0]
    expected = test_case[1]
    print(f"n={n}, expected={expected}")
    sol = Solution()
    result = sol.divisorGame(n)
    print(f"result={result} (expected={expected})")
    assert result == expected

