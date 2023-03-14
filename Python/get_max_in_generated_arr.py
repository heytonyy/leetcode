# https://leetcode.com/problems/get-maximum-in-generated-array/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:

        def dp(n, cache={}):
            if n in cache:
                return cache[n]
            if n == 0:
                return [0]
            if n == 1:
                return [0, 1]

            cache[n-1] = dp(n-1, cache)

            nums = [ *cache[n-1] ]
            if n % 2 == 0:
                i = int(n/2)
                nums.append( nums[i] )
            else:
                i = int((n-1)/2)
                nums.append( nums[i] + nums[i+1] )

            return nums

        return max( dp(n) )