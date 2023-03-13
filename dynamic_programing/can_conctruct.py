# practice from: https://youtu.be/oBt53YbR9Kk
from typing import List

def can_contruct(target: str, wordBank: List[str]) -> bool:

    def dp(target, wordBank, cache={}):
        if target in cache:
            return cache[target]
        if target == '':
            return True
        
        for word in wordBank:
            if target.find(word) == 0:
                new_target = target.replace(word, '')
                if dp(new_target, wordBank, cache):
                    cache[new_target] = True
                    return True
        
        cache[target]=False
        return False

    return dp(target, wordBank)


# TESTING
print(can_contruct('', ['cat', 'dog', 'mouse'])) # True
print(can_contruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) # True
print(can_contruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # False
print(can_contruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) # True
print(can_contruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
    ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])) # False