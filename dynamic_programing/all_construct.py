# practice from: https://youtu.be/oBt53YbR9Kk
from typing import List

def all_contruct(target: str, wordBank: List[str]) -> List[str]:

    def dp(target, wordBank, cache={}):
        if target in cache:
            return cache[target]
        if target == '':
            return []

        ans = None
        for word in wordBank:
            if target.find(word) == 0:
                new_target = target.replace(word, '')
                cache[new_target] = dp(new_target, wordBank, cache)
                if cache[new_target] != None:
                    ans = [*cache[new_target], word]

        return ans

    result = dp(target, wordBank)

    return result if result != [] else None


# TESTING
print(all_contruct('', ['cat', 'dog', 'mouse'])) # True
print(all_contruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) # True
print(all_contruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # False
print(all_contruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) # True
print(all_contruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee',
    ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])) # False