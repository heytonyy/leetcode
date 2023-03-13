# practice from: https://youtu.be/oBt53YbR9Kk

from typing import List

def best_sum(targetSum: int, numbers: List[int]):

    def dp(targetSum, numbers, cache={}):
        if targetSum in cache:
            return cache[targetSum]
        
        if targetSum == 0:
            return []
        
        if targetSum < 0:
            return None
        
        curr = None
        for n in numbers:
            remainder = targetSum - n
            result = dp(remainder, numbers)
            cache[remainder] = result

            if result != None:
                new = [*result, n]

                if curr == None or len(new) < len(curr):
                    curr = new

        return curr

    return dp(targetSum, numbers)

# TESTING
print(best_sum(7, [5, 3, 4, 7])) # [7]
print(best_sum(8, [5, 3, 2])) # [3, 5]
print(best_sum(8, [1, 4, 5])) # [4, 4]
print(best_sum(100, [1, 2, 5, 25])) # [25, 25, 25, 25]