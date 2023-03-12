# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

# took way too long to do this one... didnt think of the obvi solution

class Solution:
    def generateTheString(self, n: int) -> str:
        
        if n % 2 != 0:
            output = 'a' * n
        else: 
            output = 'a' + 'b' * (n-1)

        return output