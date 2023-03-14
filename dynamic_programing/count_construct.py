# practice from: https://youtu.be/oBt53YbR9Kk
from typing import List

def count_contruct(target: str, wordBank: List[str]) -> int:

    def dp(target, wordBank):
        # if target in cache:
        #     return cache[target]
        if target == '':
            return 1

        count = 0
        for word in wordBank:
            if target.find(word) == 0:
                new_target = target.replace(word, '')
                num_ways = dp(new_target, wordBank)
                count += num_ways

        return count

    return dp(target, wordBank)


# TESTING
print(count_contruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) # 3
print(count_contruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) # 2
print(count_contruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # 0
print(count_contruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) # 4
print(count_contruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
    ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])) # 0