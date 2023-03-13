# practice from: https://youtu.be/oBt53YbR9Kk

from typing import List

def howSum(targetSum: int, numbers: List[int]):

    def dp(targetSum, numbers, cache={}):
        if targetSum in cache:
            return cache[targetSum]
        if targetSum == 0:
            return []
        if targetSum < 0:
            return None

        for n in numbers:
            remainder = targetSum - n
            result = dp(remainder, numbers, cache)
            if result != None:
                cache[remainder] = [*result, n]
                return cache[remainder]
            
        cache[targetSum] = None
        return cache[targetSum]

    return dp(targetSum, numbers)



# TESTING
print(howSum(7, [2, 3]))
print(howSum(7, [5, 3, 4, 7]))
print(howSum(7, [2, 4]))
print(howSum(8, [5, 3, 2]))
print(howSum(300, [7, 14]))